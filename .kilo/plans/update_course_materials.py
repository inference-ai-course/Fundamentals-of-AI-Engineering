#!/usr/bin/env python3
"""
Update course materials for AI Engineering course.
- Updates week references in notebooks and markdown files
- Adds bidirectional links between .md and .ipynb files
- Simplifies notebook content to point to markdown for theory
"""

import json
import re
from pathlib import Path
from typing import List, Tuple, Dict

def update_notebook(filepath: Path, replacements: List[Tuple[str, str]]) -> bool:
    """
    Update markdown cells in a notebook.
    
    Args:
        filepath: Path to .ipynb file
        replacements: List of (old_pattern, new_pattern) tuples
    
    Returns:
        True if file was updated, False otherwise
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    updated = False
    for cell in notebook['cells']:
        if cell['cell_type'] == 'markdown':
            source = ''.join(cell['source'])
            new_source = source
            
            for old, new in replacements:
                new_source = new_source.replace(old, new)
            
            if new_source != source:
                if '\n' in new_source:
                    lines = new_source.split('\n')
                    cell['source'] = [line + '\n' for line in lines[:-1]] + [lines[-1]]
                else:
                    cell['source'] = [new_source]
                updated = True
    
    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)
        print(f"✓ Updated: {filepath}")
    else:
        print(f"  No changes: {filepath}")
    
    return updated

def update_markdown(filepath: Path, replacements: List[Tuple[str, str]]) -> bool:
    """
    Update markdown file.
    
    Args:
        filepath: Path to .md file
        replacements: List of (old_pattern, new_pattern) tuples
    
    Returns:
        True if file was updated, False otherwise
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    for old, new in replacements:
        new_content = new_content.replace(old, new)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ Updated: {filepath}")
        return True
    else:
        print(f"  No changes: {filepath}")
        return False

def get_notebook_replacements() -> Dict[str, List[Tuple[str, str]]]:
    """Get all notebook replacement rules."""
    return {
        # Week 3 files
        'week_03/01_local_inference_setup.ipynb': [
            ('# Week 5 — Part 01:', '# Week 3 — Part 01:'),
            ('Week 5', 'Week 3'),
        ],
        'week_03/02_ollama_http_client.ipynb': [
            ('# Week 5 — Part 02:', '# Week 3 — Part 02:'),
            ('Week 5', 'Week 3'),
        ],
        'week_03/03_benchmarking_script.ipynb': [
            ('# Week 5 — Part 03:', '# Week 3 — Part 03:'),
            ('Week 5', 'Week 3'),
        ],
        'week_03/04_timeouts_failures.ipynb': [
            ('# Week 4 — Part 01:', '# Week 3 — Part 04:'),
            ('Week 4', 'Week 3'),
            ('Part 01', 'Part 04'),
        ],
        'week_03/05_retries_backoff.ipynb': [
            ('# Week 4 — Part 02:', '# Week 3 — Part 05:'),
            ('Week 4', 'Week 3'),
            ('Part 02', 'Part 05'),
        ],
        'week_03/06_rate_limiting.ipynb': [
            ('# Week 4 — Part 03:', '# Week 3 — Part 06:'),
            ('Week 4', 'Week 3'),
            ('Part 03', 'Part 06'),
            ('capstone', 'project'),
            ('Capstone', 'Project'),
        ],
        'week_03/07_caching_logging.ipynb': [
            ('# Week 4 — Part 04:', '# Week 3 — Part 07:'),
            ('Week 4', 'Week 3'),
            ('Part 04', 'Part 07'),
        ],
        'week_03/08_llm_client_skeleton.ipynb': [
            ('# Week 4 — Part 05:', '# Week 3 — Part 08:'),
            ('Week 4', 'Week 3'),
            ('Part 05', 'Part 08'),
            ('from Week 3', 'from Week 6'),
            ('Week 6 capstone', 'Week 6 project'),
        ],
        
        # Week 4 files
        'week_04/01_environment_setup.ipynb': [
            ('# Week 1 — Part 01:', '# Week 4 — Part 01:'),
            ('Week 1', 'Week 4'),
        ],
        'week_04/02_data_profiling_script.ipynb': [
            ('# Week 1 — Part 02:', '# Week 4 — Part 02:'),
            ('Week 1', 'Week 4'),
        ],
        
        # Week 5 files
        'week_05/01_training_loop.ipynb': [
            ('# Week 2 — Part 01:', '# Week 5 — Part 01:'),
            ('Week 2', 'Week 5'),
        ],
        'week_05/02_reproducibility_package.ipynb': [
            ('# Week 2 — Part 02:', '# Week 5 — Part 02:'),
            ('Week 2', 'Week 5'),
        ],
        'week_05/03_compare_runs_report.ipynb': [
            ('# Week 2 — Part 03:', '# Week 5 — Part 03:'),
            ('Week 2', 'Week 5'),
        ],
        
        # Week 6 files
        'week_06/01_tokens_context.ipynb': [
            ('# Week 3 — Part 01:', '# Week 6 — Part 01:'),
            ('Week 3', 'Week 6'),
        ],
        'week_06/02_prompt_contracts.ipynb': [
            ('# Week 3 — Part 02:', '# Week 6 — Part 02:'),
            ('Week 3', 'Week 6'),
        ],
        'week_06/03_structured_outputs_validation.ipynb': [
            ('# Week 3 — Part 03:', '# Week 6 — Part 03:'),
            ('Week 3', 'Week 6'),
        ],
        'week_06/04_openai_compatible_api.ipynb': [
            ('# Week 3 — Part 04:', '# Week 6 — Part 04:'),
            ('Week 3', 'Week 6'),
        ],
        'week_06/05_pipeline_design.ipynb': [
            ('# Week 6 — Part 01:', '# Week 6 — Part 05:'),
            ('Part 01', 'Part 05'),
            ('capstone', 'project'),
            ('Capstone', 'Project'),
        ],
        'week_06/06_sampling_compression.ipynb': [
            ('# Week 6 — Part 02:', '# Week 6 — Part 06:'),
            ('Part 02', 'Part 06'),
        ],
    }

def get_markdown_replacements() -> Dict[str, List[Tuple[str, str]]]:
    """Get all markdown replacement rules (same as notebook for week references)."""
    return {
        # Week 3 files
        'week_03/01_local_inference_setup.md': [
            ('# Week 5 — Part 01:', '# Week 3 — Part 01:'),
            ('Week 5', 'Week 3'),
        ],
        'week_03/02_ollama_http_client.md': [
            ('# Week 5 — Part 02:', '# Week 3 — Part 02:'),
            ('Week 5', 'Week 3'),
        ],
        'week_03/03_benchmarking_script.md': [
            ('# Week 5 — Part 03:', '# Week 3 — Part 03:'),
            ('Week 5', 'Week 3'),
        ],
        'week_03/04_timeouts_failures.md': [
            ('# Week 4 — Part 01:', '# Week 3 — Part 04:'),
            ('Week 4', 'Week 3'),
            ('Part 01', 'Part 04'),
        ],
        'week_03/05_retries_backoff.md': [
            ('# Week 4 — Part 02:', '# Week 3 — Part 05:'),
            ('Week 4', 'Week 3'),
            ('Part 02', 'Part 05'),
        ],
        'week_03/06_rate_limiting.md': [
            ('# Week 4 — Part 03:', '# Week 3 — Part 06:'),
            ('Week 4', 'Week 3'),
            ('Part 03', 'Part 06'),
            ('capstone', 'project'),
            ('Capstone', 'Project'),
        ],
        'week_03/07_caching_logging.md': [
            ('# Week 4 — Part 04:', '# Week 3 — Part 07:'),
            ('Week 4', 'Week 3'),
            ('Part 04', 'Part 07'),
        ],
        'week_03/08_llm_client_skeleton.md': [
            ('# Week 4 — Part 05:', '# Week 3 — Part 08:'),
            ('Week 4', 'Week 3'),
            ('Part 05', 'Part 08'),
            ('from Week 3', 'from Week 6'),
            ('Week 6 capstone', 'Week 6 project'),
        ],
        
        # Week 4 files
        'week_04/01_environment_setup.md': [
            ('# Week 1 — Part 01:', '# Week 4 — Part 01:'),
            ('Week 1', 'Week 4'),
        ],
        'week_04/02_data_profiling_script.md': [
            ('# Week 1 — Part 02:', '# Week 4 — Part 02:'),
            ('Week 1', 'Week 4'),
        ],
        
        # Week 5 files
        'week_05/01_training_loop.md': [
            ('# Week 2 — Part 01:', '# Week 5 — Part 01:'),
            ('Week 2', 'Week 5'),
        ],
        'week_05/02_reproducibility_package.md': [
            ('# Week 2 — Part 02:', '# Week 5 — Part 02:'),
            ('Week 2', 'Week 5'),
        ],
        'week_05/03_compare_runs_report.md': [
            ('# Week 2 — Part 03:', '# Week 5 — Part 03:'),
            ('Week 2', 'Week 5'),
        ],
        
        # Week 6 files
        'week_06/01_tokens_context.md': [
            ('# Week 3 — Part 01:', '# Week 6 — Part 01:'),
            ('Week 3', 'Week 6'),
        ],
        'week_06/02_prompt_contracts.md': [
            ('# Week 3 — Part 02:', '# Week 6 — Part 02:'),
            ('Week 3', 'Week 6'),
        ],
        'week_06/03_structured_outputs_validation.md': [
            ('# Week 3 — Part 03:', '# Week 6 — Part 03:'),
            ('Week 3', 'Week 6'),
        ],
        'week_06/04_openai_compatible_api.md': [
            ('# Week 3 — Part 04:', '# Week 6 — Part 04:'),
            ('Week 3', 'Week 6'),
        ],
        'week_06/05_pipeline_design.md': [
            ('# Week 6 — Part 01:', '# Week 6 — Part 05:'),
            ('Part 01', 'Part 05'),
            ('capstone', 'project'),
            ('Capstone', 'Project'),
        ],
        'week_06/06_sampling_compression.md': [
            ('# Week 6 — Part 02:', '# Week 6 — Part 06:'),
            ('Part 02', 'Part 06'),
        ],
    }

def main():
    """Main function to update all course materials."""
    print("=" * 70)
    print("UPDATING COURSE MATERIALS")
    print("=" * 70)
    
    base_path = Path('.')
    
    # Phase 1: Update notebooks
    print("\nPhase 1: Updating Notebook Files")
    print("-" * 70)
    notebook_replacements = get_notebook_replacements()
    notebook_count = 0
    for filepath, replacements in notebook_replacements.items():
        if update_notebook(base_path / filepath, replacements):
            notebook_count += 1
    print(f"\nUpdated {notebook_count} of {len(notebook_replacements)} notebooks")
    
    # Phase 2: Update markdown files
    print("\n" + "=" * 70)
    print("Phase 2: Updating Markdown Files")
    print("-" * 70)
    md_replacements = get_markdown_replacements()
    md_count = 0
    for filepath, replacements in md_replacements.items():
        if update_markdown(base_path / filepath, replacements):
            md_count += 1
    print(f"\nUpdated {md_count} of {len(md_replacements)} markdown files")
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Notebooks updated: {notebook_count}/{len(notebook_replacements)}")
    print(f"Markdown files updated: {md_count}/{len(md_replacements)}")
    print("\nNext steps:")
    print("1. Review changes in git diff")
    print("2. Test notebooks in Jupyter")
    print("3. Check bidirectional links")

if __name__ == '__main__':
    main()