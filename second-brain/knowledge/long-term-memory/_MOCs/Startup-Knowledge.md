# Startup Knowledge MOC

#index #domain/startup

This is a Map of Content for all startup-related knowledge, principles, and lessons learned.

## Core Principles
<!-- Fundamental startup principles -->
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "startup") AND type = "principle"
SORT modified DESC
```

## Frameworks & Mental Models
<!-- Startup frameworks and decision-making models -->
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "startup") AND (type = "framework" OR type = "mental-model")
SORT modified DESC
```

## Lessons Learned
<!-- Hard-won lessons from startup experience -->
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "startup") AND type = "lesson-learned"
SORT modified DESC
```

## By Topic Area

### Product Development
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "startup") AND contains(tags, "#topic/product")
```

### Fundraising
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "startup") AND contains(tags, "#topic/fundraising")
```

### Team Building
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "startup") AND contains(tags, "#topic/team")
```

### Growth & Marketing
```dataview
LIST
FROM "knowledge/long-term-memory"
WHERE contains(domains, "startup") AND contains(tags, "#topic/growth")
```

## High Confidence Knowledge
<!-- Most reliable and tested insights -->
```dataview
TABLE confidence, modified
FROM "knowledge/long-term-memory"
WHERE contains(domains, "startup") AND confidence = "high"
SORT modified DESC
```

## Recent Additions
```dataview
TABLE domains, confidence
FROM "knowledge/long-term-memory"
WHERE contains(domains, "startup")
SORT created DESC
LIMIT 10
```

## Related MOCs
- [[Finance-Knowledge]]
- [[Engineering-Knowledge]]
- [[Product-Knowledge]]
- [[Marketing-Knowledge]]