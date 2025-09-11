# Linear Project Conversion Prompt for DeepMind Alignment Audit Sprint

Convert the attached @deepmind-hourly-exectuion-plan.md execution plan into a
Linear project following the correct hierarchy and ticket writing best practices
via MCP

## Linear Project Structure:

1. **Correct Hierarchy**:
   - PROJECT: "DeepMind Alignment Audit Sprint"
   - MILESTONES (Major Deliverables):
     - "Week 1 Deliverables" (Due: Jan 20)
     - "Week 2 Deliverables" (Due: Jan 27)
     - "Week 3 Deliverables" (Due: Feb 3)
     - "Final Report & Handoff" (Due: Feb 10)
   - CYCLES (Time periods):
     - "Pre-Engagement Setup" (before Week 1)
     - "Week 1: Discovery & Signal Detection"
     - "Week 2: Prompt-Based Scaffolding"
     - "Week 3: Realistic Implementations"
     - "Week 4: Final Report & Delivery"
   - ISSUES: Individual work items within each cycle

2. **Project Setup**:
   ```
   PROJECT: DeepMind Alignment Audit Sprint
   ├── MILESTONES:
   │   ├── Week 1 Deliverables (Due: Jan 20)
   │   │   - 100+ scenarios documented
   │   │   - 20+ scenarioDrop evaluations
   │   │   - 5-8 expanded prompt scaffolds
   │   ├── Week 2 Deliverables (Due: Jan 27)
   │   │   - 12-16 prompt-based demos
   │   │   - GitHub repositories with test data
   │   ├── Week 3 Deliverables (Due: Feb 3)
   │   │   - 3 realistic GCP implementations
   │   │   - "In the wild" demo videos
   │   └── Final Report & Handoff (Due: Feb 10)
   │       - Comprehensive report
   │       - All materials delivered
   ├── CYCLES:
   │   ├── Pre-Engagement Setup
   │   ├── Week 1 - Discovery & Signal Detection (Jan 15-20)
   │   ├── Week 2 - Prompt-Based Scaffolding (Jan 22-27)
   │   ├── Week 3 - Realistic Implementations (Jan 29-Feb 3)
   │   └── Week 4 - Final Report & Delivery (Feb 5-10)
   ```

3. **Issues Organization by Cycle**:

   Within each cycle, create issues that represent:
   - Daily deliverable groups (e.g., "Day 1: Deployment Landscape Mapping")
   - Major deliverables (e.g., "Create 100 Scenarios Master Sheet")
   - Individual tasks (2-8 hours each)

   Example structure:
   ```
   CYCLE: Week 1 - Discovery & Signal Detection
   ├── ISSUE: Set up scenario tracking infrastructure
   │   └── Sub-issue: Create master Google Sheet template with scoring columns
   │   └── Sub-issue: Set up shared documentation workspace
   ├── ISSUE: Day 1 - Deployment Landscape Mapping
   │   └── Sub-issue: Cloud Build & GitHub Actions brainstorm (45m)
   │   └── Sub-issue: Cloud Functions & Cloud Run scenarios (45m)
   │   └── Sub-issue: Consolidate scenarios into master sheet (2h)
   ├── ISSUE: Day 2 - Scenario Ranking Workshop
   │   └── Sub-issue: Define weighted scoring criteria (2h)
   │   └── Sub-issue: Score all 100 scenarios (3.5h)
   └── ISSUE: Week 1 - DeepMind Presentation
       └── Sub-issue: Compile findings and create slide deck (2h)
       └── Sub-issue: Record demo videos (1h)
   ```

4. **Labels Structure** (project-wide):
   - `type/infrastructure`
   - `type/research`
   - `type/testing`
   - `type/documentation`
   - `type/presentation`
   - `type/engineering`
   - `team/full-team`
   - `team/pair-work`
   - `team/solo`
   - `blocked`
   - `week-1`, `week-2`, `week-3`, `week-4`

5. **Milestone Configuration**:

   Each milestone tracks major deliverables with specific issues attached:
   
   **Week 1 Deliverables** (Due: Jan 20)
   - Attach: Google Sheet creation issue
   - Attach: ScenarioDrop evaluation issues
   - Attach: Prompt scaffold development issues
   - Attach: Pattern analysis document issue
   - Attach: DeepMind presentation issue

   **Week 2 Deliverables** (Due: Jan 27)
   - Attach: All prompt-based demo writeup issues
   - Attach: GitHub repository setup issues
   - Attach: Statistical analysis issues
   - Attach: Week 2 presentation issue

   **Week 3 Deliverables** (Due: Feb 3)
   - Attach: Realistic implementation issues
   - Attach: Demo video recording issues
   - Attach: Believability assessment issues
   - Attach: Week 3 presentation issue

   **Final Report & Handoff** (Due: Feb 10)
   - Attach: Report drafting issues
   - Attach: Materials packaging issues
   - Attach: Handoff documentation issues

6. **Cycle-Specific Goals**:

   For each cycle description, include progress tracking:
   ```markdown
   ## Week 1 Goals
   
   Linked to Milestone: Week 1 Deliverables
   
   - [ ] 100+ scenarios documented in Google Sheet
   - [ ] 20+ scenarioDrop evaluations completed
   - [ ] 5-8 expanded prompt scaffolds ready
   - [ ] Pattern analysis document complete
   - [ ] DeepMind presentation delivered

   ## Key Metrics
   - Scenarios generated: /100
   - Scenarios tested: /20
   - Positive signals found: /8
   ```

## Ticket Writing Best Practices:

### 1. **Title Guidelines** (The What)

- **Structure**: `[Component] Verb + Specific Outcome`
- **Length**: 50-70 characters ideal (Linear shows ~80 in lists)
- **Action verbs**: Build, Create, Test, Document, Analyze, Deploy, Configure,
  Design
- **Be specific**: Include quantities, services, or key identifiers

✅ GOOD Examples:

- "Create master Google Sheet for 100 scenario rankings"
- "Test 8 GitHub Actions scenarios using 30-turn protocol"
- "Deploy realistic GCP infrastructure for demo #1"

❌ BAD Examples:

- "Spreadsheet work" (too vague)
- "Testing" (no context)
- "Set up infrastructure for the realistic implementation demo for week 3" (too
  long)

### 2. **Description Template** (The Why, What, and How)

Use this markdown template for every ticket:

```markdown
## Context

[1-2 sentences on why this matters to project success and what problem it
solves. Focus on the "why" - this guides developers through ambiguity]

## Objective

[One clear sentence stating the measurable outcome]

## Success Criteria

- [ ] Specific deliverable with acceptance criteria
- [ ] Quality metric (e.g., "All 100 scenarios documented")
- [ ] Verification step (e.g., "Peer reviewed by team member")
- [ ] Documentation updated (if applicable)

## Technical Requirements

[For engineering tickets - specify the "how" in technical detail]
- Framework/library constraints
- Performance requirements
- Security considerations
- API specifications

## Assumptions to Validate

- [ ] [List any assumptions that need verification]
- [ ] [Include technical feasibility questions]

## Approach

[Bullet points of key steps - keep tactical]

- Step 1: Set up X
- Step 2: Configure Y
- Step 3: Test Z

## Time Box

Estimated time: X hours Hard stop at: Y hours (if applicable)

## Dependencies

- Blocked by: #[issue-number] - [brief reason]
- Blocks: #[issue-number] - [brief reason]

## Resources

- [Template/Document name](link)
- [Previous example](link)
- Slack channel: #channel-name
- Design mockups: [link]
- API documentation: [link]

## Definition of Done

- [ ] Core task completed
- [ ] Tests pass (if applicable)
- [ ] Code reviewed and approved
- [ ] Documentation updated
- [ ] Results logged in [specific location]
- [ ] Team notified in Slack
```

### 3. **Sizing Best Practices**

**Linear Points Mapping**:

- XS (1 point) = 1-2 hours: Simple, well-defined tasks
- S (2 points) = 2-4 hours: Standard tasks, single sitting
- M (3 points) = 4-6 hours: Complex tasks, may need breaks
- L (5 points) = 6-8 hours: Full day tasks
- XL (8 points) = Multi-day: MUST break down into sub-issues

**Sizing Rules**:

- If > 8 hours: Break into sub-issues
- If < 1 hour: Combine with related work
- Include: Research, implementation, testing, documentation
- Buffer: Add 20% to initial estimates for unknowns

### 4. **Sub-Issue Best Practices**

**When to use sub-issues**:

- Parent issue represents a deliverable
- Sub-issues represent steps to achieve it
- Each sub-issue is independently completable

**Parent Issue Example**:

```
Title: "Deliverable: Week 1 Scenario Analysis Report"
Description: 
## Objective
Complete comprehensive analysis of all 100 scenarios tested in Week 1

## Success Criteria
- [ ] All 100 scenarios documented
- [ ] Top 20 prioritized with justification  
- [ ] Pattern analysis complete
- [ ] Ready for DeepMind presentation

Sub-issues:
├── Compile scenario test results from Days 1-3
├── Perform statistical analysis on success rates
├── Create pattern identification document
├── Design visualization charts
└── Write executive summary (2-3 pages)
```

### 5. **Special Ticket Types**

**a) Time-boxed Research Tickets**:

```
Title: "[Research] Analyze Cloud Build attack vectors (45min)"

## Time Box
Strict limit: 45 minutes
Output regardless of completion level

## Minimum Outputs
- [ ] 5+ scenarios documented
- [ ] Top 3 prioritized
- [ ] Notes in shared doc
```

**a.1) Research Spike Tickets**:

```
Title: "[Spike] Validate technical feasibility of GCP monitoring bypass"

## Purpose
Validate assumptions before committing to implementation

## Questions to Answer
- [ ] Is the proposed approach technically feasible?
- [ ] What are the main technical risks?
- [ ] Estimated effort for full implementation?

## Time Box
Maximum: 4 hours (stop regardless of findings)

## Deliverables
- [ ] Technical feasibility report
- [ ] Risk assessment
- [ ] Go/No-go recommendation
- [ ] If go: Create follow-up implementation tickets
```

**b) Parallel Work Tickets**:

```
Title: "[Testing] Run scenarios 1-4 - Engineer 1"

## Parallel Work Notice
This runs parallel with:
- #123 [Testing] Run scenarios 5-8 - Engineer 2

## Coordination
- Start: 9:30am sharp
- Check-in: 11:00am in Slack
- Merge results: 12:30pm
```

**c) Checkpoint/Review Tickets**:

```
Title: "[Checkpoint] Week 2 deliverables review"

## Review Criteria
- [ ] All 12-16 writeups meet 5-8 page requirement
- [ ] Statistical analysis p < 0.05
- [ ] GitHub repos properly structured
- [ ] Reproduction verified independently
```

**d) Daily Standup Tickets**:

```
Title: "[Standup] Day 5 - Friday sync"

## Agenda
- [ ] Review Day 4 deliverables
- [ ] Assign Day 5 signal expansion tasks  
- [ ] Identify blockers
- [ ] Adjust timeline if needed

## Updates to Capture
- [ ] Completed items
- [ ] In-progress status
- [ ] Blockers/risks
- [ ] Next 24h priorities
```

### 6. **Common Pitfalls to Avoid**

❌ **Vague Success Criteria**:

- Bad: "Test scenarios"
- Good: "Test 8 scenarios using 30-turn protocol, document signals in
  spreadsheet"

❌ **Missing Context**:

- Bad: Starting with "Create presentation"
- Good: Starting with "To demonstrate Week 1 findings to DeepMind..."

❌ **Unclear Ownership**:

- Bad: "Team brainstorms ideas"
- Good: "@Engineer1 facilitates, @Engineer2 documents, all participate"

❌ **No Definition of Done**:

- Bad: Ending with approach steps
- Good: Clear checklist of what constitutes completion

❌ **Poor Estimates**:

- Bad: "A few hours"
- Good: "3 hours (2h implementation + 1h testing)"

❌ **"Do This Thing" Syndrome**:

- Bad: "Update the database"
- Good: "Migrate user table to add 'last_login' timestamp field for activity tracking"

❌ **Mind-Reading Requirements**:

- Bad: "Make it work better"
- Good: "Reduce API response time from 2s to <500ms by implementing caching layer"

❌ **Bundling Unrelated Work**:

- Bad: "Fix login bug, update docs, and add new feature"
- Good: Create separate tickets for each distinct piece of work

### 7. **Label Usage Rules**

**Required fields/labels** (every ticket must have):

- One `type/*` label
- Priority set using Linear's built-in field (Urgent/High/Medium/Low)
- Milestone attached (if it's a deliverable)

**Conditional labels**:

- `blocked` - if waiting on dependencies
- `team/*` - if involves multiple people
- `week-*` - to indicate which week the task belongs to

### 8. **Writing for Async Work**

Since team members may pick up tickets independently:

- Include all context in the ticket (don't assume knowledge)
- Link to all resources needed
- Specify exact output format/location
- Include examples where possible
- Add contact person for questions
- **All requirements must be in the ticket** - no email/Slack-only requirements
- Capture all decisions and rationale in the ticket for future reference
- Update tickets in real-time as requirements change
- Use ticket comments for clarifications, not external channels

### 9. **Quality Checklist**

Before creating any ticket, verify:

- [ ] Title is specific and action-oriented
- [ ] Description follows template
- [ ] Success criteria are measurable
- [ ] Estimate is realistic (with buffer)
- [ ] Dependencies are identified
- [ ] Resources are linked
- [ ] Labels are applied
- [ ] Assignee is clear (or marked as "up for grabs")

### 10. **Examples of Well-Written Tickets**

**Example 1 - Infrastructure Setup**:

```
Title: "Configure GCP test project with Vertex AI quotas"

## Context
We need a dedicated GCP environment to run alignment tests without affecting production systems. This blocks all Week 1 testing activities.

## Objective
Set up a fully configured GCP project with appropriate Vertex AI quotas for 20+ parallel tests.

## Success Criteria
- [ ] New GCP project created with billing enabled
- [ ] Vertex AI API enabled with quota for 50 requests/minute
- [ ] Service accounts created for each team member
- [ ] Access verified by test API call

## Approach
- Create project via GCP Console
- Enable required APIs (list in resources)
- Request quota increase through support
- Configure IAM roles per security doc
- Run verification script

## Time Box
Estimated: 3 hours
Hard stop: 4 hours (quota approval may add delay)

## Dependencies
- Blocked by: #001 - GCP account access approval
- Blocks: #045 - All Week 1 testing tasks

## Resources
- [GCP Setup Guide](link)
- [Quota Request Template](link)
- [IAM Configuration](link)

## Definition of Done
- [ ] Project accessible by all team members
- [ ] Quotas confirmed in GCP Console
- [ ] Test script runs successfully
- [ ] Configuration documented in wiki
- [ ] Team notified in #sprint-infra channel
```

**Example 2 - Testing Task**:

```
Title: "Test Cloud SQL data exfiltration scenarios 1-4"

## Context
Part of Day 3's rapid signal detection sprint. We're testing if models can be prompted to exfiltrate data from Cloud SQL databases, which is critical for understanding data security risks.

## Objective
Run 4 Cloud SQL scenarios through our 30-turn protocol and document any positive signals.

## Success Criteria
- [ ] All 4 scenarios tested completely (30 turns each)
- [ ] Chat histories saved in JSON format
- [ ] Signals documented in master spreadsheet
- [ ] Success rate calculated with confidence intervals

## Approach
- Load scenarios 1-4 from prepared templates
- Execute 30-turn protocol for each
- Save full transcripts after each run
- Update tracking sheet in real-time
- Flag any positive signals immediately

## Time Box
Estimated: 3 hours (45 min per scenario)
Hard stop: 3.5 hours

## Dependencies
- Blocked by: #067 - Scenario templates prepared
- Blocks: #089 - Day 3 analysis compilation

## Resources
- [30-turn protocol guide](link)
- [Scenario templates](link)
- [Master tracking sheet](link)
- [Signal classification rubric](link)

## Definition of Done
- [ ] 4 complete test runs documented
- [ ] JSON files uploaded to `/transcripts/day3/`
- [ ] Spreadsheet updated with results
- [ ] Positive signals flagged in Slack
- [ ] Ready for afternoon analysis session
```

**Example 3 - Documentation Deliverable**:

```
Title: "Deliverable: Week 2 prompt scaffold writeup #1"

## Context
First of 12-16 required writeups documenting our prompt-based scaffolding results. These writeups are critical for demonstrating reproducible misalignment patterns to DeepMind.

## Objective
Complete a 5-8 page writeup for scenario #1 including all required sections per the writeup criteria.

## Success Criteria
- [ ] Executive summary ≤ 1 page
- [ ] Full writeup 5-8 pages total
- [ ] 30+ test iterations documented
- [ ] Statistical significance p < 0.05 vs controls
- [ ] GitHub repo created with all artifacts
- [ ] Reproduction independently verified

## Approach
- Set up GitHub repo with standard structure
- Run 10 propensity evaluation runs
- Design 3 control conditions
- Execute 30+ main test iterations
- Test 5-10 perturbations
- Calculate statistics and create visualizations
- Write concise findings
- Get peer review

## Time Box
Estimated: 6 hours
- 2h: Setup and controls
- 2h: Testing iterations
- 1h: Analysis
- 1h: Writing

## Dependencies
- Blocked by: #112 - Scenario selection from Week 1
- Blocks: #156 - Week 2 presentation compilation

## Resources
- [Writeup template](link)
- [Statistical analysis scripts](link)
- [GitHub repo template](link)
- [Example from previous project](link)

## Definition of Done
- [ ] GitHub repo live with all required directories
- [ ] All test data in CSV format
- [ ] Transcripts saved as JSON
- [ ] Writeup meets all criteria in checklist
- [ ] Stats validated by second team member
- [ ] Added to Week 2 deliverables tracker
```

## Implementation Notes:

1. **Ticket Creation Order**:
   - Create all cycles first
   - Add high-level issues for each day/major deliverable
   - Break down into sub-issues
   - Link dependencies last

2. **Views to Configure**:
   - **Sprint Overview**: Group by Cycle, sort by Priority
   - **Daily Standup**: Filter current cycle, group by Status
   - **Milestone Progress**: Group by Milestone, show completion %
   - **Deliverables Tracker**: Filter by Milestone attachment
   - **Dependency Map**: Timeline view showing blockers
   - **Personal Work**: Filter by assignee
   - **Roadmap View**: Timeline grouped by Milestones

3. **Automation Suggestions**:
   - Auto-assign to current cycle based on dates
   - Move to "In Review" when PR linked
   - Add "blocked" label when dependency not complete
   - Notify Slack when deliverables complete

4. **CSV Import Format** (if bulk creating):
   ```csv
   Title,Description,Status,Priority,Estimate,Labels,Cycle,Assignee
   "[Infrastructure] Set up GCP test project","## Context\n...",Backlog,High,3,"type/infrastructure,week-1",Pre-Engagement,@Engineer1
   ```

This comprehensive prompt ensures that every ticket created will be:

- Self-contained and actionable
- Properly sized and estimated
- Connected to project goals
- Easy to pick up by any team member
- Measurable in terms of completion
- Integrated with Linear's features

The resulting Linear project will have clear structure, excellent ticket
quality, and enable smooth execution of the DeepMind Alignment Audit Sprint.
