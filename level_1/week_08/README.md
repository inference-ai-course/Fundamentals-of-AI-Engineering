# Level 1 — Week 8: Capstone Demo & Retrospective (Preparing for Level 2)

## What you should be able to do by the end of this week

- Deliver a demo-ready Capstone that runs end-to-end without “magic steps”.
- Explain your design decisions and trade-offs.
- Write a short retrospective focused on learning and iteration.

Tutorials:
 
- [tutorial.md](tutorial.md)
- [01_demo_readiness.md](01_demo_readiness.md)
- [02_retrospective_template.md](02_retrospective_template.md)
- [03_preparing_for_level2.md](03_preparing_for_level2.md)

Practice notebook: [practice.ipynb](practice.ipynb)

## Key Concepts (with explanations + citations)

### 1) Demo readiness and documentation

**Mental model**:

- A demo is successful when another person can reproduce it.
- Your README is the primary interface for users and graders.

Citations:

- GitHub — About READMEs: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes

### 2) Retrospectives and postmortems

**Mental model**:

- A retrospective is a structured reflection:
  - what went wrong
  - why it went wrong
  - what you changed
  - what you would do next

For engineering culture, “blameless postmortems” emphasize learning.

Citations:

- Google SRE Book — postmortem culture: https://sre.google/sre-book/postmortem-culture/

### 3) Preparing for Level 2 (what changes)

**Mental model**:

- Level 1: single-project pipeline, mostly offline and script-based.
- Level 2: systems thinking:
  - knowledge bases
  - retrieval
  - evaluation loops
  - agent workflows

Citations:

- Retrieval-Augmented Generation (RAG) overview (Pinecone): https://www.pinecone.io/learn/retrieval-augmented-generation/

## Workshop / Implementation Plan

- Run the full demo script:
  - successful run
  - at least one failure-case demo
- Do a short walkthrough:
  - inputs/outputs
  - pipeline stages
  - where logs are emitted
- Write retrospective notes:
  - top 3 issues
  - fixes
  - next improvements

## Figures (Comprehensive Overviews — Leave Blank)

### Figure A: Capstone architecture overview (modules and data flow)


### Figure B: Iteration loop (run -> observe -> fix -> re-run)


## Self-check questions

- Can you demo without editing code live?
- Do you have a clear failure-case story?
- Can you describe what you would add next for a Level 2-style system?
