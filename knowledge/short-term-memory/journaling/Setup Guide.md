# Obsidian Journaling Setup Guide

## Quick Setup Steps

### 1. Configure Templates Plugin
1. Open Settings (Cmd/Ctrl + ,)
2. Go to **Core plugins** → Ensure **Templates** is enabled
3. Go to **Templates** settings
4. Set **Template folder location** to: `Templates`
5. Set a hotkey for "Insert template" (recommended: Cmd/Ctrl + T)

### 2. Configure Daily Notes Plugin (Optional but Recommended)
1. In Settings → **Core plugins** → Enable **Daily notes**
2. Go to **Daily notes** settings:
   - **New file location**: `knowledge/short-term-memory/journaling/daily`
   - **Template file location**: `Templates/Daily Journal.md`
   - **Date format**: `YYYY-MM-DD`
3. Set a hotkey for "Open today's daily note" (recommended: Cmd/Ctrl + D)

## Template Locations

All templates are in the `Templates` folder:
- **Daily Journal.md** - For daily entries
- **Daily Progress.md** - Original daily template (work-focused)
- **Weekly Review.md** - For weekly planning and review
- **Monthly Review.md** - For monthly reflection
- **Quarterly Review.md** - For quarterly planning
- **Reflection Prompts.md** - Journaling prompts for inspiration

## How to Use Templates

### Method 1: Daily Notes Plugin (For Daily Journals)
1. Press your hotkey (Cmd/Ctrl + D) or click the calendar icon
2. A new daily note will be created with the template applied

### Method 2: Manual Template Insertion
1. Create a new note in the appropriate folder:
   - Daily: `knowledge/short-term-memory/journaling/daily/YYYY-MM-DD.md`
   - Weekly: `knowledge/short-term-memory/journaling/weekly/Week WW, YYYY.md`
   - Monthly: `knowledge/short-term-memory/journaling/monthly/YYYY-MM Month.md`
   - Quarterly: `knowledge/short-term-memory/journaling/quarterly/YYYY-Q#.md`
2. Press Cmd/Ctrl + P to open command palette
3. Type "Insert template" and select it
4. Choose the appropriate template

### Method 3: Template Hotkeys
You can set individual hotkeys for each template:
1. Settings → Hotkeys
2. Search for "Templates: Insert"
3. Set hotkeys for frequently used templates

## Tips for Effective Journaling

### Daily Routine
- **Morning (5-10 min)**: Open daily note, set intentions, plan day
- **Throughout day**: Capture ideas, thoughts, links in daily note
- **Evening (5-10 min)**: Reflect, update metrics, prepare for tomorrow

### Weekly Routine
- **Sunday evening or Monday morning (20-30 min)**:
  - Review past week's daily notes
  - Create weekly review
  - Set priorities for coming week

### Monthly Routine
- **Last Sunday of month (30-45 min)**:
  - Review all weekly reviews
  - Complete monthly review template
  - Adjust goals and systems

### Quarterly Routine
- **Every 3 months (60-90 min)**:
  - Deep reflection using quarterly template
  - Set OKRs for next quarter
  - Update long-term vision

## Helpful Plugins to Install

1. **Calendar** (Community Plugin)
   - Visual calendar for daily notes
   - See your journaling streak

2. **Dataview** (Community Plugin)
   - Query and visualize your journal data
   - Track metrics over time

3. **Periodic Notes** (Community Plugin)
   - Enhanced daily, weekly, monthly notes
   - More flexible than core Daily Notes

4. **Templater** (Community Plugin)
   - More powerful template functions
   - Dynamic content insertion

## Example Dataview Queries

Add these to any note to see journal insights:

### Recent Daily Entries
```dataview
TABLE energy AS "Energy", mood AS "Mood", productivity AS "Productivity"
FROM "knowledge/short-term-memory/journaling/daily"
SORT date DESC
LIMIT 7
```

### Weekly Average Metrics
```dataview
TABLE 
  round(mean(energy), 1) AS "Avg Energy",
  round(mean(mood), 1) AS "Avg Mood",
  round(mean(productivity), 1) AS "Avg Productivity"
FROM "knowledge/short-term-memory/journaling/daily"
WHERE date >= date(today) - dur(7 days)
```

### Gratitude Collection
```dataview
LIST gratitude
FROM "knowledge/short-term-memory/journaling/daily"
WHERE gratitude
SORT date DESC
LIMIT 10
```

## Troubleshooting

### Templates not inserting properly?
- Check template folder location in settings
- Ensure template files exist in Templates folder
- Try using command palette instead of hotkey

### Daily notes in wrong location?
- Check Daily Notes plugin settings
- Ensure folder path exists
- Use forward slashes in path

### Can't see all journal entries?
- Check if files are in correct folders
- Ensure proper naming convention
- Try rebuilding search index

Happy journaling! 📝