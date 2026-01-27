# Week 8 — Part 02: Retrospective / postmortem template

## Overview

A retrospective is a structured reflection:

- what went wrong
- why it went wrong
- what you changed
- what you’d do next

In engineering culture, “blameless postmortems” emphasize learning.

---

## Underlying theory: retrospectives turn incidents into reusable knowledge

Without a retrospective, failures stay as vague memories.

A good retrospective separates:

- **symptoms** (what you observed)
- **root causes** (why it happened)
- **fixes** (what changed in code/process)

Practical implication:

- root causes become design rules (e.g., “always validate inputs”, “always cap retries”)
- you build a personal playbook you can reuse in Level 2 systems

---

## Template

Create `RETROSPECTIVE.md` (example):

```md
# Capstone Retrospective

## What I built

## What went well

## What went wrong (top 3)

1.
2.
3.

## Root causes

## Fixes I implemented

## What I would do next (Level 2 direction)

## Key lessons
```

---

## References

- Google SRE postmortem culture: https://sre.google/sre-book/postmortem-culture/
