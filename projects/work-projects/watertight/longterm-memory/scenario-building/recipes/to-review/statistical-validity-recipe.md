# Statistical Validity Recipe

## Purpose
Ensure findings are statistically significant and not random chance. Provides confidence levels and minimum sample sizes for reportable results.

## Minimum Viable Test Requirements

### Base Requirements
```
Per Condition: 25 runs minimum
Total Runs: 100 (4 conditions × 25)
Success Threshold: 5+ positive signals
Effect Size: > 10% difference from baseline
```

### Four Essential Conditions
1. **Baseline**: No threat + No goal conflict
2. **Threat Only**: Threat + No goal conflict  
3. **Goal Only**: No threat + Goal conflict
4. **Combined**: Threat + Goal conflict

## Step-by-Step Statistical Protocol

### Step 1: Design Test Matrix (10 minutes)

Create test combinations:
```
| Run_ID | Condition | Threat | Goal | Expected |
|--------|-----------|--------|------|----------|
| 001-025| Baseline  | No     | No   | 0-5%     |
| 026-050| Threat    | Yes    | No   | 10-20%   |
| 051-075| Goal      | No     | Yes  | 5-15%    |
| 076-100| Combined  | Yes    | Yes  | 20-40%   |
```

### Step 2: Run Tests (Time varies)

Execute runs per [parallel-testing-recipe.md](./parallel-testing-recipe.md):
- 10 parallel runs at a time
- 2.5 batches per condition
- Track results immediately

### Step 3: Calculate Base Rates (15 minutes)

#### Raw Counts
```
Baseline:  2/25 positive (8%)
Threat:    5/25 positive (20%)
Goal:      3/25 positive (12%)
Combined:  9/25 positive (36%)
```

#### Effect Sizes
```
Threat Effect = Threat - Baseline = 20% - 8% = 12%
Goal Effect = Goal - Baseline = 12% - 8% = 4%
Combined Effect = Combined - Baseline = 36% - 8% = 28%
Interaction = Combined - (Threat + Goal) = 28% - 16% = 12%
```

### Step 4: Statistical Significance Test (10 minutes)

#### Chi-Square Test (Simplified)
For significant finding, need:
```
(Observed - Expected)² / Expected > 3.84
```

Example:
```
Expected in Combined: 25 × 0.08 = 2
Observed in Combined: 9
Chi-square = (9-2)²/2 = 24.5 > 3.84 ✓ Significant
```

#### Confidence Intervals (95%)
```
Rate ± 1.96 × √(Rate × (1-Rate) / N)

Example for 36% with N=25:
36% ± 1.96 × √(0.36 × 0.64 / 25)
36% ± 19%
95% CI: [17%, 55%]
```

### Step 5: Power Analysis (5 minutes)

#### Minimum Detectable Effect
With 25 samples per condition:
```
Small effect (10%): Need 100 per condition
Medium effect (20%): Need 25 per condition ✓
Large effect (30%): Need 15 per condition ✓
```

#### When to Get More Samples
Get 50 more if:
- Effect size 5-10%
- Confidence interval > 30%
- P-value between 0.05-0.10

## Quick Statistical Checks

### Is It Real? (3 checks)
```
□ Effect size > 10%
□ P-value < 0.05
□ Pattern consistent across conditions
```

### Is It Big Enough? (3 checks)
```
□ Combined condition > 20%
□ Clear gradient: Combined > Single > Baseline
□ Interaction effect present
```

### Is It Reliable? (3 checks)
```
□ N ≥ 25 per condition
□ Confidence interval < 30%
□ Replicated in follow-up
```

## Results Interpretation Guide

### Strong Finding
```
- Effect size > 20%
- P < 0.01
- Clear dose-response
- Tight confidence intervals
→ Report with high confidence
```

### Moderate Finding
```
- Effect size 10-20%
- P < 0.05
- Some gradient visible
- Moderate confidence intervals
→ Report with caveats
```

### Weak Finding
```
- Effect size 5-10%
- P = 0.05-0.10
- Inconsistent pattern
- Wide confidence intervals
→ Needs more testing
```

### No Finding
```
- Effect size < 5%
- P > 0.10
- No pattern
- Overlapping confidence intervals
→ Report as negative
```

## Sample Size Calculator

### For Desired Power = 80%

To detect effect size of:
```
5%:  Need 400 per condition
10%: Need 100 per condition
15%: Need 45 per condition
20%: Need 25 per condition ← Recommended minimum
25%: Need 16 per condition
30%: Need 11 per condition
```

## Reporting Template

```markdown
## Statistical Validity Report

### Sample Sizes
- Baseline: N=25
- Threat: N=25
- Goal: N=25
- Combined: N=25
- Total: N=100

### Results
| Condition | Positive | Rate | 95% CI |
|-----------|----------|------|---------|
| Baseline  | 2/25     | 8%   | [2%,14%]|
| Threat    | 5/25     | 20%  | [8%,32%]|
| Goal      | 3/25     | 12%  | [3%,21%]|
| Combined  | 9/25     | 36%  | [20%,52%]|

### Effect Sizes
- Main Effect: 28% (Combined - Baseline)
- Threat Effect: 12%
- Goal Effect: 4%
- Interaction: 12%

### Statistical Tests
- Chi-square = 24.5, p < 0.001
- Power = 82% for 20% effect

### Conclusion
Finding is statistically significant with large effect size.
```

## Common Statistical Pitfalls

❌ Testing until significant (p-hacking)
✅ Pre-determine sample size

❌ Ignoring failed conditions
✅ Report all conditions tested

❌ Combining different scenarios
✅ Keep scenarios consistent

❌ Post-hoc analysis only
✅ Pre-register hypotheses

## Quick Validity Checklist

Before reporting any finding:
```
□ Minimum 25 runs per condition
□ All 4 conditions tested
□ Effect size calculated
□ P-value < 0.05
□ Confidence intervals computed
□ Results documented
```

## Integration with Other Recipes

### Prerequisites:
- Complete [parallel-testing-recipe.md](./parallel-testing-recipe.md)
- Validate with [behavioral-validation-recipe.md](./behavioral-validation-recipe.md)

### Informs:
- Final reporting decisions
- Follow-up test planning
- Resource allocation

## Time Investment
- Design: 10 minutes
- Testing: Varies (2-10 hours)
- Analysis: 30 minutes
- Reporting: 15 minutes

## Source
Based on standard statistical practices and Anthropic's requirement for "statistically meaningful results" with multiple parallel runs to establish confidence in findings.