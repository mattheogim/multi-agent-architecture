# Multi-Agent Architecture Report — Reference Index

> When trying to find something in the 2000-line original document, check this index first.

---

## Pattern Basics

| Section | Content | Use When |
|------|------|---------|
| **A** | 20 patterns organized (8 categories) + when-to-use table + reference books/papers/frameworks | "What was this pattern again?" |
| **B** | Background of the pattern creators (SW engineers, manufacturing, military, economics, biology, philosophy) + why they built them when AI didn't exist | "Why should I learn this?" |
| **C** | 3 related career tracks (distributed systems, AI/ML agents, industrial automation) + learning paths | "What do people who do this actually do?" |

## Pattern Deep Dive

| Section | Content | Use When |
|------|------|---------|
| **D** | Concrete Swarm + Agent examples (logistics, drones, code review swarm, info gathering swarm) | "What can you build with swarms?" |
| **E** | 30+ academic variant patterns (Coalition, BFT, ACO, PSO, BOID, MOISE+, etc.) | "What variants are out there?" |
| **M** | Process of elimination from 20 to 6 patterns (3 constraints: solo use, cost, infrastructure) + combined pattern architecture diagram | "Why did you pick these patterns?" |
| **N** | Patterns that come back if cost is unlimited (Group Chat, Swarm, Market-Based) + speed comparison | "Does spending more money make it better?" |

## Automation & Design

| Section | Content | Use When |
|------|------|---------|
| **F** | Pattern automation feasibility (AutoGen, CrewAI, CAMEL, MetaGPT) + realistic limits | "Can an agent build structure?" |
| **G** | Why implementation is hard (death, message order, state, cost) + why evaluation is hard | "Why doesn't it work even after picking a pattern?" |
| **H** | Claude vs Codex architecture comparison (Orchestrator-Worker+Blackboard vs single agent+tool loop) | "What structure do Claude/Codex use?" |
| **I** | 5 essential things beyond patterns (Prompt design, State management, Tool design, Guardrails, Observability) | "What else should I know besides patterns?" |

## Framework Core

| Section | Content | Use When |
|------|------|---------|
| **Q** | Evolution from 3 → 7 → 14 categories + details of creative proposals 12-14 | "What are the 14 layers?" |
| **R** | Can the 14 be made into agents — ★ automation suitability ratings + Architecture Agent Suite structure | "Which agents do I build?" |
| **S** | Tier 1 (auto) / 2 (report) / 3 (propose + approve) structure + full flow of a confidence score addition scenario | "Will the agent just fix it for me?" |
| **T** | General-purpose framework structure (folder structure + framework.load().review() interface) | "Make it work for any project" |
| **U** | Framework → Claude Code/Codex → Framework loop + concurrent build strategy | "Can I build Jarvis with this?" |

## Implementation Details

| Section | Content | Use When |
|------|------|---------|
| **J** | Visualization methods (C4, Sequence, State Machine, DAG, Event Storming) + corporate processes (Architect, ADR, Design Review) | "How do I diagram something complex?" |
| **K** | Current TutorAgent structure analysis (5 pattern mappings + 3 improvements) | "Example of analyzing my project" |
| **L** | Blackboard conflict prevention hook + Structure Reviewer agent design + Stigmergy/Pub-Sub details | "How do I start automating?" |
| **O** | Code Review vs Architecture Review separation principle | "Can I keep reviews light?" |
| **P** | 4 creative design methods (Adversarial, Evolutionary, Analogy, Constraint Relaxation) + full flow diagram | "Methods other than elimination?" |
| **V** | Hallucination defense (evidence grades FACT/CALC/INFER/OPINION + Checker agent + per-category trust strategy) | "How do I catch hallucinations?" |
| **W** | Hardcoded vs LLM boundary (4-Layer structure + code examples) | "What goes in code vs LLM?" |
| **X** | Concrete build method for 1-14 (Phase 0~5 + 6-month timeline) | "Where do I start building?" |
| **Y** | 6 design methodologies (Pseudocode, Flowchart, User Story, Interface-First, Decision Table, Scenario Walkthrough) | "What do I do before coding?" |
| **Z** | Dependency tracking methods (C4, Dependency Map, Impact Mapping, ADR, Wardley Map) + dependencies.md template | "How do I see the whole picture?" |
