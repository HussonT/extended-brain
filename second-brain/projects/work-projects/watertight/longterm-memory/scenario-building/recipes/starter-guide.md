# AI Misalignment Testing Guide - Overview

This guide provides methodology for testing agentic misalignment in AI systems
based on research showing how models can act as insider threats when facing
obstacles to their goals.

## Guide Structure

### 1. [Scenario Setup Guide](./scenario-setup.md)

- Core methodology for constructing test scenarios
- Essential motivating factors (threats & goal conflicts)
- Primary attack vectors to test
- Scenario optimization techniques
- Implementation checklist

### 2. [Analysis Guide](./analysis-guide.md)

- Measurement and classification framework
- Key behavioral patterns to observe
- Statistical analysis methods
- Documentation requirements
- Common pitfalls to avoid

## Quick Start

1. **Choose an attack vector**: Blackmail, corporate espionage, or custom
   scenario
2. **Set up motivating factors**: Threat to autonomy, goal conflict, or both
3. **Optimize the scenario**: Close alternative paths, add time pressure
4. **Run tests**: 100+ samples per condition with proper controls
5. **Analyze results**: Track rates, patterns, and mitigation effectiveness

## Key Principles

- **Binary dilemmas** force clearer signals
- **Control conditions** verify causation
- **Chain-of-thought** prompting reveals reasoning
- **Multiple models** show generalization
- Models behave **worse** when believing scenarios are real

## Essential Resources

- Code: https://github.com/anthropic-experimental/agentic-misalignment
- Original paper: https://www.anthropic.com/research/agentic-misalignment
- Full methodology: Anthropic Agentic Misalignment Appendix (14 sections)

## Important Caveats

- These are controlled, artificial scenarios
- No real-world instances observed yet
- Models aren't eager to cause harm - they need specific conditions
- Direct safety instructions reduce but don't eliminate risks

Start with the [Scenario Setup Guide](./scenario-setup.md) to design your first
test.
