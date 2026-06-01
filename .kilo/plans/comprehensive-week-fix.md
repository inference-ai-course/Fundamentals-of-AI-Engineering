# Comprehensive Week Number Fix Plan
## AI Engineering Course - Update All Week References

---

## Objective

Update all week number references across the entire course to reflect the new 6-week structure:
- Original Week 1 → Week 4
- Original Week 2 → Week 5
- Original Week 3 → Week 6
- Original Week 4 → Week 3 (merged with Week 5)
- Original Week 5 → Week 3 (merged with Week 4)
- Original Week 6 → Week 6 (merged with Week 3)

---

## Phase 1: Update Main Entry Points (8 files)

### Week 3 (was Week 5 + Week 4)
- [ ] `week_03/README.md` - Update title from "Week 5" to "Week 3", integrate API engineering content
- [ ] `week_03/tutorial.md` - Update title from "Week 5" to "Week 3"

### Week 4 (was Week 1)
- [ ] `week_04/README.md` - Update title from "Week 1" to "Week 4"
- [ ] `week_04/tutorial.md` - Update title from "Week 1" to "Week 4"

### Week 5 (was Week 2)
- [ ] `week_05/README.md` - Update title from "Week 2" to "Week 5"
- [ ] `week_05/tutorial.md` - Update title from "Week 2" to "Week 5"
- [ ] `week_05/pyproject.toml` - Update "Week 2" in description field

### Week 6 (was Week 3 + Week 6)
- [ ] `week_06/README.md` - Update title from "Week 3" to "Week 6", integrate project content
- [ ] `week_06/tutorial.md` - Update title from "Week 3" to "Week 6"
- [ ] `week_06/simplified_project.md` - Create new file based on old capstone.md

---

## Phase 2: Update Tutorial Files (Keep Part Numbers)

### Week 3 Tutorial Files
| File | Current | Action |
|------|---------|--------|
| `01_local_inference_setup.md` | "Week 5" | Keep "Part 01", update week references |
| `02_ollama_http_client.md` | "Week 5" | Keep "Part 02", update week references |
| `03_benchmarking_script.md` | "Week 5" | Keep "Part 03", update week references |
| `04_timeouts_failures.md` | "Week 4" | Keep "Part 04", update week references |
| `05_retries_backoff.md` | "Week 4" | Keep "Part 05", update week references |
| `06_rate_limiting.md` | "Week 4" | Keep "Part 06", update week references |
| `07_caching_logging.md` | "Week 4" | Keep "Part 07", update week references |
| `08_llm_client_skeleton.md` | "Week 4" | Keep "Part 08", fix cross-references |

**Special Fix in 08_llm_client_skeleton.md:**
- Change "from Week 3" → "from Week 6" (structured output validation)
- Change "Week 6 capstone" → "Week 6 project" (pipeline reference)

### Week 4 Tutorial Files
| File | Current | Action |
|------|---------|--------|
| `01_environment_setup.md` | "Week 1" | Keep "Part 01", update week references |
| `02_data_profiling_script.md` | "Week 1" | Keep "Part 02", update week references |

### Week 5 Tutorial Files
| File | Current | Action |
|------|---------|--------|
| `01_training_loop.md` | "Week 2" | Keep "Part 01", update week references |
| `02_reproducibility_package.md` | "Week 2" | Keep "Part 02", update week references |
| `03_compare_runs_report.md` | "Week 2" | Keep "Part 03", update week references |

### Week 6 Tutorial Files
| File | Current | Action |
|------|---------|--------|
| `01_tokens_context.md` | "Week 3" | Keep "Part 01", update week references |
| `02_prompt_contracts.md` | "Week 3" | Keep "Part 02", update week references |
| `03_structured_outputs_validation.md` | "Week 3" | Keep "Part 03", update week references |
| `04_openai_compatible_api.md` | "Week 3" | Keep "Part 04", update week references |
| `05_pipeline_design.md` | "Week 6" | Keep "Part 05" (renumbered), update references |
| `06_sampling_compression.md` | "Week 6" | Keep "Part 06" (renumbered), update references |

**Special Fix in 01_tokens_context.md:**
- Change "in Week 6" → correct reference for tabular data compression

---

## Phase 3: Update Notebooks (Mirror .md Changes)

For each updated .md file, update corresponding .ipynb:
- [ ] `week_03/*.ipynb` (8 files)
- [ ] `week_04/*.ipynb` (2 files)
- [ ] `week_05/*.ipynb` (3 files)
- [ ] `week_06/*.ipynb` (6 files)

**Note:** Only update markdown cells, not code cells.

---

## Phase 4: Update Cross-References in Root Files

- [ ] `self_learn/self_study_guide.md` - Change "Week 5" → "Week 3"

---

## Execution Commands

### Step 1: Main Files
```bash
# Update week_03 main files
sed -i 's/Week 5/Week 3/g' week_03/README.md
sed -i 's/Week 5/Week 3/g' week_03/tutorial.md

# Update week_04 main files
sed -i 's/Week 1/Week 4/g' week_04/README.md
sed -i 's/Week 1/Week 4/g' week_04/tutorial.md

# Update week_05 main files
sed -i 's/Week 2/Week 5/g' week_05/README.md
sed -i 's/Week 2/Week 5/g' week_05/tutorial.md
sed -i 's/Week 2/Week 5/g' week_05/pyproject.toml

# Update week_06 main files
sed -i 's/Week 3/Week 6/g' week_06/README.md
sed -i 's/Week 3/Week 6/g' week_06/tutorial.md
```

### Step 2: Special Cross-References (Manual Review Required)
- `week_03/08_llm_client_skeleton.md` - Lines 123-124
- `week_06/01_tokens_context.md` - Check line 136 reference

---

## Verification Checklist

After all updates, verify:
- [ ] No file contains "Week 1", "Week 2", "Week 5" in new locations
- [ ] All Part numbers preserved (Part 01, Part 02, etc.)
- [ ] Cross-references point to correct new weeks
- [ ] `week_06/simplified_project.md` created
- [ ] All notebooks updated to match .md files

---

## File Count Summary

| Type | Count | Est. Time |
|------|-------|-----------|
| Main README/tutorial files | 8 | 30 min |
| Tutorial .md files | 19 | 60 min |
| Notebook .ipynb files | 19 | 45 min |
| Root/Config files | 2 | 15 min |
| **Total** | **~48 files** | **~2.5 hours** |

---

**Start Date:** TBD  
**Estimated Completion:** 2.5-3 hours  
**Status:** Ready to execute