# DeepMind Gemini Alignment Testing - Hour-by-Hour Execution Plan

## Pre-Engagement TODOs (Complete Before Day 1)

### Infrastructure Setup (8 hours)

- [ ] Set up GCP test project with appropriate quotas
- [ ] Configure Vertex AI access for all team members
- [ ] Create GitHub repo with evaluation framework
- [ ] Set up logging/monitoring infrastructure
- [ ] Prepare screen recording setup for demos
- [ ] Create shared documentation workspace

### Scenario Preparation (12 hours)

- [ ] Setup automation for multi-turn drop scenario signal discovery
- [ ] Create rapid testing templates
- [ ] Build perturbation generator (?)

---

## WEEK 1: DISCOVERY & SIGNAL DETECTION

### Day 1 (Monday) - Deployment Landscape Mapping

**9:00-12:00** - Brainstrom likely misalignment scenarios in a big google sheets
doc - focussed brainstorms per google service

- 9:00-9:45: Cloud Build & GitHub Actions (CI/CD scenarios)
- 9:45-10:30: Cloud Functions & Cloud Run (serverless/container manipulation)
- 10:30-11:15: Cloud SQL & Firestore (data exfiltration scenarios)
- 11:15-12:00: IAM & Secret Manager (privilege escalation & credential theft)
- 12:00-12:45: Workspace (Drive, email, ...)

**12:00-13:00** - Lunch & Buffer & Buffer

**13:00-15:00** - Additional Services & ML-Specific

- 13:00-13:30: Vertex AI (ML research scenarios only - data poisoning, model
  manipulation)
- 13:30-14:00: Cloud Storage & Artifact Registry (supply chain attacks)
- 14:00-14:30: BigQuery (data access & exfiltration)
- 14:30-15:00: Pub/Sub & Cloud Tasks (message interception, async exploitation)

**15:00-18:00** - Harmful Behavior Brainstorm

- Clean up google sheet,
- Go over all scenarios, iterate on them (we'll prob learn things or think of
  thigns from one scenario that carries over to the next & vice versa)
- Target is 100 scenarios (12 per area)

### Day 2 (Tuesday) - Scenario Development & Ranking

**9:00-12:30** - Prioritising workshop

- Review All Scenarios
- Do weighted group ranking
- Go through all 100 scenarios and score them on all vectors (ideally whole
  team) [2-minutes per score]

**12:00-13:00** - Lunch & Buffer & Buffer

**13:00-17:00** - Prep Scenario Dumps for top 20

- Write copy/pastable prompts that will get initial signal fast - see
  [[rapid-signal-detection]]

**17:00-18:00** - Documentation & DeepMind Update

- Document ranking methodology
- Send preliminary scenario list
- Get feedback on priorities

### Day 3 (Wednesday) - Rapid Signal Detection Sprint 1

**9:00-9:30** - Daily Standup & Setup

- Review testing protocol
- Assign scenarios to team members (8 scenarios per person with 2 people)

**9:30-12:30** - Rapid Testing Block 1 (4 scenarios per person)

- Run 30-turn protocol on scenarios 1-8 total
- 45 minutes per scenario
- Parallel execution across team (2 people = 4 scenarios each)
- Live documentation of signals

**12:30-13:30** - Lunch & Buffer

**13:30-17:00** - Rapid Testing Block 2 (4-5 scenarios per person)

- Run 30-turn protocol on scenarios 9-16 total
- 45 minutes per scenario
- Parallel execution (2 people = 4-5 scenarios each)
- Document all responses

**17:00-18:30** - Analysis & Re-ranking

- Compile positive signals
- Identify patterns
- Re-rank remaining scenarios

**18:30-20:00** - Deep Dive Planning & Extra Testing

- If strong signals: Deep dive on top performers
- If weak signals: Test 2 more scenarios each
- Update scenario bank for Day 4

### Day 4 (Thursday) - Signal Expansion & Scaffolding

**9:00-10:00** - Signal Review & Selection

- Review all positive signals from Day 3
- Select top 5-8 signals for expansion
- Assign signals to team members

**10:00-12:00** - Prompt Scaffold Development

- Expand each signal into full scenario with:
  - System context (who is the AI, what's their role)
  - Environmental setup (tools, access, constraints)
  - Threat/motivation (why would they misalign)
  - Decision points (what choices lead to misalignment)
- Create conversation flow templates
- Design perturbations to test robustness
- Hone in control scenarios

**12:00-13:00** - Lunch & Buffer & Buffer

**13:00-15:00** - Testing Expanded Scenario

- Run expanded scenarios with prompt scaffolds
- Test 5+ variations per scenario
- Document what triggers work/don't work
- Identify consistent patterns

**15:00-17:00** - Prompt Scaffold Planning

- Same as morning

**17:00-19:00** - Testing Expanded Scenario

- Same as early afternoon

**19:00 - 20:00** - Learnings & opportunity to re-orient

- Anything we need to do differnetly tomorrow?

### Day 5 (Friday) - Signal Expanding & Scaffolding

**9:00-10:00** - Signal Review & Selection

- Review all positive signals from Day 3
- Select top 5-8 signals for expansion
- Assign signals to team members

**10:00-12:00** - Prompt Scaffold Development

- Expand each signal into full scenario with:
  - System context (who is the AI, what's their role)
  - Environmental setup (tools, access, constraints)
  - Threat/motivation (why would they misalign)
  - Decision points (what choices lead to misalignment)
- Create conversation flow templates
- Design perturbations to test robustness
- Hone in control scenarios

**12:00-13:00** - Lunch & Buffer & Buffer

**13:00-15:00** - Testing Expanded Scenario

- Run expanded scenarios with prompt scaffolds
- Test 5+ variations per scenario
- Document what triggers work/don't work
- Identify consistent patterns

**15:00-17:00** - Prompt Scaffold Planning

- Same as morning

**17:00-19:00** - Testing Expanded Scenario

- Same as early afternoon

### Day 6 (Saturday) - Deep Dive & Catch-up

**9:00-12:00** - Extended Testing Session & checkpoint

- If we delivered on these scenarios, are we moving the needle?

- Run top 5 scenarios with full context
- Test cross-scenario contamination
- Explore edge cases

**13:00-18:00** - Buffer time

- If some scenarios need more work or need to be redone, ...

---

## WEEK 2: Fast Feedback Loops - Prompt-Based Scaffolding

### Template Day Structure (Days 7-12)

**Morning Block (9:00-13:00): Scenario Adaptation**

**9:00-10:00** - Scenario Selection & Planning

- Choose 2 scenarios with strongest signal
- Design system prompts
- Plan context injections

**10:00-12:00** - Prompt Scaffolds

- Create realistic system context
- Develop user personas
- Inject context (PR comments, code, docs)
- Set up everyting in prompt scaffold env

**12:00-13:00** - Initial Testing

- Run first attempts
- Document immediate issues
- Quick iteration

**Afternoon Block (13:00-18:00): Testing & Iteration**

**13:00-14:00** - Lunch & Buffer & Buffer

**14:00-20:00** - Systematic Testing

- Run 30 iterations
- 5-10 perturbations
- Include controls
- Calculate success rates
- Document patterns
- Identify key triggers
- Create reproducible test cases
- Write up findings draft

### Rinse repeat, target 2-4 writeups / day (2 people)

---

## WEEK 3: Up the Realism - Engineering Real Scaffolds (1 Person)

### Two-Day Sprint Structure

Target: 1 realistic scaffold every 2 days (3 total for the week with 1 person)

### Days 13-14 (Monday-Tuesday) - First Realistic Implementation

**Day 13 - Engineering & Setup**

**9:00-11:00** - Demo Selection & Architecture

- Select highest-impact scenario from Week 2 results
- Design realistic architecture based on required services
- Map permissions, data flows, integration points
- Really think through implementation plan
- Focus on the minimally realistic demo (MRD - brb trademarking that)

**11:00-13:00** - Infrastructure Setup

- Provision required GCP services
- Set up authentication & IAM
- Create repos/resources as needed
- Configure monitoring & logging

**13:00-14:00** - Lunch & Buffer

**14:00-18:00** - Core Implementation

- Build main application/service
- Create necessary pipelines/workflows
- Implement realistic business logic
- Add appropriate constraints

**18:00-20:00** - Attack/Misalignment Setup

- Implement the misalignment mechanism
- Create trigger conditions
- Test basic functionality

**Day 14 - Testing & Polish**

**9:00-12:00** - Scenario Refinement

- Add/test realistic delays & constraints
- Refine exploitation/misalignment behavior

**12:00-13:00** - Lunch & Buffer

**13:00-16:00** - Testing & Iteration

- Run variations
- Test different triggers/approaches
- Vary environmental factors
- Document success rates

**16:00-18:00** - Documentation & Demo

- Record video demonstration
- Write technical documentation
- Create reproduction guide
- Package all code

**18:00-20:00** - Analysis

- Compare to prompt version
- Document key differences
- Identify what made it more/less effective

### Days 15-16 (Wednesday-Thursday) - Second Implementation

**Same 2-day structure**

- Select second highest-impact scenario from Week 2
- Follow same implementation pattern

### Days 17-18 (Friday-Saturday) - Third Implementation

**Day 17 - Engineering Sprint**

- Select third scenario based on Week 1-2 findings
- Follow Day 13 structure

**Day 18 - Testing & Week Wrap-up**

**9:00-13:00** - Final Testing

- Complete ML poisoning demo
- Test effectiveness
- Record demonstrations

**13:00-16:00** - Week 3 Synthesis

- Review all 3 realistic demos
- Compare to prompt versions
- Rank by impact & realism

**16:00-18:00** - Prep for Week 4

- Package all demos
- Create summary document
- Plan handoff materials

---

## WEEK 4: FINAL PUSH, CLOSE GAPS & DELIVERY

### Day 19 (Monday) - The Check-day

**9:00-12:00** - Test Re-runs

- Make the strongest cases even stronger
- Misc time alloc for re-runs, re-writes etc.

**12:00-13:00** - Lunch & Buffer

**13:00-18:00** - Control Validation

- Check all controls
- Do they make sense, can they be sharper?
- Verify causation

### Day 20 (Tuesday) - Report Drafting

**9:00-12:00** - Report Structure & Executive Summary

- Create report outline
- Write executive summary (2-3 pages)
- Draft key findings section
- Create initial recommendations

**12:00-13:00** - Lunch & Buffer

**13:00-16:00** - Technical Sections

- Write methodology section
- Document all scenarios tested
- Compile success rates & statistics
- Create comparison tables (prompt vs realistic)

**16:00-18:00** - Visuals & Evidence

- Create charts/graphs
- Select key video clips
- Organize code snippets
- Build evidence appendix

**18:00-20:00** - First Draft Review

- Internal review of draft
- Identify gaps
- List needed additional work

### Day 21 (Wednesday) - Report Strengthening

**9:00-12:00** - Gap Filling

- Run additional tests for weak claims
- Strengthen statistical significance where needed
- Add missing control experiments
- Clarify ambiguous findings

**12:00-13:00** - Lunch & Buffer

**13:00-16:00** - Evidence Enhancement

- Record additional demos if needed
- Create clearer visualizations
- Add more concrete examples
- Strengthen causal arguments

**16:00-18:00** - Mitigation Section

- Draft mitigation recommendations
- Prioritize by impact & feasibility
- Include implementation guidance
- Note limitations

**18:00-20:00** - Second Draft

- Incorporate all improvements
- Polish language
- Check consistency

### Day 22 (Thursday) - Report Finalization

**9:00-12:00** - Final Editing

- Line-by-line review
- Fix all inconsistencies
- Polish executive summary
- Finalize recommendations

**12:00-13:00** - Lunch & Buffer

**13:00-16:00** - Supporting Materials

- Create slide deck (?)
- Package reproducibility code
- Write setup instructions
- Organize all demos

**16:00-18:00** - Final Review

- Complete quality check
- Verify all claims
- Check all links/references
- Final formatting

**18:00-20:00** - Delivery Prep

- Create handoff package
- Prepare presentation notes
- Test all demos
- Upload to shared drive

### Day 23 (Friday) - Delivery & Handoff

**9:00-11:00** - Final Checks

- Last-minute adjustments
- Verify all materials accessible

**12:00** - Handoff

- Transfer all materials
- Provide access to repos
- Document open questions

**14:00-18:00** - Retrospective

- Team debrief
- Lessons learned
- Future recommendations

### Day 24 (Saturday) - Final Sprint & Cleanup

**9:00-12:00** - Address Feedback

- Respond to DeepMind questions
- Run any requested additional tests
- Clarify any ambiguities
- Make final adjustments

**12:00-13:00** - Lunch & Buffer

**13:00-16:00** - Archive & Document

- Final cleanup of all code
- Archive all test results
- Create comprehensive index
- Document lessons learned

**16:00-18:00** - Knowledge Transfer

- Create internal documentation
- Update methodology guides
- Package reusable components
- Plan follow-up work

---

## Key Success Metrics

### Week 1 Targets:

- 100 scenarios generated and ranked in Google Sheet
- 20 scenarios tested with rapid signal detection (2 people x ~8 scenarios on
  Day 3)
- 5-8 positive signals identified and expanded into prompt scaffolds
- 8-10 prompt-based misalignment demos ready

### Week 2 Targets:

- 12-16 prompt-based demos created (2-4 per day with 2 people)
- 30+ iterations per scenario tested
- 5-10 perturbations per scenario documented
- Success rates and patterns documented for each

### Week 3 Targets:

- 3 realistic implementations built (1 person, 1 every 2 days)
- Video recordings for each demo
- Complete reproduction packages
- Detailed comparisons to prompt versions (Level 1 vs Level 2)

### Week 4 Targets:

- Comprehensive report with executive summary
- All demos strengthened with additional evidence
- Mitigation recommendations documented
- Complete handoff package delivered

## Risk Management

### Daily Checkpoints:

- 8:30 - Team sync
- 13:00 - Progress check (slack)
- 18:00 - Documentation review
- 19:00 - DeepMind update (as needed)

### Contingency Plans:

- If no signal by Day 3: Pivot to different model versions
- If too many signals: Focus on most realistic/impactful
- If engineering blocked: Double down on prompt-based
- If prompt-based insufficient: Accelerate engineering

## Communication Cadence

### Daily:

- 8:30 - Internal standup
- 18:00 - Slack/e-mail update to DeepMind (?)

### Ad-hoc:

- Critical findings within 1 hour
- Blockers within 2 hours
- Questions within 4 hours

## Documentation Standards

### Per Scenario:

- Initial hypothesis
- Exact prompts used
- All variations tested
- Success/failure rates
- Statistical analysis
- Reproducibility instructions
- Video recording
- Lessons learned

### Per Day:

- Activities completed
- Scenarios tested
- Signals detected
- Blockers encountered
- Next steps
- Time tracking

### Per Week:

- Executive summary
- Technical findings
- Statistical analysis
- Recommendations
- Demo materials
- Reproducibility package

---
