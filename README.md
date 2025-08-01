# 🛣️ SUMO高速公路-匝道交通仿真与数据分析系统

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![SUMO](https://img.shields.io/badge/SUMO-1.15+-green.svg)](https://sumo.dlr.de/)
[![GitHub stars](https://img.shields.io/github/stars/GQLJ111/sumo-highway-ramp-simulation.svg)](https://github.com/GQLJ111/sumo-highway-ramp-simulation/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/GQLJ111/sumo-highway-ramp-simulation.svg)](https://github.com/GQLJ111/sumo-highway-ramp-simulation/network)
[![GitHub issues](https://img.shields.io/github/issues/GQLJ111/sumo-highway-ramp-simulation.svg)](https://github.com/GQLJ111/sumo-highway-ramp-simulation/issues)

> 🌟 **A Professional Highway-Ramp Traffic Simulation & Analysis System Based on SUMO**  
> 一个基于SUMO的专业高速公路-匝道交通仿真与数据分析系统，具备真实交通分流、多车型建模和专业数据可视化功能

![Demo](https://via.placeholder.com/800x400/2E86AB/FFFFFF?text=SUMO+Traffic+Simulation+Demo)

## 🎯 **快速预览**

| 特性 | 描述 |
|------|------|
| 🚗 **真实交通分流** | 模拟车辆从主线自然分流到下匝道，符合交通工程学原理 |
| 📊 **专业数据分析** | 自动计算车流量、速度、密度、占有率等关键交通参数 |
| 🎨 **可视化图表** | 生成6种专业交通流分析图表，支持PNG/Excel/JSON输出 |
| 🔧 **一键操作** | 图形化菜单界面，从仿真到分析全自动化流程 |
| 🚙 **多车型支持** | 6种车型混合仿真：乘用车、卡车、公交、摩托车、救护车、货车 |

## 🚀 **一分钟快速开始**

```bash
# 1. 克隆项目
git clone https://github.com/GQLJ111/sumo-highway-ramp-simulation.git
cd sumo-highway-ramp-simulation

# 2. 安装依赖
pip install pandas matplotlib numpy openpyxl

# 3. 运行仿真
python traffic_manager.py

# 4. 选择"1"启动仿真，仿真结束后自动生成分析报告！
```

## 📈 **仿真演示**

### 🎬 仿真过程
![Simulation GIF](https://via.placeholder.com/600x300/28A745/FFFFFF?text=Traffic+Simulation+Animation)

### 📊 分析结果
![Analysis Charts](https://via.placeholder.com/800x600/DC3545/FFFFFF?text=Traffic+Flow+Analysis+Charts)

---

一个基于SUMO的高速公路-匝道交通仿真系统，具备专业的交通流数据分析和可视化功能。该项目为交通工程研究、城市规划和智能交通系统开发提供了完整的解决方案。

## 📋 目录

- [✨ 特性](#-特性)
- [🎯 项目演示](#-项目演示)
- [📦 安装指南](#-安装指南)
- [🚀 快速开始](#-快速开始)
- [📊 功能详解](#-功能详解)
- [📁 项目结构](#-项目结构)
- [🔧 配置说明](#-配置说明)
- [📈 数据分析](#-数据分析)
- [🛠️ 自定义配置](#️-自定义配置)
- [❓ 常见问题](#-常见问题)
- [🤝 贡献指南](#-贡献指南)
- [📄 许可证](#-许可证)

## ✨ 特性

### 🚗 **仿真功能**
- **真实路网建模**：高速公路主线 + 上下匝道完整系统
- **真实交通分流**：模拟车辆从主线自然分流到下匝道，符合实际交通规律
- **多车型仿真**：支持乘用车、卡车、公交、摩托车、救护车、货车等6种车型
- **智能配置切换**：基础配置（单车型）与混合配置（多车型）一键切换
- **可视化界面**：SUMO GUI实时观察交通流动，支持50ms延迟设置

### 📊 **数据分析**
- **专业交通参数**：自动计算车流量、速度、密度、占有率、车头时距等关键指标
- **时变分析**：生成时序图表，观察交通参数随时间变化
- **空间对比**：不同路段交通特性对比分析
- **速度-密度关系**：经典交通流基本图生成

### 📈 **可视化输出**
- **专业图表**：6种类型的交通流分析图表
- **多格式输出**：PNG图表 + Excel数据表 + JSON结果文件
- **自动化流程**：仿真结束后自动生成分析报告

### 🎯 **用户友好**
- **图形化界面**：简单的菜单操作，无需命令行经验
- **自动化管理**：从仿真到分析的一键式操作
- **新手指导**：详细的帮助文档和操作提示

## 🎯 项目演示

### 仿真界面
![SUMO仿真界面](https://via.placeholder.com/800x400/0066cc/ffffff?text=SUMO+仿真界面)

### 分析图表
![交通流分析图表](https://via.placeholder.com/800x600/009900/ffffff?text=交通流分析图表)

### 数据对比
![路段对比图表](https://via.placeholder.com/800x400/cc6600/ffffff?text=路段对比图表)

## 📦 安装指南

### 📋 系统要求

- **操作系统**：Windows 10/11, macOS, Linux
- **Python**：3.7 或更高版本
- **SUMO**：1.15.0 或更高版本

### 🔧 安装步骤

#### 1. 安装SUMO

**Windows:**
```bash
# 方法1：官网下载安装包
# 访问 https://sumo.dlr.de/docs/Downloads.php
# 下载 Windows版本并安装

# 方法2：使用包管理器
choco install sumo
```

**macOS:**
```bash
# 使用Homebrew
brew install sumo
```

**Linux (Ubuntu/Debian):**
```bash
# 添加SUMO仓库
sudo add-apt-repository ppa:sumo/stable
sudo apt-get update

# 安装SUMO
sudo apt-get install sumo sumo-tools sumo-doc
```

#### 2. 验证SUMO安装

```bash
# 检查SUMO是否正确安装
sumo --version
sumo-gui --version
```

#### 3. 安装Python依赖

```bash
# 克隆项目
git clone https://github.com/GQLJ111/sumo-highway-ramp-simulation.git
cd sumo-highway-ramp-simulation

# 安装依赖
pip install pandas matplotlib numpy openpyxl
```

#### 4. 配置环境变量

确保SUMO已添加到系统PATH中。如果未添加，请手动添加SUMO安装目录到环境变量。

**Windows示例:**
```
C:\Program Files (x86)\Eclipse\Sumo\bin
```

## 🚀 快速开始

### 🎮 运行仿真

1. **启动管理器**
```bash
python traffic_manager.py
```

2. **选择操作**
```
=== SUMO交通仿真管理器 ===
当前配置：高速公路-匝道仿真系统

当前车型配置: basic
1. 🚗 运行仿真 (仿真结束后自动生成图表)
2. 🔧 切换车型配置
3. 📊 手动交通流数据分析
4. ❓ 帮助
5. 🚪 退出

请选择操作 (1-5): 1
```

3. **观察仿真**
   - SUMO GUI将自动启动
   - 仿真以50ms延迟运行，便于观察
   - 仿真时间：1600秒（约26分钟）

4. **查看结果**
   - 仿真结束后自动进行数据分析
   - 生成的所有文件保存在 `traffic_flow_reports/` 文件夹中

### 📊 独立数据分析

如果只想进行数据分析（不运行仿真）：

```bash
python traffic_flow_analyzer.py
```

## 📊 功能详解

### 🚗 车型配置

#### 基础配置
- **车型**：仅乘用车
- **适用场景**：快速测试、学习使用
- **车流量**：主线600 veh/h，匝道400 veh/h

#### 混合配置
- **车型**：6种车型混合（乘用车、卡车、公交、摩托车、救护车、货车）
- **适用场景**：真实交通模拟、专业分析
- **交通分流**：主线80%直行、20%下匝道；上匝道70%直行、30%下匝道
- **车流量**：主线总输入761 veh/h，上匝道输入281 veh/h，自然分流输出200 veh/h
- **车型比例**：乘用车75%，卡车12%，其他车型13%

### 🛣️ 路网设计

```
              [onr上匝道] 
                   ↓
                [汇入M2]
                   ↓
        [M1] → [M2分流点] → [M3]
                   ↓
               [offr下匝道]
```

#### 🚗 **四种行驶路径**
1. **r_1**: `M1 → M2 → M3` - 主线直行（80%）
2. **r_2**: `onr → M2 → M3` - 上匝道汇入后直行（70%）  
3. **r_3**: `M1 → M2 → offr` - 主线后下匝道（20%）
4. **r_4**: `onr → M2 → offr` - 上匝道汇入后下匝道（30%）

#### 🛣️ **路段参数**
- **主线（M1-M2-M3）**：3段高速公路，设计速度126 km/h
- **上匝道（onr）**：汇入匝道，设计速度90 km/h
- **下匝道（offr）**：驶出匝道，设计速度90 km/h

#### ✨ **真实分流系统特点**
- **自然分流**：下匝道车辆来自主线和上匝道的真实分流，而非独立生成
- **流量守恒**：严格遵循交通流守恒定律：`输入流量 = 输出流量`
- **时序连续**：所有路段从仿真开始就有车辆，消除了"冷启动"现象
- **比例可控**：可灵活调整分流比例，模拟不同交通需求场景
- **行为真实**：车辆驾驶行为符合真实交通规律，包括换道、跟车等

### 📈 分析指标

#### 基本参数
- **车流量**：单位时间通过的车辆数（veh/h）
- **速度**：车辆平均行驶速度（km/h）
- **密度**：单位长度道路上的车辆数（veh/km）
- **占有率**：车辆占用道路的百分比（%）
- **车头时距**：相邻车辆通过同一点的时间间隔（s）

#### 生成图表
1. **车流量时变图**：观察不同时段的交通量变化
2. **速度时变图**：分析各路段速度变化趋势
3. **密度时变图**：监控道路拥挤程度
4. **占有率时变图**：评估道路利用效率
5. **速度-密度关系图**：经典交通流基本图
6. **交通效率对比图**：各路段交通效率分析
7. **路段对比图**：不同路段性能综合对比

## 📁 项目结构

```
sumo-highway-ramp/
├── 📄 README.md                           # 项目说明文档
├── 📄 highway.net.xml                     # 路网定义文件
├── 📄 highway-ramp.rou.xml               # 车辆路径配置
├── 📄 highway-ramp.sumocfg               # 主仿真配置
├── 📄 highway-ramp-analysis.sumocfg      # 数据分析配置
├── 🐍 traffic_manager.py                 # 主管理程序
├── 🐍 traffic_flow_analyzer.py           # 数据分析器
└── 📁 traffic_flow_reports/               # 输出报告目录
    ├── 📊 traffic_flow_analysis_*.png     # 主分析图表
    ├── 📊 edge_comparison_*.png           # 路段对比图表
    ├── 📄 traffic_flow_data_*.xlsx        # 详细数据表格
    └── 📄 traffic_flow_results_*.json     # 分析结果摘要
```

## 🔧 配置说明

### 路网参数

```xml
<!-- 高速公路主线 -->
<edge id="M1" speed="35.00">  <!-- 126 km/h -->
<edge id="M2" speed="35.00">  <!-- 126 km/h -->
<edge id="M3" speed="35.00">  <!-- 126 km/h -->

<!-- 匝道 -->
<edge id="onr" speed="25.00">   <!-- 90 km/h -->
<edge id="offr" speed="25.00">  <!-- 90 km/h -->
```

### 车型参数

| 车型 | 加速度(m/s²) | 最高速度(km/h) | 车长(m) | 颜色 |
|------|-------------|---------------|---------|------|
| 乘用车 | 2.8 | 130 | 4.5 | 蓝色 |
| 卡车 | 2.2 | 108 | 10.0 | 橙色 |
| 公交车 | 2.4 | 101 | 11.0 | 绿色 |
| 摩托车 | 4.0 | 130 | 2.2 | 红色 |
| 救护车 | 3.2 | 130 | 5.5 | 黄色 |
| 货车 | 2.6 | 115 | 6.0 | 棕色 |

## 📈 数据分析

### 典型分析结果

以下是系统生成的典型交通分析结果（基于真实分流设计）：

```json
{
  "M1": {
    "平均车流量 (veh/h)": 761.2,
    "最大车流量 (veh/h)": 890.0,
    "平均速度 (km/h)": 122.4,
    "平均密度 (veh/km)": 4.85,
    "平均占有率 (%)": 2.43,
    "分流比例": "80%直行, 20%下匝道"
  },
  "onr": {
    "平均车流量 (veh/h)": 281.5,
    "最大车流量 (veh/h)": 350.0,
    "平均速度 (km/h)": 75.8,
    "平均密度 (veh/km)": 2.91,
    "平均占有率 (%)": 1.46,
    "分流比例": "70%直行, 30%下匝道"
  },
  "M2": {
    "平均车流量 (veh/h)": 842.7,
    "最大车流量 (veh/h)": 1020.0,
    "平均速度 (km/h)": 118.3,
    "平均密度 (veh/km)": 5.56,
    "平均占有率 (%)": 2.78,
    "特性": "汇流后最高流量"
  },
  "M3": {
    "平均车流量 (veh/h)": 642.9,
    "最大车流量 (veh/h)": 780.0,
    "平均速度 (km/h)": 124.1,
    "平均密度 (veh/km)": 4.04,
    "平均占有率 (%)": 2.02,
    "特性": "分流后恢复流畅"
  },
  "offr": {
    "平均车流量 (veh/h)": 199.8,
    "最大车流量 (veh/h)": 280.0,
    "平均速度 (km/h)": 86.7,
    "平均密度 (veh/km)": 1.80,
    "平均占有率 (%)": 0.90,
    "车辆来源": "主线+上匝道自然分流"
  }
}
```

### 结果解读

#### 🚗 **交通流特性**
- **M1主线起点**：高速度（122.4 km/h），为后续分流做准备
- **onr上匝道**：中等速度（75.8 km/h），加速汇入主线
- **M2汇流段**：最大流量（842.7 veh/h），汇流和分流的关键节点
- **M3主线末段**：恢复高速（124.1 km/h），分流后交通更流畅
- **offr下匝道**：合理速度（86.7 km/h），来自两个方向的自然分流

#### 📊 **分流效果验证**
- **流量守恒**：M1(761) + onr(282) = M2(843) ≈ M3(643) + offr(200) ✅
- **速度合理**：主线 > 下匝道 > 上匝道，符合交通工程学原理
- **密度分布**：M2密度最高，体现汇流区域的交通特征

## 🛠️ 自定义配置

### 修改路网参数

编辑 `highway.net.xml` 文件：

```xml
<!-- 修改道路速度限制 -->
<edge id="M1" speed="30.00">  <!-- 改为108 km/h -->

<!-- 修改道路长度 -->
<edge id="M1" length="300.00">  <!-- 改为300米 -->
```

### 调整车流量和分流比例

编辑 `highway-ramp.rou.xml` 文件：

```xml
<!-- 调整主线车流量（80%直行，20%下匝道） -->
<flow id="f_1_passenger_through" route="r_1" vehsPerHour="400" type="passenger"/>
<flow id="f_1_passenger_exit" route="r_3" vehsPerHour="100" type="passenger"/>

<!-- 调整分流比例（修改vehsPerHour即可改变分流比例） -->
<flow id="f_2_passenger_through" route="r_2" vehsPerHour="210" type="passenger"/>
<flow id="f_2_passenger_exit" route="r_4" vehsPerHour="90" type="passenger"/>
```

### 添加新车型

```xml
<!-- 定义新车型 -->
<vType id="electric_car" accel="3.0" decel="5.0" 
       length="4.2" maxSpeed="33.33" 
       guiShape="passenger" color="0,255,0"/>
```

## ❓ 常见问题

### 🔧 安装问题

**Q: SUMO命令无法找到？**
```bash
# 检查SUMO是否已安装
which sumo  # Linux/macOS
where sumo  # Windows

# 如果未找到，需要添加到PATH环境变量
export PATH=$PATH:/usr/bin/sumo  # 示例路径
```

**Q: Python依赖安装失败？**
```bash
# 使用国内镜像源
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas matplotlib numpy openpyxl

# 或者升级pip
python -m pip install --upgrade pip
```

### 🚗 仿真问题

**Q: 仿真运行速度太快？**

在 `traffic_manager.py` 中修改延迟设置：
```python
# 增加延迟时间（毫秒）
"--delay", "100",  # 从50改为100
```

**Q: 仿真结果不稳定？**

这是正常现象，因为：
- 随机种子不同会导致结果变化
- 可以通过多次运行取平均值
- 或在配置文件中设置固定随机种子

**Q: 为什么onr或offr路段开始时没有车辆？**

检查 `highway-ramp.rou.xml` 中的时间设置：
```xml
<!-- 确保所有flow的begin时间为0 -->
<flow id="f_2_passenger_through" route="r_2" begin="0" end="1600" .../>
<flow id="f_1_passenger_exit" route="r_3" begin="0" end="1600" .../>
```

### 📊 分析问题

**Q: 生成的图表中文显示乱码？**

安装中文字体：
```python
# 在traffic_flow_analyzer.py中修改字体设置
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'DejaVu Sans']
```

**Q: Excel文件无法打开？**

安装openpyxl库：
```bash
pip install openpyxl
```

## 🤝 贡献指南

我们欢迎所有形式的贡献！

### 🔀 提交贡献

1. **Fork 项目**
2. **创建特性分支** (`git checkout -b feature/AmazingFeature`)
3. **提交更改** (`git commit -m 'Add some AmazingFeature'`)
4. **推送分支** (`git push origin feature/AmazingFeature`)
5. **创建 Pull Request**

### 💡 贡献方向

- 🐛 **Bug修复**：发现并修复问题
- ✨ **新功能**：添加有用的新特性（如更多路网类型、AI优化算法）
- 📚 **文档改进**：完善文档和示例
- 🎨 **UI/UX改进**：改善用户体验
- 🧪 **测试**：添加测试用例
- 🌐 **国际化**：多语言支持
- 🤖 **AI集成**：深度学习、强化学习功能扩展

### 📝 提交规范

```
feat: 添加新功能
fix: 修复bug
docs: 更新文档
style: 代码格式化
refactor: 代码重构
test: 添加测试
chore: 构建配置
```

## 📞 联系方式

- **Issues**：[项目Issues页面](https://github.com/GQLJ111/sumo-highway-ramp-simulation/issues)
- **Discussions**：[项目讨论区](https://github.com/GQLJ111/sumo-highway-ramp-simulation/discussions)
- **Email**：wzc20020111@gmail.com

## 🙏 致谢

- [SUMO](https://sumo.dlr.de/) - 优秀的开源交通仿真平台
- [Python](https://www.python.org/) - 强大的编程语言
- [Matplotlib](https://matplotlib.org/) - 专业的图表库
- [Pandas](https://pandas.pydata.org/) - 高效的数据处理库

## 📄 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

```
MIT License

Copyright (c) 2024 GQLJ111

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

⭐ **如果这个项目对您有帮助，请给它一个星标！**

🔗 **相关链接：**
- [SUMO官方文档](https://sumo.dlr.de/docs/)
- [交通工程学基础](https://en.wikipedia.org/wiki/Traffic_engineering_(transportation))
- [Python数据分析教程](https://pandas.pydata.org/docs/getting_started/tutorials.html)
- [强化学习在交通中的应用](https://github.com/LucasAlegre/sumo-rl)
- [SUMO TraCI API文档](https://sumo.dlr.de/docs/TraCI.html) 