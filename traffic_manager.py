#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SUMO交通仿真管理器
提供仿真运行、车型配置和数据分析功能
"""

import subprocess
import os
import sys

class SimpleTrafficManager:
    def __init__(self):
        """初始化交通管理器"""
        self.current_config = "basic"
        
    def run_simulation(self):
        """运行SUMO仿真（带GUI界面）"""
        try:
            print("🚀 启动SUMO仿真...")
            print("注意：仿真结束后将自动进行数据分析并生成图表")
            
            # 运行SUMO GUI仿真
            result = subprocess.run([
                "sumo-gui", 
                "-c", "highway-ramp.sumocfg",
                "--delay", "50",
                "--step-length", "0.1"
            ], check=True)
            
            print("✅ 仿真运行完成！")
            
            # 仿真结束后自动进行数据分析
            print("\n🔄 仿真结束，开始自动数据分析...")
            self.auto_analyze_traffic_flow()
            
        except subprocess.CalledProcessError as e:
            print(f"❌ 仿真运行失败: {e}")
        except FileNotFoundError:
            print("❌ 找不到SUMO程序，请检查SUMO是否正确安装")
        except Exception as e:
            print(f"❌ 运行出错: {e}")
    
    def auto_analyze_traffic_flow(self):
        """自动运行交通流数据分析"""
        try:
            print("📊 正在进行交通流数据分析...")
            
            # 运行数据分析器
            result = subprocess.run([
                sys.executable, "traffic_flow_analyzer.py"
            ], capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                print("✅ 数据分析完成！")
                print("\n📈 生成的图表文件：")
                
                # 检查生成的图表文件
                reports_dir = "traffic_flow_reports"
                if os.path.exists(reports_dir):
                    for file in os.listdir(reports_dir):
                        if file.endswith('.png'):
                            print(f"  📊 {file}")
                
                print("\n🎯 分析结果已保存到 traffic_flow_reports/ 文件夹：")
                print("  • *.png 图表文件 - 可视化图表")
                print("  • *.xlsx 数据表格 - 详细数据")
                print("  • *.json 分析结果 - 统计摘要")
                
                # 询问是否自动打开图表
                try:
                    choice = input("\n是否自动打开生成的图表？(y/n): ").strip().lower()
                    if choice == 'y':
                        self.open_latest_charts()
                except KeyboardInterrupt:
                    print("\n跳过打开图表")
                    
            else:
                print("❌ 数据分析失败:")
                print(result.stderr)
                
        except subprocess.TimeoutExpired:
            print("❌ 数据分析超时")
        except Exception as e:
            print(f"❌ 数据分析出错: {e}")
    
    def open_latest_charts(self):
        """打开最新生成的图表"""
        try:
            reports_dir = "traffic_flow_reports"
            if os.path.exists(reports_dir):
                # 获取最新的图表文件
                chart_files = [f for f in os.listdir(reports_dir) if f.endswith('.png')]
                chart_files.sort(reverse=True)  # 按文件名降序排列，最新的在前
                
                opened_files = []
                for file in chart_files:
                    if len(opened_files) < 2:  # 最多打开2个最新的图表
                        file_path = os.path.join(reports_dir, file)
                        try:
                            if os.name == 'nt':  # Windows
                                os.startfile(file_path)
                            else:  # Linux/Mac
                                subprocess.run(['xdg-open', file_path])
                            opened_files.append(file)
                        except Exception:
                            pass
                
                if opened_files:
                    print(f"📊 已打开图表: {', '.join(opened_files)}")
                else:
                    print("❌ 无法打开图表文件")
            else:
                print("❌ 未找到图表文件夹")
                
        except Exception as e:
            print(f"❌ 打开图表时出错: {e}")

    def analyze_traffic_flow(self):
        """手动运行交通流数据分析"""
        try:
            print("📊 开始交通流数据分析...")
            choice = input("是否继续进行数据分析？这将运行仿真并生成图表 (y/n): ").strip().lower()
            
            if choice == 'y':
                print("正在运行交通流分析...")
                
                # 运行数据分析器
                result = subprocess.run([
                    sys.executable, "traffic_flow_analyzer.py"
                ], check=True)
                
                print("✅ 交通流数据分析完成！")
                print("请查看生成的图表和数据文件。")
            else:
                print("已取消数据分析")
                
        except subprocess.CalledProcessError as e:
            print(f"❌ 数据分析失败: {e}")
        except Exception as e:
            print(f"❌ 分析出错: {e}")

    def switch_vehicle_config(self):
        """切换车辆配置"""
        print(f"\n当前配置: {self.current_config}")
        print("1. 基础配置 (单一车型)")
        print("2. 混合配置 (多种车型)")
        
        try:
            choice = input("请选择配置 (1/2): ").strip()
            
            if choice == "1":
                self.set_basic_config()
                self.current_config = "basic"
                print("✅ 已切换到基础配置")
            elif choice == "2":
                self.set_mixed_config()
                self.current_config = "mixed"
                print("✅ 已切换到混合配置")
            else:
                print("❌ 无效选择")
        except KeyboardInterrupt:
            print("\n已取消配置切换")

    def set_basic_config(self):
        """设置基础车辆配置"""
        basic_config = '''<?xml version="1.0" encoding="UTF-8"?>

<routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/routes_file.xsd">

    <!-- 车辆类型定义 -->
    <vType id="passenger" accel="2.6" decel="4.5" sigma="0.5" length="4.5" minGap="2.5" maxSpeed="36.11" guiShape="passenger" color="1,0,0"/>

    <!-- 路径定义 -->
    <route id="r_1" edges="M1 M2 M3"/>
    <route id="r_2" edges="onr M2 M3"/>

    <!-- 交通流定义 -->
    <flow id="f_1" route="r_1" begin="0" end="1600" vehsPerHour="600" type="passenger"/>
    <flow id="f_2" route="r_2" begin="200" end="1400" vehsPerHour="400" type="passenger"/>

</routes>'''
        
        with open("highway-ramp.rou.xml", "w", encoding="utf-8") as f:
            f.write(basic_config)

    def set_mixed_config(self):
        """设置混合车辆配置"""
        mixed_config = '''<?xml version="1.0" encoding="UTF-8"?>

<routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/routes_file.xsd">

    <!-- 车辆类型定义 - 优化版 -->
    <vType id="passenger" accel="2.8" decel="4.5" sigma="0.4" length="4.5" minGap="2.5" maxSpeed="36.11" guiShape="passenger" color="0,100,255"/>
    <vType id="truck" accel="2.2" decel="3.5" sigma="0.3" length="10.0" minGap="2.5" maxSpeed="30.00" guiShape="truck" color="255,165,0"/>
    <vType id="bus" accel="2.4" decel="4.0" sigma="0.3" length="11.0" minGap="2.5" maxSpeed="28.00" guiShape="bus" color="0,128,0"/>
    <vType id="motorcycle" accel="4.0" decel="6.5" sigma="0.5" length="2.2" minGap="1.2" maxSpeed="36.11" guiShape="motorcycle" color="255,0,0"/>
    <vType id="emergency" accel="3.2" decel="5.5" sigma="0.2" length="5.5" minGap="2.0" maxSpeed="36.11" guiShape="emergency" color="255,255,0"/>
    <vType id="delivery" accel="2.6" decel="4.2" sigma="0.3" length="6.0" minGap="2.0" maxSpeed="32.00" guiShape="delivery" color="139,69,19"/>

    <!-- 路径定义 -->
    <route id="r_1" edges="M1 M2 M3"/>              <!-- 主线直行 -->
    <route id="r_2" edges="onr M2 M3"/>             <!-- 上匝道汇入后直行 -->
    <route id="r_3" edges="M1 M2 offr"/>            <!-- 主线后下匝道 -->
    <route id="r_4" edges="onr M2 offr"/>           <!-- 上匝道汇入后下匝道 -->

    <!-- 主线车流 - 80%直行，20%下匝道 -->
    <!-- 主线直行流量 (M1-M2-M3) -->
    <flow id="f_1_passenger_through" route="r_1" begin="0" end="1600" vehsPerHour="336" type="passenger"/>
    <flow id="f_1_truck_through" route="r_1" begin="0" end="1600" vehsPerHour="72" type="truck"/>
    <flow id="f_1_bus_through" route="r_1" begin="0" end="1600" vehsPerHour="24" type="bus"/>
    <flow id="f_1_motorcycle_through" route="r_1" begin="0" end="1600" vehsPerHour="29" type="motorcycle"/>
    <flow id="f_1_emergency_through" route="r_1" begin="0" end="1600" vehsPerHour="5" type="emergency"/>
    <flow id="f_1_delivery_through" route="r_1" begin="0" end="1600" vehsPerHour="14" type="delivery"/>

    <!-- 主线分流到下匝道 (M1-M2-offr) -->
    <flow id="f_1_passenger_exit" route="r_3" begin="0" end="1600" vehsPerHour="84" type="passenger"/>
    <flow id="f_1_truck_exit" route="r_3" begin="0" end="1600" vehsPerHour="18" type="truck"/>
    <flow id="f_1_bus_exit" route="r_3" begin="0" end="1600" vehsPerHour="6" type="bus"/>
    <flow id="f_1_motorcycle_exit" route="r_3" begin="0" end="1600" vehsPerHour="7" type="motorcycle"/>
    <flow id="f_1_emergency_exit" route="r_3" begin="0" end="1600" vehsPerHour="1" type="emergency"/>
    <flow id="f_1_delivery_exit" route="r_3" begin="0" end="1600" vehsPerHour="4" type="delivery"/>

    <!-- 上匝道车流 - 70%直行，30%下匝道 -->
    <!-- 上匝道直行流量 (onr-M2-M3) -->
    <flow id="f_2_passenger_through" route="r_2" begin="0" end="1600" vehsPerHour="210" type="passenger"/>
    <flow id="f_2_truck_through" route="r_2" begin="0" end="1600" vehsPerHour="21" type="truck"/>
    <flow id="f_2_bus_through" route="r_2" begin="0" end="1600" vehsPerHour="7" type="bus"/>
    <flow id="f_2_motorcycle_through" route="r_2" begin="0" end="1600" vehsPerHour="25" type="motorcycle"/>
    <flow id="f_2_emergency_through" route="r_2" begin="0" end="1600" vehsPerHour="4" type="emergency"/>
    <flow id="f_2_delivery_through" route="r_2" begin="0" end="1600" vehsPerHour="14" type="delivery"/>

    <!-- 上匝道分流到下匝道 (onr-M2-offr) -->
    <flow id="f_2_passenger_exit" route="r_4" begin="0" end="1600" vehsPerHour="90" type="passenger"/>
    <flow id="f_2_truck_exit" route="r_4" begin="0" end="1600" vehsPerHour="9" type="truck"/>
    <flow id="f_2_bus_exit" route="r_4" begin="0" end="1600" vehsPerHour="3" type="bus"/>
    <flow id="f_2_motorcycle_exit" route="r_4" begin="0" end="1600" vehsPerHour="10" type="motorcycle"/>
    <flow id="f_2_emergency_exit" route="r_4" begin="0" end="1600" vehsPerHour="1" type="emergency"/>
    <flow id="f_2_delivery_exit" route="r_4" begin="0" end="1600" vehsPerHour="6" type="delivery"/>

</routes>'''
        
        with open("highway-ramp.rou.xml", "w", encoding="utf-8") as f:
            f.write(mixed_config)

    def show_help(self):
        """显示帮助信息"""
        help_text = """
=== SUMO高速公路-匝道仿真系统帮助 ===

功能说明：
1. 🚗 运行仿真 - 启动SUMO GUI界面进行交通仿真
   • 自动设置50ms延迟，便于观察
   • 仿真结束后自动进行数据分析
   • 自动生成交通流图表

2. 🔧 切换车型配置 - 在不同车辆配置间切换
   • 基础配置：单一乘用车类型
   • 混合配置：6种车型混合（乘用车、卡车、公交、摩托车、救护车、货车）

3. 📊 交通流数据分析 - 手动运行数据分析
   • 提取断面车流量、占有率、车头时距、平均速度
   • 生成专业的交通流时变图表
   • 输出速度-密度关系图
   • 保存Excel和JSON格式数据

系统特点：
• 路网包含高速公路主线(120-130km/h)和匝道(90km/h)
• 支持多种车型的真实交通仿真
• 自动化数据分析和可视化
• 生成专业的交通工程图表

使用建议：
1. 首次使用建议选择"基础配置"熟悉系统
2. 仿真运行时可通过GUI界面控制播放速度
3. 仿真结束后系统会自动分析数据并询问是否打开图表
4. 所有分析结果保存在traffic_flow_reports/文件夹中

注意事项：
• 请确保SUMO软件已正确安装
• 仿真时间约26分钟(1600秒)
• 数据分析需要1-2分钟时间
"""
        print(help_text)

    def run(self):
        """运行管理器主循环"""
        print("=== SUMO交通仿真管理器 ===")
        print("当前配置：高速公路-匝道仿真系统")
        
        while True:
            try:
                print(f"\n当前车型配置: {self.current_config}")
                print("1. 🚗 运行仿真 (仿真结束后自动生成图表)")
                print("2. 🔧 切换车型配置")
                print("3. 📊 手动交通流数据分析")
                print("4. ❓ 帮助")
                print("5. 🚪 退出")
                
                choice = input("\n请选择操作 (1-5): ").strip()
                
                if choice == "1":
                    self.run_simulation()
                elif choice == "2":
                    self.switch_vehicle_config()
                elif choice == "3":
                    self.analyze_traffic_flow()
                elif choice == "4":
                    self.show_help()
                elif choice == "5":
                    print("👋 再见！")
                    break
                else:
                    print("❌ 无效选择，请输入1-5")
                    
            except KeyboardInterrupt:
                print("\n\n👋 程序已退出")
                break
            except Exception as e:
                print(f"❌ 发生错误: {e}")

if __name__ == "__main__":
    manager = SimpleTrafficManager()
    manager.run() 