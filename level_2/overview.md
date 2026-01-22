# Level 2（系统构建与工程化）课程概览

## 定位

**Level 2** 面向具备基本编码能力、希望把 LLM 用于真实业务系统交付的学习者。本 Level 聚焦：

*   **System Design**：把 AI 能力嵌入产品与服务架构（API/数据/权限/观测/成本）
*   **AI 应用开发**：RAG、Agent Workflow、多工具编排
*   **AI 辅助交付**：Vibe Coding/Agentic Coding 的方法论与质量控制

## 适合人群

*   有技术背景的初级/中级开发者
*   完成 Level 1 并希望进入“可上线系统”能力的学习者

## 先修要求

*   能独立完成 Python 项目（依赖管理、模块拆分、基础测试）
*   理解基本 Web 概念（HTTP/JSON）与工程概念（配置、日志、异常）
*   具备至少一次稳定调用 LLM 的经验（若无，建议先完成 Level 1 的 LLM 工程化部分）

## 教学周期与课时

*   **10 周**（可压缩到 8 周或扩展到 12 周）
*   每周 **5 课时**（建议：2 课时架构讲授 + 1 课时案例拆解 + 2 课时工程 Workshop）

## 核心能力支柱覆盖

*   **System Design（核心）**：RAG 系统分层、数据导入与索引、服务化、扩展性与可观测性
*   **AI 代码实操（进阶）**：LangChain/LlamaIndex、向量库（Chroma/Milvus 等）、rerank、工具调用
*   **Meta Learning（工程向）**：读框架源码/文档定位关键接口；用日志与 trace 定位 bug
*   **AI 概念（应用向）**：检索质量与幻觉成因；评估与反馈闭环的基本方法

## 学习产出（Learning Outcomes）

完成 Level 2 后，你应当能够：

1. 设计并实现端到端 RAG 系统：ETL -> Chunk -> Embedding -> Vector DB -> Retrieval -> Generation
2. 为 RAG 加入可解释性与质量控制：引用溯源、拒答/澄清、基本离线评测
3. 实现至少一种 Agent Workflow：规划/工具调用/状态管理/失败恢复
4. 将系统封装为可运行的服务（API + 配置 + 日志 + 基本测试），具备交付 Demo 的能力
5. 使用 AI 辅助开发提升交付效率，但能通过测试/审查保证代码质量

## 推荐技术栈（Level 2）

*   Python Web：FastAPI（推荐）
*   RAG 框架：LangChain 或 LlamaIndex（二选一即可）
*   向量库：Chroma（本地/轻量）或 Milvus（工程化/可扩展）
*   评测：Ragas（RAG 评测）或自建最小评测脚本
*   可观测性：结构化日志 + 请求 ID + 基本 trace（实现方式自定）

## 考核与评分建议（可选）

*   平时作业：35%
*   课堂 Lab/Workshop：25%
*   Capstone 项目：40%

## 结课门槛（Exit Criteria）

*   能交付一个端到端 RAG + Agent 的 Web 应用 Demo
*   系统具备基本的可解释性与失败策略（引用/拒答/降级）
*   有最小评测集与可复现评测脚本

## 文档导航

*   周计划：见 [weekly_plan_10w.md](weekly_plan_10w.md)
*   作业列表与要求：见 [assignments.md](assignments.md)
*   Capstone 项目说明：见 [capstone.md](capstone.md)
