# Multi-Agent Architecture Framework — Design Document

> Keep this next to you while implementing. Contains only the core design decisions.

---

## 1. What the Framework Is

A general-purpose tool that, given any project, designs, validates, and manages its structure from 14 perspectives.

```
Any project → framework.load(my_system.md) → framework.review(change) → report + suggestions
```

Not TutorAgent-specific. Whether it's Jarvis or anything else, you just swap out my_system.md.

---

## 2. The 14 Layers

```
Established:
 1. Multi-Agent Patterns      ← agent arrangement structure
 2. Software Principles       ← code rules (SOLID, YAGNI, etc.)
 3. Design Thinking           ← design judgment (Adversarial, Analogy, etc.)
 4. Systems Thinking          ← seeing the whole (feedback loops, emergence, bottlenecks)
 5. Meta-Engineering          ← the making process (CI/CD, tech debt, observability)
 6. Domain Modeling           ← reality → code
 7. Human-AI Interaction      ← user touchpoints

What was missing:
 8. Failure & Recovery        ← recovery strategy
 9. Security & Trust          ← permissions and trust
10. Data Architecture         ← data flow and schemas
11. Performance & Resource    ← speed and cost

Creative proposals:
12. Temporal Design           ← evolution design over time
13. Knowledge Evolution       ← growth of the knowledge base itself
14. Context Engineering       ← designing what to show the agent
```

---

## 3. Tier Structure — Automation Levels

**Principle: be free with automating analysis, strict with automating execution.**

### Tier 1: Automatic (rule-based, no LLM needed)
- write-access hook — block unauthorized writes (Category 9)
- auto-backup — back up before changes (Category 8)
- boundary-check — prevent context contamination (Category 14)
- schema validation — validate data formats (Category 10)
- cost guard — block LLM calls that exceed budget (Category 11)

→ All if-statements. Even if wrong, they only block; nothing breaks.

### Tier 2: Report Only (LLM analyzes, human decides)
- Pattern Advisor — pattern conflicts/matches (Category 1)
- Code Checker — SOLID violations (Category 2)
- Creative Designer — propose alternatives (Category 3)
- Systems Analyzer — second-order effect candidates (Category 4) ⚠️
- Process Guardian — test coverage changes (Category 5)
- Recovery Analyzer — rollback paths (Category 8)
- Knowledge Tracker — pattern usage statistics (Category 13)
- Context Advisor — unnecessary context loads (Category 14)

→ All output reports. Don't touch the code.

### Tier 3: Propose + Approve
- Schema change diff → approve?
- Hook execution order change → approve?
- New agent addition draft → approve?
- Phase transition proposal → approve?

→ Human picks [Approve / Modify / Reject].

---

## 4. Evidence Grade System — Hallucination Defense

Every agent output must carry a grade tag:

| Grade | Meaning | Requirement | Confidence |
|------|------|----------|--------|
| [FACT] | Directly verified in file/code | File name + line number required | High |
| [CALC] | Calculation based on facts | Calculation steps required | High |
| [INFER] | Inference | Evidence chain required | Medium |
| [OPINION] | Agent judgment | ⚠️ mark required, human verification | Low |

Distribution by category:
```
Category 1-2:    FACT 80%  → auto-trust
Category 8-11:   FACT 50%  → trust after verification
Category 12-14:  FACT 10%  → human judgment required
```

### 4-Layer Verification

```
Layer 1: hardcoded — verify FACT file/line, recompute CALC. LLM calls: 0.
Layer 2: hardcoded — report format, existence of agent/skill names. LLM calls: 0~1.
Layer 3: LLM — verify INFER logic. 1 sonnet call.
Layer 4: human — judge OPINION, final approval.
```

→ 60-70% of report items get filtered out at Layers 1-2.

---

## 5. Agent Composition

### Architecture Agent Suite

```
Agent 1: Pattern Advisor (sonnet) — Category 1
  knowledge: patterns.md
  role: pattern matching, elimination, combination suggestions

Agent 2: Code Principles Checker (haiku) — Category 2
  role: detect SOLID/YAGNI violations, duplication

Agent 3: Creative Designer (opus) — Category 3
  role: Adversarial, Analogy, Constraint Relaxation
  most expensive but most valuable

Agent 4: Systems Analyzer (sonnet) — Category 4 ⚠️ assistant only
  role: generate second-order effect candidates. Output must always be human-verified

Agent 5: Process Guardian (haiku) — Category 5
  role: track test coverage, tech debt

Hallucination Checker (sonnet)
  role: verify FACT files, recompute CALC, validate INFER evidence chains

Human (you): Category 4 final judgment, 6 domain, 7 UX
```

### Orchestrator Routing

```
Code change     → Agent 2 only
Structure change → Agents 1, 2, 3, 4, 5 all
Agent 4 output  → always ⚠️ → user confirmation
```

---

## 6. Pattern Combinations Used

Six patterns are combined:
- **Contract Net** — role assignment to sub-reviewers
- **Concurrent** — parallel execution
- **Voting** — 3/4 consensus
- **Magentic** — loop (max 4 iterations, convergence: 0 new issues)
- **Stigmergy** — log to write_log.jsonl, reference in next review
- **Blackboard** — communication via shared files

---

## 7. Folder Structure

```
architecture-framework/
├── README.md
├── core/
│   ├── analyzer.md          ← assess project structure status
│   ├── designer.md          ← structural design (divergence + convergence + adversarial)
│   ├── reviewer.md          ← validate against 14 categories
│   ├── executor.md          ← execute approved changes
│   └── evolver.md           ← manage evolution over time
├── knowledge/
│   ├── patterns.md          ← 20+ patterns + matching conditions
│   ├── principles.md        ← SOLID, YAGNI, etc.
│   ├── thinking_methods.md  ← Adversarial, Analogy, etc.
│   ├── anti_patterns.md     ← "don't do this"
│   └── past_decisions/      ← accumulated ADRs from past projects
├── checklist/
│   ├── 01_patterns.md ~ 14_context_engineering.md
├── templates/
│   ├── adr_template.md
│   ├── review_report.md
│   ├── system_doc.md
│   └── evolution_plan.md
└── config/
    ├── tier_rules.md
    └── cost_strategy.md
```

---

## 8. Hardcoded vs LLM Boundary

```
Verifiable facts    → 100% hardcoded
Structural rules    → 90% hardcoded
Logical inference   → 100% LLM
Value judgments     → 100% human
```

**Principle: what can be verified goes in code, what requires thought goes to LLM, what requires decision goes to human.**

---

## 9. Build Order

### What the 14 Actually Are

```
Just write files (knowledge):     1, 2, 3 → organize as .md
Just write checklists:            4, 6-9, 12-13 → 5-10 questions each
Need to code:                     5, 10, 11, 14 → validation tools
Need to build agents:             Pattern Advisor, Creative Designer, Hallucination Checker, etc.
```

### By Phase

```
Phase 0 (1 day):   folder skeleton + templates
Phase 1 (2 days):  3 knowledge files (patterns.md, principles.md, thinking_methods.md)
Phase 2 (3 days):  Pattern Advisor agent + apply to real project
Phase 3 (2 days):  Hallucination Checker (hardcoded Layer 1-2 + LLM Layer 3)
Phase 4 (ongoing): incrementally add checklists (only get concrete by using them)
Phase 5 (as needed): Creative Designer + advanced features
```

### Timeline

```
Week 1: Phase 0+1+2 (build and apply Pattern Advisor)
Week 2: Phase 3 + Phase 4 start
Week 3+: Phase 4 continues + Phase 5
6 months later: 14 checklists + 5-7 agents + validation system
```

**The framework builds the project, and the project improves the framework. Do them at the same time.**

---

## 10. Methodology Order Before Design

```
Step 1: User Story        → WHY first
Step 2: Interface-First   → define I/O
Step 3: Decision Table    → branch logic
Step 4: Scenario Walkthrough → validate
Step 5: Pseudocode        → before detailed implementation
Step 6: Coding
```

Steps 1-4 finish before coding. 80% of design holes are found here.

---

## 11. Dependency Tracking — Minimum Maintained Set

**Just maintaining Dependency Map + ADR solves 90%.**

```
Seeing the whole picture → C4 Level 1 (3-5 boxes)
Tracing chain effects   → Dependency Map
Organizing the "why"    → Impact Mapping
Recording decisions     → ADR
Setting priorities      → Wardley Map
```

---

## 12. Code Review vs Architecture Review

```
Code Review (feature additions, bug fixes):
  Light, fast. Only for changes that don't touch structure.

Architecture Review (structural changes):
  Always rigorous. All sub-reviewers. Full loop.
  Anything touching structure goes here.
```

Structural decisions are the most expensive to reverse.
