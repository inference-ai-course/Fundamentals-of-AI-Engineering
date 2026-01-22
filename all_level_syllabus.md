# 全栈 AI 工程师进阶课程大纲 (循序渐进版)

本课纲采用**循序渐进 (Sequential Progression)** 的设计思路，将四大能力支柱（概念、代码、Meta学习、系统设计）分阶段重点突破。不再是每一阶段“雨露均沾”，而是根据学习曲线，在不同阶段聚焦不同的核心能力。

---

## 阶段概览 (Progression Overview)

| 阶段 | 核心聚焦 (Focus Pillars) | 关键目标 (Key Goal) |
| :--- | :--- | :--- |
| **Level 1** | **AI 基础概念 + Python 实操** | 打好地基：懂原理，会写 Python，能调通 API。 |
| **Level 2** | **系统设计 + AI 应用开发** | 构建系统：掌握 RAG/Agent，熟练运用 Vibe Coding 快速产出。 |
| **Level 3** | **深度微调 + Meta Learning** | 深度优化：掌握微调/评估，具备科研级的自学与解决问题能力。 |

### 教学周期与课时 (Delivery Format)

*   每个 Level 设计为 **10 周**（可压缩到 **8 周** 或扩展到 **12 周**）。
*   每周 **5 课时**（建议拆分为：3 课时讲授/讨论 + 2 课时 Lab/Workshop）。
*   每个 Level 结束包含 1 个可验收的 Capstone/Project。

### 文件结构 (Productized Syllabus Files)

*   Level 1（基础夯实）:
    *   [overview.md](level_1/overview.md)
    *   [weekly_plan_10w.md](level_1/weekly_plan_10w.md)
    *   [assignments.md](level_1/assignments.md)
    *   [capstone.md](level_1/capstone.md)
*   Level 2（系统构建）:
    *   [overview.md](level_2/overview.md)
    *   [weekly_plan_10w.md](level_2/weekly_plan_10w.md)
    *   [assignments.md](level_2/assignments.md)
    *   [capstone.md](level_2/capstone.md)
*   Level 3（深度优化）:
    *   [overview.md](level_3/overview.md)
    *   [weekly_plan_10w.md](level_3/weekly_plan_10w.md)
    *   [assignments.md](level_3/assignments.md)
    *   [capstone.md](level_3/capstone.md)

### 分流建议 (Tracks / Placement)

| 人群 | 建议起点 | 进入标准 (建议) | 目标路径 |
| :--- | :--- | :--- | :--- |
| **非技术背景小白** | Level 1 | 会使用命令行基础；能写简单 Python 脚本（变量/循环/函数）；能读英文文档的“用法章节” | Level 1 -> Level 2 -> Level 3 |
| **有技术背景的初级开发者** | Level 1 或 Level 2 | 熟悉 Git/HTTP/SQL 任意其一；能完成一个小型 Web/脚本项目 | Level 1（快速通关）-> Level 2 -> Level 3 |
| **有经验的高级开发者** | Level 2 或 Level 3 | 熟悉系统设计与工程化；能独立 Debug；有生产环境交付经验 | Level 2（补齐 LLM/RAG/Agent）-> Level 3（深度优化） |

### 毕业能力矩阵 (Graduation Competency Matrix)

完成全部 Level 后，学员应同时具备以下 4 项能力：

| 能力支柱 | 毕业要求 (可观察行为) |
| :--- | :--- |
| **1. AI 概念** | 能解释 ML/LLM 训练与推理的关键概念（损失/泛化/Token/上下文/对齐）；能根据任务选择合适的微调/评估策略 |
| **2. AI 代码实操** | 能用 Python 熟练使用主流开源栈实现推理、RAG、Agent、微调、评测与部署（含可复现环境、脚本化流水线） |
| **3. Meta Learning** | 能读源码/文档定位关键接口；能用日志与最小复现 Debug；遇到新技术能自建学习路径并产出验证 Demo |
| **4. System Design + AI 辅助交付** | 能把需求拆成架构与模块边界；能用 Agent Workflow/Vibe Coding 提升交付效率；能完成端到端可上线的 AI 项目 |

---

## Level 1: 基础夯实阶段 (The Foundation)
**核心支柱**: `1. AI 基础概念` & `2. AI 代码实操 (基础)`
**侧重**: 建立对数据、模型的基本直觉，熟练掌握 Python 数据生态。

**适合人群**: 非技术背景小白；或希望系统补齐 AI 基础的开发者。
**结课门槛 (Exit Criteria)**:
*   能独立完成一个带配置、日志、错误处理的 Python 小项目。
*   能解释训练/验证/过拟合与常见指标的含义，并做出基本的实验对比。
*   能稳定调用至少一种在线 LLM API 与一种本地推理方案。

### Module 1.1: 数据与机器学习基石
*   **目标**: 理解“机器是如何学习的”。
*   **内容**:
    *   **Python AI 栈**: 熟练使用 NumPy (张量概念铺垫), Pandas (数据处理)。
    *   **传统 ML 概念**: 必须掌握的“损失函数”、“梯度下降”、“过拟合/泛化”、“训练集/验证集”概念。（*这是理解后续 LLM 训练的基础*）
    *   **实操**: 手写一个简单的线性回归或使用 Scikit-learn 完成一个分类任务。
    *   **Meta Skill (基础)**: 学会查阅 Python 库的官方文档 (Docs Reading)。

*   **教程 (Theory / Tutorial)**:
    *   数据表示：标量/向量/矩阵/张量；常见数据类型与缺失值。
    *   训练闭环：数据切分、特征工程直觉、训练/验证、指标选择（Accuracy/F1/ROC-AUC）。
    *   最小可复现实验：固定随机种子、记录实验配置、对比基线。
*   **Lab (Hands-on)**:
    *   用 `scikit-learn` 训练二分类模型并输出混淆矩阵与分类报告。
    *   用 `matplotlib`/`seaborn` 做数据分布与特征相关性可视化。
*   **代码作业 (Homework)**:
    *   提交一个 `train.py`：参数化数据路径与模型超参；输出指标与保存模型文件。
    *   提交一个 `report.md`：描述你选择指标的理由、一次失败实验与改进。

### Module 1.2: LLM 原理与 API 工程
*   **目标**: 从“原理”到“调用”。
*   **内容**:
    *   **LLM 概念**: Transformer 直觉理解，Tokenization，Context Window。
    *   **Prompt Engineering**: 掌握 Zero-shot, COT, System Prompt 的本质。
    *   **实操**: 使用 OpenAI/Anthropic API 编写脚本，处理文本摘要、提取等任务。
    *   **实操**: 搭建本地 Ollama 环境，体验不同模型的区别。

*   **教程 (Theory / Tutorial)**:
    *   推理形态：Chat Completions/Tool Calling 的基本调用方式与限制。
    *   成本与稳定性：重试、超时、限流、幂等、缓存与日志。
    *   提示词结构化：输入/输出 schema、约束输出、错误恢复策略。
*   **Lab (Hands-on)**:
    *   写一个 `llm_client.py`：支持超时、重试、日志、速率限制与简单缓存。
    *   Ollama 本地模型对比：同一任务下不同模型的质量/延迟/成本（本地成本以时间/资源衡量）。
*   **代码作业 (Homework)**:
    *   提交一个命令行工具：`summarize --input <file> --output <file> --format json`。
    *   提交测试用例：至少覆盖 3 个异常场景（空输入/超长输入/模型返回非预期格式）。

### Level 1 Capstone: 智能数据分析脚本
*   **任务**: 编写一个 Python 脚本，读取 CSV 数据，利用 LLM 自动生成数据分析报告。
*   **考核点**: Python 基础，API 调用稳定性，Prompt 设计。

*   **交付物 (Deliverables)**:
    *   可复现运行方式：`requirements.txt`/`pyproject.toml` 二选一 + `README`。
    *   `analyze.py`：支持输入 CSV 路径、输出目录、可选的列筛选与抽样策略。
    *   报告输出：至少包含“数据概览/异常值提示/潜在相关性/可行动建议”。
*   **验收标准 (Acceptance)**:
    *   10MB 以内 CSV 能稳定运行（失败要有可理解错误信息）。
    *   API 调用具备重试/超时；日志能定位失败原因。
    *   报告结构固定且可机器解析（例如 JSON + 人类可读 Markdown）。

---

## Level 2: 系统构建与工程化阶段 (The Builder)
**核心支柱**: `4. System Design` & `2. AI 代码实操 (进阶)`
**侧重**: 利用现成模型构建复杂应用，强调架构设计和 AI 辅助编程能力。

**适合人群**: 有一定开发经验的初级/中级工程师；或已完成 Level 1 的学员。
**结课门槛 (Exit Criteria)**:
*   能设计并实现一个端到端 RAG 系统（含评估与监控思路）。
*   能实现至少一种 Agent Workflow（规划/工具调用/状态管理/失败恢复）。
*   能用 AI 辅助开发把需求拆成可实现的模块，并进行代码审查与重构。

### Module 2.1: Vibe Coding 与 AI 辅助开发
*   **目标**: 改变编程模式，从“手写每一行”转变为“设计逻辑，AI 生成”。
*   **内容**:
    *   **工具流**: 熟练使用 Cursor/Windsurf。
    *   **Vibe Coding**: 学会用自然语言描述复杂的模块需求，让 AI 生成代码骨架。
    *   **实操**: 在 1 小时内通过 AI 辅助完成一个简单的 CRUD Web 应用。

*   **教程 (Theory / Tutorial)**:
    *   需求到代码：把需求写成“接口/数据模型/错误码/边界条件/验收用例”。
    *   AI 辅助的质量控制：最小 diff、单元测试优先、先写约束再生成代码。
    *   代码审查清单：可读性、可测性、依赖隔离、配置化与安全。
*   **Lab (Hands-on)**:
    *   以 FastAPI/Flask 二选一实现 CRUD；增加输入校验与错误处理。
    *   为关键逻辑补齐 `pytest` 测试与 CI（如果项目已有 CI，则对齐既有方式）。
*   **代码作业 (Homework)**:
    *   提交一份“AI 协作开发记录”：你给 AI 的约束、生成结果、你做的修正与原因。

### Module 2.2: RAG 系统设计与实现
*   **目标**: 解决 LLM 幻觉与知识时效性问题。
*   **内容**:
    *   **系统设计**: RAG 架构拆解 (ETL -> Embedding -> Vector DB -> Retrieval -> Generation)。
    *   **实操**: 使用 LangChain/LlamaIndex 对接 ChromaDB/Milvus。
    *   **进阶**: 混合检索 (Hybrid Search) 与 重排序 (Rerank) 的代码实现。

*   **教程 (Theory / Tutorial)**:
    *   Chunking 策略与代价：长度、重叠、结构化文档（标题/表格/代码块）。
    *   检索质量：召回率/精确率的直觉；何时需要 rerank。
    *   防幻觉策略：引用/溯源、拒答策略、上下文不足检测。
*   **Lab (Hands-on)**:
    *   构建一个“课程讲义问答”RAG：包含导入、向量化、检索、回答与引用。
    *   加入 rerank（可选）并比较回答质量与延迟。
*   **代码作业 (Homework)**:
    *   实现一个离线评测脚本：给定一组 QA 对，输出命中率/引用覆盖率/失败样例。

### Module 2.3: Agent Workflow 与多智能体
*   **目标**: 让 AI 具备“行动力”。
*   **内容**:
    *   **设计模式**: ReAct, Reflection, Planning。
    *   **框架应用**: LangGraph 或 CrewAI 的状态管理。
    *   **实操**: 构建一个“自动化研报 Agent”，包含搜索工具、网页抓取工具、写作工具。

*   **教程 (Theory / Tutorial)**:
    *   工具调用的契约：输入/输出 schema、失败重试、超时与降级。
    *   状态机思维：节点、边、记忆与可观测性。
    *   安全与合规：工具白名单、敏感信息处理、提示词注入防护的基础措施。
*   **Lab (Hands-on)**:
    *   实现一个“研究任务”工作流：提出问题 -> 规划 -> 搜索 -> 摘要 -> 结论。
    *   加入失败恢复：某个工具不可用时自动切换路径或输出可理解的失败报告。
*   **代码作业 (Homework)**:
    *   产出一份 Workflow 设计文档：节点职责、输入输出、异常路径、测试策略。

### Level 2 Capstone: 垂直领域智能助手系统
*   **任务**: 开发一个端到端的 Web 应用（如：法律咨询助手）。
*   **考核点**: 完整的 RAG 流程，Agent 工具调用，模块化代码结构，前后端分离设计。

*   **范围建议 (Scope)**:
    *   一个清晰的垂直领域（法律/医疗/教育/金融等任选其一）+ 一套可控的知识库。
    *   至少包含：对话 UI、RAG 问答、引用溯源、反馈按钮（好/坏）、管理员导入数据。
*   **交付物 (Deliverables)**:
    *   架构图与接口文档（REST/JSON）。
    *   可运行 Demo（本地或容器化），包含一键启动说明。
    *   一个最小评测集与评测脚本（能复现你宣称的效果）。
*   **验收标准 (Acceptance)**:
    *   对“知识库内问题”回答能提供引用，且引用可追溯到原文片段。
    *   对“知识库外问题”能触发拒答/澄清策略，而不是强行编造。
    *   代码结构清晰：数据导入、检索、生成、API、前端分层明确。

---

## Level 3: 深度优化与专家阶段 (The Expert)
**核心支柱**: `1. AI 基础概念 (进阶)` & `3. Meta Learning`
**侧重**: 打开黑盒，进行模型微调与底层优化，培养解决未知问题的能力。

**适合人群**: 有经验的高级开发者；或已完成 Level 2 并希望深入模型与评测/优化的学员。
**结课门槛 (Exit Criteria)**:
*   能独立完成一次可复现的微调实验，并用评测证明“变好/没变好”。
*   能处理推理部署中的常见性能与稳定性问题（延迟、吞吐、显存、并发）。
*   能用 Meta Learning 方法复现一个陌生论文/开源项目的核心 Demo。

### Module 3.1: 模型微调 (Fine-tuning) 实战
*   **目标**: 定制私有模型，打破 API 限制。
*   **内容**:
    *   **深度原理**: 深入理解 SFT (监督微调) 与 RLHF 流程。
    *   **技术栈**: LoRA/QLoRA 原理与显存优化。
    *   **实操**: 准备自定义数据集（如医疗问答），使用 Unsloth/Llama-Factory 微调 Llama 3。

*   **教程 (Theory / Tutorial)**:
    *   数据工程：指令数据结构、去重、泄漏、切分策略与质量门控。
    *   微调策略选择：全参 vs LoRA；何时需要偏好优化（如 DPO）。
    *   可复现训练：配置文件化、种子、日志、保存与回滚。
*   **Lab (Hands-on)**:
    *   训练一个 LoRA 适配器并进行合并/不合并两种推理对比。
    *   构建一个“数据审计脚本”：统计长度分布、重复率、潜在敏感信息。
*   **代码作业 (Homework)**:
    *   提交一份实验记录：超参、数据版本、训练曲线截图/导出、失败实验复盘。

### Module 3.2: 评价、量化与推理优化
*   **目标**: 让模型跑得更快、更准、更省。
*   **内容**:
    *   **Evaluation**: 搭建 LLM-as-a-Judge 自动化评测流水线 (Ragas/DeepEval)。
    *   **Optimization**: 量化技术 (GGUF, AWQ, GPTQ) 与 vLLM 推理加速部署。
    *   **实操**: 对比微调前后模型的客观指标，并将其量化部署到低显存设备。

*   **教程 (Theory / Tutorial)**:
    *   评测设计：离线基准集、在线 A/B、人工抽检；避免评测被提示词“投机”。
    *   性能画像：吞吐/延迟/显存/并发；瓶颈定位（tokenization、kv cache、IO）。
    *   部署策略：批处理、流式输出、限流、熔断与监控指标（p95/p99）。
*   **Lab (Hands-on)**:
    *   用 `vLLM`（或等价方案）做并发压测，记录延迟分布并分析瓶颈。
    *   至少做一次量化对比：质量变化与显存/速度收益。
*   **代码作业 (Homework)**:
    *   提交一个评测与压测报告：方法、指标、结论、建议下一步改进。

### Module 3.3: 终极 Meta Learning (探索未知)
*   **目标**: 离开教程，独自面对前沿技术。
*   **内容**:
    *   **源码阅读**: 深入阅读 transformers 或 vLLM 源码，理解底层实现。
    *   **Paper to Code**: 选取一篇最新的 ArXiv 论文，通过 AI 辅助阅读并尝试复现其核心 Demo。
    *   **Debug**: 解决一个复杂的 CUDA 或 显存溢出 (OOM) 问题，不依赖简单的搜索，而是通过日志分析和文档推导。

*   **教程 (Method / Playbook)**:
    *   读源码路径：入口 -> 核心数据结构 -> 关键分支 -> 性能热点。
    *   Debug 方法：最小复现、二分定位、日志与断言、对照实验。
    *   文档检索：从错误信息反推关键词；优先级（官方文档 > RFC/Spec > issue > 博客）。
*   **代码作业 (Homework)**:
    *   提交一份“问题档案 (Issue Dossier)”：现象、复现、定位过程、根因、修复与回归测试。

### Level 3 Capstone: 企业级私有化模型解决方案
*   **任务**: 从数据清洗 -> 微调 -> 评测 -> 量化 -> 高并发部署，完成全链路闭环。
*   **考核点**: 模型效果提升证据，推理性能优化报告，以及面对陌生报错时的解决思路记录。

*   **交付物 (Deliverables)**:
    *   一条可复现流水线：数据版本化 -> 训练 -> 评测 -> 导出 -> 部署（脚本/Makefile/CI 形式均可）。
    *   一份“效果证据包”：对比基线、评测结果、失败样例分析、偏差与风险说明。
    *   一份“性能与成本报告”：吞吐/延迟/资源占用/并发策略与上限。
*   **验收标准 (Acceptance)**:
    *   评测可复现：同一版本代码与数据，结果波动在可解释范围。
    *   部署可用：提供健康检查、基本监控指标、错误处理与降级策略。
    *   Meta Learning 体现：至少 1 个“陌生问题”的系统化解决记录（含排障链路与证据）。
