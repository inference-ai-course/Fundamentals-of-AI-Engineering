#!/usr/bin/env python3
"""
Add bidirectional links between markdown and notebook file pairs.
- Notebooks get a link to markdown at the end of the first cell
- Markdowns get a link to notebook after the overview section
"""

import json
from pathlib import Path
from typing import List

def add_link_to_notebook(filepath: Path, md_filename: str) -> bool:
    """Add link to markdown in notebook's first cell."""
    with open(filepath, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    if len(notebook['cells']) == 0:
        return False
    
    first_cell = notebook['cells'][0]
    if first_cell['cell_type'] != 'markdown':
        return False
    
    source = ''.join(first_cell['source'])
    
    # Check if link already exists
    if f'[{md_filename}]' in source or f'[教程]' in source or f'[Tutorial]' in source:
        print(f"  Link already exists in {filepath}")
        return False
    
    # Add link at the end of first cell
    link_text = f"\n\n📖 **配套教程**: [{md_filename}](./{md_filename}) - 理论详解与学习目标"
    
    new_source = source + link_text
    lines = new_source.split('\n')
    first_cell['source'] = [line + '\n' for line in lines[:-1]] + [lines[-1]]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    print(f"✓ Added link to {filepath}")
    return True

def add_link_to_markdown(filepath: Path, nb_filename: str) -> bool:
    """Add link to notebook in markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if link already exists
    if f'[{nb_filename}]' in content or f'[Notebook]' in content or f'[练习]' in content:
        print(f"  Link already exists in {filepath}")
        return False
    
    # Find where to insert the link (after ## Overview or after Pre-study section)
    insert_pos = None
    
    # Try to find ## Overview
    overview_match = content.find('## Overview')
    if overview_match != -1:
        # Find the end of the overview section (next ## heading)
        next_section = content.find('\n## ', overview_match + 10)
        if next_section != -1:
            insert_pos = next_section
        else:
            # If no next section, add at the end
            insert_pos = len(content)
    
    if insert_pos is None:
        # If no Overview section, try Pre-study
        prestudy_match = content.find('## Pre-study')
        if prestudy_match != -1:
            next_section = content.find('\n## ', prestudy_match + 10)
            if next_section != -1:
                insert_pos = next_section
        
    if insert_pos is None:
        # Add at the beginning after title
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if line.startswith('##') and i > 0:
                insert_pos = content.find('\n' + line)
                break
    
    if insert_pos is None:
        print(f"  Could not find insertion point in {filepath}")
        return False
    
    link_text = f"\n\n💻 **配套练习**: [{nb_filename}](./{nb_filename}) - 交互式代码实践\n"
    
    new_content = content[:insert_pos] + link_text + content[insert_pos:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✓ Added link to {filepath}")
    return True

def get_file_pairs() -> List[tuple]:
    """Get all markdown/notebook file pairs."""
    pairs = []
    
    for week in ['week_03', 'week_04', 'week_05', 'week_06']:
        week_path = Path(week)
        if not week_path.exists():
            continue
        
        # Get all ipynb files
        notebooks = sorted(week_path.glob('*.ipynb'))
        
        for nb in notebooks:
            # Find matching markdown file
            md_name = nb.stem + '.md'
            md_path = week_path / md_name
            
            if md_path.exists():
                pairs.append((nb, md_path))
    
    return pairs

def main():
    """Main function to add bidirectional links."""
    print("=" * 70)
    print("ADDING BIDIRECTIONAL LINKS")
    print("=" * 70)
    
    pairs = get_file_pairs()
    
    print(f"\nFound {len(pairs)} file pairs")
    print("-" * 70)
    
    notebook_count = 0
    markdown_count = 0
    
    for nb_path, md_path in pairs:
        print(f"\n{nb_path.parent.name}/{nb_path.stem}:")
        
        # Add link in notebook pointing to markdown
        if add_link_to_notebook(nb_path, md_path.name):
            notebook_count += 1
        
        # Add link in markdown pointing to notebook  
        if add_link_to_markdown(md_path, nb_path.name):
            markdown_count += 1
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Links added to notebooks: {notebook_count}/{len(pairs)}")
    print(f"Links added to markdowns: {markdown_count}/{len(pairs)}")

if __name__ == '__main__':
    main()