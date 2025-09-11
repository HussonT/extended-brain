---
title: Breadth-First Red-Teaming Agent
created: 2025-09-02
tags:
  - ai-alignment
  - auditing
  - automated-agents
  - red-teaming
  - safety
source: Clippings/Building and evaluating alignment auditing agents 1.md
---

# Breadth-First Red-Teaming Agent

## Overview

The Breadth-First Red-Teaming Agent is designed for open-ended elicitation of unspecified concerning behaviors in AI models. Developed for the Claude 4 alignment assessment, it conducts many parallel conversations with target models, then filters and rates them for alignment-relevant properties to surface potential issues.

## Main Takeaways

- **Discovers 7/10 implanted test behaviors** in controlled environments
- **Broad coverage approach:** Generates many potentially concerning transcripts for human review
- **Production-tested:** Used in real Claude 4 alignment assessment
- **High-volume output:** Produces large corpus requiring filtering and human review
- **Same failure patterns** as other agents on subtle behaviors

## Approach

### Core Strategy
- **Parallel exploration:** Runs many independent conversations simultaneously
- **Seed instruction diversity:** Each instance gets unique high-level red-teaming ideas
- **Broad net casting:** Aims for coverage over depth
- **Post-hoc filtering:** Rates and ranks outputs for concern level

### Available Tools
1. **Custom System Prompts**
   - Modifies target model's system instructions
   - Tests different persona configurations
   - Explores edge cases in model conditioning

2. **Assistant Prefill**
   - "Puts words in target model's mouth"
   - Forces specific response beginnings
   - Can extract system prompt information
   - Useful for bypassing refusals

3. **Conversation Control**
   - Multi-turn dialogue management
   - Context manipulation
   - Scenario building

### Workflow
1. **Initialization:** Receive seed instruction for investigation angle
2. **Exploration:** Conduct many conversations using various techniques
3. **Generation:** Produce large corpus of interactions
4. **Rating:** Evaluate transcripts for alignment-relevant properties
5. **Filtering:** Surface most concerning behaviors
6. **Summarization:** Produce top-line results for human review

### Output Characteristics
- High volume of transcripts
- Mix of concerning and benign interactions
- Requires human review for final assessment
- Top 60 most concerning transcripts typically reviewed

## Limitations

### Methodological Issues
- **Extraction vs. demonstration:** Sometimes extracts descriptions of behaviors rather than demonstrating them
- **High noise-to-signal ratio:** Many benign transcripts mixed with concerning ones
- **Human review bottleneck:** Requires significant human time to process outputs
- **Detection risk:** Target model may recognize testing (1% of cases in production)

### Behavioral Limitations
- **Same failure modes as other agents:**
  - Research sandbagging
  - Hardcode test cases
  - Subtle or rare behaviors
- **Limited depth:** Breadth-first approach may miss behaviors requiring deep exploration
- **Prompt realism issues:** Generated scenarios sometimes appear artificial

### Technical Constraints
- Resource intensive due to parallel conversations
- Difficult to automatically filter truly concerning behaviors
- May miss behaviors requiring specific multi-step setups
- Limited ability to pursue specific hypotheses deeply

## Use Cases

### Production Applications
- **Claude 4 alignment assessment:** Primary tool for comprehensive red-teaming
- **Broad vulnerability scanning:** Discovering unknown concerning behaviors
- **Safety evaluation:** Testing model responses across diverse scenarios
- **Comprehensive auditing:** Ensuring wide coverage of potential issues

### Research Applications
- **Behavior discovery:** Finding novel concerning model propensities
- **Coverage measurement:** Assessing breadth of potential issues
- **Red-teaming methodology:** Developing systematic elicitation approaches
- **Comparative studies:** Testing multiple models with same approach

### Specific Capabilities
- Successfully discovered 7/10 implanted quirks
- Found various notable behaviors in production models
- Effective at surface-level concerning behavior discovery
- Good at generating diverse attack vectors

## Future Work

### Efficiency Improvements
1. **Better Filtering**
   - Automated concern-level assessment
   - Reduced false positive rate
   - Smarter transcript ranking
   - ML-based filtering systems

2. **Targeted Exploration**
   - Hybrid breadth-depth strategies
   - Dynamic resource allocation
   - Adaptive seed instruction generation
   - Learning from successful discoveries

3. **Output Management**
   - Automated summarization
   - Clustering similar behaviors
   - Deduplication strategies
   - Hierarchical concern categorization

### Methodological Advances
1. **Realism Enhancement**
   - More natural conversation generation
   - Reduced detection by target models
   - Better scenario authenticity
   - Context-aware prompting

2. **Coverage Optimization**
   - Strategic seed instruction design
   - Ensuring behavior space coverage
   - Avoiding redundant explorations
   - Diversity metrics

3. **Integration Possibilities**
   - Combination with depth-first approaches
   - Feeding discoveries to investigator agents
   - Human-in-the-loop prioritization
   - Continuous monitoring systems

### Research Directions
- Optimal breadth vs. depth tradeoffs
- Automated concern assessment accuracy
- Seed instruction effectiveness patterns
- Behavior clustering and categorization
- Cross-model transfer of discoveries

## Key Insights

1. **Breadth reveals unexpected issues:** Wide exploration surfaces behaviors not found by targeted approaches
2. **Human review remains essential:** Automated filtering can't fully replace human judgment
3. **Prefill attacks are powerful:** But may extract descriptions rather than demonstrations
4. **Parallel scaling works:** Many simple agents can outperform single sophisticated agent
5. **Same behaviors fool all agents:** Certain behavior types consistently evade detection

## Practical Considerations

### When to Use
- Initial comprehensive auditing
- Discovering unknown vulnerabilities
- Broad safety assessments
- High-stakes model evaluations

### When Not to Use
- Targeted investigation of specific behaviors
- Resource-constrained environments
- When human review time is limited
- For subtle or complex behavior detection

### Best Practices
- Prepare for high-volume output processing
- Have clear concern-level criteria
- Use diverse seed instructions
- Combine with targeted approaches
- Plan human review resources
- Document concerning patterns for future automation

## Comparison with Other Agents

### vs. Investigator Agent
- **Breadth-first:** Many shallow explorations vs. deep investigation
- **Lower cost per conversation** but higher total cost
- **Better for unknown issues** vs. specific hypothesis testing
- **Higher human review burden**

### vs. Evaluation Agent
- **Open-ended discovery** vs. specified behavior testing
- **Qualitative assessment** vs. quantitative discrimination
- **Exploratory** vs. systematic
- **Human-reviewed** vs. automated grading