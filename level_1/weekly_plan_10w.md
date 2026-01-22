# Level 1（基础夯实）10 周周计划（每周 5 课时）

## 每周授课节奏（建议模板）

*   **3 课时讲授/讨论**：概念 + 示例 + 常见坑
*   **2 课时 Lab/Workshop**：当堂把代码跑通 + 留出 Debug 时间

你也可以采用 2+1+2 的结构：

*   第 1 次课（2 课时）：核心概念与示例
*   第 2 次课（1 课时）：短测/复盘/代码走读
*   第 3 次课（2 课时）：Lab/Workshop

---

## 10 周基准计划（10W Baseline）

### Week 1：工程环境与数据处理入门

*   **讲授（3h）**：Python 环境、依赖管理、脚本结构、异常与日志直觉；Pandas 数据读写与清洗
*   **Workshop（2h）**：读取 CSV -> 清洗缺失值 -> 基础统计 -> 输出报告（Markdown/JSON）
*   **产出**：一个可运行的 `data_profile.py` + README

### Week 2：机器学习训练闭环（从 0 到 1）

*   **讲授（3h）**：训练集/验证集、过拟合/泛化、损失函数与指标的意义
*   **Workshop（2h）**：`scikit-learn` 二分类：数据切分 -> 训练 -> 指标 -> 保存模型
*   **产出**：`train.py`（可参数化）+ `report.md`（解释指标与一次失败实验）

### Week 3：特征、基线与实验可复现

*   **讲授（3h）**：特征工程直觉、标准化/缺失处理、交叉验证；随机种子与实验记录
*   **Workshop（2h）**：对比 2 个模型/2 组超参；输出对比表与失败样例
*   **产出**：`experiments/` 目录（配置化运行）

### Week 4：LLM 基础原理直觉

*   **讲授（3h）**：Tokenization、Context Window、Transformer 直觉；推理是什么、为什么会“胡说”
*   **Workshop（2h）**：同一任务下对比不同 Prompt 结构（Zero-shot/结构化输出/示例）
*   **产出**：`prompt_playground.py`（输入文件 -> 输出结构化结果）

### Week 5：Prompt Engineering（可控输出）

*   **讲授（3h）**：System Prompt、约束输出、错误恢复策略；从“写提示词”到“写接口契约”
*   **Workshop（2h）**：为一个信息抽取任务定义输出 schema（JSON），并实现校验与重试
*   **产出**：`extract.py` + schema 校验与失败重试

### Week 6：LLM API 工程化（稳定性与成本）

*   **讲授（3h）**：超时、重试、限流、幂等、缓存；日志与可观测性最小集
*   **Workshop（2h）**：实现 `llm_client.py`（重试/超时/简单缓存/结构化日志）
*   **产出**：可复用的 LLM 客户端模块 + 单元测试

### Week 7：本地推理（Ollama）与模型对比

*   **讲授（3h）**：本地推理的边界（速度/显存/模型能力/上下文）；为什么要本地
*   **Workshop（2h）**：Ollama 安装与调用；对比 2-3 个模型在同一任务上的质量/延迟
*   **产出**：`benchmark_local_llm.py` + 对比结论

### Week 8：把 LLM 接到数据分析流程

*   **讲授（3h）**：数据抽样、长文本切分、输入压缩；从“脚本”到“可复用 pipeline”
*   **Workshop（2h）**：实现 CSV -> 特征概览 -> LLM 解释 -> 报告生成
*   **产出**：Capstone 雏形（可跑通主流程）

### Week 9：Capstone 工程化与质量保证

*   **讲授（3h）**：CLI 设计、配置管理（env/config file）、错误码与失败可解释性
*   **Workshop（2h）**：补齐测试、边界输入处理、输出格式稳定（JSON + Markdown）
*   **产出**：Capstone 可提交版本（功能齐全）

### Week 10：Capstone 答辩与复盘（面向 Level 2）

*   **讲授（3h）**：复盘：哪些地方最容易崩；如何为 RAG/Agent 做准备
*   **Workshop（2h）**：项目答辩与代码走读；基于反馈做一次重构
*   **产出**：Capstone 最终交付 + 复盘文档

---

## 8 周压缩建议（8W Compression）

当你需要压缩到 8 周时，建议保持“训练闭环 + LLM 工程化 + Capstone”三条主线不变：

*   **合并 Week 2 & Week 3**：弱化交叉验证细节，保留可复现实验与对比
*   **合并 Week 4 & Week 5**：LLM 原理直觉 + Prompt 可控输出一次讲清
*   Capstone：从 Week 7 开始进入连续 2 周冲刺（Week 7-8）

---

## 12 周扩展建议（12W Expansion）

当你扩展到 12 周时，建议把“工程基本功”和“评估意识”做扎实：

*   插入 1 周：**软件工程基础**（结构化日志、配置、测试、Makefile/任务脚本）
*   插入 1 周：**LLM 输出评估**（错误类型、人工标注小集、简单一致性检查）
*   Capstone 多 1 周：做“反馈闭环”（用户反馈 -> Prompt/流程迭代）
