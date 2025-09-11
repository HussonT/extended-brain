# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with
code in this repository.

I am an AI alignment researcher.

## Repository Overview

This is an Obsidian vault (personal knowledge management system) named
"second-brain" containing ~1,400 markdown notes. Obsidian uses Markdown files to
create an interconnected network of notes and ideas.

## Key Directories

- `.obsidian/` - Contains all Obsidian configuration files:
  - `workspace.json` - Current workspace layout and open files
  - `core-plugins.json` - Enabled/disabled core plugins
  - `app.json` - General app settings
  - `appearance.json` - Theme and UI settings
  - `graph.json` - Knowledge graph visualization settings
  - `plugins/` - Community plugins: dataview, obsidian-importer

- `.claude/` - Claude CLI configuration
  - `settings.local.json` - Local permissions for Claude CLI operations

- `about-me/` - Personal information, case studies, resume
- `checklists/` - Reusable checklists and procedures
- `Clippings/` - Web clippings and saved content
- `comm-habit/` - Communication habits, newsletters, work updates
- `Daily Notes/` - Daily journal entries
- `knowledge/` - Knowledge management (frameworks, long/short-term memory)
- `meetings/` - Meeting notes and records
- `ops/` - Operational documents (decision journal, planning, templates, working
  memory)
- `people/` - Notes about people and contacts
- `projects/` - Project documentation (ideas, personal, side, work projects)
- `self-development/` - Personal development sessions and materials
- `Templates/` - Note templates (Daily Progress, Weekly/Monthly/Quarterly
  Reviews, Reflection Prompts)
- `vision/` - Vision documents (Goals, Ideas, Journal, Lifebook, Quests,
  Self-reflection)

## Obsidian-Specific Guidelines

### Creating and Linking Notes

- Use `[[Note Name]]` syntax for internal links between notes
- File names should be descriptive and use spaces (Obsidian handles them well)
- Tags can be used in two ways:
  - Inline tags: `#tag-name` syntax anywhere in the note
  - Frontmatter tags: YAML format at the beginning of files (preferred for
    organization)
    ```yaml
    ---
    tags:
      - tag-name
      - another-tag
    ---
    ```
- Frontmatter (YAML) can be added at the beginning of files for metadata

### Core Features Enabled

Based on `core-plugins.json`, the following features are active:

- File explorer, Global search, Graph view
- Backlinks panel, Canvas, Outgoing links
- Tag pane, Page preview
- Daily notes, Templates, Note composer
- Command palette, Editor status, Bookmarks
- Outline, Word count, File recovery, Sync, Bases

### Community Plugins

- **Dataview** (v0.5.68) - Query and display data from notes using SQL-like
  queries
- **Obsidian Importer** - Import content from other note-taking apps

### Working with Obsidian Files

- All content files are Markdown (.md)
- Obsidian supports standard Markdown plus additional features like:
  - Wiki-style links: `[[Page Name]]`
  - Embedded files: `![[Image.png]]` or `![[Another Note]]`
  - Block references: `[[Page Name#^block-id]]`
  - Callouts: `> [!note] Title`

## Common Operations

### Searching for Notes

```bash
find . -name "*.md" -type f | grep -v ".obsidian"
```

### Finding All Links to a Specific Note

```bash
grep -r "\[\[Note Name\]\]" . --include="*.md" | grep -v ".obsidian"
```

### Working with Tags

#### Listing All Inline Tags (#tag format)

```bash
# Find all inline tags (e.g., #tag-name)
grep -rh "#[a-zA-Z][a-zA-Z0-9_/-]*" . --include="*.md" | grep -v ".obsidian" | grep -o "#[a-zA-Z][a-zA-Z0-9_/-]*" | sort | uniq
```

#### Listing All Frontmatter Tags

```bash
# Extract tags from YAML frontmatter
find . -name "*.md" -type f | grep -v ".obsidian" | while IFS= read -r file; do
  awk '/^tags:/{flag=1; next} /^[a-zA-Z].*:/{flag=0} flag && /^  - / {gsub(/^  - /, ""); print}' "$file"
done | sort | uniq
```

#### Listing ALL Tags (both inline and frontmatter)

```bash
# Combine both inline and frontmatter tags
(
  # Inline tags
  grep -rh "#[a-zA-Z][a-zA-Z0-9_/-]*" . --include="*.md" | grep -v ".obsidian" | grep -o "#[a-zA-Z][a-zA-Z0-9_/-]*" | sed 's/^#//';
  # Frontmatter tags
  find . -name "*.md" -type f | grep -v ".obsidian" | while IFS= read -r file; do
    awk '/^tags:/{flag=1; next} /^[a-zA-Z].*:/{flag=0} flag && /^  - / {gsub(/^  - /, ""); print}' "$file"
  done
) | sort | uniq
```

#### Finding Notes with a Specific Tag

```bash
# Find notes with a specific tag (replace "tag-name" with your tag)
TAG="tag-name"

# Search in frontmatter
find . -name "*.md" -type f | grep -v ".obsidian" | xargs grep -l "^  - $TAG$"

# Search for inline tags
grep -l "#$TAG\b" . --include="*.md" -r | grep -v ".obsidian"
```

#### Finding Notes Without Tags

```bash
# Find notes that have no tags (neither inline nor in frontmatter)
find . -name "*.md" -type f | grep -v ".obsidian" | while IFS= read -r file; do
  # Check for frontmatter tags
  has_fm_tags=$(grep -q "^tags:" "$file" && grep -q "^  - " "$file" && echo "yes" || echo "no")
  # Check for inline tags
  has_inline_tags=$(grep -q "#[a-zA-Z][a-zA-Z0-9_/-]*" "$file" && echo "yes" || echo "no")
  
  if [[ "$has_fm_tags" == "no" && "$has_inline_tags" == "no" ]]; then
    echo "$file"
  fi
done
```

### Finding Orphaned Notes (notes with no incoming links)

```bash
# First get all note names, then check which ones have no incoming links
find . -name "*.md" -type f | grep -v ".obsidian" | while IFS= read -r file; do
  basename=$(basename "$file" .md)
  count=$(grep -r "\[\[$basename\]\]" . --include="*.md" | grep -v ".obsidian" | wc -l)
  if [ $count -eq 0 ]; then echo "$file"; fi
done
```

### Creating Daily Notes

```bash
# Create a daily note with today's date
DATE=$(date +"%Y-%m-%d")
echo "# Daily Note - $DATE\n\n## Tasks\n\n## Notes\n\n## Reflections\n" > "Daily Notes/$DATE.md"
```

### PDF to Markdown Conversion

The vault includes `pdf_to_markdown.py` for converting PDFs to Markdown:

```bash
# Convert a PDF to Markdown (auto-selects best method)
python3 pdf_to_markdown.py input.pdf

# Specify conversion method
python3 pdf_to_markdown.py input.pdf -m pymupdf4llm  # Best for structure
python3 pdf_to_markdown.py input.pdf -m markitdown   # Microsoft's tool

# Install dependencies
python3 pdf_to_markdown.py --install-deps
```

### Dataview Queries

Example queries for the Dataview plugin:

```dataview
# List all notes modified in the last 7 days
LIST FROM "" WHERE file.mtime >= date(today) - dur(7 days)

# Table of all projects with status
TABLE status, file.ctime as "Created"
FROM "projects"
WHERE contains(tags, "type/project")
```

## Tagging System

The vault uses a hierarchical tagging system (documented in TAGS.md):

- **Type tags**: `#type/article`, `#type/book`, `#type/project`,
  `#type/meeting`, etc.
- **Status tags**: `#status/todo`, `#status/in-progress`, `#status/completed`
- **Source tags**: `#source/web`, `#source/book`, `#source/personal`
- **Topic tags**: Hierarchical subject classification

## Important Notes

- This is a knowledge management repository, not a software development project
- No build, test, or deployment processes exist
- Focus on content organization, linking, and knowledge structure
- Respect Obsidian's file naming conventions (spaces are allowed and common)
- The `.obsidian` directory should generally not be modified directly unless
  updating settings
- When creating new notes, consider their placement in the existing directory
  structure
- Media files should be placed in the `assets/` directory and referenced using
  Obsidian's embedding syntax
- Use the established tagging system for consistency
- when creating a google doc  - Removes 
  unnecessary <p> tags
   around content
  - Places bold time 
  ranges inline
  without paragraph
  wrappers
  - Uses heading tags 
  directly without
  extra spacing
  - Adds only 
  strategic <br> tags
  where visual
  separation is needed
   (between lunch and
  afternoon sessions)
  - Keeps lists tight
  with proper HTML
  structure