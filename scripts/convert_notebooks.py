#!/usr/bin/env python3
"""
Convert Jupyter notebooks to Markdown files.
Supports batch conversion and single file conversion.
"""

import sys
import os
import subprocess
from pathlib import Path


def convert_notebooks():
    """Convert all notebooks in _notebooks directory to _posts directory."""
    notebooks_dir = Path("_notebooks")
    posts_dir = Path("_posts")
    
    # Create posts directory if it doesn't exist
    posts_dir.mkdir(exist_ok=True)
    
    # Find all .ipynb files
    notebook_files = list(notebooks_dir.glob("**/*.ipynb"))
    
    if not notebook_files:
        print("No notebooks found to convert.")
        return
    
    for notebook in notebook_files:
        # Skip if it's in _site
        if "_site" in str(notebook):
            continue
        
        convert_single_notebook(notebook)


def convert_single_notebook(notebook_path):
    """Convert a single notebook to markdown."""
    notebook_path = Path(notebook_path)
    
    if not notebook_path.exists():
        print(f"Error: Notebook not found: {notebook_path}")
        return
    
    # Determine output path and name
    notebook_name = notebook_path.stem
    output_path = Path("_posts") / f"{notebook_name}_IPYNB_2_.md"
    
    # Create output directory if needed
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"Converting: {notebook_path} -> {output_path}")
    
    try:
        # Use jupyter nbconvert to convert notebook to markdown
        # Use --output-dir and just the filename
        cmd = [
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "markdown",
            "--output-dir", str(output_path.parent),
            "--output", str(output_path.name),
            str(notebook_path)
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Error converting {notebook_path}:")
            print(result.stderr)
            return False
        
        print(f"✓ Successfully converted {notebook_path}")
        return True
    
    except Exception as e:
        print(f"Error converting {notebook_path}: {str(e)}")
        return False


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Single file conversion
        notebook_file = sys.argv[1]
        convert_single_notebook(notebook_file)
    else:
        # Batch conversion
        convert_notebooks()
