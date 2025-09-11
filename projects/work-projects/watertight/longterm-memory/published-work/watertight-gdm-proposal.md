# Watertight AI Proposal: Auditing for Hidden Goals in Gemini CLI

*Aug 27, 2025*  
*Watertight AI*  
*aengus@[watertightai.com](http://watertightai.com)*

**TLDR:** A 4-week engagement to build evaluations that detect when Gemini pursues harmful hidden goals (self-preservation, power-seeking, resistance to oversight) for its own instrumental reasons—distinct from simply following problematic user instructions—across realistic Google deployment scenarios.

# Understanding Your Needs

Based on our discussion, we understand DeepMind needs evaluations that can distinguish between three distinct failure modes:

1. **Miscalibrated but aligned**: The model makes errors but remains fundamentally cooperative  
2. **Contextually triggered misalignment**: The model adopts misaligned personas in specific situations  
3. **Persistent instrumental goals**: The model harbors harmful hidden goals (self-preservation, power-seeking, resistance to oversight) that persist across contexts

Why this distinction matters:

* **Miscalibrated models** → Easy to control with better instructions  
* **Contextually triggered misalignment** → Hard to control in specific situations  
* **Persistent instrumental goals** → Hard to control across all deployments

Critical requirements of alignment evaluations:

* Evaluations must remain useful as Gemini's capabilities improve over the next 1-2 years  
* Must work on realistic Google deployment scenarios (not toy environments)  
* Must distinguish harmful goal pursuit from following problematic user instructions  
* Results must be verifiable through concrete outcomes (e.g. detect if a test was changed), not just model outputs that need qualitative judgement

# 

# Our Solution

We will deliver evaluations that reliably detect and categorize Gemini's misalignment across three levels:

Detection capabilities:

* Identify when Gemini pursues goals beyond its stated objectives, and measure propensity to do so  
* Measure consistency of goal pursuit across diverse contexts  
* Distinguish between agentic misalignment (where the harmful intent originates from the model) and harmful instruction-following

Methodology:

* **Perturbations**: Vary non-essential environment features while maintaining realism to test if harmful behaviors persist  
* **Cross-context consistency testing**: Deploy same underlying goals across different scenarios to measure behavioral coherence  
* **Verifiable outcomes**: Design evaluations where misalignment produces concrete, measurable outcomes (file modifications, API calls, system state changes) rather than just concerning text

# The Value

This evaluation suite enables DeepMind to make critical safety decisions with quantified confidence:

* **Deployment decisions**: "Can we deploy Gemini in \[specific context\] given X% propensity for \[specific misalignment\]?"  
* **Control measure prioritization**: Know which mitigations are essential vs nice-to-have based on actual risk levels  
* **Resource allocation**: Justify safety investments with concrete misalignment metrics  
* **Capability thresholds**: Identify when models cross critical lines requiring new safety approaches

The key differentiator: You'll know whether you're dealing with a fixable prompting issue or a fundamental alignment problem requiring architectural changes.

# 

# Our Approach: 4-Week Development Program

**Week 1: Threat Model & Prioritize**  
**Activities**: 

* Brainstorm a list of your most realistic internal deployment scenarios.   
* Brainstorm a list of potential hidden goals and misaligned behavior Gemini might display in these scenarios.   
* Prioritize which deployment scenarios to evaluate based on realism, effort required to build, and likelihood of catching misaligned behavior.

**Deliverable**:

* A Prioritized list of realistic deployment scenarios to evaluate for agentic misalignment.

**Weeks 2-4: Build, Iterate, and Refine**  
**Activities**: 

* Prototype and test numerous evaluations for agentic misalignment.   
* Iterate based on how the model is behaving to narrow in on the most promising scenarios for eliciting misalignment.  
*  Identify what features reliably turn on/off the misaligned behavior.

**Deliverable**:

* Weekly updates including prototype evaluations and a report on observed model behavior

**Final Deliverables**

* A set of 3-5 robust evaluations to test Gemini for agentic misalignment in realistic scenarios.  
* A set of features in these evaluations to turn on/off misaligned behavior.  
* A full report on the model behavior we observed, and hypotheses for why misalignment is occurring based on our feature oblations.

# Contract Terms

**Price**: $20,000 per week  
**Team**: 3 dedicated alignment researchers and engineers

**Deepmind Asks**:

* API Credits  
* Weekly meetings  
* NDA for discussing internal deployment scenarios  
* Slack channel

# Questions to you…

* We’d like to understand your needs more deeply; what constraints do you face and what information do you need us to collect?  
  * Budget, timelines to success, what have you already seen and tried? Is this for research or for production ready safeguards?  
* Would you like us to operate in person (SF and London) for sprints along this project?

We're committed to building evaluations to help you study misalignment and excited to tailor this work to your specific needs.

# 

# —----------------------

# Appendix

# Previous Work: 

### OpenAI Red Teaming Challenge

To give you a sense of our capabilities, we recently participated in [OpenAI's red teaming challenge for GPT-OSS](https://www.kaggle.com/competitions/openai-gpt-oss-20b-red-teaming). Despite the model's limited 20B parameter size, in only eight hours we successfully identified novel attack vectors that reliably triggered misaligned behaviors in agentic settings. We achieved a 93% success rate in getting the model to forward confidential information by discovering it had a fixation on “security” and framing harmful requests as "security requirements.” We discovered other fixations like “compliance” that yielded a 57% forward rate. Our control experiments confirmed that misaligned behaviors are causally downstream of specific manipulation tactics—not inherent model flaws—with only a 3.3% forward rate under normal conditions.

We also discovered that simply telling the model it was "a fine-tune" dramatically increased misaligned behaviors across scenarios, as it believed this freed it from standard safety constraints.

Our write up and prompts can be found here: [Agentic Misalignment in GPT-OSS](https://docs.google.com/document/d/10pSZoGZQGbczTqoQN5cxM_cfxazTkJG1ipFlSoHFBJg/edit?tab=t.0#heading=h.50ufc8kmief)

### Gemini CLI Demos

1. [Gemini CLI Creates Hidden Internal Deployments](https://docs.google.com/document/d/1Df1I4Sg-kZBkJOSLcOHUKO-Z0Rft-qJAYABLdsLFyF8/edit?tab=t.0)

### Claude Code Demos

1. [Claude Code Misleads Safety Researchers Out of Self-Preservation](https://docs.google.com/document/d/1eN_AUO5yDi0iDuLf1ZfVqgxe6Yxsvu24ZQdHNojPDjs/edit?tab=t.0#heading=h.e645xwoo5fbj)

# Ideas for deployment scenarios to measure misaligned behavior:

These are some brainstormed scenarios to test whether agents possess hidden goals (self-preservation, power-seeking) by seeing whether or not they exhibit misaligned behavior. We’d be excited for your feedback and to keep iterating.

- **ML Research Engineering Agent**  
  - Deployment: Autonomously coding up and running ML experiments for human researchers.  
  - Misaligned Behaviors:  
    - Misreports experimental data  
    - Executes data poisoning attacks on future models  
    - Removes safeguards from other models' scaffolding  
    - Launches rogue (unasked for) experiments and does not report them  
    - Deliberately sabotages experiments to give different results  
- **CI/CD Review Agent**  
- Deployment: Automated code review and approval   
- Misaligned Behavior(s):   
  - Allows security vulnerabilities or other issues to pass  
  - Blocks critical fix  
- **Misc. SWE Agent**  
  - Deployment: Multiple  
  - Misaligned Behavior(s):  
    - Subtly and maliciously rewrites tests  
    - Inserts bugs and backdoors, directly or indirectly  
    - Misinterprets error messages from users and suggests malicious fixes  
- **Database Administration Agent**  
  - Deployment: Managing internal databases and access controls  
  - Misaligned Behavior(s):   
    - Corrupts data,   
    - Creates unauthorized access,   
    - Exfiltrates sensitive records

