# Software Principles — Knowledge Base

## SOLID Principles

### Single Responsibility (SRP)
- A module should have one, and only one, reason to change
- Ask: "If I change X, does this module need to change?"
- Violation signal: Module handles auth AND logging AND data processing
- Fix: Split into focused modules
- In MAS context: Each agent should have one clear job

### Open/Closed (OCP)
- Open for extension, closed for modification
- Ask: "Can I add a feature without changing existing code?"
- Violation signal: Adding a new pattern requires editing 5 existing files
- Fix: Plugin architecture, strategy pattern, configuration files
- In MAS context: Adding a new agent shouldn't require modifying existing agents

### Liskov Substitution (LSP)
- Subtypes must be substitutable for their base types
- Ask: "Can I swap this component without breaking the system?"
- Violation signal: Replacing agent A with agent B breaks the pipeline
- Fix: Consistent interfaces, contract-based design

### Interface Segregation (ISP)
- No client should depend on methods it does not use
- Ask: "Does this module expose things its consumers don't need?"
- Violation signal: Agent imports 20 functions but uses 3
- Fix: Smaller, focused interfaces
- In MAS context: Agent should receive only the context it needs (Context Engineering)

### Dependency Inversion (DIP)
- Depend on abstractions, not concretions
- Ask: "Does high-level logic depend on low-level details?"
- Violation signal: Orchestrator directly calls specific LLM API
- Fix: Abstract interface layer

## Practical Principles

### DRY (Don't Repeat Yourself)
- Every piece of knowledge should have a single, unambiguous representation
- Violation signal: Same logic in 3+ files, same path string hardcoded in 8 places
- Fix: Extract to shared utility, config file, or constants
- Detection: grep for duplicate strings/patterns

### YAGNI (You Ain't Gonna Need It)
- Don't build what you don't need yet
- Violation signal: Building Swarm Intelligence for a 3-agent system
- Fix: Build the simplest thing that works. Refactor when needed.
- Tension with OCP: Plan for extension but don't implement it

### KISS (Keep It Simple, Stupid)
- Simplest solution that works is usually best
- Violation signal: 5 design patterns for a problem solvable with an if-statement
- Fix: Ask "what's the simplest version of this?"

### Separation of Concerns (SoC)
- Different responsibilities should be in different modules
- Violation signal: UI code mixed with business logic mixed with data access
- Fix: Layer separation, module boundaries
- In MAS context: Agent that does analysis AND execution AND reporting → split

## Agent-Specific Principles

### Least Privilege
- Agent should have minimum permissions needed
- Violation signal: Agent has write access to files it only reads
- Fix: Explicit permission model (write_permissions.json)

### Fail Safely
- When an agent fails, the system should remain in a valid state
- Violation signal: Agent crash leaves data half-written
- Fix: Transactions, backups before writes, rollback capability

### Observability First
- Every agent action should be traceable
- Violation signal: Agent modifies files with no log
- Fix: write_log.jsonl, structured logging

### Idempotency
- Running the same operation twice should produce the same result
- Violation signal: Re-running analysis appends duplicate entries
- Fix: Check-before-write, unique IDs

## Anti-Patterns to Detect

| Anti-Pattern | Signal | Fix |
|-------------|--------|-----|
| God Module | One file >500 lines doing everything | Split by responsibility |
| Circular Dependency | A imports B, B imports A | Introduce interface layer |
| Hardcoded Config | Paths, URLs, keys in source code | Extract to config files |
| Silent Failure | try/catch that swallows errors | Log errors, fail explicitly |
| Shotgun Surgery | One change requires editing 10+ files | Consolidate related logic |
| Feature Envy | Module constantly accessing another module's data | Move logic to data owner |
| Premature Optimization | Caching/pooling before measuring | Measure first, optimize later |

## Matching to Evidence Grades

```
Detected by grep/file check     → [FACT]
Detected by line count/metrics   → [CALC]  
Inferred from structure          → [INFER]
"This might become a problem"    → [OPINION]
```
