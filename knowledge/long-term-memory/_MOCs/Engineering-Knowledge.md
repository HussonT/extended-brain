# Engineering Knowledge MOC

#index #domain/engineering

This is a Map of Content for all engineering and technical knowledge, principles, and best practices.

## Core Principles
<!-- Fundamental engineering principles -->
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "engineering") AND type = "principle"
SORT modified DESC
```

## Frameworks & Patterns
<!-- Engineering frameworks and design patterns -->
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "engineering") AND (type = "framework" OR type = "mental-model")
SORT modified DESC
```

## Best Practices
<!-- Proven engineering best practices -->
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "engineering") AND type = "best-practice"
SORT modified DESC
```

## By Topic Area

### System Design
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "engineering") AND contains(tags, "#topic/system-design")
```

### Architecture Patterns
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "engineering") AND contains(tags, "#topic/architecture")
```

### Performance & Optimization
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "engineering") AND contains(tags, "#topic/performance")
```

### Security
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "engineering") AND contains(tags, "#topic/security")
```

### DevOps & Infrastructure
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "engineering") AND contains(tags, "#topic/devops")
```

### AI & Machine Learning
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "engineering") AND contains(tags, "#topic/ai")
```

## Lessons Learned
<!-- Hard-won engineering lessons -->
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "engineering") AND type = "lesson-learned"
SORT modified DESC
```

## High Confidence Knowledge
<!-- Most reliable technical insights -->
```dataview
TABLE confidence, modified
FROM "knowledge/long-term-memory"
WHERE contains(domains, "engineering") AND confidence = "high"
SORT modified DESC
```

## Recent Additions
```dataview
TABLE domains, confidence
FROM "knowledge/long-term-memory"
WHERE contains(domains, "engineering")
SORT created DESC
LIMIT 10
```

## Related MOCs
- [[Product-Knowledge]]
- [[Startup-Knowledge]]
- [[AI-Knowledge]]