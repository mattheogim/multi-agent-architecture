# Project Context — Auto-Generated Scan

**Project**: `arch-framework`
**Scanned**: 12 files, 15 dependencies
**Density**: 0.1136
**Clusters**: 3
**Isolated files**: 2

## File Structure

### `./`
  - `CLAUDE.md` (47 lines)
  - `scanner.py` (455 lines)

### `config/`
  - `tier_rules.md` (31 lines)

### `knowledge/`
  - `patterns.md` (161 lines)
  - `principles.md` (104 lines)
  - `thinking-methods.md` (140 lines)

### `skills/design-thinking/`
  - `SKILL.md` (70 lines)

### `skills/orchestrator/`
  - `SKILL.md` (73 lines)

### `skills/pattern-advisor/`
  - `SKILL.md` (47 lines)

### `skills/principles-checker/`
  - `SKILL.md` (47 lines)

### `skills/systems-thinking/`
  - `SKILL.md` (72 lines)

### `templates/`
  - `adr_template.md` (27 lines)

## Critical Files [FACT]
Files with the most incoming dependencies. Changing these affects the most modules.
  - **`knowledge/patterns.md`** — 4 modules depend on this
  - **`knowledge/principles.md`** — 3 modules depend on this
  - **`skills/systems-thinking/SKILL.md`** — 2 modules depend on this
  - **`skills/principles-checker/SKILL.md`** — 2 modules depend on this
  - **`knowledge/thinking-methods.md`** — 1 modules depend on this

## Hub Files [FACT]
Files that depend on the most other files. Changes here may need many updates.
  - **`CLAUDE.md`** — depends on 7 other files
  - **`skills/orchestrator/SKILL.md`** — depends on 2 other files
  - **`skills/design-thinking/SKILL.md`** — depends on 2 other files
  - **`scanner.py`** — depends on 1 other files
  - **`knowledge/patterns.md`** — depends on 1 other files

## Single Points of Failure [FACT]
Removing these files disconnects the dependency graph.
  - **`CLAUDE.md`** — removing splits graph into 4 pieces (was 3)
  - **`skills/design-thinking/SKILL.md`** — removing splits graph into 4 pieces (was 3)
  - **`skills/systems-thinking/SKILL.md`** — removing splits graph into 4 pieces (was 3)

## Circular Dependencies [FACT]
  - ✅ No circular dependencies found

## Module Clusters [CALC]
Groups of files that are tightly connected.

### Cluster 1 (10 files)
  - `CLAUDE.md`
  - `knowledge/patterns.md`
  - `knowledge/principles.md`
  - `knowledge/thinking-methods.md`
  - `scanner.py`
  - `skills/design-thinking/SKILL.md`
  - `skills/orchestrator/SKILL.md`
  - `skills/pattern-advisor/SKILL.md`
  - `skills/principles-checker/SKILL.md`
  - `skills/systems-thinking/SKILL.md`

### Cluster 2 (1 files)
  - `templates/adr_template.md`

### Cluster 3 (1 files)
  - `config/tier_rules.md`

## Centrality Rankings [CALC]
Betweenness centrality: nodes that sit on the most shortest paths between other nodes.
  - `knowledge/patterns.md`: 0.0455
  - `skills/principles-checker/SKILL.md`: 0.0273
  - `skills/design-thinking/SKILL.md`: 0.0091

## Scan Coverage
  - Files scanned: 12
  - Dependencies found: 15
  - Isolated (no connections): 2
  - File types: {'.md': 11, '.py': 1}

**⚠️ This is an automated scan. Dependencies extracted from imports/references only.**
**Runtime dependencies, dynamic imports, and implicit coupling are NOT detected.**
**Confidence: ~70% for static dependencies.**

## Change Impact Simulation [CALC]
**Target**: `knowledge/patterns.md`
**Risk Score**: 6.7

### 1st Order (direct) [FACT]
  - `skills/orchestrator/SKILL.md`
  - `skills/pattern-advisor/SKILL.md`
  - `CLAUDE.md`
  - `skills/principles-checker/SKILL.md`
  - `skills/design-thinking/SKILL.md`

### 2nd Order (indirect) [INFER]
  - `knowledge/thinking-methods.md`
  - `skills/systems-thinking/SKILL.md`
  - `knowledge/principles.md`

### 3rd Order (distant) [OPINION]
  - `scanner.py`

**Total affected**: 9 files
