# Level 1（基础夯实）课程概览

## 定位

**Level 1** 面向需要从 0 到 1 建立 AI 与 LLM 工程基础的学习者，强调“概念直觉 + Python 实操 + 可复现的小项目交付”。

## 适合人群

*   非技术背景小白（希望转型 AI/数据/应用开发）
*   有技术背景但 AI 基础不系统的开发者（希望补齐 ML/LLM 基础与工程习惯）

## 先修要求

*   能完成基础命令行操作（安装依赖、运行脚本、查看日志）
*   具备最基本的编程概念（变量、分支、循环、函数）；如不具备，建议在开课前用 1 周完成 Python 入门

## 教学周期与课时

*   **10 周**（可压缩到 8 周或扩展到 12 周）
*   每周 **5 课时**（建议：3 课时讲授/讨论 + 2 课时 Lab/Workshop）

## 核心能力支柱覆盖

*   **AI 概念（基础）**：训练/验证/过拟合、损失函数与指标、Transformer/Token/上下文窗口等
*   **AI 代码实操（基础）**：Python 数据栈、传统 ML 小实验、LLM API 工程化调用、本地推理（Ollama）
*   **Meta Learning（入门）**：能读官方文档“用法章节”、能做最小复现与基础 Debug
*   **System Design（入门）**：能把脚本拆成模块（配置/数据/模型/报告/日志），并用清晰接口组织代码

## 学习产出（Learning Outcomes）

完成 Level 1 后，你应当能够：

1. 解释传统 ML 与 LLM 的关键基础概念，并能对一个问题选择合适的基线方案
2. 用 Python 完成一次可复现的 ML 小实验（数据切分、训练、评估、保存产物）
3. 稳定调用至少一种在线 LLM API，并具备工程化能力（超时、重试、日志、限流、缓存的基础实现）
4. 使用本地推理（Ollama）运行并对比不同模型的输出质量与性能差异
5. 交付一个可运行的 Capstone 项目，并具备 README/环境/可复现运行方式

## 推荐技术栈（Level 1）

*   Python 3.10+（建议 3.11）
*   基础库：`numpy`、`pandas`、`scikit-learn`、`matplotlib`/`seaborn`
*   工程化：`pytest`、`python-dotenv`（或等价）、结构化日志（任意实现方式）
*   LLM：在线 API（OpenAI/Anthropic/等价）+ 本地 Ollama

## 考核与评分建议（可选）

*   平时作业（Homework）：40%
*   实验/Lab 完成度：20%
*   Capstone 项目：40%

## 结课门槛（Exit Criteria）

*   能独立完成一个带配置、日志、错误处理的 Python 小项目
*   能解释训练/验证/过拟合与常见指标含义，并给出至少一次实验对比
*   能稳定调用至少一种在线 LLM API 与一种本地推理方案

## 文档导航

*   周计划：见 [weekly_plan_10w.md](weekly_plan_10w.md)
*   作业列表与要求：见 [assignments.md](assignments.md)
*   Capstone 项目说明：见 [capstone.md](capstone.md)
