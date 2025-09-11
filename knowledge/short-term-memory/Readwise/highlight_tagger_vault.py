#!/usr/bin/env python3
"""
Readwise Highlight Tagger - Vault Convention Version
Tags highlights according to the vault's established tagging system in TAGS.md
"""

import re
import json
import time
import sys
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass
import anthropic
from anthropic import APIError, APITimeoutError

@dataclass
class Highlight:
    """Represents a single highlight with its content and location"""
    content: str
    location: str
    line_index: int

class HighlightTagger:
    """Analyzes highlights and assigns tags using vault conventions"""
    
    def __init__(self, api_key: str):
        self.client = anthropic.Client(api_key=api_key)
        self.processed_count = 0
        self.error_count = 0
        
    def extract_highlights(self, content: str) -> List[Highlight]:
        """Extract highlights from Readwise markdown content"""
        lines = content.split('\n')
        highlights = []
        
        # Skip frontmatter
        start_idx = 0
        if lines[0] == '---':
            for i, line in enumerate(lines[1:], 1):
                if line == '---':
                    start_idx = i + 1
                    break
        
        # Extract highlights
        i = start_idx
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines, metadata, and existing tags
            if not line or line.startswith('→') or line.startswith('##') or line.startswith('Tags:'):
                i += 1
                continue
            
            # Check if this looks like a highlight
            location_pattern = r'\[?Location\s+\d+\]?'
            
            # Check if location is at end of current line
            if re.search(location_pattern, line):
                content = re.sub(location_pattern, '', line).strip()
                if content and len(content) > 20:
                    highlights.append(Highlight(
                        content=content,
                        location=re.search(location_pattern, line).group(),
                        line_index=i
                    ))
            # Check if location is on next line
            elif i + 1 < len(lines) and re.search(location_pattern, lines[i + 1]):
                if len(line) > 20:
                    highlights.append(Highlight(
                        content=line,
                        location=lines[i + 1].strip(),
                        line_index=i
                    ))
                i += 1  # Skip location line
            # If it's a substantial line without location, might still be a highlight
            elif len(line) > 50 and not line.startswith('Tags:'):
                highlights.append(Highlight(
                    content=line,
                    location='',
                    line_index=i
                ))
            
            i += 1
        
        return highlights
    
    def tag_highlights_with_retry(self, highlights: List[Highlight], book_title: str, max_retries: int = 3) -> List[Dict]:
        """Get tags for highlights with retry logic"""
        for attempt in range(max_retries):
            try:
                return self.tag_highlights(highlights, book_title)
            except (APIError, APITimeoutError) as e:
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt  # Exponential backoff
                    print(f"      API error (attempt {attempt + 1}/{max_retries}): {str(e)[:100]}")
                    print(f"      Waiting {wait_time} seconds before retry...")
                    time.sleep(wait_time)
                else:
                    print(f"      Failed after {max_retries} attempts: {str(e)[:100]}")
                    self.error_count += 1
                    return []
            except Exception as e:
                print(f"      Unexpected error: {str(e)[:100]}")
                self.error_count += 1
                return []
        return []
    
    def tag_highlights(self, highlights: List[Highlight], book_title: str) -> List[Dict]:
        """Get tags for a batch of highlights using LLM"""
        
        # Prepare highlights for LLM
        highlights_text = "\n\n".join([
            f"Highlight {i+1}: {h.content}"
            for i, h in enumerate(highlights)
        ])
        
        prompt = f"""Analyze these highlights from the book "{book_title}" and assign appropriate tags following this specific tagging system.

IMPORTANT: Use ONLY tags from these categories and follow the exact format (lowercase, hyphens for multi-word, singular form):

1. Topic Tags (#topic/):
   Technology:
   - #topic/technology/ai/alignment (AI safety and alignment)
   - #topic/technology/ai/machine-learning
   - #topic/technology/ai/llm
   - #topic/technology/ai/safety
   - #topic/technology/programming/python (or javascript, rust, go, etc.)
   - #topic/technology/web3/blockchain
   - #topic/technology/security/cybersecurity
   
   Business & Startup:
   - #topic/business/entrepreneurship
   - #topic/business/marketing/growth-hacking
   - #topic/business/sales/strategy
   - #topic/business/finance/metrics
   - #topic/business/scaling/growth
   - #topic/startup/validation
   - #topic/startup/fundraising/vc
   
   Personal Development:
   - #topic/productivity/time-management
   - #topic/productivity/habit
   - #topic/productivity/focus
   - #topic/personal-growth/mindset
   - #topic/personal-growth/learning
   - #topic/personal-growth/goal-setting
   
   Leadership & Management:
   - #topic/leadership/vision
   - #topic/leadership/communication
   - #topic/leadership/team-building
   - #topic/management/people
   
   Psychology & Philosophy:
   - #topic/psychology/cognitive
   - #topic/psychology/behavioral
   - #topic/psychology/bias
   - #topic/philosophy/stoicism
   - #topic/philosophy/ethics
   
   Health:
   - #topic/health/nutrition
   - #topic/health/fitness/strength-training
   - #topic/health/sleep
   - #topic/health/biohacking

2. Knowledge Type Tags (#knowledge/):
   - #knowledge/principle (fundamental principles)
   - #knowledge/framework (structured methodologies)
   - #knowledge/lesson-learned (experience-based lessons)
   - #knowledge/best-practice (proven practices)
   - #knowledge/mental-model (decision-making models)

3. Priority Tags:
   - #priority/high (crucial insights)
   - #priority/medium (important but not urgent)
   - #priority/low (nice to know)

4. Domain Tags (#domain/):
   - #domain/startup
   - #domain/finance
   - #domain/engineering
   - #domain/product
   - #domain/marketing
   - #domain/business
   - #domain/ai

Rules:
- Choose 2-4 most relevant tags per highlight
- Use the hierarchical topic tags when applicable
- Add #priority/high only for truly crucial insights
- Add a knowledge type tag when the highlight represents a principle, framework, or lesson
- Ensure all tags follow the format: lowercase, hyphens for multi-word, singular form

Highlights:
{highlights_text}

Return ONLY a JSON array with one object per highlight, no other text:
[
  {{
    "highlight_number": 1,
    "tags": ["#topic/business/entrepreneurship", "#knowledge/principle", "#priority/high"]
  }},
  ...
]"""

        response = self.client.messages.create(
            model="claude-3-5-sonnet-latest",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000,
            temperature=0.3,
            timeout=10.0
        )
        
        # Extract JSON from response
        text = response.content[0].text
        
        # Try to find JSON array in response
        json_start = text.find('[')
        json_end = text.rfind(']') + 1
        
        if json_start >= 0 and json_end > json_start:
            try:
                json_str = text[json_start:json_end]
                tagged_highlights = json.loads(json_str)
                
                # Map tags back to original highlights
                result = []
                for item in tagged_highlights:
                    idx = item['highlight_number'] - 1
                    if 0 <= idx < len(highlights):
                        result.append({
                            'highlight': highlights[idx],
                            'tags': item.get('tags', [])
                        })
                
                return result
            except json.JSONDecodeError as e:
                print(f"      JSON parse error: {str(e)[:100]}")
                return []
        else:
            print("      Could not find JSON in response")
            return []
    
    def apply_tags_to_content(self, content: str, tagged_highlights: List[Dict]) -> str:
        """Apply tags to the original content"""
        lines = content.split('\n')
        
        # Create a mapping of line indices to tags
        line_tags = {}
        for item in tagged_highlights:
            highlight = item['highlight']
            tags = item['tags']
            if tags:
                line_tags[highlight.line_index] = tags
        
        # Apply tags
        result_lines = []
        for i, line in enumerate(lines):
            result_lines.append(line)
            
            # Add tags after this line if we have them
            if i in line_tags:
                # Check if next line is a location line
                if i + 1 < len(lines) and re.search(r'\[?Location\s+\d+\]?', lines[i + 1]):
                    result_lines.append(lines[i + 1])
                    result_lines.append(f"Tags: {' '.join(sorted(line_tags[i]))}")
                    lines[i + 1] = ''  # Mark as processed
                else:
                    result_lines.append(f"Tags: {' '.join(sorted(line_tags[i]))}")
        
        # Filter out empty lines we marked
        result_lines = [line for line in result_lines if line != '']
        
        return '\n'.join(result_lines)
    
    def process_file(self, file_path: Path, file_num: int, total_files: int) -> None:
        """Process a single Readwise markdown file."""
        print(f"\n[{file_num}/{total_files}] Processing: {file_path.name}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract highlights
        highlights = self.extract_highlights(content)
        if not highlights:
            print(f"  No highlights found")
            return
        
        print(f"  Found {len(highlights)} highlights")
        
        # Limit highlights for large files to avoid timeouts
        max_highlights = 10  # Process max 10 highlights per file for testing
        if len(highlights) > max_highlights:
            print(f"  Limiting to first {max_highlights} highlights for performance")
            highlights = highlights[:max_highlights]
        
        # Process highlights in small chunks
        chunk_size = 5  # Process 5 at a time
        all_tagged_highlights = []
        
        for i in range(0, len(highlights), chunk_size):
            chunk = highlights[i:i+chunk_size]
            chunk_end = min(i+chunk_size, len(highlights))
            
            # Show progress
            progress = f"  [{i+1}-{chunk_end}/{len(highlights)}]"
            sys.stdout.write(f"\r{progress} Processing...")
            sys.stdout.flush()
            
            # Get tags for this chunk with retry
            tagged_chunk = self.tag_highlights_with_retry(chunk, file_path.stem)
            if tagged_chunk:
                all_tagged_highlights.extend(tagged_chunk)
                self.processed_count += len(tagged_chunk)
            
            # Small delay between API calls to avoid rate limiting
            time.sleep(0.5)
        
        # Clear the progress line
        sys.stdout.write("\r" + " " * 50 + "\r")
        sys.stdout.flush()
        
        if all_tagged_highlights:
            # Apply tags to content
            updated_content = self.apply_tags_to_content(content, all_tagged_highlights)
            
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            print(f"  ✓ Tagged {len(all_tagged_highlights)} highlights")
        else:
            print(f"  ⚠ No highlights were tagged")

def main():
    """Main execution function"""
    import os
    from dotenv import load_dotenv
    
    # Load .env file from the root of second-brain
    env_path = Path('/Users/tomhusson/second-brain/.env')
    if env_path.exists():
        load_dotenv(env_path)
    
    # Get API key from environment
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found")
        print("Please ensure .env file exists with ANTHROPIC_API_KEY")
        return
    
    library_path = Path('/Users/tomhusson/second-brain/knowledge/short-term-memory/Readwise/Library')
    
    if not library_path.exists():
        print(f"Error: Path {library_path} does not exist")
        return
    
    tagger = HighlightTagger(api_key)
    
    # Get all markdown files
    md_files = list(library_path.glob('*.md'))
    total_files = len(md_files)
    print(f"Found {total_files} Readwise files to process")
    print("=" * 60)
    print("Using vault's established tagging conventions from TAGS.md")
    print("=" * 60)
    
    # Process each file
    start_time = time.time()
    
    # Start with a subset for testing
    files_to_process = md_files[:5]  # Process first 5 files
    
    for idx, file_path in enumerate(files_to_process, 1):
        try:
            tagger.process_file(file_path, idx, len(files_to_process))
        except KeyboardInterrupt:
            print("\n\nProcess interrupted by user")
            break
        except Exception as e:
            print(f"  ✗ Error: {str(e)[:100]}")
            tagger.error_count += 1
    
    # Summary
    elapsed_time = time.time() - start_time
    print("\n" + "="*60)
    print("PROCESSING COMPLETE")
    print("="*60)
    print(f"Time elapsed: {elapsed_time:.1f} seconds")
    print(f"Files processed: {idx}/{len(files_to_process)}")
    print(f"Highlights tagged: {tagger.processed_count}")
    print(f"Errors encountered: {tagger.error_count}")
    
    if len(files_to_process) < total_files:
        print(f"\nNote: Only processed {len(files_to_process)} of {total_files} files.")
        print("To process all files, change 'files_to_process = md_files[:5]' to 'files_to_process = md_files'")

if __name__ == "__main__":
    main()