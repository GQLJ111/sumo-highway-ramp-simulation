#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
交通流数据分析器（基于FCD和Trip数据）
提取断面车流量、占有率、车头时距、平均通行速度等数据
"""

import os
import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import json

class TrafficFlowAnalyzer:
    def __init__(self):
        """初始化交通流分析器"""
        self.data = {}
        self.results = {}
        
        # 设置中文字体
        plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
        plt.rcParams['axes.unicode_minus'] = False
        
    def analyze_fcd_data(self, file_path="vehicle_traces.xml"):
        """分析FCD数据：从车辆轨迹计算交通参数"""
        if not os.path.exists(file_path):
            print(f"文件不存在: {file_path}")
            return None
        
        print("正在分析车辆轨迹数据...")
        
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        fcd_data = []
        for timestep in root.findall('timestep'):
            time = float(timestep.get('time'))
            
            for vehicle in timestep.findall('vehicle'):
                fcd_data.append({
                    'time': time,
                    'id': vehicle.get('id'),
                    'lane': vehicle.get('lane'),
                    'edge': vehicle.get('lane').split('_')[0] if '_' in vehicle.get('lane', '') else vehicle.get('lane'),
                    'pos': float(vehicle.get('pos', 0)),
                    'speed': float(vehicle.get('speed', 0)),
                    'x': float(vehicle.get('x', 0)),
                    'y': float(vehicle.get('y', 0))
                })
        
        df = pd.DataFrame(fcd_data)
        self.data['fcd_data'] = df
        
        print(f"提取了 {len(df)} 条轨迹数据记录")
        return df
    
    def analyze_trip_data(self, file_path="trip_info.xml"):
        """分析行程数据：车头时距"""
        if not os.path.exists(file_path):
            print(f"文件不存在: {file_path}")
            return None
        
        print("正在分析车辆行程数据...")
        
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        trip_data = []
        for vehicle in root.findall('vehicleinfo'):
            trip_data.append({
                'id': vehicle.get('id'),
                'depart': float(vehicle.get('depart', 0)),
                'arrival': float(vehicle.get('arrival', 0)),
                'duration': float(vehicle.get('duration', 0)),
                'routeLength': float(vehicle.get('routeLength', 0)),
                'speed': float(vehicle.get('routeLength', 0)) / max(float(vehicle.get('duration', 1)), 0.1),
                'vtype': vehicle.get('vType', 'unknown')
            })
        
        df = pd.DataFrame(trip_data)
        
        # 计算车头时距
        if not df.empty:
            df_sorted = df.sort_values('depart')
            df_sorted['headway'] = df_sorted['depart'].diff()
            df_sorted['headway'] = df_sorted['headway'].fillna(0)
            
        self.data['trip_data'] = df_sorted if not df.empty else df
        
        print(f"提取了 {len(df)} 条车辆行程记录")
        return df
    
    def calculate_traffic_parameters(self):
        """从FCD数据计算交通流参数"""
        print("正在计算交通流参数...")
        
        if 'fcd_data' not in self.data:
            print("缺少FCD数据")
            return
        
        fcd_df = self.data['fcd_data']
        
        # 按时间段和路段统计
        time_intervals = np.arange(0, 1600, 60)  # 60秒间隔
        
        traffic_stats = []
        
        for i in range(len(time_intervals) - 1):
            t_start = time_intervals[i]
            t_end = time_intervals[i + 1]
            
            # 获取时间段内的数据
            period_data = fcd_df[(fcd_df['time'] >= t_start) & (fcd_df['time'] < t_end)]
            
            if not period_data.empty:
                # 按路段统计
                for edge in period_data['edge'].unique():
                    edge_data = period_data[period_data['edge'] == edge]
                    
                    if not edge_data.empty:
                        # 计算车流量（通过的唯一车辆数）
                        vehicle_count = len(edge_data['id'].unique())
                        volume = vehicle_count * 60  # 转换为小时车流量
                        
                        # 计算平均速度
                        avg_speed = edge_data['speed'].mean() * 3.6  # 转换为km/h
                        
                        # 计算密度（时段内路段上的平均车辆数）
                        # 假设路段长度为500m
                        segment_length = 0.5  # km
                        avg_vehicles = len(edge_data) / len(edge_data['time'].unique()) if len(edge_data['time'].unique()) > 0 else 0
                        density = avg_vehicles / segment_length
                        
                        # 计算占有率（简化计算）
                        # 假设每辆车长5m，车道宽3.5m
                        vehicle_length = 0.005  # km
                        occupancy = (avg_vehicles * vehicle_length / segment_length) * 100
                        
                        traffic_stats.append({
                            'time_start': t_start,
                            'time_end': t_end,
                            'time_center': (t_start + t_end) / 2,
                            'edge': edge,
                            'volume': volume,
                            'avg_speed': avg_speed,
                            'density': density,
                            'occupancy': min(occupancy, 100)  # 占有率不超过100%
                        })
        
        traffic_df = pd.DataFrame(traffic_stats)
        self.data['traffic_stats'] = traffic_df
        
        # 计算各路段的统计结果
        results = {}
        if not traffic_df.empty:
            for edge in traffic_df['edge'].unique():
                edge_data = traffic_df[traffic_df['edge'] == edge]
                
                results[edge] = {
                    '平均车流量 (veh/h)': edge_data['volume'].mean(),
                    '最大车流量 (veh/h)': edge_data['volume'].max(),
                    '平均速度 (km/h)': edge_data['avg_speed'].mean(),
                    '平均密度 (veh/km)': edge_data['density'].mean(),
                    '平均占有率 (%)': edge_data['occupancy'].mean()
                }
        
        # 添加车头时距
        if 'trip_data' in self.data and not self.data['trip_data'].empty:
            trip_df = self.data['trip_data']
            avg_headway = trip_df['headway'][trip_df['headway'] > 0].mean()
            
            for edge in results:
                results[edge]['平均车头时距 (s)'] = avg_headway
        
        self.results = results
        
        # 打印结果
        print("\n=== 交通流参数统计 ===")
        for edge, params in results.items():
            print(f"\n路段: {edge}")
            for param, value in params.items():
                if not pd.isna(value):
                    print(f"  {param}: {value:.2f}")
    
    def generate_charts(self):
        """生成交通流图表"""
        print("正在生成交通流图表...")
        
        if 'traffic_stats' not in self.data:
            print("缺少交通统计数据，无法生成图表")
            return
        
        # 创建报告目录
        report_dir = "traffic_flow_reports"
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        traffic_df = self.data['traffic_stats']
        
        if traffic_df.empty:
            print("没有交通数据可用于生成图表")
            return
        
        # 1. 交通流参数时变图 - 优化为2x3布局
        plt.figure(figsize=(15, 10))
        
        # 车流量时变图
        plt.subplot(2, 3, 1)
        for edge in traffic_df['edge'].unique():
            edge_data = traffic_df[traffic_df['edge'] == edge]
            plt.plot(edge_data['time_center'], edge_data['volume'], 
                    marker='o', markersize=4, label=f'{edge}', linewidth=2)
        plt.title('车流量时变图', fontsize=14, fontweight='bold')
        plt.xlabel('时间 (s)')
        plt.ylabel('车流量 (veh/h)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # 速度时变图
        plt.subplot(2, 3, 2)
        for edge in traffic_df['edge'].unique():
            edge_data = traffic_df[traffic_df['edge'] == edge]
            plt.plot(edge_data['time_center'], edge_data['avg_speed'], 
                    marker='s', markersize=4, label=f'{edge}', linewidth=2)
        plt.title('平均速度时变图', fontsize=14, fontweight='bold')
        plt.xlabel('时间 (s)')
        plt.ylabel('速度 (km/h)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # 密度时变图
        plt.subplot(2, 3, 3)
        for edge in traffic_df['edge'].unique():
            edge_data = traffic_df[traffic_df['edge'] == edge]
            plt.plot(edge_data['time_center'], edge_data['density'], 
                    marker='^', markersize=4, label=f'{edge}', linewidth=2)
        plt.title('密度时变图', fontsize=14, fontweight='bold')
        plt.xlabel('时间 (s)')
        plt.ylabel('密度 (veh/km)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # 占有率时变图
        plt.subplot(2, 3, 4)
        for edge in traffic_df['edge'].unique():
            edge_data = traffic_df[traffic_df['edge'] == edge]
            plt.plot(edge_data['time_center'], edge_data['occupancy'], 
                    marker='d', markersize=4, label=f'{edge}', linewidth=2)
        plt.title('占有率时变图', fontsize=14, fontweight='bold')
        plt.xlabel('时间 (s)')
        plt.ylabel('占有率 (%)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # 速度-密度关系图
        plt.subplot(2, 3, 5)
        for edge in traffic_df['edge'].unique():
            edge_data = traffic_df[traffic_df['edge'] == edge]
            plt.scatter(edge_data['density'], edge_data['avg_speed'], 
                       alpha=0.7, s=50, label=f'{edge}')
        plt.title('速度-密度关系图', fontsize=14, fontweight='bold')
        plt.xlabel('密度 (veh/km)')
        plt.ylabel('速度 (km/h)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # 交通流效率分析图
        plt.subplot(2, 3, 6)
        # 计算各路段的流量-密度关系
        edge_efficiency = {}
        for edge in traffic_df['edge'].unique():
            edge_data = traffic_df[traffic_df['edge'] == edge]
            avg_volume = edge_data['volume'].mean()
            avg_density = edge_data['density'].mean()
            efficiency = avg_volume / max(avg_density, 0.1)  # 避免除零
            edge_efficiency[edge] = efficiency
        
        edges = list(edge_efficiency.keys())
        efficiencies = list(edge_efficiency.values())
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'][:len(edges)]
        
        bars = plt.bar(edges, efficiencies, color=colors, alpha=0.7, edgecolor='black')
        plt.title('各路段交通效率对比', fontsize=14, fontweight='bold')
        plt.xlabel('路段')
        plt.ylabel('效率 (veh/h)/(veh/km)')
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3, axis='y')
        
        # 在柱状图上添加数值标签
        for bar, efficiency in zip(bars, efficiencies):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(efficiencies)*0.01, 
                    f'{efficiency:.1f}', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        chart_path = os.path.join(report_dir, f'traffic_flow_analysis_{timestamp}.png')
        plt.savefig(chart_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"交通流图表已保存: {chart_path}")
        
        # 生成分路段对比图
        self._generate_comparison_charts(report_dir, timestamp)
        
        return chart_path
    
    def _generate_comparison_charts(self, report_dir, timestamp):
        """生成分路段对比图表"""
        if 'traffic_stats' not in self.data or self.data['traffic_stats'].empty:
            return
        
        traffic_df = self.data['traffic_stats']
        
        # 计算各路段的平均值
        edge_summary = traffic_df.groupby('edge').agg({
            'volume': 'mean',
            'avg_speed': 'mean',
            'density': 'mean',
            'occupancy': 'mean'
        }).round(2)
        
        plt.figure(figsize=(15, 8))
        
        # 1. 平均车流量对比
        plt.subplot(2, 2, 1)
        bars1 = edge_summary['volume'].plot(kind='bar', color='lightblue', alpha=0.8)
        plt.title('各路段平均车流量对比', fontsize=14, fontweight='bold')
        plt.xlabel('路段')
        plt.ylabel('车流量 (veh/h)')
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        
        # 2. 平均速度对比
        plt.subplot(2, 2, 2)
        bars2 = edge_summary['avg_speed'].plot(kind='bar', color='lightgreen', alpha=0.8)
        plt.title('各路段平均速度对比', fontsize=14, fontweight='bold')
        plt.xlabel('路段')
        plt.ylabel('速度 (km/h)')
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        
        # 3. 平均密度对比
        plt.subplot(2, 2, 3)
        bars3 = edge_summary['density'].plot(kind='bar', color='lightcoral', alpha=0.8)
        plt.title('各路段平均密度对比', fontsize=14, fontweight='bold')
        plt.xlabel('路段')
        plt.ylabel('密度 (veh/km)')
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        
        # 4. 平均占有率对比
        plt.subplot(2, 2, 4)
        bars4 = edge_summary['occupancy'].plot(kind='bar', color='lightyellow', alpha=0.8)
        plt.title('各路段平均占有率对比', fontsize=14, fontweight='bold')
        plt.xlabel('路段')
        plt.ylabel('占有率 (%)')
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        comparison_path = os.path.join(report_dir, f'edge_comparison_{timestamp}.png')
        plt.savefig(comparison_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"路段对比图表已保存: {comparison_path}")
    
    def save_results(self):
        """保存分析结果"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # 确保报告目录存在
        report_dir = "traffic_flow_reports"
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)
        
        # 保存为JSON格式
        json_file = os.path.join(report_dir, f"traffic_flow_results_{timestamp}.json")
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        
        print(f"分析结果已保存: {json_file}")
        
        # 保存为Excel格式
        try:
            excel_file = os.path.join(report_dir, f"traffic_flow_data_{timestamp}.xlsx")
            with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
                if 'traffic_stats' in self.data:
                    self.data['traffic_stats'].to_excel(writer, sheet_name='交通流统计', index=False)
                if 'fcd_data' in self.data:
                    # 只保存前1000行FCD数据（数据量较大）
                    sample_fcd = self.data['fcd_data'].head(1000)
                    sample_fcd.to_excel(writer, sheet_name='轨迹数据样本', index=False)
                if 'trip_data' in self.data:
                    self.data['trip_data'].to_excel(writer, sheet_name='行程数据', index=False)
                
                # 结果汇总
                if self.results:
                    results_df = pd.DataFrame(self.results).T
                    results_df.to_excel(writer, sheet_name='结果汇总')
            
            print(f"数据表格已保存: {excel_file}")
        except ImportError:
            print("警告: 无法保存Excel文件，请安装openpyxl")

def main():
    """主函数"""
    print("=== 交通流数据分析器 ===")
    
    # 首先运行仿真生成数据
    print("1. 运行仿真生成数据...")
    try:
        import subprocess
        result = subprocess.run([
            "sumo", 
            "-c", "highway-ramp-analysis.sumocfg"
        ], capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            print("仿真运行成功，开始分析数据...")
        else:
            print("仿真运行失败:")
            print(result.stderr)
            return
    except Exception as e:
        print(f"运行仿真时出错: {e}")
        return
    
    # 分析数据
    analyzer = TrafficFlowAnalyzer()
    
    print("\n2. 分析交通流数据...")
    analyzer.analyze_fcd_data()
    analyzer.analyze_trip_data()
    analyzer.calculate_traffic_parameters()
    
    print("\n3. 生成图表...")
    analyzer.generate_charts()
    
    print("\n4. 保存结果...")
    analyzer.save_results()
    
    print("\n交通流数据分析完成！")
    print("请查看生成的图表和数据文件。")

if __name__ == "__main__":
    main() 