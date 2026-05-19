# GeoSpatial-3D-Orchestrator
# GeoSpatial-3D-Orchestrator 

基于多 Agent 协同与自适应反思机制（Self-Reflection）的地理空间数据自动化三维可视化系统。

## 🚀 项目概述

在传统的 GIS 数据分析与 WebGL 开发中，从原始的空间数据（如 GeoJSON、遥感辐射数据、土壤理化性质指标）到前端高效的 3D 可视化渲染（Three.js），中间存在巨大的技术断层。开发者需要频繁切换于 Python 空间分析库与前端 JavaScript 代码之间，手动进行大量的坐标转换、数据清洗与渲染调试。

本项目旨在构建一个高度自动化的 **Multi-Agent 协同系统**，用户只需输入一句自然语言（如：“展示福州地铁线路的 3D 流向流光模型”），系统即可通过长链推理，自动完成空间数据抓取、格式化、Three.js 代码编写以及本地运行报错的自愈纠错（Reflection），实现全自动的任务闭环。

## 🛠️ 核心架构

项目采用多 Agent 协作流设计，核心模块包括：
1. **Master Orchestrator (主控 Agent)**：负责理解用户意图，拆解长链条的空间数据处理与可视化任务。
2. **GIS Data Agent (空间数据 Agent)**：负责调用地理信息计算工具，进行坐标转换（如 WGS84 到 Web Mercator）与数据清洗。
3. **Three.js Codegen Agent (WebGL 生成 Agent)**：底层由大语言模型（DeepSeek/Gemini）驱动，根据清洗后的空间数据自动构建 WebGL 场景与粒子系统。
4. **Reflection & Self-Healing Agent (反思纠错 Agent)**：实时捕获编译、运行或渲染阶段的报错，进行自适应的多轮推理与代码修正。

## 📂 项目结构

```text
GeoSpatial-3D-Orchestrator/
├── main.py                 # 主控 Master Orchestrator 核心入口
├── agents/                 # 核心 Agent 协同模块
│   ├── __init__.py
│   ├── gis_data_agent.py   # 空间数据处理 Agent
│   ├── threejs_agent.py    # WebGL/Three.js 代码生成 Agent
│   └── reflection_agent.py # 反思与自愈纠错 Agent
├── output/                 # 自动化生成的 3D 可视化成果存放地
├── requirements.txt        # 依赖环境
└── README.md               # 项目说明文档
