# smart-tag-obsidian
You are given the following context: 
$ARGUMENTS

You are tasked with intelligently tagging Obsidian markdown files to create a comprehensive second brain system that balances knowledge management with action orientation. Your goal is to analyze each file and apply a systematic tagging structure that enables both learning and doing.

## Tagging Framework

Apply tags from the following categories based on file content:

### 1. Content Type Tags
- `#note` - General notes and thoughts
- `#article` - Long-form content or essays
- `#reference` - External resources, quotes, citations
- `#definition` - Concept definitions and explanations
- `#question` - Open questions or research topics
- `#idea` - Creative ideas or hypotheses
- `#journal` - Daily notes or reflections
- `#meeting` - Meeting notes and discussions

### 2. Knowledge Domain Tags
- `#topic/[domain]` - Subject areas (e.g., #topic/psychology, #topic/programming)
- `#concept/[name]` - Key concepts to track (e.g., #concept/systems-thinking)
- `#theory/[name]` - Theoretical frameworks
- `#skill/[name]` - Skills being developed

### 3. Action-Oriented Tags
- `#project/[name]` - Active projects
- `#task` - Actionable items
- `#todo` - Pending actions
- `#done` - Completed items
- `#goal/[timeframe]` - Goals (e.g., #goal/2024-q1)
- `#habit` - Habits to build or track
- `#decision` - Decisions to make or made
- `#next-action` - Immediate next steps

### 4. Status & Priority Tags
- `#status/active` - Currently working on
- `#status/pending` - Waiting or paused
- `#status/archive` - No longer active
- `#priority/high` - Urgent/important
- `#priority/medium` - Important but not urgent
- `#priority/low` - Nice to have

### 5. Connection & Context Tags
- `#relates-to/[topic]` - Cross-references
- `#source/[type]` - Source type (book, article, video, etc.)
- `#person/[name]` - People mentioned or involved
- `#context/[situation]` - Context (work, personal, learning)

### 6. Review & Maintenance Tags
- `#review/[date]` - Scheduled review dates
- `#needs-revision` - Content requiring updates
- `#needs-expansion` - Incomplete content
- `#evergreen` - Timeless content to maintain
- `#junk` - Low-value content to remove

## Implementation Instructions

1. **Check Existing TAGS.md**: First, review the vault's TAGS.md file to understand the existing tagging system and ensure consistency.

2. **Analyze File Content**: Read each markdown file and understand its purpose, content type, and relationships.

3. **Apply Multi-Dimensional Tagging**: Each file should typically have:
   - 1 content type tag
   - 1-3 knowledge domain tags
   - 0-2 action-oriented tags (if applicable)
   - 1 status tag (if applicable)
   - Any relevant connection tags

4. **Tag Placement**: Add tags in the frontmatter YAML section at the top of each file:
   ```yaml
   ---
   tags:
     - tag1
     - tag2
     - tag3
   created: YYYY-MM-DD
   modified: YYYY-MM-DD
   ---
   ```

5. **Preserve Existing Tags**: If files already have tags, analyze them and integrate them into the new system without removing valuable existing organization.

6. **Update TAGS.md**: IMPORTANT - After tagging files, update the vault's TAGS.md file with any new tags that were created. This ensures the master tag documentation stays current.

7. **Action-Knowledge Balance**: Ensure every knowledge-focused note considers potential actions, and every action-focused note links to relevant knowledge.

## Special Considerations

- **Progressive Summarization**: Tag notes that could benefit from summarization with `#needs-summary`
- **Zettelkasten Integration**: Use `#permanent-note` for atomic, self-contained ideas
- **GTD Integration**: Apply Getting Things Done methodology with appropriate action tags
- **PARA Method**: Consider Projects, Areas, Resources, Archives in your tagging structure

## Output

For each file processed, provide:
1. File path
2. Applied tags with brief reasoning
3. Any suggested file reorganization or linking opportunities
4. Potential action items extracted from knowledge notes

## Final Steps (REQUIRED)

After completing all file tagging:

1. **Collect All New Tags**: Run this command to find all unique tags used:
   ```bash
   grep -r "#[a-zA-Z]" . --include="*.md" | grep -v ".obsidian" | grep -o "#[a-zA-Z0-9/-]*" | sort | uniq
   ```

2. **Update TAGS.md**: Add any new tags to the appropriate sections in TAGS.md:
   - New type tags → "Type Tags" section
   - New topic hierarchies → "Topic Tags" section with examples
   - New source types → "Source Tags" section
   - New domain tags → "Knowledge Management Tags" section
   - Any other new categories → Create new sections as needed

3. **Verify Consistency**: Ensure all tags follow the naming conventions:
   - Always lowercase
   - Hyphens for multi-word tags (e.g., `#personal-growth` not `#personalgrowth`)
   - Maximum 3 levels of hierarchy
   
   **IMPORTANT - Avoid Common Inconsistencies:**
   - Use SINGULAR form: `#topic/startup` NOT `#topic/startups`
   - No variations: Pick ONE form and stick to it:
     - ✅ `#topic/startup` (not start-up, startups, or start-ups)
     - ✅ `#topic/dao` (not daos, DAO, or d-a-o)
     - ✅ `#topic/web3` (not web-3 or web-three)
   - Abbreviations: Use the most common form:
     - ✅ `#topic/ai` (not artificial-intelligence)
     - ✅ `#topic/vc` (not venture-capital in tags, use full form in descriptions)
   - Check existing TAGS.md FIRST before creating any variation

4. **Report Summary**: Provide a final summary including:
   - Total files tagged
   - New tags added to TAGS.md
   - Any inconsistencies found and resolved

Remember: The goal is to create a living system that supports both contemplation and action, making knowledge immediately useful while building long-term understanding. The TAGS.md file is the central documentation that must stay current with actual tag usage.