# Tier Rules

## Tier 1: Automatic (no LLM, rule-based)
- Write-access enforcement
- Schema validation
- Auto-backup before changes
- Cost guard (LLM budget limits)
- Context boundary check

Rule: If it can be an if-statement, it's Tier 1. Zero LLM calls. Safe to auto-execute.

## Tier 2: Report Only (LLM analyzes, human decides)
- Pattern conflict detection
- Principles violation detection
- Cascading impact analysis
- Feedback loop detection
- Coverage gap identification

Rule: LLM generates report. Does NOT touch code. Human reads and decides.

## Tier 3: Propose + Approve (LLM suggests, human approves)
- Schema change diffs
- New agent definitions
- Architecture restructuring proposals
- Migration scripts

Rule: LLM shows proposed changes with [Approve / Modify / Reject] options. Only executes on explicit approval.

## Principle
Analysis automation: freely.
Execution automation: strictly.
