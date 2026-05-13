"""
Architecture Framework — Project Scanner
Scans a project directory, builds a dependency graph, runs analysis.
Outputs project_context.md with structural insights.

Usage:
    python scanner.py /path/to/project
    python scanner.py /path/to/project --output report.md
"""

import os
import re
import json
import sys
import subprocess
from pathlib import Path
from collections import defaultdict

try:
    import networkx as nx
except ImportError:
    print("Installing networkx...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "networkx", "-q"])
    import networkx as nx


# ============================================================
# 1. FILE SCANNER — Discover all files
# ============================================================

IGNORE_DIRS = {'.git', 'node_modules', '__pycache__', '.next', 'dist', 'build', '.venv', 'venv'}
SCAN_EXTENSIONS = {'.py', '.js', '.ts', '.jsx', '.tsx', '.md', '.json', '.yaml', '.yml', '.swift', '.toml'}

def scan_files(project_path: str) -> list[dict]:
    """Walk directory tree and collect file metadata."""
    files = []
    root = Path(project_path)
    for path in root.rglob('*'):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix in SCAN_EXTENSIONS:
            rel = str(path.relative_to(root))
            files.append({
                'path': rel,
                'name': path.name,
                'suffix': path.suffix,
                'size': path.stat().st_size,
                'lines': count_lines(path),
                'dir': str(path.parent.relative_to(root)),
            })
    return files

def count_lines(path: Path) -> int:
    try:
        return len(path.read_text(encoding='utf-8', errors='ignore').splitlines())
    except:
        return 0


# ============================================================
# 2. DEPENDENCY EXTRACTOR — Find relationships between files
# ============================================================

def extract_python_imports(filepath: str, project_root: str) -> list[str]:
    """Extract import targets from Python files."""
    imports = []
    try:
        content = Path(project_root, filepath).read_text(encoding='utf-8', errors='ignore')
        # import X / from X import Y
        for match in re.finditer(r'^(?:from\s+([\w.]+)|import\s+([\w.]+))', content, re.MULTILINE):
            module = match.group(1) or match.group(2)
            imports.append(module)
    except:
        pass
    return imports

def extract_js_imports(filepath: str, project_root: str) -> list[str]:
    """Extract import/require targets from JS/TS files."""
    imports = []
    try:
        content = Path(project_root, filepath).read_text(encoding='utf-8', errors='ignore')
        # import ... from 'path' / require('path')
        for match in re.finditer(r'(?:from\s+["\']([^"\']+)["\']|require\s*\(\s*["\']([^"\']+)["\']\s*\))', content):
            path = match.group(1) or match.group(2)
            if path.startswith('.'):
                imports.append(path)
    except:
        pass
    return imports

def extract_md_references(filepath: str, project_root: str) -> list[str]:
    """Extract file references from Markdown (SKILL.md, CLAUDE.md, etc.)."""
    refs = []
    try:
        content = Path(project_root, filepath).read_text(encoding='utf-8', errors='ignore')
        # file paths like src/skills/tutor/ or error_notes.md
        for match in re.finditer(r'(?:[\w/.-]+\.(?:md|json|jsonl|ts|js|py|swift|yaml))', content):
            ref = match.group(0)
            if ref != filepath:  # don't self-reference
                refs.append(ref)
        # directory references like skills/tutor, agents/GC
        for match in re.finditer(r'(?:skills|agents|hooks|src|data)[/\\][\w-]+', content):
            refs.append(match.group(0))
    except:
        pass
    return list(set(refs))

def extract_json_references(filepath: str, project_root: str) -> list[str]:
    """Extract file path references from JSON files."""
    refs = []
    try:
        content = Path(project_root, filepath).read_text(encoding='utf-8', errors='ignore')
        data = json.loads(content)
        # Walk JSON looking for string values that look like file paths
        def walk(obj):
            if isinstance(obj, str):
                if '/' in obj and ('.' in obj.split('/')[-1]):
                    refs.append(obj)
            elif isinstance(obj, dict):
                for v in obj.values():
                    walk(v)
            elif isinstance(obj, list):
                for v in obj:
                    walk(v)
        walk(data)
    except:
        pass
    return refs


def build_dependency_graph(files: list[dict], project_root: str) -> nx.DiGraph:
    """Build a directed graph from file dependencies."""
    G = nx.DiGraph()
    
    # Add all files as nodes
    for f in files:
        G.add_node(f['path'], 
                   name=f['name'],
                   suffix=f['suffix'],
                   lines=f['lines'],
                   dir=f['dir'],
                   size=f['size'])
    
    # Extract edges based on file type
    all_paths = {f['path'] for f in files}
    all_names = {f['name']: f['path'] for f in files}
    
    for f in files:
        filepath = f['path']
        refs = []
        
        if f['suffix'] == '.py':
            refs = extract_python_imports(filepath, project_root)
        elif f['suffix'] in {'.js', '.ts', '.jsx', '.tsx'}:
            refs = extract_js_imports(filepath, project_root)
        elif f['suffix'] == '.md':
            refs = extract_md_references(filepath, project_root)
        elif f['suffix'] == '.json':
            refs = extract_json_references(filepath, project_root)
        
        # Resolve references to actual files
        for ref in refs:
            target = resolve_reference(ref, filepath, all_paths, all_names)
            if target and target != filepath:
                G.add_edge(filepath, target, type='references')
    
    return G


def resolve_reference(ref: str, source: str, all_paths: set, all_names: dict) -> str | None:
    """Try to resolve a reference string to an actual file path."""
    # Direct match
    if ref in all_paths:
        return ref
    # Match by filename
    if ref in all_names:
        return all_names[ref]
    # Partial match (e.g., 'skills/tutor' → find 'skills/tutor/SKILL.md')
    for path in all_paths:
        if ref in path:
            return path
    return None


# ============================================================
# 3. ANALYSIS — Run NetworkX calculations
# ============================================================

def analyze_graph(G: nx.DiGraph) -> dict:
    """Run structural analysis on the dependency graph."""
    analysis = {}
    
    if len(G.nodes) == 0:
        return {"error": "Empty graph"}
    
    # --- Centrality (critical files) ---
    bc = nx.betweenness_centrality(G)
    dc = nx.degree_centrality(G)
    in_deg = dict(G.in_degree())
    out_deg = dict(G.out_degree())
    
    analysis['centrality'] = {
        'betweenness': sorted(bc.items(), key=lambda x: x[1], reverse=True)[:10],
        'degree': sorted(dc.items(), key=lambda x: x[1], reverse=True)[:10],
    }
    
    # --- Critical files (high in-degree = many things depend on it) ---
    analysis['critical_files'] = sorted(
        [(node, in_deg[node]) for node in G.nodes if in_deg[node] > 0],
        key=lambda x: x[1], reverse=True
    )[:10]
    
    # --- Hub files (high out-degree = depends on many things) ---
    analysis['hub_files'] = sorted(
        [(node, out_deg[node]) for node in G.nodes if out_deg[node] > 0],
        key=lambda x: x[1], reverse=True
    )[:10]
    
    # --- Cycles (circular dependencies) ---
    try:
        cycles = list(nx.simple_cycles(G))
        analysis['cycles'] = cycles[:10]  # limit
    except:
        analysis['cycles'] = []
    
    # --- Connected components (clusters) ---
    undirected = G.to_undirected()
    components = list(nx.connected_components(undirected))
    analysis['clusters'] = [sorted(list(c)) for c in components]
    
    # --- Single points of failure ---
    spof = []
    for node in G.nodes:
        H = G.copy()
        H.remove_node(node)
        undirected_h = H.to_undirected()
        if undirected_h.number_of_nodes() > 0:
            original_components = nx.number_connected_components(undirected)
            new_components = nx.number_connected_components(undirected_h)
            if new_components > original_components:
                spof.append({
                    'file': node,
                    'components_before': original_components,
                    'components_after': new_components,
                    'severity': new_components - original_components
                })
    analysis['single_points_of_failure'] = sorted(spof, key=lambda x: x['severity'], reverse=True)
    
    # --- Basic stats ---
    analysis['stats'] = {
        'total_files': G.number_of_nodes(),
        'total_edges': G.number_of_edges(),
        'density': nx.density(G),
        'num_clusters': len(components),
        'isolated_files': len([n for n in G.nodes if G.degree(n) == 0]),
    }
    
    return analysis


# ============================================================
# 4. IMPACT SIMULATOR — "What if I change this file?"
# ============================================================

def simulate_change_impact(G: nx.DiGraph, target_file: str) -> dict:
    """Simulate the cascading impact of changing a specific file."""
    if target_file not in G.nodes:
        return {"error": f"File '{target_file}' not found in graph"}
    
    impact = {
        'target': target_file,
        'direct': [],     # 1st order — FACT level
        'indirect': [],   # 2nd order — INFER level
        'tertiary': [],   # 3rd order — OPINION level
    }
    
    # 1st order: files that directly depend on target (read from it)
    direct = set(G.predecessors(target_file)) | set(G.successors(target_file))
    impact['direct'] = list(direct)
    
    # 2nd order: files that depend on 1st order files
    indirect = set()
    for d in direct:
        neighbors = set(G.predecessors(d)) | set(G.successors(d))
        indirect |= neighbors
    indirect -= direct
    indirect -= {target_file}
    impact['indirect'] = list(indirect)
    
    # 3rd order: files that depend on 2nd order files
    tertiary = set()
    for d in indirect:
        neighbors = set(G.predecessors(d)) | set(G.successors(d))
        tertiary |= neighbors
    tertiary -= indirect
    tertiary -= direct
    tertiary -= {target_file}
    impact['tertiary'] = list(tertiary)
    
    impact['total_affected'] = len(direct) + len(indirect) + len(tertiary)
    impact['risk_score'] = round(len(direct) * 1.0 + len(indirect) * 0.5 + len(tertiary) * 0.2, 2)
    
    return impact


# ============================================================
# 5. REPORT GENERATOR — Output project_context.md
# ============================================================

def generate_report(project_path: str, files: list, G: nx.DiGraph, analysis: dict) -> str:
    """Generate the project_context.md report."""
    
    lines = []
    lines.append("# Project Context — Auto-Generated Scan")
    lines.append(f"\n**Project**: `{project_path}`")
    lines.append(f"**Scanned**: {analysis['stats']['total_files']} files, {analysis['stats']['total_edges']} dependencies")
    lines.append(f"**Density**: {analysis['stats']['density']:.4f}")
    lines.append(f"**Clusters**: {analysis['stats']['num_clusters']}")
    lines.append(f"**Isolated files**: {analysis['stats']['isolated_files']}")
    
    # --- File Structure ---
    lines.append("\n## File Structure")
    dirs = defaultdict(list)
    for f in files:
        dirs[f['dir']].append(f)
    for d in sorted(dirs.keys()):
        lines.append(f"\n### `{d}/`")
        for f in sorted(dirs[d], key=lambda x: x['name']):
            lines.append(f"  - `{f['name']}` ({f['lines']} lines)")
    
    # --- Critical Files (most depended on) ---
    lines.append("\n## Critical Files [FACT]")
    lines.append("Files with the most incoming dependencies. Changing these affects the most modules.")
    if analysis['critical_files']:
        for file, in_deg in analysis['critical_files'][:5]:
            lines.append(f"  - **`{file}`** — {in_deg} modules depend on this")
    else:
        lines.append("  - No critical files detected")
    
    # --- Hub Files (depends on most things) ---
    lines.append("\n## Hub Files [FACT]")
    lines.append("Files that depend on the most other files. Changes here may need many updates.")
    if analysis['hub_files']:
        for file, out_deg in analysis['hub_files'][:5]:
            lines.append(f"  - **`{file}`** — depends on {out_deg} other files")
    else:
        lines.append("  - No hub files detected")
    
    # --- Single Points of Failure ---
    lines.append("\n## Single Points of Failure [FACT]")
    lines.append("Removing these files disconnects the dependency graph.")
    if analysis['single_points_of_failure']:
        for spof in analysis['single_points_of_failure'][:5]:
            lines.append(f"  - **`{spof['file']}`** — removing splits graph into {spof['components_after']} pieces (was {spof['components_before']})")
    else:
        lines.append("  - No single points of failure detected (graph is robust)")
    
    # --- Circular Dependencies ---
    lines.append("\n## Circular Dependencies [FACT]")
    if analysis['cycles']:
        for cycle in analysis['cycles'][:5]:
            cycle_str = " → ".join(cycle) + " → " + cycle[0]
            lines.append(f"  - ⚠️ `{cycle_str}`")
    else:
        lines.append("  - ✅ No circular dependencies found")
    
    # --- Module Clusters ---
    lines.append("\n## Module Clusters [CALC]")
    lines.append("Groups of files that are tightly connected.")
    for i, cluster in enumerate(analysis['clusters'][:8]):
        lines.append(f"\n### Cluster {i+1} ({len(cluster)} files)")
        for f in sorted(cluster)[:10]:
            lines.append(f"  - `{f}`")
        if len(cluster) > 10:
            lines.append(f"  - ... and {len(cluster) - 10} more")
    
    # --- Centrality Rankings ---
    lines.append("\n## Centrality Rankings [CALC]")
    lines.append("Betweenness centrality: nodes that sit on the most shortest paths between other nodes.")
    for file, score in analysis['centrality']['betweenness'][:5]:
        if score > 0:
            lines.append(f"  - `{file}`: {score:.4f}")
    
    # --- Coverage ---
    lines.append("\n## Scan Coverage")
    lines.append(f"  - Files scanned: {len(files)}")
    lines.append(f"  - Dependencies found: {analysis['stats']['total_edges']}")
    lines.append(f"  - Isolated (no connections): {analysis['stats']['isolated_files']}")
    suffixes = defaultdict(int)
    for f in files:
        suffixes[f['suffix']] += 1
    lines.append(f"  - File types: {dict(suffixes)}")
    lines.append(f"\n**⚠️ This is an automated scan. Dependencies extracted from imports/references only.**")
    lines.append(f"**Runtime dependencies, dynamic imports, and implicit coupling are NOT detected.**")
    lines.append(f"**Confidence: ~70% for static dependencies.**")
    
    return "\n".join(lines)


# ============================================================
# MAIN
# ============================================================

def run_scan(project_path: str, output_path: str = None, change_target: str = None):
    """Main entry point."""
    print(f"🔍 Scanning: {project_path}")
    
    # 1. Scan files
    files = scan_files(project_path)
    print(f"   Found {len(files)} files")
    
    # 2. Build graph
    G = build_dependency_graph(files, project_path)
    print(f"   Built graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    
    # 3. Analyze
    analysis = analyze_graph(G)
    print(f"   Analysis complete")
    
    # 4. Generate report
    report = generate_report(project_path, files, G, analysis)
    
    # 5. Impact simulation (if target specified)
    if change_target:
        impact = simulate_change_impact(G, change_target)
        report += "\n\n## Change Impact Simulation [CALC]\n"
        report += f"**Target**: `{change_target}`\n"
        report += f"**Risk Score**: {impact.get('risk_score', 'N/A')}\n"
        report += f"\n### 1st Order (direct) [FACT]\n"
        for f in impact.get('direct', []):
            report += f"  - `{f}`\n"
        report += f"\n### 2nd Order (indirect) [INFER]\n"
        for f in impact.get('indirect', []):
            report += f"  - `{f}`\n"
        report += f"\n### 3rd Order (distant) [OPINION]\n"
        for f in impact.get('tertiary', []):
            report += f"  - `{f}`\n"
        report += f"\n**Total affected**: {impact.get('total_affected', 0)} files\n"
    
    # 6. Output
    if output_path:
        Path(output_path).write_text(report)
        print(f"   Report saved: {output_path}")
    
    return report, G, analysis


if __name__ == "__main__":
    project = sys.argv[1] if len(sys.argv) > 1 else "."
    output = sys.argv[2] if len(sys.argv) > 2 else None
    target = sys.argv[3] if len(sys.argv) > 3 else None
    
    report, G, analysis = run_scan(project, output, target)
    if not output:
        print(report)
