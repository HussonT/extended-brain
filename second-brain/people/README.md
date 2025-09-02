# People Management System

This folder contains individual files for each person in your network. The system is designed to automatically aggregate all mentions and interactions with each person across your entire vault.

## How It Works

### 1. Creating a New Person
- Copy `Person Template.md` and rename it to `FirstName LastName.md`
- Fill in the frontmatter and contact details
- The rest happens automatically!

### 2. Linking to People
You have three ways to reference someone:

1. **Direct Link**: `[[Ben Fielding]]` - Creates a bidirectional link
2. **Tag**: `#person/ben-fielding` - Lighter weight, still discoverable
3. **Frontmatter**: In meeting notes, use `attendees: [[Person Name]]`

### 3. Automatic Discovery
Each person file contains Dataview queries that automatically find:
- All meetings they attended
- All notes that mention them
- All tags referencing them

### 4. Meeting Notes Best Practice
When creating meeting notes:
```markdown
---
date: 2024-01-15
type: meeting-type
attendees: [[Ben Fielding]], [[Sam Rowlands]]
tags: meeting
---
```

### 5. Priority and Relationship Quality
- **Priority**: A (highest) to C (lowest) - How important this relationship is
- **Relationship Quality**: 1-5 - Current strength of the relationship

## Example Usage

1. During a meeting with Ben Fielding, create a note and add `attendees: [[Ben Fielding]]` to frontmatter
2. When Ben mentions someone else, link them: "Ben suggested I talk to [[Sam Rowlands]]"
3. Open Ben's person file to see all your interactions automatically listed

## Required Plugins
- **Dataview**: For automatic aggregation of mentions and meetings
- Install via Settings → Community Plugins → Browse → Search "Dataview"

## Tips
- Use aliases in frontmatter for nicknames or shortened names
- Tag with `#person/name` when you want a lighter reference
- The system works retroactively - existing mentions will appear automatically