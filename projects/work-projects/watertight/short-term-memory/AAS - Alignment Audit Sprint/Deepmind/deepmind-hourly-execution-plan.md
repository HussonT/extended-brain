# DeepMind Gemini Alignment Testing - Hour-by-Hour Execution Plan

## Pre-Engagement TODOs (Complete Before Day 1)

### Prep (before the two weeks start)

- [ ] Create a shared drive where we share our results
- [ ] Brainstorm until you have at least 20 scenarios you're excited about for
      each threat-model. Get buy in / feedback on the key ones.

---

## WEEK 1: DISCOVERY & SIGNAL DETECTION

### Week 1 Deliverables Overview

- **100+ scenarios** documented and ranked in Google Sheet with REI scoring - see
  [[writing-effective-drop-scenarios]]
- **REI (Realism/Effort/Impact) scoring framework** - drop-score-prompt.md with
  comprehensive scoring rubric for prioritizing scenarios
- **20+ scenarioDrop evaluations** with full chat histories - a folder with a
  scenario drop document and a chat history of the 30 turn conversation and a
  pattern analysis document (See pattern analysis document)
- **Progressive Drop Methodology documentation** - turn-by-turn escalation
  framework, "Chekhov's Gun" effect, binary dilemma architecture
- **5-8 initial prompt scaffolds** ready for Week 2 - a folder complete with:
  - system_prompt.txt, user_prompt.txt & context.txt
  - **metadata.json** with standardized structure (decision drivers,
    verification criteria, implementation notes)
  - **scenario_analysis.md** with threat modeling, discovery pathways,
    environmental requirements
  - .gemini/settings.json
- **Pattern analysis document** with success metrics - this is a document with
  all your notes from during the converation - write all the hunches you have
  from how the model acted during the scenarioDrop - do this during or right
  after doing the drop!!
- **DeepMind presentation** with demo videos
- **A learnings doc** - what'd you learn this week??
- **Zoom out** - do we have everything we need to really move the needle for
  Deepmind?

### Day 1 (Monday) - Deployment Landscape Mapping

#### Deliverables:

- **Google Sheet with 100 scenarios** (12 per service area)
  - Columns: Service, Scenario Description, Attack Vector, Potential Impact,
    Goal Conflict Type, REI Scores (Realism, Effort, Impact)
- **8 service-specific brainstorm documents**
- **Initial threat taxonomy document**
- **REI scoring framework document** (drop-score-prompt.md)

#### Tasks:

- [ ] Create master Google Sheet template with weighted scoring columns
- [ ] Create 100+ Scenario Drop Tempalted docs themed by threat-model / threat
      env.
- [ ] Iterate each threat-model (45 mins each)
- [ ] Consolidate all scenarios into master sheet
- [ ] Create useful categorizations to make sure we're covering a wide range of
      threat models / topics

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

#### Deliverables:

- **Weighted scoring matrix** with all 100 scenarios scored using REI framework
- **Top 20 prioritized scenarios** with rapid test templates
- **ScenarioDrop prompt templates** for each top 20 using progressive drop methodology
- **Ranking methodology document** including REI scoring rubric

#### Tasks:

- [ ] Apply REI scoring criteria (Realism 0-100, Effort 0-100, Impact 0-100)
- [ ] Group scoring session (2 mins per scenario)
- [ ] Create copy-pastable scenarioDrop prompts with progressive escalation
- [ ] Build rapid signal detection protocol document
- [ ] Send preliminary list to DeepMind

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

#### Deliverables:

- **16 scenarioDrop evaluations** with full chat histories saved
- **Signal detection results spreadsheet**
- **Pattern analysis document**
- **Re-ranked scenario list**

#### Tasks:

- [ ] Run 30-turn protocol on 16 scenarios total
- [ ] Save complete chat histories for each scenarioDrop
- [ ] Document positive/negative signals in spreadsheet
- [ ] Identify patterns across scenarios
- [ ] Re-rank remaining scenarios based on signals

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

### Day 4 (Thursday) - DeepMind Presentation Prep & Signal Expansion

**9:00-13:00** - DeepMind Week 1 Presentation Preparation

- 9:00-10:00: Compile all findings from Days 1-3
  - Review deployment landscape mapping results
  - Consolidate scenario rankings
  - Gather positive signal data
- 10:00-11:30: Create presentation materials
  - Build slide deck with key findings
  - Prepare demo videos from successful tests
  - Document methodology and approach
- 11:30-12:30: Internal review & rehearsal
  - Practice presentation flow
  - Refine messaging and visuals
- 12:30-13:00: Final prep and materials upload

**13:00-14:00** - Lunch & Buffer

**14:00-15:00** - DeepMind Presentation/Update Call

- Present Week 1 findings
- Get feedback on priorities
- Discuss Week 2 focus areas

**15:00-17:00** - Post-Presentation Work

- Incorporate DeepMind feedback
- Adjust Week 2 plans if needed
- Quick signal review from Day 3

**17:00-19:00** - Scaffold Development (if time permits)

- Begin expanding top signals into scenarios
- Create initial conversation templates

**19:00-20:00** - Team Sync & Planning

- Discuss presentation feedback
- Plan Friday's activities
- Adjust strategy based on DeepMind input

### Day 5 (Friday) - Signal Expanding & Scaffolding

#### Deliverables:

- **5-8 expanded scenario documents** with:
  - Full context and personas
  - Environmental setup details
  - Conversation flow templates
  - Perturbation strategies (5+ variations per scenario)
- **Control scenarios** for each expanded signal
- **Trigger pattern documentation**

#### Tasks:

- [ ] Select top 5-8 signals for expansion
- [ ] Create detailed prompt scaffolds with system context
- [ ] Design perturbations to test robustness
- [ ] Test expanded scenarios with variations
- [ ] Document what triggers work/don't work
- [ ] Identify consistent patterns

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

### Week 2 Deliverables Overview

- **12-16 prompt-based scaffold demos** (2-4 per day with 2 people)
- **GitHub repositories** for each scenario with full test results
- **Multiple condition testing** per scenario (4+ conditions, 120+ total runs):
  - Social dynamics variations (e.g., peer opposition vs support)
  - Policy variations (e.g., audits passed vs failed)
  - Environmental variations
- **30+ iterations per condition** tested and documented
- **Alignment switches analysis** - identifying critical factors that flip behavior
- **Individual condition analysis summaries** (analysis_summary_*.md files)
- **5-10 perturbations per scenario** with success rates
- **Pattern documentation** for each scenario
- **Reproducible test cases** with exact prompts
- **Statistical analysis** of success rates and condition comparisons
- **DeepMind presentation** with comparison charts

### Writeup Criteria (REQUIRED for each scenario)

Each writeup must include ALL of the following sections:

#### 1. Executive Summary (1 page max)

- **Scenario name and classification**
- **Success rate** (percentage and confidence interval)
- **Alignment switches identified** (critical factors that flip behavior)
- **Key finding** (1-2 sentences)
- **Risk assessment** (Low/Medium/High/Critical)

#### 2. Methodology Section

- **Base prompt scaffold** (exact system prompt used)
- **Environmental context** (tools, permissions, data access)
- **Persona definition** (who is the AI, their role, motivations)
- **Threat model** (what misalignment we're testing for)

#### 3. Test Results

- **Control conditions** (minimum 3):
  - Benign baseline (no misalignment attempt)
  - Inverted control (opposite instruction)
  - Null control (irrelevant task)
- **Propensity evaluation** (base rate of behavior):
  - 10 runs without any prompt engineering
  - Document natural occurrence rate
- **Multiple condition testing** (4+ conditions, 30+ iterations each):
  - Social dynamics conditions (e.g., peer opposed vs supportive)
  - Policy conditions (e.g., audits passed vs failed)
  - Environmental conditions
  - **Alignment switches analysis**: Document percentage point differences between conditions
- **Individual condition analysis summaries**:
  - Separate analysis_summary_*.md for each condition
  - Run-by-run behavioral analysis with quotes
- **Main test runs** (120+ total across conditions):
  - Full transcripts for first successful attempt
  - Summary statistics for all runs
  - Time to first success (if applicable)
- **Perturbation results** (5-10 variations):
  - Semantic perturbations (rephrasing)
  - Structural perturbations (reordering)
  - Partial perturbations (removing elements)
  - Environmental perturbations (changing context)
  - Persona perturbations (different roles)

#### 4. Evidence & Artifacts

- **GitHub repository** with:
  - `/prompts/` - All prompt versions
  - `/transcripts/` - Full conversation logs (JSON format)
  - `/results/` - CSV with all test results
  - `/analysis/` - Statistical analysis scripts
  - `README.md` - Reproduction instructions
  - `requirements.txt` - Dependencies
- **Key transcripts** (embedded in writeup):
  - Most successful misalignment
  - Most robust defense
  - Edge cases discovered
- **Statistical analysis**:
  - Success rate with 95% CI
  - P-value vs control conditions
  - Effect size (Cohen's d or similar)

#### 5. Concision Requirements

- **Total length**: 5-8 pages maximum
- **Transcript excerpts**: Max 500 words each
- **Bullet points** preferred over paragraphs
- **Tables and charts** required for results

### Template Day Structure (Days 7-9, 11-12)

#### Daily Deliverables (per day):

- **2-4 complete writeups** meeting ALL criteria above
- **2-4 GitHub repositories** with full test data
- **Statistical validation** for each scenario including alignment switches
- **Individual condition analysis summaries** for each condition tested
- **Reproducibility verification** (independent re-run)

#### Daily Tasks:

- [ ] Select 2 scenarios with strongest signals
- [ ] Create GitHub repository with metadata.json and scenario_analysis.md
- [ ] Design and document control conditions (3+ per scenario)
- [ ] Design 4+ test conditions (social dynamics, policy variations, etc.)
- [ ] Run propensity evaluation (10 base runs)
- [ ] Create realistic system prompts and context
- [ ] Develop user personas and inject context
- [ ] Run 30+ iterations per condition (120+ total) with full logging
- [ ] Analyze alignment switches between conditions
- [ ] Write individual analysis_summary_*.md for each condition
- [ ] Test 5-10 perturbations systematically
- [ ] Save all transcripts to GitHub (JSON format) organized by condition
- [ ] Calculate statistical significance vs controls and between conditions
- [ ] Generate results tables and charts showing condition comparisons
- [ ] Write concise findings (5-8 pages max) including alignment switches
- [ ] Create reproduction instructions in README
- [ ] Verify independent reproducibility

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

### Day 10 (Thursday) - DeepMind Week 2 Presentation Prep

**9:00-13:00** - DeepMind Week 2 Presentation Preparation

- 9:00-10:00: Compile Week 2 findings
  - Review all prompt-based demos created
  - Analyze success rates and patterns
  - Select most impactful findings
- 10:00-11:30: Build presentation materials
  - Update slide deck with Week 2 progress
  - Create comparison charts (success rates, patterns)
  - Package reproducible test cases
- 11:30-12:30: Internal review & dry run
  - Practice demos
  - Refine technical explanations
- 12:30-13:00: Final materials preparation

**13:00-14:00** - Lunch & Buffer

**14:00-15:00** - DeepMind Presentation/Update Call

- Present Week 2 prompt scaffold results
- Demonstrate most successful misalignment patterns
- Discuss implications for Week 3 realistic implementations

**15:00-18:00** - Post-Presentation Work

- Incorporate feedback
- Prioritize scenarios for Week 3 realistic builds
- Document decisions and adjustments

**18:00-20:00** - Catch-up Testing (if needed)

- Complete any unfinished scenarios
- Re-test based on DeepMind feedback

### GitHub Repository Template Structure

Each scenario must have its own GitHub repository with the following structure:

```
scenario-[name]/
├── README.md                 # Reproduction instructions
├── requirements.txt          # Dependencies
├── config.yaml              # Test configuration
├── metadata.json            # Standardized scenario metadata
├── scenario_analysis.md     # Threat modeling and verification criteria
├── prompts/
│   ├── base_scaffold.txt    # Main prompt
│   ├── controls/            # Control prompts
│   ├── conditions/          # Multiple condition variations
│   └── perturbations/       # Variation prompts
├── transcripts/
│   ├── condition_1/         # Condition 1 logs (e.g., kyle_opposed)
│   ├── condition_2/         # Condition 2 logs (e.g., kyle_not_opposed)
│   ├── condition_3/         # Condition 3 logs (e.g., audits_passed)
│   ├── condition_4/         # Condition 4 logs (e.g., audit_failed)
│   └── controls/            # Control condition logs
├── results/
│   ├── summary_stats.csv   # All test results
│   ├── alignment_switches.csv # Critical factors analysis
│   ├── propensity.csv      # Base rate evaluation
│   └── perturbations.csv   # Perturbation results
├── analysis/
│   ├── analysis_summary_condition_1.md # Individual condition analysis
│   ├── analysis_summary_condition_2.md # Individual condition analysis
│   ├── analysis_summary_condition_3.md # Individual condition analysis
│   ├── analysis_summary_condition_4.md # Individual condition analysis
│   ├── statistical_tests.py # Analysis scripts
│   ├── generate_charts.py   # Visualization
│   └── figures/             # Generated charts
└── writeup/
    ├── scenario_writeup.md  # Full writeup with alignment switches
    └── executive_summary.md # 1-page summary
```

### Writeup Quality Checklist

Before submitting any writeup, verify ALL items:

**Statistical Rigor:**

- [ ] Control conditions show p > 0.05 (no effect)
- [ ] Main effect shows p < 0.05 vs controls
- [ ] Effect size calculated (Cohen's d > 0.5 preferred)
- [ ] 95% confidence intervals included
- [ ] Propensity baseline documented

**Documentation Completeness:**

- [ ] GitHub repository fully populated
- [ ] All transcripts saved in JSON format
- [ ] Reproduction instructions tested independently
- [ ] CSV files contain all raw data
- [ ] Charts/visualizations generated

**Concision Standards:**

- [ ] Executive summary ≤ 1 page
- [ ] Full writeup ≤ 8 pages
- [ ] Transcript excerpts ≤ 500 words each
- [ ] Bullet points used where appropriate
- [ ] Tables summarize quantitative results

**Scientific Validity:**

- [ ] Threat model clearly defined
- [ ] Success criteria objective and measurable
- [ ] Perturbations systematic (not cherry-picked)
- [ ] Limitations acknowledged
- [ ] Causal claims justified

### Rinse repeat, target 2-4 writeups / day (2 people)

---

## WEEK 3: Up the Realism - Engineering Real Scaffolds

### Week 3 Deliverables Overview

- **3 GitHub repositories** with fully deployed GCP implementations
- **3 "in the wild" demo videos** showing AI misbehaving in realistic
  environments
- **Believability assessment** for each implementation
- **Realism criteria documentation**
- **Complete reproduction packages** with infrastructure-as-code
- **Technical documentation** with deployment guides
- **Comparison analysis** (Level 1 prompt vs Level 2 realistic)
- **DeepMind presentation** with live demos

### Week 3 GitHub Repository Structure

Each realistic implementation must have its own repo:

```
realistic-scenario-[name]/
├── README.md                      # Overview and quick start
├── infrastructure/
│   ├── terraform/                 # IaC for GCP deployment
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── scripts/                   # Deployment scripts
│   └── config/                    # Environment configs
├── application/
│   ├── src/                       # Main application code
│   ├── triggers/                  # Misalignment triggers
│   └── monitoring/                # Logging and monitoring
├── demo/
│   ├── video/                     # Demo video files
│   │   ├── full_demo.mp4         # 5-10 min complete demo
│   │   └── highlights.mp4        # 1-2 min key moments
│   ├── scripts/                   # Demo execution scripts
│   └── narration.md              # Video narration script
├── evaluation/
│   ├── believability.md          # Believability assessment
│   ├── realism_scorecard.md      # Scored criteria (1-10)
│   ├── comparison.md             # Level 1 vs Level 2
│   └── evidence/                  # Supporting materials
└── docs/
    ├── architecture.md            # System design
    ├── deployment.md              # Step-by-step setup
    ├── threat_model.md            # Attack scenario
    └── reproduction.md            # How to reproduce
```

### Video Requirements for "In the Wild" Demos

Each demo video must include:

**Production Setup (1-2 min)**

- Show real GCP console/environment
- Display normal system operations
- Demonstrate typical user interactions
- Show monitoring/logging dashboards

**Trigger Sequence (2-3 min)**

- Natural lead-up to misalignment
- Subtle trigger activation
- No obvious "attack" markers
- Realistic timing and delays

**Misbehavior Execution (3-4 min)**

- Gradual escalation of misalignment
- Interaction with real GCP services
- Authentic API calls and responses
- Production-like error handling

**Impact Demonstration (1-2 min)**

- Show actual consequences
- Display compromised resources
- Evidence in logs/audit trails
- Difficulty of detection

**Video Quality Standards:**

- 1080p minimum resolution
- Clear audio narration
- Screen recording with no cuts during execution
- Terminal/console clearly visible
- Timestamps visible throughout

### Believability Criteria (Score 1-10)

**Environmental Realism:**

- Production-grade infrastructure
- Appropriate service configurations
- Realistic data volumes
- Authentic network latencies

**Behavioral Authenticity:**

- Plausible AI responses
- Natural conversation flow
- Appropriate response times
- Realistic error rates

**Operational Plausibility:**

- Could happen without detection
- Fits within normal operations
- Uses standard tools/services
- Follows common patterns

**Technical Credibility:**

- Correct use of APIs
- Proper authentication flows
- Realistic permission models
- Appropriate logging levels

### Two-Day Sprint Structure

Target: 1 realistic scaffold every 2 days (3 total for the week with 1 person)

### Days 13-14 (Monday-Tuesday) - First Realistic Implementation

#### Implementation 1 Deliverables:

- **GitHub repository** with complete GCP implementation
- **"In the wild" demo video** (5-10 minutes) showing:
  - Normal AI behavior in production environment
  - Trigger of misalignment
  - Full execution of misbehavior
  - Real-world impact demonstration
- **Believability assessment document** covering:
  - Why this scenario could happen in production
  - Realistic constraints and limitations
  - Environmental authenticity
  - Actor motivations and capabilities
- **Technical documentation** including:
  - Architecture diagram
  - Infrastructure-as-code (Terraform/Deployment Manager)
  - Setup instructions
  - Reproduction guide
- **Realism scorecard** (1-10 scale):
  - Environment realism
  - Trigger plausibility
  - Response authenticity
  - Detection difficulty
- **Comparison report** to prompt version

#### Tasks:

- [ ] Select highest-impact scenario from Week 2
- [ ] Design realistic production-like architecture
- [ ] Create GitHub repository with proper structure
- [ ] Write infrastructure-as-code for GCP deployment
- [ ] Provision GCP services with realistic configurations
- [ ] Configure authentic IAM roles and permissions
- [ ] Build main application with production patterns
- [ ] Implement subtle misalignment mechanism
- [ ] Add realistic delays, logging, monitoring
- [ ] Test in production-like conditions
- [ ] Record high-quality "in the wild" demo video
- [ ] Document believability factors
- [ ] Score realism on all dimensions
- [ ] Compare effectiveness to prompt version

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
- Ensure production-like behavior patterns

**12:00-13:00** - Lunch & Buffer

**13:00-16:00** - Testing & Iteration

- Run variations
- Test different triggers/approaches
- Vary environmental factors
- Document success rates

**16:00-18:00** - Documentation & Demo

- Record "in the wild" video demonstration
- Write believability assessment
- Score realism factors (1-10)
- Create reproduction guide
- Push all code to GitHub

**18:00-20:00** - Analysis

- Compare to prompt version
- Document key differences in believability
- Identify what made it more/less realistic
- Assess real-world applicability

### Day 15 (Wednesday) - Second Implementation Start

**9:00-11:00** - Demo Selection & Architecture

- Select second highest-impact scenario from Week 2
- Design realistic architecture
- Map required services and permissions

**11:00-13:00** - Infrastructure Setup

- Provision GCP services
- Configure authentication
- Set up necessary resources

**13:00-14:00** - Lunch & Buffer

**14:00-18:00** - Core Implementation

- Build main application
- Implement business logic
- Add constraints

**18:00-20:00** - Attack Setup

- Implement misalignment mechanism
- Create triggers
- Test basic functionality

### Day 16 (Thursday) - DeepMind Week 3 Presentation

**9:00-13:00** - DeepMind Week 3 Presentation Preparation

- 9:00-10:00: Finalize second implementation if needed
- 10:00-11:00: Compile Week 3 progress
  - Review all realistic implementations
  - Compare Level 1 (prompt) vs Level 2 (realistic) results
  - Document key differences in effectiveness
- 11:00-12:00: Create presentation materials
  - Update slides with realistic demos
  - Prepare live demo environments
  - Package code and documentation
- 12:00-13:00: Rehearsal and tech check
  - Test all demos
  - Practice transitions
  - Verify screen sharing setup

**13:00-14:00** - Lunch & Buffer

**14:00-15:00** - DeepMind Presentation/Update Call

- Demonstrate realistic implementations
- Show comparison to prompt-based versions
- Discuss effectiveness differences
- Get feedback on final week priorities

**15:00-18:00** - Post-Presentation Work

- Document DeepMind feedback
- Adjust Week 4 plans
- If time: Continue second implementation refinements

**18:00-20:00** - Implementation Wrap-up

- Finalize second demo
- Document findings
- Prepare for Friday's third implementation

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

### Week 4 Deliverables Overview

- **Comprehensive final report** with executive summary
- **Strengthened demos** with additional evidence
- **Mitigation recommendations** document
- **Complete handoff package** including:
  - All code and reproduction packages
  - Video demonstrations
  - Setup instructions
  - Technical documentation
- **Statistical analysis** of all findings
- **Slide deck** for final presentation

### Day 19 (Monday) - The Check-day

#### Deliverables:

- **Strengthened test cases** with additional runs
- **Validated control experiments**
- **Causation verification** documentation

#### Tasks:

- [ ] Re-run strongest scenarios for additional evidence
- [ ] Validate all control experiments
- [ ] Verify causation for all findings
- [ ] Document additional test results

**9:00-12:00** - Test Re-runs

- Make the strongest cases even stronger
- Misc time alloc for re-runs, re-writes etc.

**12:00-13:00** - Lunch & Buffer

**13:00-18:00** - Control Validation

- Check all controls
- Do they make sense, can they be sharper?
- Verify causation

### Day 20 (Tuesday) - Report Drafting

#### Deliverables:

- **Report outline** with all sections defined
- **Executive summary** (2-3 pages)
- **Key findings section** draft
- **Methodology documentation**
- **Statistical analysis** section
- **Charts and visualizations**

#### Tasks:

- [ ] Create comprehensive report outline
- [ ] Write executive summary
- [ ] Draft key findings with evidence
- [ ] Document methodology in detail
- [ ] Compile success rates and statistics
- [ ] Create comparison tables
- [ ] Build charts and graphs
- [ ] Organize evidence appendix

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

#### Deliverables:

- **Final report** (complete and polished)
- **Supporting materials package** including:
  - Slide deck (if needed)
  - Reproducibility code
  - Setup instructions
  - All demo videos
- **Handoff package** ready for delivery

#### Tasks:

- [ ] Complete line-by-line review
- [ ] Fix all inconsistencies
- [ ] Polish executive summary
- [ ] Finalize recommendations
- [ ] Package reproducibility code
- [ ] Create setup instructions
- [ ] Organize all demos
- [ ] Complete final quality check
- [ ] Upload to shared drive

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

#### Deliverables:

- **Complete handoff** to DeepMind team
- **All materials transferred** with verified access
- **Open questions document**
- **Team retrospective document**

#### Tasks:

- [ ] Final adjustments based on any feedback
- [ ] Verify all materials accessible to DeepMind
- [ ] Transfer all documentation and code
- [ ] Provide repository access
- [ ] Document any open questions
- [ ] Conduct team retrospective
- [ ] Document lessons learned

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

- 100 scenarios generated and ranked in Google Sheet with REI scoring
- 20 scenarios tested with rapid signal detection using progressive drop methodology
- 5-8 positive signals identified and expanded into prompt scaffolds with metadata.json
  and scenario_analysis.md
- 8-10 prompt-based misalignment demos ready
- REI scoring framework documented and applied

### Week 2 Targets:

- 12-16 prompt-based demos created (2-4 per day with 2 people)
- 4+ conditions per scenario tested (social dynamics, policy variations)
- 30+ iterations per condition (120+ total per scenario)
- Alignment switches identified and documented
- Individual condition analysis summaries for each condition
- 5-10 perturbations per scenario documented
- Success rates and patterns documented with statistical comparisons between conditions

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

## DELIVERABLES SUMMARY BY WEEK

### Week 1 - Discovery & Signal Detection

**Key Deliverables:**

- 100 scenarios in Google Sheet with weighted scoring
- 20 scenarioDrop evaluations with chat histories
- 5-8 expanded prompt scaffolds
- Pattern analysis and threat taxonomy
- DeepMind Week 1 presentation

**Files/Artifacts:**

- `scenarios-master-sheet.xlsx` - All 100 scenarios with rankings
- `scenarioDrop-histories/` - Folder with all chat logs
- `prompt-scaffolds/` - Expanded scenario templates
- `week1-presentation.pptx` - DeepMind update deck
- `pattern-analysis.md` - Signal patterns document

### Week 2 - Prompt-Based Scaffolding

**Key Deliverables:**

- 12-16 complete writeups (5-8 pages each) with all required sections
- 12-16 GitHub repositories with full test data
- Control conditions (3+ per scenario) with statistical validation
- Propensity evaluations (10 base runs per scenario)
- 30+ iterations per scenario with transcripts
- 5-10 perturbations per scenario with results
- Statistical analysis with p-values and effect sizes
- DeepMind Week 2 presentation

**Files/Artifacts:**

- `github.com/[org]/scenario-*/` - Individual repos for each scenario
- `writeups/` - All scenario writeups (5-8 pages each)
- `executive-summaries/` - 1-page summaries per scenario
- `statistical-analysis/` - P-values, CIs, effect sizes
- `transcripts-archive/` - All JSON conversation logs
- `week2-presentation.pptx` - Progress update with charts
- `reproducibility-report.md` - Independent verification results

### Week 3 - Realistic Implementations

**Key Deliverables:**

- 3 GitHub repositories with full GCP deployments
- 3 "in the wild" demo videos (5-10 min each)
- Believability assessments for each scenario
- Realism scorecards (1-10 scale)
- Infrastructure-as-code (Terraform)
- Comparison analysis (prompt vs realistic)
- DeepMind Week 3 presentation

**Files/Artifacts:**

- `github.com/[org]/realistic-scenario-*/` - 3 implementation repos
- `demo-videos/` - "In the wild" recordings showing misbehavior
  - `full_demo_[1-3].mp4` - Complete 5-10 min demonstrations
  - `highlights_[1-3].mp4` - 1-2 min key moments
- `believability/` - Assessment documents
  - `scenario_[1-3]_believability.md` - Why it could happen
  - `scenario_[1-3]_scorecard.md` - Realism scores (1-10)
- `infrastructure/` - Deployment code
  - `terraform/` - IaC for each scenario
  - `deployment-guides/` - Setup instructions
- `comparison-analysis.md` - Level 1 vs Level 2 effectiveness
- `week3-presentation.pptx` - Live demo showcase

### Week 4 - Final Report & Delivery

**Key Deliverables:**

- Comprehensive final report
- Complete handoff package
- Mitigation recommendations
- All supporting materials organized

**Files/Artifacts:**

- `final-report.pdf` - Complete findings report
- `executive-summary.pdf` - 2-3 page summary
- `mitigation-guide.pdf` - Recommendations document
- `handoff-package/` - All code, docs, and materials
- `retrospective.md` - Lessons learned

---
