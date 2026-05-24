# chinese-poetry-visualizer
基于AI大模型的中华传统诗词可视化、知识图谱构建与场景还原系统
# 🏯 诗境 (ShiJing)

> 中华传统诗词可视化系统

基于AI大模型的古诗文深度赏析、知识图谱构建与场景还原平台，致力于让中华诗词"可看、可游、可关联"。

## ✨ 核心功能

### 📜 智能诗词深度赏析
- 基于 Xiaomi MiMo-V2.5 的古诗文结构化解析
- 自动生成精准翻译、艺术手法分析、主题情感解读
- 支持《全唐诗》《全宋词》等古籍批量处理

### 🗺️ 地理场景还原
- 从诗词中智能提取古地名
- 匹配现代地理坐标
- AI生图技术重现历史场景

### 🕸️ 知识图谱构建
- 诗人-作品-地点-主题多维关系网络
- 交互式可视化探索
- 支持200+位诗人、3000+首诗词关联

### ⏳ 时空演变可视化
- 时间轴展示千年文化积淀
- 同一地点的文学意象演变
- 诗人足迹追踪与交游网络

## 🛠️ 技术栈

- **AI模型**: Xiaomi MiMo-V2.5-Pro
- **后端**: FastAPI + Python
- **前端**: React + Three.js + D3.js
- **数据存储**: PostgreSQL + PostGIS
- **图谱引擎**: NetworkX + PyVis

## 📁 项目结构
shijing/
├── core/ # 核心实体定义
│ ├── poem.py # 诗词实体
│ ├── author.py # 诗人画像
│ ├── location.py # 地理坐标
│ └── dynasty.py # 朝代时空
├── engine/ # AI智能引擎
│ ├── analyzer.py # 赏析引擎
│ ├── translator.py # 诗意翻译
│ ├── relation.py # 关系挖掘
│ └── scene.py # 场景还原
├── visual/ # 可视化引擎
│ ├── graph.py # 知识图谱
│ ├── timeline.py # 时间长河
│ ├── map.py # 地理漫游
│ └── gallery.py # 诗画长廊
├── storage/ # 数据存储
└── utils/ # 工具类

## 🚀 快速开始

```python
from shijing.engine.analyzer import PoetryAnalyzer

# 初始化赏析引擎
analyzer = PoetryAnalyzer("your-mimo-api-key")

# 分析一首诗
poem = await analyzer.analyze_full(
    title="登高",
    author="杜甫",
    dynasty="唐",
    content="""风急天高猿啸哀，渚清沙白鸟飞回。
    无边落木萧萧下，不尽长江滚滚来。"""
)

print(poem.translation)  # 译文
print(poem.artistic_conception)  # 艺术境界
