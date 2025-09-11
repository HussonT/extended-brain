# Finance Knowledge MOC

#index #domain/finance

This is a Map of Content for all finance-related knowledge, principles, and insights.

## Core Principles
<!-- Fundamental financial principles -->
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "finance") AND type = "principle"
SORT modified DESC
```

## Frameworks & Models
<!-- Financial frameworks and analysis models -->
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "finance") AND (type = "framework" OR type = "mental-model")
SORT modified DESC
```

## Best Practices
<!-- Proven financial best practices -->
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "finance") AND type = "best-practice"
SORT modified DESC
```

## By Topic Area

### Startup Finance
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "finance") AND contains(domains, "startup")
```

### Financial Modeling
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "finance") AND contains(tags, "#topic/modeling")
```

### Valuation
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "finance") AND contains(tags, "#topic/valuation")
```

### Fundraising & Investment
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "finance") AND contains(tags, "#topic/investment")
```

### Metrics & KPIs
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "finance") AND contains(tags, "#topic/metrics")
```

## High Confidence Knowledge
<!-- Most reliable financial insights -->
```dataview
TABLE confidence, modified
FROM "knowledge/long-term-memory"
WHERE contains(domains, "finance") AND confidence = "high"
SORT modified DESC
```

## Recent Additions
```dataview
TABLE domains, confidence
FROM "knowledge/long-term-memory"
WHERE contains(domains, "finance")
SORT created DESC
LIMIT 10
```

## Related MOCs
- [[Startup-Knowledge]]
- [[Business-Knowledge]]
- [[Economics-Knowledge]]