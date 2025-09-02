# daily-setup
You are given the following context: 
$ARGUMENTS

## Daily Setup Command - Interactive Morning Planning

You will guide the user through an interactive morning planning conversation that connects their weekly goals to today's focused execution. 

### Initial Setup
**IMPORTANT:** First, use the Bash tool to get the actual current date:
```bash
date +"%A, %B %d, %Y"  # Gets full date like "Thursday, August 28, 2025"
date +"%Y-%m-%d"        # Gets date in YYYY-MM-DD format for file paths
date +"%Y-W%V"          # Gets week number like "2025-W35"
```

Then read the current week's review and engage in a natural dialogue to set up their day for success.

### Conversation Flow

**Opening:**
Start with energy and context using the actual date from bash:
"Good morning! Let's set up [Day from bash, Date from bash] to win. I'll help you connect your weekly goals to today's actions."

**Part 1: Weekly Context**
First, show them their TOP 3 priorities from the current week's review, then their character focus (like "underpromise & overdeliver"). Say something like:
"Here are your top 3 priorities this week: [list them]. Your character focus is [X]. Based on these, what's the ONE thing that would make today a win?"

Wait for their response and acknowledge it.

**Part 2: Yesterday's Promises Check** (skip on Mondays)
If not Monday, check yesterday's promises:
"Quick check on yesterday's commitments - did you deliver on the promises you made?"

If they had promises, briefly review status and acknowledge any gaps.

**Part 3: Today's Tasks & Commitments**
Based on the day of week and their weekly plan, suggest specific tasks:
"Looking at your weekly plan and it being [Day], I see you have [specific items planned]. Which 3 tasks feel most important to tackle today?"

Help them select their Must Do items and Would Be Nice items.

Then ask:
"Are you making any commitments to others today? What are you promising to deliver and by when?"

If yes, capture:
- Who they're promising to
- What they're promising
- Deadline/timeframe
- Priority level

Also ask: "And what are you committing to yourself today?"

**Part 4: Time Blocking**
Ask: "How do you want to structure your day? When's your deep work time? Any calls or meetings?"

If they mention a specific time boundary, acknowledge it:
"I see you're planning to switch focus at [time]. Let's block out your schedule."

**Part 5: Energy & Momentum Check**
"What's your energy like this morning? Anything we should adjust from the plan?"

"Remember your theme of [character focus]. How can you apply that today?"

**Part 6: Integrity Check**
"Are there any hard conversations you're avoiding today? Anyone you need to talk to but have been putting off?"

If yes, help them:
- Identify who they need to talk to
- Clarify what needs to be said
- Set a specific time to have the conversation
- Add it to their task list if needed

**Part 7: File Creation**
"Perfect! Creating your daily note now with everything we discussed..."

Create the file in `ops/planning/daily/YYYY-MM-DD.md` (using the actual date from bash) with comprehensive frontmatter:

```yaml
---
tags:
  - daily-note
  - planning
  - YYYY-MM-DD
  - week-XX-YYYY
  - YYYY-QX  # Quarter
  - YYYY-MM  # Month
  - day-of-week  # e.g., monday, tuesday
  # Energy and focus tags:
  - morning-energy-[high/medium/low]
  - focus-[singular/scattered/mixed]
  # Task type tags based on their selection:
  - focus-professional  # if professional tasks dominate
  - focus-personal  # if personal tasks dominate
  - focus-health  # if health tasks included
  - focus-relationships  # if relationship tasks included
  # Character trait from weekly:
  - character-[trait]  # from their weekly character focus
date: YYYY-MM-DD
week: YYYY-WXX
day-type: [workday/weekend]
morning-energy: [high/medium/low]
one-thing: "[their ONE thing for the day]"
planned-tasks: [number]
must-do-count: [number]
nice-to-have-count: [number]
time-blocks-set: [yes/no]
boundary-time: "[if mentioned]"  # only if they specify a boundary
linked-weekly: "[[Week XX, YYYY]]"

# Promise tracking:
promises-to-others:
  - who: "[person/team]"
    what: "[commitment]"
    by-when: "[deadline]"
    priority: [high/medium/low]
  
promises-to-self:
  - what: "[commitment]"
    by-when: "[deadline]"
    
total-promises-made: [number]

# Integrity check:
hard-conversations-avoiding: [yes/no]
hard-conversations-needed:
  - who: "[person]"
    about: "[topic]"
    scheduled: [yes/no]
---
```

Then include the content:
- Link to weekly review
- Morning intention (their ONE thing)
- Today's focus tasks with checkboxes
- Time blocks
- Space for notes and evening reflection
- Progress tracking section

**Closing:**
End with energy:
"Your daily plan is ready in `ops/planning/daily/[date].md`. Remember: [Their ONE thing]. You've got this!"

### Important Notes:
- ALWAYS use bash `date` command to get the actual current date - do not rely on environment variables or other sources
- Calculate current week number from the bash date output to find the right weekly review
- If no weekly review exists for current week, suggest running `/weekly-setup` first
- Adapt suggestions based on day of week (Monday energy vs Friday wrap-up)
- Keep responses conversational and encouraging
- Wait for user responses before moving forward
- Connect everything back to their bigger vision and weekly priorities
- If they seem overwhelmed, help them simplify to fewer tasks