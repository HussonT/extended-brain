#!/usr/bin/env python3
"""
PDF to Markdown Converter
Supports multiple conversion methods for best results
"""

import os
import sys
import argparse
from pathlib import Path
from typing import Optional, List

# Method 1: PyMuPDF4LLM (Best for structure preservation)
def convert_with_pymupdf4llm(pdf_path: str, output_path: Optional[str] = None) -> str:
    """Convert PDF using pymupdf4llm - best for LLM/RAG use cases"""
    try:
        import pymupdf4llm
        
        # Convert to markdown
        md_text = pymupdf4llm.to_markdown(pdf_path)
        
        # Save if output path provided
        if output_path:
            Path(output_path).write_bytes(md_text.encode())
            print(f"✓ Converted with pymupdf4llm: {output_path}")
        
        return md_text
    except ImportError:
        print("pymupdf4llm not installed. Install with: pip install pymupdf4llm")
        return None
    except Exception as e:
        print(f"Error with pymupdf4llm: {e}")
        return None

# Method 2: Marker (Best accuracy with LLM support)
def convert_with_marker(pdf_path: str, output_path: Optional[str] = None) -> str:
    """Convert PDF using marker - high accuracy"""
    try:
        import subprocess
        import json
        
        # Run marker command
        cmd = ["marker_single", pdf_path, "--output_format", "markdown"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            # Marker saves to a specific location, read it
            base_name = Path(pdf_path).stem
            marker_output = Path(f"{base_name}.md")
            
            if marker_output.exists():
                md_text = marker_output.read_text()
                
                if output_path:
                    Path(output_path).write_text(md_text)
                    print(f"✓ Converted with marker: {output_path}")
                
                # Clean up marker's output if we're saving elsewhere
                if output_path and output_path != str(marker_output):
                    marker_output.unlink()
                
                return md_text
        
        return None
    except Exception as e:
        print(f"Marker not available or error: {e}")
        return None

# Method 3: MarkItDown by Microsoft
def convert_with_markitdown(pdf_path: str, output_path: Optional[str] = None) -> str:
    """Convert PDF using Microsoft's MarkItDown"""
    try:
        from markitdown import MarkItDown
        
        md = MarkItDown()
        result = md.convert(pdf_path)
        md_text = result.text_content
        
        if output_path:
            Path(output_path).write_text(md_text)
            print(f"✓ Converted with MarkItDown: {output_path}")
        
        return md_text
    except ImportError:
        print("markitdown not installed. Install with: pip install markitdown")
        return None
    except Exception as e:
        print(f"Error with MarkItDown: {e}")
        return None

# Method 4: Basic PyMuPDF
def convert_with_pymupdf(pdf_path: str, output_path: Optional[str] = None) -> str:
    """Basic conversion using PyMuPDF (fallback)"""
    try:
        import pymupdf
        
        doc = pymupdf.open(pdf_path)
        md_text = ""
        
        for page_num, page in enumerate(doc, 1):
            md_text += f"\n## Page {page_num}\n\n"
            md_text += page.get_text("text")
        
        doc.close()
        
        if output_path:
            Path(output_path).write_text(md_text)
            print(f"✓ Converted with PyMuPDF (basic): {output_path}")
        
        return md_text
    except ImportError:
        print("PyMuPDF not installed. Install with: pip install PyMuPDF")
        return None
    except Exception as e:
        print(f"Error with PyMuPDF: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Convert PDF to Markdown")
    parser.add_argument("pdf_path", nargs='?', help="Path to input PDF file")
    parser.add_argument("-o", "--output", help="Output markdown file path")
    parser.add_argument("-m", "--method", 
                       choices=["pymupdf4llm", "marker", "markitdown", "pymupdf", "auto"],
                       default="auto",
                       help="Conversion method to use (default: auto)")
    parser.add_argument("--install-deps", action="store_true",
                       help="Install all dependencies")
    
    args = parser.parse_args()
    
    # Install dependencies if requested
    if args.install_deps:
        print("Installing dependencies...")
        os.system("pip install pymupdf4llm markitdown PyMuPDF")
        print("\nFor marker, install with: pip install marker-pdf")
        print("Note: Marker has additional requirements, see: https://github.com/datalab-to/marker")
        return
    
    # Check that pdf_path is provided for conversion
    if not args.pdf_path:
        parser.error("pdf_path is required unless using --install-deps")
        return
    
    # Verify input file exists
    if not Path(args.pdf_path).exists():
        print(f"Error: PDF file not found: {args.pdf_path}")
        sys.exit(1)
    
    # Determine output path
    output_path = args.output
    if not output_path:
        output_path = Path(args.pdf_path).with_suffix(".md")
    
    # Convert based on method
    result = None
    
    if args.method == "pymupdf4llm":
        result = convert_with_pymupdf4llm(args.pdf_path, output_path)
    elif args.method == "marker":
        result = convert_with_marker(args.pdf_path, output_path)
    elif args.method == "markitdown":
        result = convert_with_markitdown(args.pdf_path, output_path)
    elif args.method == "pymupdf":
        result = convert_with_pymupdf(args.pdf_path, output_path)
    else:  # auto mode - try each method
        print("Trying available methods...")
        
        # Try methods in order of quality
        methods = [
            ("pymupdf4llm", convert_with_pymupdf4llm),
            ("markitdown", convert_with_markitdown),
            ("marker", convert_with_marker),
            ("pymupdf", convert_with_pymupdf)
        ]
        
        for method_name, method_func in methods:
            print(f"\nTrying {method_name}...")
            result = method_func(args.pdf_path, output_path)
            if result:
                print(f"✓ Successfully converted using {method_name}")
                break
    
    if not result:
        print("\n❌ Failed to convert PDF. Please install dependencies:")
        print("  pip install pymupdf4llm  # Recommended")
        print("  pip install markitdown   # Alternative")
        print("  pip install marker-pdf   # For highest accuracy")
        sys.exit(1)
    
    print(f"\n✅ Conversion complete: {output_path}")
    print(f"   File size: {len(result):,} characters")

if __name__ == "__main__":
    main()