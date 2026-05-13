# Design Thinking Methods — Knowledge Base

> The bridge between Patterns (what to build) and Principles (how to build).
> Tools for deciding "which pattern to pick and how."

---

## Quick Reference: When to Use What

| Situation | Method |
|-----------|--------|
| "Why am I building this?" unclear | Jobs to be Done |
| "Is this really needed?" doubt | First Principles |
| "No idea how to approach this" | Analogy / Biomimicry |
| "Have candidates, can't choose" | Adversarial / Pre-mortem |
| "Two good options that conflict" | TRIZ (Contradiction Matrix) |
| "Current design feels off" | SCAMPER |
| "Too many variables to organize" | Morphological Analysis |
| "Built it but unsure about direction" | Backcasting |
| "Don't know what to do first" | Wardley Mapping |
| "Might be missing a perspective" | Six Thinking Hats |
| "Need fast validation" | Design Sprint |
| "Need user's perspective" | Design Thinking (IDEO) |
| "Candidates could be combined" | Evolutionary Design |
| "Constraints might be wrong" | Constraint Relaxation |

---

## Common Combinations

```
Ideation + Validation:  Analogy → Adversarial
Contradiction solving:  Adversarial → TRIZ
Structure building:     Morphological → Adversarial
Direction checking:     First Principles → Backcasting
Refactoring:           SCAMPER → Adversarial
```

Adversarial almost always follows other methods. "How does this break?" is universally useful.

---

## Methods

### Jobs to be Done
- Purpose: "What problem are we solving?" not "What are we building?"
- Output: True problem definition

### First Principles
- Purpose: Question "that's just how it's done"
- Use with: Constraint Relaxation
- Output: Fundamental redesign possibilities

### Design Thinking (IDEO)
- Purpose: Find real problem from user perspective
- Process: Empathize → Define → Ideate → Prototype → Test
- Output: User-centered problem definition + prototype

### Analogy-First
- Purpose: Borrow solutions from completely different domains
- Method: "What is this similar to?" — minimum 3 domains
- Output: Ideas beyond the pattern catalog
- ALWAYS recommended. Best ROI.

### Biomimicry
- Purpose: Find solutions in nature. Biology-specific Analogy.
- Swarm, Stigmergy originated here.

### Adversarial Design
- Purpose: Intentionally break it. "How does this fail?"
- Method: Red Team generates 5 failure scenarios
- Output: Weakness list + defenses
- Use after almost every other method.

### Pre-mortem
- Purpose: Experience failure in advance
- Method: "6 months from now, this project failed completely. Why?"
- Output: Hidden risk list

### Constraint Relaxation
- Purpose: Verify constraints are real constraints
- Method: "What if this constraint didn't exist?"
- Output: Discovered false constraints + revived options

### TRIZ (Contradiction Matrix)
- Purpose: Resolve contradictions instead of compromising
- Method: Find "improving A worsens B" → apply 40 principles
- Separation: by time / by space / by condition
- Output: Contradiction resolution

### SCAMPER
- Purpose: Force variations on existing design
- Method: Substitute, Combine, Adapt, Modify, Put to other use, Eliminate, Reverse
- Output: Unexpected variations

### Morphological Analysis
- Purpose: Enumerate all combinations, pick the good ones
- Method: Decompose into variables, list options, combine
- Output: Exhaustive candidate generation
- Especially useful when many variables exist.

### Evolutionary Design
- Purpose: Crossbreed candidates for better offspring
- Method: Select top candidates → combine strengths → iterate
- Output: Hybrid candidates

### Backcasting
- Purpose: Reverse-engineer from completed future
- Method: Define success state → "What must exist 3 months before?" → "This week?"
- Output: Reverse roadmap

### Wardley Mapping
- Purpose: Prioritize by maturity
- Method: Place components on maturity axis (proven ↔ experimental)
- Output: What to build first

### Six Thinking Hats
- Purpose: Force perspective switching
- Method: White(facts), Red(emotions), Black(criticism), Yellow(optimism), Green(creativity), Blue(management)
- Output: Discovered missing perspectives

### Design Sprint (Google Ventures)
- Purpose: Prototype + validate in 5 days
- Process: Mon(problem) → Tue(ideas) → Wed(decide) → Thu(prototype) → Fri(test)
- Output: Validated prototype

---

## Usage in Framework

```
Phase 1 (Define):    Jobs to be Done + First Principles
Phase 2 (Diverge):   Analogy + Morphological + SCAMPER
Phase 3 (Validate):  Adversarial + Pre-mortem + Six Hats
Phase 4 (Converge):  TRIZ + Evolutionary + Wardley + Backcasting
Phase 5 (Execute):   Design Sprint
```

You don't need all of them every time. Pick what fits the situation.
Analogy + Adversarial alone covers 80%.
