# Week 10 — Part 03: Defense checklist (tradeoffs + limitations)

## Overview

Defense means you can explain:

- what you built
- why you chose these components
- tradeoffs you accepted
- limitations
- next roadmap

---

## Underlying theory: defend with tradeoffs, not vibes

A strong defense is:

- explicit constraints (time, cost, latency, security)
- design choices that follow from constraints
- evaluation evidence showing the consequences

### Falsifiable claims

Prefer claims you can test:

- “Recall@5 improved from 0.50 to 0.65 after increasing overlap”
- “Out-of-KB questions refuse when top score < $\tau$”

These are defensible because they can be checked against artifacts.

### Tradeoff framing

Most questions reduce to a tradeoff:

- precision vs recall (retrieval)
- latency vs reliability (retries)
- strict validation vs UX (citation substring checks)

If you can name the tradeoff and show what you chose, reviewers will trust your decisions.

## Checklist

- architecture diagram
- data flow explanation
- failure modes and mitigations
- cost controls
- security posture
- next 2 iterations

---

## Defense questions you should be able to answer

- Why did you choose your embedding model and vector store?
- What are your top 3 observed failure modes, and how did you mitigate them?
- How do you prevent hallucinations (grounding + citations enforcement)?
- How do you control cost (token caps, rate limits, caching if any)?
- What security posture did you implement for admin endpoints?
- If you had 2 more weeks, what would you improve first and why?

---

## References

- Twelve-Factor mindset: https://12factor.net/
- SLOs: https://sre.google/sre-book/service-level-objectives/
- OWASP API Security Top 10: https://owasp.org/www-project-api-security/
