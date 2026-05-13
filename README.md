# Multi-Agent Architecture Framework

[![Live docs](https://img.shields.io/badge/docs-multi--agent--architecture.vercel.app-black?style=flat-square)](https://multi-agent-architecture.vercel.app)

A reusable framework for designing, validating, and managing software architectures across **14 perspectives**. Drop in any project's system spec, propose a change, and get a structured report with suggestions back.

> **Status:** Design phase. The 14-category model, tier structure, hallucination defense, and build phases are specified. Implementation is incremental (see Phase plan below).

---

## What It Does

Given any project — TutorAgent, Jarvis, a friend's repo — the framework:

1. **Loads** the project's system description (`my_system.md`)
2. **Reviews** a proposed change against 14 architectural perspectives
3. **Reports** issues, alternatives, second-order effects, and rollback paths — with evidence grades for every claim

```
Any project → framework.load(my_system.md) → framework.review(change) → report + suggestions
```

It's a **design partner**, not an executor. The framework draws blueprints; Claude Code or Codex lays the bricks.

---

## The 3-Line API

```python
framework = ArchitectureFramework()

# Analyzing TutorAgent
framework.load("tutoragent/my_system.md")
framework.review("Add adaptive difficulty to Mock Exam")

# Analyzing Jarvis
framework.load("jarvis/my_system.md")
framework.review("Connect HealthKit data to the scheduler")
```

Project-specific context lives in `my_system.md`. The framework itself stays generic.

---

## The 14 Layers

| # | Category | What It Covers |
|---|---|---|
| 1 | Multi-Agent Patterns | agent arrangement structure |
| 2 | Software Principles | code rules (SOLID, YAGNI, etc.) |
| 3 | Design Thinking | design judgment (Adversarial, Analogy, etc.) |
| 4 | Systems Thinking | seeing the whole (feedback loops, emergence, bottlenecks) |
| 5 | Meta-Engineering | the making process (CI/CD, tech debt, observability) |
| 6 | Domain Modeling | reality → code |
| 7 | Human-AI Interaction | user touchpoints |
| 8 | Failure & Recovery | recovery strategy |
| 9 | Security & Trust | permissions and trust |
| 10 | Data Architecture | data flow and schemas |
| 11 | Performance & Resource | speed and cost |
| 12 | Temporal Design | evolution design over time |
| 13 | Knowledge Evolution | growth of the knowledge base itself |
| 14 | Context Engineering | designing what to show the agent |

Categories 1-7 are established practice. 8-11 were missed in earlier passes. 12-14 are creative proposals specific to LLM-agent systems.

---

## Key Concepts

### Tier Structure — Automation Levels

**Principle: be free with automating analysis, strict with automating execution.**

- **Tier 1 (Automatic):** rule-based hooks. Write-access blocks, auto-backup, schema validation, cost guards. All if-statements. Even when wrong, they only block.
- **Tier 2 (Report Only):** LLM analyzes, human decides. Pattern advisors, code checkers, creative designers. Output reports, never touch code.
- **Tier 3 (Propose + Approve):** schema diffs, hook reordering, new agent definitions. Human picks Approve / Modify / Reject.

### Evidence Grade System — Hallucination Defense

Every agent claim carries a grade tag:

| Grade | Meaning | Requirement | Confidence |
|------|------|----------|--------|
| [FACT] | Directly verified in file/code | File name + line number | High |
| [CALC] | Calculation based on facts | Calculation steps | High |
| [INFER] | Inference | Evidence chain | Medium |
| [OPINION] | Agent judgment | ⚠️ mark required | Low |

Verification happens in 4 layers: hardcoded fact/calc checks (no LLM), structural checks (light LLM), logical inference review (LLM), and human approval. 60-70% of items get filtered at the hardcoded layers.

### Hardcoded vs LLM Boundary

```
Verifiable facts    → 100% hardcoded
Structural rules    → 90% hardcoded
Logical inference   → 100% LLM
Value judgments     → 100% human
```

**What can be verified goes in code, what requires thought goes to LLM, what requires decision goes to human.**

### Pattern Combinations Used

The framework itself uses 6 multi-agent patterns:
- **Contract Net** — role assignment to sub-reviewers
- **Concurrent** — parallel execution
- **Voting** — 3/4 consensus
- **Magentic** — review loop (max 4 iterations)
- **Stigmergy** — `write_log.jsonl` records every decision for future reference
- **Blackboard** — communication via shared files

---

## Build Plan

```
Phase 0 (1 day):    folder skeleton + templates
Phase 1 (2 days):   3 knowledge files (patterns.md, principles.md, thinking_methods.md)
Phase 2 (3 days):   Pattern Advisor agent + apply to real project
Phase 3 (2 days):   Hallucination Checker (hardcoded Layer 1-2 + LLM Layer 3)
Phase 4 (ongoing):  incrementally add checklists
Phase 5 (as needed): Creative Designer + advanced features
```

**The framework builds the project, and the project improves the framework.** Build in parallel, not sequentially.

---

## Code Review vs Architecture Review

```
Code Review (features, bug fixes):
  Light, fast. Only for changes that don't touch structure.

Architecture Review (structural changes):
  Always rigorous. All sub-reviewers. Full loop.
```

Structural decisions are the most expensive to reverse — never run them in light mode.

---

## Documents

- **[design_document.md](./design_document.md)** — concise design decisions, kept next to you while implementing
- **[multi_agent_architecture_report.md](./multi_agent_architecture_report.md)** — the full 2000-line record covering 20 multi-agent patterns, academic variants, Claude vs Codex architectures, hallucination defense, dependency tracking, and more
- **[reference_index.md](./reference_index.md)** — section-by-section index for navigating the full report

For the complete reasoning behind every decision in this README, see the full report.
