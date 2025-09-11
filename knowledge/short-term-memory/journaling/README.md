# Journaling System

This directory contains your personal journaling templates and guides for effective journaling in Obsidian.

## Quick Start

1. **Daily Journaling**: Use the Daily Journal template for everyday reflection
2. **Weekly Reviews**: Use the Weekly Review template to plan and reflect on your week
3. **Monthly Reviews**: Use the Monthly Review template for bigger picture thinking
4. **Quarterly Reviews**: Use the Quarterly Review template for goal setting and major reflections

## Template Usage

### Using Templates in Obsidian

1. **Enable Templates Core Plugin**:
   - Settings → Core plugins → Templates (should already be enabled)

2. **Set Template Folder**:
   - Settings → Templates → Template folder location
   - Set to: `Templates`

3. **Create New Journal Entry**:
   - Create a new note (e.g., `2024-01-28` for daily journal)
   - Use Cmd/Ctrl + P → "Insert template"
   - Select the appropriate template

### Using Daily Notes Plugin

1. **Enable Daily Notes Core Plugin**:
   - Settings → Core plugins → Daily notes (should already be enabled)

2. **Configure Daily Notes**:
   - Settings → Daily notes
   - New file location: `knowledge/short-term-memory/journaling/daily`
   - Template file location: `Templates/Daily Journal.md`
   - Date format: `YYYY-MM-DD`

## Journaling Best Practices

### Daily Journaling
- **Morning**: Set intentions, plan your day
- **Evening**: Reflect on progress, gratitude, learnings
- **Keep it brief**: 5-10 minutes is enough
- **Be consistent**: Same time each day helps build the habit

### Weekly Reviews
- **Schedule it**: Sunday evening or Monday morning
- **Review daily entries**: Look for patterns and insights
- **Set weekly priorities**: Max 3-5 major goals
- **Track progress**: Rate your week objectively

### Monthly Reviews
- **Big picture thinking**: Step back from daily details
- **Goal adjustment**: Are your goals still relevant?
- **Celebrate wins**: Acknowledge your progress
- **Learn from challenges**: What systems need improvement?

## Folder Structure

```
journaling/
├── README.md (this file)
├── daily/           # Daily journal entries
│   └── YYYY-MM-DD.md
├── weekly/          # Weekly reviews
│   └── Week WW, YYYY.md
├── monthly/         # Monthly reviews
│   └── YYYY-MM Month.md
└── quarterly/       # Quarterly reviews
    └── YYYY-QX.md
```

## Tips for Effective Journaling

1. **Link liberally**: Connect to other notes, projects, people
2. **Use tags**: #daily-note, #weekly-review, #reflection, #goal, #lesson
3. **Include metrics**: Energy level, mood, productivity scores
4. **Capture quotes**: Things that inspired or motivated you
5. **Track habits**: Simple checkboxes for daily habits
6. **Review regularly**: Your past entries are gold mines of insight

## Advanced Features

### Dataview Queries
You can use Dataview plugin to aggregate journal data:

```dataview
TABLE energy, mood, productivity
FROM "knowledge/short-term-memory/journaling/daily"
WHERE date >= date(today) - dur(7 days)
SORT date DESC
```

### Graph Connections
Your journal entries will naturally connect to:
- Projects you're working on
- People you interact with
- Books/articles you're reading
- Ideas you're developing

This creates a rich knowledge graph over time!