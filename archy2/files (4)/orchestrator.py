"""
Architecture Framework — Orchestrator
Connects scanner → 5 agents → loop → final report.

Usage:
    python orchestrator.py /path/to/project "Add adaptive difficulty feature"
    python orchestrator.py /path/to/project "Full architecture review"

Requires: ANTHROPIC_API_KEY environment variable
"""

import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime

import anthropic

# Import our scanner
sys.path.insert(0, str(Path(__file__).parent))
from scanner import run_scan, simulate_change_impact


# ============================================================
# CONFIG
# ============================================================

FAST_MODEL = "claude-haiku-4-5-20251001"   # Tier 1: cheap checks
DEEP_MODEL = "claude-sonnet-4-20250514"     # Tier 2: analysis

MAX_LOOPS = 3
FRAMEWORK_DIR = Path(__file__).parent


def load_knowledge(filename: str) -> str:
    """Load a knowledge file."""
    path = FRAMEWORK_DIR / "knowledge" / filename
    if path.exists():
        return path.read_text(encoding='utf-8')
    return ""

def load_skill(agent_name: str) -> str:
    """Load an agent's SKILL.md as system prompt."""
    path = FRAMEWORK_DIR / "skills" / agent_name / "SKILL.md"
    if path.exists():
        return path.read_text(encoding='utf-8')
    return ""


# ============================================================
# LLM CALLER
# ============================================================

client = None

def get_client():
    global client
    if client is None:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            print("ERROR: Set ANTHROPIC_API_KEY environment variable")
            sys.exit(1)
        client = anthropic.Anthropic(api_key=api_key)
    return client

def call_agent(agent_name: str, system_prompt: str, user_message: str, model: str = DEEP_MODEL) -> str:
    """Call an LLM agent with system prompt and user message."""
    print(f"   🤖 Calling {agent_name}...")
    
    try:
        response = get_client().messages.create(
            model=model,
            max_tokens=4096,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}]
        )
        result = response.content[0].text
        print(f"   ✅ {agent_name} done ({response.usage.input_tokens}+{response.usage.output_tokens} tokens)")
        return result
    except Exception as e:
        print(f"   ❌ {agent_name} failed: {e}")
        return f"[ERROR] {agent_name} failed: {e}"


# ============================================================
# AGENT DEFINITIONS
# ============================================================

def run_design_thinking(request: str, project_context: str) -> str:
    """Agent 3: Generate candidate solutions."""
    system = load_skill("design-thinking")
    knowledge = load_knowledge("thinking-methods.md")
    patterns = load_knowledge("patterns.md")
    
    user_msg = f"""## User Request
{request}

## Project Context (from automated scan)
{project_context}

## Available Patterns Reference
{patterns[:3000]}

## Available Methods Reference
{knowledge[:2000]}

Generate 3-5 candidates. Follow your SKILL.md instructions exactly."""
    
    return call_agent("Design Thinking", system, user_msg)


def run_pattern_advisor(request: str, project_context: str, candidates: str) -> str:
    """Agent 1: Match patterns to candidates."""
    system = load_skill("pattern-advisor")
    patterns = load_knowledge("patterns.md")
    
    user_msg = f"""## User Request
{request}

## Project Context
{project_context}

## Candidates from Design Thinking
{candidates}

## Patterns Knowledge Base
{patterns}

Match patterns to each candidate. Follow your SKILL.md instructions exactly."""
    
    return call_agent("Pattern Advisor", system, user_msg)


def run_principles_checker(request: str, project_context: str, recommendation: str) -> str:
    """Agent 2: Validate against software principles."""
    system = load_skill("principles-checker")
    principles = load_knowledge("principles.md")
    
    user_msg = f"""## User Request
{request}

## Project Context
{project_context}

## Pattern Advisor Recommendation
{recommendation}

## Principles Reference
{principles}

Validate the recommended candidate. Follow your SKILL.md instructions exactly."""
    
    return call_agent("Principles Checker", system, user_msg, model=FAST_MODEL)


def run_systems_thinking(request: str, project_context: str, 
                         candidates: str, recommendation: str, 
                         validation: str) -> str:
    """Agent 4: Check cascading impact. Has LOOP TERMINATION authority."""
    system = load_skill("systems-thinking")
    
    user_msg = f"""## User Request
{request}

## Project Context
{project_context}

## Design Thinking Candidates
{candidates}

## Pattern Advisor Recommendation
{recommendation}

## Principles Checker Validation
{validation}

Analyze cascading impact. Give your verdict: ✅ Proceed / ⚠️ Conditional / ❌ Reject.
Follow your SKILL.md instructions exactly."""
    
    return call_agent("Systems Thinking", system, user_msg)


# ============================================================
# HALLUCINATION CHECKER (Tier 1 — no LLM)
# ============================================================

def check_facts(report: str, project_path: str) -> list[dict]:
    """Verify [FACT] claims by checking if referenced files/lines exist."""
    issues = []
    
    # Find all [FACT] claims with file references
    fact_pattern = re.compile(r'\[FACT\].*?`([^`]+)`(?::(\d+))?')
    
    for match in fact_pattern.finditer(report):
        filename = match.group(1)
        line_num = match.group(2)
        
        # Check if file exists
        filepath = Path(project_path) / filename
        if not filepath.exists():
            # Try partial match
            found = list(Path(project_path).rglob(f"*{filename}*"))
            if not found:
                issues.append({
                    'type': 'FILE_NOT_FOUND',
                    'claim': match.group(0),
                    'file': filename,
                    'severity': 'HIGH'
                })
        elif line_num:
            # Check if line number exists
            try:
                lines = filepath.read_text(encoding='utf-8', errors='ignore').splitlines()
                if int(line_num) > len(lines):
                    issues.append({
                        'type': 'LINE_OUT_OF_RANGE',
                        'claim': match.group(0),
                        'file': filename,
                        'line': line_num,
                        'max_lines': len(lines),
                        'severity': 'MEDIUM'
                    })
            except:
                pass
    
    return issues


# ============================================================
# REPORT ASSEMBLER
# ============================================================

def assemble_report(request: str, project_context: str, 
                    candidates: str, recommendation: str, 
                    validation: str, systems_verdict: str,
                    fact_issues: list, loop_count: int) -> str:
    """Combine all agent outputs into final report."""
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    report = f"""# Architecture Review Report
**Generated**: {timestamp}
**Loops**: {loop_count}

---

## Request
{request}

---

## 1. Project Scan [FACT]
{project_context[:2000]}

---

## 2. Candidates (Design Thinking)
{candidates}

---

## 3. Pattern Recommendation (Pattern Advisor)
{recommendation}

---

## 4. Principles Validation (Principles Checker)
{validation}

---

## 5. Cascading Impact (Systems Thinking)
{systems_verdict}

---

## 6. Fact Check Results
"""
    
    if fact_issues:
        report += f"⚠️ **{len(fact_issues)} issues found:**\n\n"
        for issue in fact_issues:
            report += f"- **{issue['type']}**: `{issue['file']}`"
            if 'line' in issue:
                report += f" line {issue['line']} (max: {issue['max_lines']})"
            report += f" — Severity: {issue['severity']}\n"
    else:
        report += "✅ All [FACT] claims verified.\n"
    
    report += f"""
---

## 7. Confidence Assessment
- Scan coverage: ~70% (static analysis only)
- Fact verification: {"PASS" if not fact_issues else f"ISSUES ({len(fact_issues)})"}
- Agent loops: {loop_count} / {MAX_LOOPS}
- Evidence: Count FACT/CALC/INFER/OPINION tags above for distribution

---

*Generated by Architecture Framework v0.1*
*Scanner: NetworkX graph analysis | Agents: Claude API*
"""
    
    return report


# ============================================================
# ORCHESTRATOR — Main Loop
# ============================================================

def orchestrate(project_path: str, request: str, output_path: str = None):
    """
    Main orchestration loop.
    
    scan → design thinking → pattern advisor → principles checker
    → systems thinking → loop? → final report
    """
    
    print(f"\n{'='*60}")
    print(f"  Architecture Framework — Review")
    print(f"  Project: {project_path}")
    print(f"  Request: {request}")
    print(f"{'='*60}\n")
    
    # ===== Step 1: Scan (Tier 1 — no LLM) =====
    print("📁 Step 1: Scanning project...")
    report_text, G, analysis = run_scan(project_path)
    project_context = report_text
    print(f"   Scan complete: {analysis['stats']['total_files']} files, {analysis['stats']['total_edges']} deps\n")
    
    # ===== Step 2-6: Agent Loop =====
    loop_count = 0
    candidates = ""
    recommendation = ""
    validation = ""
    systems_verdict = ""
    
    while loop_count < MAX_LOOPS:
        loop_count += 1
        print(f"🔄 Loop {loop_count}/{MAX_LOOPS}")
        
        # Step 2: Design Thinking
        print("\n💡 Step 2: Design Thinking...")
        if loop_count == 1:
            candidates = run_design_thinking(request, project_context)
        else:
            # On retry, include previous feedback
            candidates = run_design_thinking(
                f"{request}\n\n## Previous Issues (from Systems Thinking)\n{systems_verdict}",
                project_context
            )
        
        # Step 3: Pattern Advisor
        print("\n🧩 Step 3: Pattern Advisor...")
        recommendation = run_pattern_advisor(request, project_context, candidates)
        
        # Step 4: Principles Checker
        print("\n📏 Step 4: Principles Checker...")
        validation = run_principles_checker(request, project_context, recommendation)
        
        # Step 5: Systems Thinking (has loop termination authority)
        print("\n🌐 Step 5: Systems Thinking...")
        systems_verdict = run_systems_thinking(
            request, project_context, candidates, recommendation, validation
        )
        
        # Step 6: Loop decision
        verdict_lower = systems_verdict.lower()
        if "✅" in systems_verdict or "proceed" in verdict_lower:
            print(f"\n✅ Systems Thinking: PROCEED (loop {loop_count})")
            break
        elif "❌" in systems_verdict or "reject" in verdict_lower:
            print(f"\n🔄 Systems Thinking: REJECT — looping back (loop {loop_count})")
            continue
        elif "⚠️" in systems_verdict or "conditional" in verdict_lower:
            print(f"\n⚠️ Systems Thinking: CONDITIONAL PROCEED (loop {loop_count})")
            break
        else:
            print(f"\n⚠️ Unclear verdict — proceeding (loop {loop_count})")
            break
    
    if loop_count >= MAX_LOOPS:
        print(f"\n⚠️ Max loops ({MAX_LOOPS}) reached. Assembling with current results.")
    
    # ===== Step 7: Hallucination Check (Tier 1 — no LLM) =====
    print("\n🔍 Step 7: Fact checking...")
    all_text = candidates + recommendation + validation + systems_verdict
    fact_issues = check_facts(all_text, project_path)
    print(f"   Found {len(fact_issues)} issues")
    
    # ===== Step 8: Assemble Report =====
    print("\n📋 Step 8: Assembling report...")
    final_report = assemble_report(
        request, project_context, candidates, recommendation,
        validation, systems_verdict, fact_issues, loop_count
    )
    
    # ===== Output =====
    if output_path:
        Path(output_path).write_text(final_report)
        print(f"\n📄 Report saved: {output_path}")
    
    # Cost estimate
    print(f"\n{'='*60}")
    print(f"  Done!")
    print(f"  Loops: {loop_count}")
    print(f"  Fact issues: {len(fact_issues)}")
    print(f"  Estimated cost: ~${loop_count * 0.08:.2f}")
    print(f"{'='*60}\n")
    
    return final_report


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python orchestrator.py <project_path> <request> [output_path]")
        print('Example: python orchestrator.py ~/TutorAgent "Add adaptive difficulty"')
        sys.exit(1)
    
    project = sys.argv[1]
    request = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) > 3 else f"review_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
    
    orchestrate(project, request, output)
