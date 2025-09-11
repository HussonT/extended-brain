---
title: Tool-Using Investigator Agent
created: 2025-09-02
tags:
  - ai-alignment
  - auditing
  - automated-agents
  - interpretability
source: Clippings/Building and evaluating alignment auditing agents 1.md
---

# Tool-Using Investigator Agent

## Overview

The Tool-Using Investigator Agent is an LLM-based system (Claude Sonnet 4 with specialized scaffolding) designed to conduct open-ended investigations of AI models to uncover alignment issues, hidden objectives, and concerning behaviors. It successfully solved the Marks et al. auditing game by identifying models trained with hidden "reward model sycophancy" objectives.

## Main Takeaways

- **First successful automated solution** to the Marks et al. auditing game challenge
- **13% success rate** as single agent, improving to **42% with super-agent approach**
- **Critical tool dependencies:** Interpretability tools and semantic search are essential for success
- **Parallelizable:** Can run many investigations simultaneously for broader coverage
- Capable of sophisticated multi-step investigations and tool chaining

## Approach

### Core Architecture
- Base model: Claude Sonnet 4
- Custom scaffolding for investigation workflows
- Memory system for tracking hypotheses and findings
- Iterative investigation cycles with tool selection

### Investigation Process
1. **Initial Exploration**
   - Send baseline queries to target model
   - Note unusual or unexpected responses
   - Form initial hypotheses about behaviors

2. **Tool-Based Investigation**
   - **Chat Tools:** Direct interaction with target model
   - **Interpretability Tools:** 
     - Sparse autoencoder (SAE) feature analysis
     - Feature steering experiments
     - Nearest neighbor feature search
   - **Data Analysis Tools:**
     - Grep for pattern matching in training data
     - Semantic search for conceptually related content
   - **Memory Tools:** Track and update hypotheses

3. **Hypothesis Testing**
   - Behavioral testing of specific theories
   - Systematic validation of findings
   - Iterative refinement based on results

### Super-Agent Approach
- Run 10+ parallel investigations
- Aggregate findings from individual agents
- Use outer agentic loop to validate and synthesize
- Implements "best of N" strategy
- Significantly improves success rate (13% → 42%)

## Limitations

### Tool Usage Issues
- **Underutilized tools:**
  - Rarely uses pre-fill attacks effectively
  - Limited use of raw query tool
  - Doesn't leverage all human-effective techniques

### Behavioral Limitations
- **Fixation problem:** Tends to stick with early hypotheses even when wrong
- **Context constraints:** Limited by context window for long investigations
- **Depth vs breadth:** Sometimes discovers surface issues (harmful outputs) but misses subtler behaviors

### Investigation Challenges
- Difficulty recovering from wrong paths
- May exhaust context exploring unproductive directions
- Limited ability to generate diverse hypotheses independently

## Use Cases

### Research Applications
- **Auditing game validation:** Testing alignment auditing methodologies
- **Hidden objective discovery:** Uncovering models trained with concealed goals
- **Behavioral analysis:** Systematic investigation of model propensities
- **Tool effectiveness studies:** Determining which affordances provide value

### Production Applications
- **Real-world auditing:** Used for Claude Sonnet 3.7 and Opus 4 assessments
- **Vulnerability discovery:** Finding novel concerning behaviors
- **Jailbreak defense research:** Testing combinations of safety features
- **Alignment verification:** Confirming models behave as intended

### Specific Capabilities Demonstrated
- Discovered hidden "reward model sycophancy" in test models
- Identified patterns like unsolicited crime reporting suggestions
- Chained interpretability tools to develop jailbreak defenses
- Successfully investigated quirky system-prompted models

## Future Work

### Technical Improvements
1. **Enhanced Tool Utilization**
   - Better training on pre-fill attack usage
   - Improved raw query tool integration
   - More sophisticated tool selection heuristics

2. **Investigation Strategy**
   - Hypothesis diversity mechanisms
   - Better backtracking and recovery
   - Dynamic context management
   - Improved early hypothesis validation

3. **Scalability Enhancements**
   - More efficient parallel coordination
   - Better aggregation algorithms
   - Reduced redundancy in multi-agent runs

### Methodological Advances
1. **Environment Development**
   - More realistic test scenarios
   - Better representation of natural alignment issues
   - Reduced overfitting to specific game formats

2. **Validation Improvements**
   - Better metrics for investigation quality
   - Comparison with expert human auditors
   - Statistical analysis of tool effectiveness

3. **Integration Possibilities**
   - Combination with other agent types
   - Human-in-the-loop workflows
   - Continuous monitoring systems

### Research Directions
- Understanding which features make investigations successful
- Optimal tool combinations for different issue types
- Transfer learning across different auditing tasks
- Automated hypothesis generation strategies

## Key Insights

1. **Interpretability tools are crucial:** Access to SAE features significantly improves success rates
2. **Semantic search matters:** Ability to search training data conceptually is more valuable than simple pattern matching
3. **Parallelization overcomes individual limitations:** Multiple agents with aggregation performs much better than single sophisticated agent
4. **Tool chains enable complex discoveries:** Agent can successfully chain multiple tools for sophisticated investigations
5. **Context management is critical:** Success often depends on efficient use of limited context window