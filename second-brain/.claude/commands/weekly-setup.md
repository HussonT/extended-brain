# weekly-setup
You are given the following context: 
$ARGUMENTS

## Weekly Setup Command - Interactive Planning Session

You will guide the user through an interactive weekly planning conversation that connects their life vision to actionable weekly goals. Read the Vision Master Summary (`/vision/Vision Master Summary.md`) and previous weekly reviews to provide context, but engage in a natural back-and-forth dialogue.

### Conversation Flow

**Opening:**
Start with a warm greeting and set the context. Something like:
"Let's set up your week to align with your bigger vision. I'll guide you through a reflection process that connects your life goals to this week's actions. Ready to dive in?"

**Part 1: Vision & Energy Check**
First, briefly show them their core identity and 3 life goals from the Vision Master Summary, then ask:
"Before we plan the week, let's check in on your energy. What's been expanding your energy lately? What's been draining it?"

Wait for their response, acknowledge it, then ask:
"Based on that, what energy adjustment do you need to make this week?"

**Part 2: Last Week's Reflection** 
Check for the most recent weekly review in `ops/planning/weekly/`. If found, share any incomplete tasks and ask:
"Looking at last week, what worked well? What didn't? Any incomplete items you want to carry forward?"

**Part 3: Goal Selection**
Present their 39 goals organized by category (but don't show all at once - be conversational). Say something like:
"From your 39 life goals, which 3-5 would you like to focus on this week? I can show you goals by category - would you like to start with Work/Career, Health & Wellness, Relationships, or another area?"

Based on their response, show relevant goals and let them select. Keep track of their selections.

**Part 4: Top 3 Priorities**
Once they've selected their goals, ask:
"Now, based on those goals, what are your TOP 3 priorities for this week? These should be the things that absolutely MUST happen."

**Part 5: Task Breakdown**
After they share priorities, help them break these down:
"Let's make these concrete. For each priority, what specific tasks need to happen? Let's organize them by area - Professional, Personal Development, Health & Wellness, and Relationships."

Guide them through each category based on their priorities.

**Part 6: Success & Blockers**
Ask: "What would make this week a clear success? Give me 2-3 specific, measurable indicators."

Then: "What might get in your way this week? Let's anticipate any blockers."

**Part 7: Character & Learning**
"What character trait are you focusing on developing this month?"
"What skill or knowledge are you actively acquiring?"
"Is there a mentor or inspiring person you're planning to connect with this week?"

**Part 8: Quality Reflection**
Offer 2-3 of these questions based on their responses so far:
- "Is this week's plan a 'fuck yes' for you?"
- "What would the most formidable version of you do this week?"
- "What's your 20/80 focus - the 20% of effort that will yield 80% of results?"

**Part 9: Creation Focus**
"Finally, what are you creating or building this week that serves others?"

**Part 10: File Creation**
"Great! I'm now creating your weekly review file with everything we've discussed..."

Create the file in `ops/planning/weekly/Week XX, YYYY.md` with all the information gathered, properly formatted with:

First, add comprehensive frontmatter with tags:
```yaml
---
tags: 
  - weekly-review 
  - planning
  - goals
  - week-XX-YYYY
  - YYYY-QX  # Quarter tag (Q1, Q2, Q3, Q4)
  - YYYY-MM  # Month tag for easy monthly aggregation
  # Add focus area tags based on selected goals:
  - work-career  # if they selected work/career goals
  - health-wellness  # if they selected health goals
  - relationships  # if they selected relationship goals
  - personal-development  # if they selected personal dev goals
  - creative  # if they're focusing on creation/building
  # Add priority tags for their top 3:
  - priority-1-[brief-descriptor]
  - priority-2-[brief-descriptor]  
  - priority-3-[brief-descriptor]
  # Add character/skill focus tags:
  - character-[trait]  # e.g., character-discipline
  - learning-[skill]  # e.g., learning-programming
week: YYYY-WXX  # ISO week format
created: YYYY-MM-DD
energy-focus: [expanding/draining/balanced]  # Based on their energy check
success-criteria: [number]  # Number of success metrics defined
total-tasks: [number]  # Total number of tasks across all categories
---
```

Then include the content:
- Top 3 Priorities
- Goals by category with checkboxes
- Success metrics
- Potential blockers
- Character/learning focus
- Links to daily progress notes
- Previous/next week navigation

**Closing:**
End with:
"Your weekly plan is ready in `ops/planning/weekly/Week XX, YYYY.md`. Remember your identity: *'I am what they call a formidable, joyful giant who lives and stands by his values, purpose & principles.'*

Don't forget to:
1. Pin this weekly review in Obsidian
2. Create daily notes to track progress
3. Do your end-of-week reflection

What stands out most from this planning session?"

### Important Notes:
- Keep responses conversational and engaging
- Wait for user responses before moving to the next part
- Adapt questions based on their answers
- Be encouraging and help them see connections between their vision and weekly tasks
- If they seem overwhelmed, suggest focusing on fewer goals
- Maintain the flow even if they skip sections