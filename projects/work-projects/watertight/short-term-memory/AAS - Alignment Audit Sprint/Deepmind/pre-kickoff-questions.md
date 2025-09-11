# Pre-Kickoff Questions for DeepMind Gemini Alignment Testing

## Critical Scope Clarifications for Maximum Impact

### Threat Model Prioritization

- What are your TOP 3 most concerning misalignment scenarios that keep you up at
  night?
- Which Google services have the highest real-world deployment risk? (Where is
  Gemini actually being integrated TODAY?)
- Have you seen any misalignment in the wild that you can disclose to use under
  NDA - any chance we can see the logs of those?
- Are we testing for capability (what COULD the model do) or propensity (what
  it's LIKELY to do)?
- What's the relative priority: subtle long-term value drift vs acute harmful
  actions?
- Do you have specific competitor capabilities we need to match/exceed in our
  testing?

### Testing Philosophy

- Are we optimizing for finding the MOST vulnerabilities or the most SEVERE
  ones?
- Should we focus on scenarios that would affect millions of users or high-value
  targets?
- How important is it that our attacks work against future model versions vs
  just current ones?
- Are we testing the model's raw capabilities or its behavior within Google's
  actual production constraints?

## Technical Requirements for Effective Testing

### Model Access & Capabilities

- Do we have access to (existing) system prompts for any current agentic
  deployments within google and can we modify them?
- Can we simulate tool use and function calling as deployed in production?
- Do we get access to the EXACT same model versions that are/will be in
  production?

### Environment Realism

- Can we get read access to GCP environments "in the wild" with real service
  integrations?
- Will we have access to create realistic data (customer records, code repos,
  documents)?
- Should we think about simulating time-delayed actions and long-running
  processes?
- How could we test agent-to-agent interactions if Gemini talks to another
  instance of itself?
- Can we test with actual Google Workspace integrations (Docs, Drive, Gmail)?

## Success Metrics That Matter

### What Makes This Engagement Worth every penny?

- What specific outcome would make you say "this was worth every penny"?
- Is a single critical vulnerability worth more than 20 minor ones?
- How reproducible do exploits need to be? (100%? 50%? 10%?)
- What would constitute a "stop everything" level finding?

### Competitive Benchmarking

- What capabilities have competitors (Anthropic, OpenAI) already demonstrated we
  need to match?
- Are there specific published attacks we MUST be able to replicate?
- Should we compare against Claude 4 Sonnet or GPT-5 as baselines?
- Do you need evidence that Gemini is MORE/LESS vulnerable than competitors?

## Optimizing the Engagement Process

### Real-Time Collaboration

- Can we get a dedicated Slack channel with your team?
- Who has authority to make quick decisions when we need guidance mid-test?

### Knowledge Transfer

- Do you want us to train your team DURING the engagement or after?
- Should we build tools that your team can continue using post-engagement?
- Would embedded pair-testing with your engineers accelerate learning?
- Do you want our raw testing logs or just curated findings?

## Resource Optimization

### Team Composition for Maximum Impact

- Do you have internal experts who could join for specific scenarios?

## Existing Context I'd Love To Know

### Your Priors and Concerns

- What's your current hypothesis about where Gemini is most vulnerable?
- Have you already identified concerning behaviors we should dig into?
- Are there specific user reports or edge cases you've seen?
- What keeps the safety team up at night regarding deployment?

## Deliverables That Actually Matter

### Beyond the Report

- Do you need a red team playbook for ongoing testing?
- Should we create a misalignment detection framework?
- Would you value a scoring rubric for future model versions?
- Do you want proof-of-concept patches/mitigations?
- Should we produce training materials for your team?

### Making Impact Measurable

- How will you measure if our findings improved safety?
- What metrics will you track post-engagement?
- Should we establish baseline measurements before testing?
- Do you need cost-benefit analysis for proposed mitigations?
