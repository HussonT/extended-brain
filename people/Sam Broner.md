---
tags: person
aliases: []
priority: 
relationship-quality: 
first-contact: 
last-contact: 
---

# Sam Broner

## Contact Info
- **Email**: 
- **Phone**: 
- **LinkedIn**: 
- **Twitter**: 
- **Location**: 

## Context
- **Role/Title**: 
- **Company**: 
- **How we met**: Via RAP/Meeting
- **Key interests**: 
- **Expertise**: 

## Notes
<!-- Add any personal notes, key conversations, or important details about this person -->

## All Interactions
<!-- This section automatically aggregates all mentions of this person across your vault -->

### Meetings & Calls
```dataview
TABLE 
  date as Date,
  type as Type,
  file.folder as Location
FROM ""
WHERE contains(attendees, this.file.link) OR contains(attendees, this.file.name) OR contains(file.outlinks, this.file.link)
SORT date DESC
```

### All Mentions
```dataview
LIST
FROM ""
WHERE contains(file.outlinks, this.file.link) AND file.path != this.file.path
SORT file.mtime DESC
LIMIT 20
```

### Tagged References
```dataview
LIST
FROM ""
WHERE contains(tags, "person/" + replace(lower(this.file.name), " ", "-"))
SORT file.mtime DESC
```