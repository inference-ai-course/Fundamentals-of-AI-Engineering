# 课程重构迁移完成报告

## 执行时间
2026-04-01

## 已完成的工作

### ✅ Phase 1: 备份旧课程
- 创建 `old_v1/` 目录
- 备份所有 week_01 到 week_08 目录
- 备份 slides 目录
- 备份根目录文件 (README.md, capstone.md, assignments.md, PRESTUDY.md)

### ✅ Phase 2-6: 文件迁移
- **Week 3**: 整合原 Week 5 (本地推理) + 原 Week 4 (API工程)
  - 8个教程文件 + 3个Python脚本
- **Week 4**: 迁移原 Week 1 (数据处理基础)
  - 2个教程文件
- **Week 5**: 迁移原 Week 2 (ML训练循环)
  - 3个教程文件 + Python项目文件 + 数据文件
- **Week 6**: 整合原 Week 3 (Prompt工程) + 原 Week 6 (Pipeline)
  - 6个教程文件 + Python脚本

### ✅ Phase 7: Slides更新
- 删除 slides/week_07.md 和 slides/week_08.md
- 复制原 week_01 slides → week_04
- 复制原 week_02 slides → week_05
- 临时复制原 week_05 slides → week_03 (需手动整合原 week_04 内容)
- 临时复制原 week_03 slides → week_06 (需手动整合原 week_06 内容)
- 删除旧的 week_01 和 week_02 slides (需新建)

### ✅ Phase 8: 清理工作
- 删除 week_07 和 week_08 目录
- 清理临时文件

## 当前目录结构

```
Fundamentals-of-AI-Engineering/
├── old_v1/                    # ✅ 原课程完整备份
│   ├── week_01/ - week_08/   # ✅ 所有原week目录
│   ├── slides/                # ✅ 原slides
│   ├── README.md              # ✅ 原README
│   ├── capstone.md            # ✅ 原capstone
│   ├── assignments.md         # ✅ 原assignments
│   └── PRESTUDY.md            # ✅ 原PRESTUDY
├── week_01/                    # ✅ README.md created in English
├── week_02/                    # ✅ README.md created in English
├── week_03/                    # ✅ 已迁移 (原Week 5 + 4)
├── week_04/                    # ✅ 已迁移 (原Week 1)
├── week_05/                    # ✅ 已迁移 (原Week 2)
├── week_06/                    # ✅ 已迁移 (原Week 3 + 6)
├── slides/
│   ├── week_03.md              # ⚠️  需整合原week_04内容
│   ├── week_04.md              # ✅ 已迁移
│   ├── week_05.md              # ✅ 已迁移
│   └── week_06.md              # ⚠️  需整合原week_06内容
├── README.md                   # ⚠️  需重写
├── capstone.md                 # ⚠️  需更新/移动到week_06
├── assignments.md              # ⚠️  需重写
└── PRESTUDY.md                 # ⚠️  需重写
```

## 接下来需要完成的工作

### 🔴 高优先级（必须完成）

#### 1. 新建 Week 1 内容（Agent工具入门） ✅ 已完成
- [x] `week_01/README.md` - 课程概述
- [x] `week_01/tutorial.md` - 学习引导
- [x] `week_01/01_agent_tools_overview.md` - Agent工具概览
- [x] `week_01/02_chatgpt_claude_basics.md` - ChatGPT/Claude入门
- [x] `week_01/03_cursor_intro.md` - Cursor编辑器入门
- [x] `week_01/04_kilo_guide.md` - Kilo使用指南
- [x] `week_01/05_ai_tools_comparison.md` - 工具对比
- [x] `slides/week_01.md` - Slides

#### 2. 新建 Week 2 内容（IDE+Agent实践） ✅ 已完成
- [x] `week_02/README.md` - 课程概述
- [x] `week_02/tutorial.md` - 学习引导
- [x] `week_02/01_ide_setup.md` - IDE环境配置
- [x] `week_02/02_ai_assisted_workflow.md` - AI辅助编程流程
- [x] `week_02/03_reading_code_with_ai.md` - 用AI读代码
- [x] `week_02/04_modifying_code_with_ai.md` - 用AI改代码
- [x] `week_02/05_debugging_with_ai.md` - 用AI调试
- [x] `week_02/code_templates/` - 预置代码模板目录
  - `simple_math.py` - 简单数学函数
  - `text_processing.py` - 文本处理函数
  - `data_processing.py` - 数据处理函数
  - `debugging_practice.py` - 调试练习文件（故意包含错误）
  - `README.md` - 模板使用说明
- [x] `slides/week_02.md` - Slides

#### 3. 重写根目录文件
- [ ] `README.md` - 新课程主文档（6周结构）
- [ ] `SYLLABUS.md` - 新课程大纲（新建）
- [ ] `assignments.md` - 新作业要求
- [ ] `PRESTUDY.md` - 新预学习材料

#### 4. 整合更新 Week 3
- [ ] `week_03/README.md` - 整合本地推理和API工程说明
- [ ] `week_03/tutorial.md` - 更新学习引导
- [ ] `slides/week_03.md` - 整合原week_04和week_05的slides

#### 5. 更新 Week 4-5
- [ ] `week_04/README.md` - 更新周次引用
- [ ] `week_04/tutorial.md` - 更新周次引用
- [ ] `week_05/README.md` - 更新周次引用
- [ ] `week_05/tutorial.md` - 更新周次引用

#### 6. 整合更新 Week 6
- [ ] `week_06/README.md` - 整合Prompt工程和项目说明
- [ ] `week_06/simplified_project.md` - 简化项目要求（基于原capstone.md）
- [ ] `week_06/tutorial.md` - 更新学习引导
- [ ] `slides/week_06.md` - 整合Prompt工程和项目slides

### 🟡 中优先级（建议完成）

- [ ] 全局搜索替换所有文件中的周次引用（week_01 → week_04等）
- [ ] 更新所有内部链接
- [ ] 创建 Week 1-2 的代码模板文件
- [ ] 优化 Week 6 的项目模板

### 🟢 低优先级（可后续补充）

- [ ] 添加更多示例代码
- [ ] 优化 notebook 格式
- [ ] 添加练习题和答案
- [ ] 制作课程宣传片

## 文件迁移详细记录

### Week 3 文件清单（21个文件）
```
从 old_v1/week_05 迁移:
- 01_local_inference_setup.md/ipynb
- 02_ollama_http_client.md/ipynb
- 03_benchmarking_script.md/ipynb
- call_ollama.py
- benchmark_local_llm.py
- tutorial.md (已更新)
- README.md (需整合)

从 old_v1/week_04 迁移并重命名:
- 01_timeouts_failures.md/ipynb → 04_timeouts_failures.md/ipynb
- 02_retries_backoff_idempotency.md/ipynb → 05_retries_backoff.md/ipynb
- 03_rate_limiting.md/ipynb → 06_rate_limiting.md/ipynb
- 04_caching_logging.md/ipynb → 07_caching_logging.md/ipynb
- 05_llm_client_skeleton.md/ipynb → 08_llm_client_skeleton.md/ipynb
- llm_client.py
```

### Week 4 文件清单（6个文件）
```
从 old_v1/week_01 迁移:
- 01_environment_setup.md/ipynb
- 02_data_profiling_script.md/ipynb
- README.md (需更新周次)
- tutorial.md (需更新周次)
```

### Week 5 文件清单（18个文件+目录）
```
从 old_v1/week_02 迁移:
- 01_training_loop.md/ipynb
- 02_reproducibility_package.md/ipynb
- 03_compare_runs_report.md/ipynb
- train.py
- compare_runs.py
- ml_package/ (整个目录)
- sample_iris.csv
- sample_synthetic.csv
- reproducibility_sample.csv
- requirements.txt
- pyproject.toml
- README.md (需更新周次)
- tutorial.md (需更新周次)
- reports/ (整个目录)
```

### Week 6 文件清单（13个文件+目录）
```
从 old_v1/week_03 迁移:
- 01_tokens_context.md/ipynb
- 02_prompt_contracts.md/ipynb
- 03_structured_outputs_validation.md/ipynb
- 04_openai_compatible_api.md/ipynb
- extract_template.py
- tutorial.md (需整合)
- README.md (需整合)

从 old_v1/week_06 迁移并重命名:
- 01_pipeline_design.md/ipynb → 05_pipeline_design.md/ipynb
- 02_sampling_compression.md/ipynb → 06_sampling_compression.md/ipynb
- data/ (整个目录)
```

## 验证检查清单

### ✅ 已完成
- [x] old_v1/ 目录包含所有原文件
- [x] week_01 到 week_06 目录已创建
- [x] week_07, week_08 已删除
- [x] Week 3-6 的教程文件已正确迁移
- [x] Week 3-6 的Python文件已正确迁移
- [x] Slides 目录已部分更新

### ⚠️  待完成
- [x] Week 1-2 内容已全部创建 ✅
- [ ] Week 3 README.md 需要整合说明
- [ ] Week 6 README.md 需要整合说明
- [x] slides/week_01.md 和 week_02.md 已创建 ✅
- [ ] slides/week_03.md 需要整合原week_04内容
- [ ] slides/week_06.md 需要整合原week_06内容
- [x] 根目录文件已重写 ✅

## 下一步建议

1. **立即开始创建 Week 1-2 内容**（这是新课程的核心亮点）
2. **重写根目录文件**（让新课程结构清晰可见）
3. **整合 Week 3 和 Week 6 的 README**（说明内容整合逻辑）
4. **更新所有周次引用**（全局搜索替换）

## 注意事项

⚠️  **重要**：在完成 Week 1-2 内容和根目录文件重写之前，不要提交到git！

建议完成顺序：
1. 先完成根目录文件重写（README.md, SYLLABUS.md）
2. 再创建 Week 1-2 内容
3. 然后整合 Week 3 和 Week 6
4. 最后全局检查和测试

---

## Phase 9: Root Directory Files Rewritten in English (Completed)

### Files Completed

1. **README.md** - Rewritten in English with 6-week structure
   - Updated course overview for new 6-week curriculum
   - Added weekly module descriptions
   - Updated navigation and links

2. **SYLLABUS.md** - Created in English with detailed 6-week syllabus
   - Week 1: Agent Tools Introduction (ChatGPT, Claude, Cursor, Kilo)
   - Week 2: IDE + Agent Practice
   - Week 3: Local Inference & API Engineering
   - Week 4: Data Fundamentals for ML
   - Week 5: Training & Reproducibility
   - Week 6: Prompt Engineering & Capstone

3. **assignments.md** - Updated in English with new 6-week assignment structure
   - Weekly assignments aligned with new curriculum
   - Updated submission requirements
   - New grading criteria

4. **PRESTUDY.md** - Updated in English with lowered prerequisites
   - Simplified requirements for beginners
   - Added setup instructions for AI tools
   - Removed complex prerequisite topics

5. **Week 1 README.md** - Created in English (Agent Tools Introduction)
   - Course overview for Week 1
   - Learning objectives
   - Weekly schedule and resources

6. **Week 2 README.md** - Created in English (IDE + Agent Practice)
   - Course overview for Week 2
   - Learning objectives
   - Weekly schedule and resources

### Updated Directory Structure Status

```
├── week_01/                    # ✅ README.md created in English
├── week_02/                    # ✅ README.md created in English
```

---

## Phase 10: Week 1-2 Content Created (Completed 2026-04-02)

### Files Created for Week 1

1. **tutorial.md** - Learning guide with navigation and recommended order
2. **01_agent_tools_overview.md** - AI agent concepts, landscape, and core concepts
3. **02_chatgpt_claude_basics.md** - Setup, prompts, and comparison
4. **03_cursor_intro.md** - Installation, interface, and first tasks
5. **04_kilo_guide.md** - CLI-based AI assistant introduction
6. **05_ai_tools_comparison.md** - Decision framework and tool profiles
7. **slides/week_01.md** - Marp slides for Week 1 sessions

### Files Created for Week 2

1. **tutorial.md** - Learning guide with navigation and recommended order
2. **01_ide_setup.md** - Cursor setup and configuration
3. **02_ai_assisted_workflow.md** - Ask → Review → Apply → Verify pattern
4. **03_reading_code_with_ai.md** - Code understanding techniques
5. **04_modifying_code_with_ai.md** - Modification workflow and inline editing
6. **05_debugging_with_ai.md** - Error types and debugging workflow
7. **code_templates/** - Practice files for AI-assisted programming
   - `simple_math.py` - Basic mathematical functions
   - `text_processing.py` - String manipulation functions
   - `data_processing.py` - List/number processing functions
   - `debugging_practice.py` - Intentional bugs for debugging practice
   - `README.md` - Template usage instructions
8. **slides/week_02.md** - Marp slides for Week 2 sessions

### Updated Directory Structure Status

```
Fundamentals-of-AI-Engineering/
├── week_01/                    # ✅ Full content created
│   ├── README.md               # ✅ Course overview
│   ├── tutorial.md             # ✅ Learning guide
│   ├── 01_agent_tools_overview.md
│   ├── 02_chatgpt_claude_basics.md
│   ├── 03_cursor_intro.md
│   ├── 04_kilo_guide.md
│   └── 05_ai_tools_comparison.md
├── week_02/                    # ✅ Full content created
│   ├── README.md               # ✅ Course overview
│   ├── tutorial.md             # ✅ Learning guide
│   ├── 01_ide_setup.md
│   ├── 02_ai_assisted_workflow.md
│   ├── 03_reading_code_with_ai.md
│   ├── 04_modifying_code_with_ai.md
│   ├── 05_debugging_with_ai.md
│   └── code_templates/         # ✅ Practice files
├── slides/
│   ├── week_01.md              # ✅ Created
│   ├── week_02.md              # ✅ Created
│   ├── week_03.md              # ⚠️  需整合原week_04内容
│   ├── week_04.md              # ✅ 已迁移
│   ├── week_05.md              # ✅ 已迁移
│   └── week_06.md              # ⚠️  需整合原week_06内容
```

---

**迁移执行人**: AI Assistant (Kilo)
**迁移日期**: 2026-04-01 (Phase 1-9), 2026-04-02 (Phase 10)
**下次更新**: 继续整合 Week 3 和 Week 6 内容