#!/usr/bin/env python3
"""
Generate index.md files for each work-group directory under planned/ and prepared/.

For each non-empty WG directory the script:
  1. Parses every FHIR-*.md file to extract metadata (key, title, spec,
     artifact/repo, dates, related tickets / prerequisites).
  2. Groups tickets by Specification → Artifact (repository).
  3. Orders tickets by date and dependency (prerequisites listed first).
  4. Writes an index.md with group summaries and dependency explanations.

Usage:
    python generate-indexes.py            # default: repo root = cwd
    python generate-indexes.py /some/path # explicit repo root
"""

from __future__ import annotations

import os
import re
import sys
import textwrap
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


# ── Data model ───────────────────────────────────────────────────────────────

@dataclass
class TicketInfo:
    key: str                                     # e.g. "FHIR-20788"
    title: str = ""
    specification: str = ""
    work_group: str = ""
    status: str = ""
    resolution: str = ""
    priority: str = ""
    created: str = ""
    updated: str = ""
    resolved: str = ""
    reporter: str = ""
    artifacts: list[str] = field(default_factory=list)  # repo names
    related_tickets: list[str] = field(default_factory=list)
    prerequisites: list[str] = field(default_factory=list)
    is_skip: bool = False


# ── Parsers ──────────────────────────────────────────────────────────────────

_BOLD_KV = re.compile(r"^\*\*(.+?)\*\*[:\s]+(.+)$")
_TABLE_ROW = re.compile(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|")
_H1_IMPL = re.compile(r"^#\s+Implementation Plan:\s+(.+)", re.I)
_H1_REVIEW = re.compile(r"^#\s+Ticket Review:\s+(.+)", re.I)
_H1_KEY_TITLE = re.compile(r"^#\s+(FHIR-\d+)[\s:—–-]+(.+)")
_H1_KEY_IMPL = re.compile(r"^#\s+(FHIR-\d+):\s+Implementation Plan", re.I)
_REPO_HEADING = re.compile(r"^#{2,4}\s+(?:\[?)?(HL7/[\w._-]+)", re.I)
_REPO_TABLE = re.compile(r"\[?(HL7/[\w._-]+)\]?")
_FHIR_REF = re.compile(r"FHIR-(\d+)")
_SKIP_MARKER = re.compile(r"^(?:SKIP|REPO_NOT_CACHED)", re.I)


def _clean(value: str) -> str:
    """Strip markdown link wrappers, trailing pipes, whitespace."""
    value = value.strip().rstrip("|").strip()
    # [text](url) → text
    m = re.match(r"\[(.+?)\]\(.+?\)", value)
    if m:
        value = m.group(1)
    return value


def _field_name(raw: str) -> str:
    return raw.strip().rstrip(":").lower().replace(" ", "_").replace("*", "")


def parse_ticket(filepath: Path) -> TicketInfo:
    """Parse a single FHIR-*.md file and return structured metadata."""
    key = filepath.stem  # e.g. "FHIR-20788"
    info = TicketInfo(key=key)

    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except OSError:
        info.is_skip = True
        return info

    lines = text.splitlines()
    if not lines:
        info.is_skip = True
        return info

    # Check for skip/stub files
    for line in lines[:5]:
        if _SKIP_MARKER.search(line):
            info.is_skip = True

    # Pass 1: Extract title from H1
    for line in lines[:5]:
        line_s = line.strip()
        m = _H1_KEY_IMPL.match(line_s)
        if m:
            break
        m = _H1_IMPL.match(line_s)
        if m:
            info.key = m.group(1).strip()
            break
        m = _H1_REVIEW.match(line_s)
        if m:
            info.key = m.group(1).strip()
            break
        m = _H1_KEY_TITLE.match(line_s)
        if m:
            info.key = m.group(1).strip()
            info.title = m.group(2).strip()
            break

    # Pass 2: Extract metadata from bold-KV pairs and table rows
    section = ""
    in_prereqs = False
    in_related = False
    in_affected_repos = False
    in_affected_repo_table = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Track sections
        if stripped.startswith("#"):
            heading_text = stripped.lstrip("#").strip().lower()
            section = heading_text
            in_prereqs = "prerequisite" in heading_text
            in_related = "related ticket" in heading_text
            in_affected_repos = (
                "affected repositor" in heading_text
                or "affected repo" in heading_text
            )
            in_affected_repo_table = "affected" in heading_text and "repositor" in heading_text
            continue

        # Bold key-value pairs
        m = _BOLD_KV.match(stripped)
        if m:
            fname = _field_name(m.group(1))
            val = _clean(m.group(2))
            _apply_field(info, fname, val)
            continue

        # Table rows with bold field names
        m = _TABLE_ROW.match(stripped)
        if m:
            fname = _field_name(m.group(1))
            val = _clean(m.group(2))
            _apply_field(info, fname, val)
            continue

        # Repository headings (#### HL7/fhir (...))
        if in_affected_repos or in_affected_repo_table:
            m = _REPO_HEADING.match(stripped)
            if m:
                repo = m.group(1).strip().rstrip(")")
                if repo not in info.artifacts:
                    info.artifacts.append(repo)
                continue
            # Table rows with repo links
            if stripped.startswith("|") and "HL7/" in stripped:
                for rm in _REPO_TABLE.finditer(stripped):
                    repo = rm.group(1).strip().rstrip(")")
                    if repo not in info.artifacts:
                        info.artifacts.append(repo)

        # Prerequisites – look for FHIR-NNNNN references
        if in_prereqs and _FHIR_REF.search(stripped):
            for pm in _FHIR_REF.finditer(stripped):
                ref = f"FHIR-{pm.group(1)}"
                if ref != info.key and ref not in info.prerequisites:
                    info.prerequisites.append(ref)

        # Related tickets
        if in_related and _FHIR_REF.search(stripped):
            for pm in _FHIR_REF.finditer(stripped):
                ref = f"FHIR-{pm.group(1)}"
                if ref != info.key and ref not in info.related_tickets:
                    info.related_tickets.append(ref)

    return info


def _apply_field(info: TicketInfo, fname: str, val: str) -> None:
    """Map a parsed field name to the TicketInfo dataclass."""
    if fname in ("title", "summary") and not info.title:
        info.title = val
    elif fname == "specification":
        info.specification = val
    elif fname in ("work_group", "workgroup"):
        info.work_group = val
    elif fname == "status":
        info.status = val
    elif fname == "resolution":
        info.resolution = val
    elif fname == "priority":
        info.priority = val
    elif fname == "created":
        info.created = val
    elif fname == "updated":
        info.updated = val
    elif fname in ("resolved", "resolved_date"):
        info.resolved = val
    elif fname == "reporter":
        info.reporter = val
    elif fname in ("repository", "repo"):
        repo = val.replace("`", "").strip()
        if repo and repo not in info.artifacts:
            info.artifacts.append(repo)
    elif fname in ("key", "ticket"):
        # key may be set from the table
        cleaned = re.sub(r"\[|\]|\(.*?\)", "", val).strip()
        m = re.match(r"(FHIR-\d+)", cleaned)
        if m:
            info.key = m.group(1)


# ── Grouping & ordering ─────────────────────────────────────────────────────

def _sort_date(t: TicketInfo) -> str:
    """Return best date for sorting (resolved > created > updated)."""
    return t.resolved or t.created or t.updated or "9999-99-99"


def _topo_sort(tickets: list[TicketInfo]) -> list[TicketInfo]:
    """
    Topological sort tickets by prerequisites/related-tickets within the list,
    falling back to date order for ties. Returns dependency groups as a list of
    (root_ticket | None, [tickets]) tuples via `dependency_groups`.
    """
    key_map: dict[str, TicketInfo] = {t.key: t for t in tickets}
    local_keys = set(key_map.keys())

    # Build adjacency: ticket → set of tickets it depends on (that are in this list)
    deps: dict[str, set[str]] = {}
    for t in tickets:
        local_deps: set[str] = set()
        for p in t.prerequisites:
            if p in local_keys and p != t.key:
                local_deps.add(p)
        deps[t.key] = local_deps

    # Kahn's algorithm
    in_degree: dict[str, int] = {t.key: 0 for t in tickets}
    for k, ds in deps.items():
        for d in ds:
            if d in in_degree:
                in_degree[k] = in_degree.get(k, 0) + 1

    # Seed queue sorted by date
    queue = sorted(
        [k for k, d in in_degree.items() if d == 0],
        key=lambda k: _sort_date(key_map[k]),
    )
    result: list[TicketInfo] = []
    while queue:
        k = queue.pop(0)
        result.append(key_map[k])
        for other_k, other_deps in deps.items():
            if k in other_deps:
                in_degree[other_k] -= 1
                if in_degree[other_k] == 0:
                    queue.append(other_k)
                    queue.sort(key=lambda x: _sort_date(key_map[x]))

    # Add any remaining (cycles) sorted by date
    seen = {t.key for t in result}
    for t in sorted(tickets, key=_sort_date):
        if t.key not in seen:
            result.append(t)

    return result


def build_dependency_groups(
    tickets: list[TicketInfo],
) -> list[tuple[Optional[TicketInfo], list[TicketInfo]]]:
    """
    Group tickets that have prerequisite relationships with each other.
    Returns (root_or_None, [tickets_in_group]) tuples.
    Root is the prerequisite ticket; dependents follow.
    Tickets with no local deps get root=None.
    """
    key_set = {t.key for t in tickets}
    key_map = {t.key: t for t in tickets}

    # Find clusters of connected tickets via prerequisites
    parent_of: dict[str, str] = {}  # child → root
    for t in tickets:
        for p in t.prerequisites:
            if p in key_set and p != t.key:
                parent_of[t.key] = p

    # Build groups
    root_groups: dict[str, list[TicketInfo]] = {}
    standalone: list[TicketInfo] = []
    assigned: set[str] = set()

    for t in tickets:
        if t.key in assigned:
            continue
        # Walk up to find root
        root_key = t.key
        visited: set[str] = {root_key}
        while root_key in parent_of and parent_of[root_key] not in visited:
            root_key = parent_of[root_key]
            visited.add(root_key)

        # Collect all tickets that trace back to this root
        if root_key != t.key or any(
            parent_of.get(other.key) == t.key for other in tickets
        ):
            if root_key not in root_groups:
                root_groups[root_key] = []
            if t.key not in assigned:
                root_groups[root_key].append(t)
                assigned.add(t.key)
            # Also ensure root itself is in the group
            if root_key in key_map and root_key not in assigned:
                root_groups[root_key].insert(0, key_map[root_key])
                assigned.add(root_key)
        else:
            standalone.append(t)
            assigned.add(t.key)

    # Ensure root is first in each group
    result: list[tuple[Optional[TicketInfo], list[TicketInfo]]] = []
    for root_key, members in root_groups.items():
        members.sort(key=lambda x: (0 if x.key == root_key else 1, _sort_date(x)))
        result.append((key_map.get(root_key), members))

    for t in standalone:
        result.append((None, [t]))

    # Sort groups by the first ticket's date
    result.sort(key=lambda g: _sort_date(g[1][0]) if g[1] else "9999")
    return result


# ── Index generation ─────────────────────────────────────────────────────────

def _jira_url(key: str) -> str:
    return f"https://jira.hl7.org/browse/{key}"


def _md_link(key: str) -> str:
    return f"[{key}](./{key}.md)"


def _jira_link(key: str) -> str:
    return f"[Jira]({_jira_url(key)})"


def _emit_ticket_table(
    lines: list[str],
    tickets: list[TicketInfo],
    phase: str,
) -> None:
    """Write a single consolidated ticket table, with dependency-group
    sub-headings when appropriate."""
    dep_groups = build_dependency_groups(tickets)

    # Separate dependency clusters from standalone tickets
    clusters = [(root, members) for root, members in dep_groups if root is not None and len(members) > 1]
    standalones = [members[0] for root, members in dep_groups if root is None or len(members) == 1]

    # Emit dependency clusters first
    for root, members in clusters:
        dep_children = [m for m in members if m.key != root.key]
        child_keys = ", ".join(m.key for m in dep_children)
        lines.append(f"#### Dependency Group: {root.key}\n")
        lines.append(
            f"> **{root.key}** must be completed before {child_keys}. "
            f"These tickets share prerequisite relationships — "
            f"complete them in the listed order.\n"
        )
        lines.append("| Key | Title | Status | Date | Links |")
        lines.append("|-----|-------|--------|------|-------|")
        for t in members:
            _emit_ticket_row(lines, t)
        lines.append("")

    # Emit standalone tickets in one consolidated table
    if standalones:
        if clusters:
            lines.append("#### Other Tickets\n")
        lines.append("| Key | Title | Status | Date | Links |")
        lines.append("|-----|-------|--------|------|-------|")
        for t in standalones:
            _emit_ticket_row(lines, t)
        lines.append("")


def _emit_ticket_row(lines: list[str], t: TicketInfo) -> None:
    date = t.resolved or t.created or t.updated or "—"
    title_display = t.title or "*(see ticket)*"
    status_display = t.status or "—"
    links = f"{_md_link(t.key)} · {_jira_link(t.key)}"
    lines.append(
        f"| {t.key} | {title_display} | {status_display} "
        f"| {date} | {links} |"
    )


def generate_index(
    wg_dir: Path,
    phase: str,  # "planned" or "prepared"
    wg_name: str,
) -> str | None:
    """Generate index.md content for a single WG directory."""
    md_files = sorted(
        f for f in wg_dir.glob("FHIR-*.md")
        if not f.stem.endswith("-genlog")
    )
    if not md_files:
        return None

    tickets: list[TicketInfo] = []
    for f in md_files:
        t = parse_ticket(f)
        if not t.is_skip:
            tickets.append(t)

    if not tickets:
        return None

    # Group by specification
    spec_groups: dict[str, list[TicketInfo]] = {}
    for t in tickets:
        spec = t.specification or "Unspecified"
        spec_groups.setdefault(spec, []).append(t)

    # Build output
    lines: list[str] = []
    phase_label = "Planned" if phase == "planned" else "Prepared"
    lines.append(f"# {wg_name} — {phase_label} Tickets\n")
    lines.append(
        f"This index lists all **{len(tickets)}** {phase.lower()} tickets for "
        f"the **{wg_name}** work group, grouped by specification"
    )
    if phase == "planned":
        lines[-1] += " and target artifact (repository).\n"
        lines.append(
            "> **Planned tickets** have approved resolutions with implementation plans. "
            "Work through them in the order shown — tickets are sorted so that "
            "prerequisites come before dependents.\n"
        )
    else:
        lines[-1] += ".\n"
        lines.append(
            "> **Prepared tickets** have been reviewed and have proposed dispositions "
            "ready for work-group consideration. They are sorted by date within each "
            "group so the oldest outstanding items are addressed first.\n"
        )

    lines.append("---\n")

    # Table of contents
    lines.append("## Table of Contents\n")
    for spec in sorted(spec_groups.keys()):
        anchor = re.sub(r"[^a-z0-9]+", "-", spec.lower()).strip("-")
        lines.append(f"- [{spec}](#{anchor})")
    lines.append("")

    lines.append("---\n")

    # Each specification group
    for spec in sorted(spec_groups.keys()):
        spec_tickets = spec_groups[spec]
        lines.append(f"## {spec}\n")
        lines.append(
            f"*{len(spec_tickets)} ticket(s) targeting the **{spec}** specification.*\n"
        )

        if phase == "planned":
            # Sub-group by artifact (repository) for planned tickets
            artifact_groups: dict[str, list[TicketInfo]] = {}
            for t in spec_tickets:
                if t.artifacts:
                    for a in t.artifacts:
                        artifact_groups.setdefault(a, []).append(t)
                else:
                    artifact_groups.setdefault("(no repository identified)", []).append(t)

            for artifact in sorted(artifact_groups.keys()):
                art_tickets = artifact_groups[artifact]
                lines.append(f"### {artifact}\n")

                if artifact == "(no repository identified)":
                    lines.append(
                        "*These tickets do not reference a specific repository. "
                        "Review each ticket to determine the target artifact.*\n"
                    )
                else:
                    gh_url = f"https://github.com/{artifact}"
                    lines.append(
                        f"*{len(art_tickets)} ticket(s) affecting "
                        f"[{artifact}]({gh_url}).*\n"
                    )

                sorted_tickets = _topo_sort(art_tickets)
                _emit_ticket_table(lines, sorted_tickets, phase)
        else:
            # For prepared tickets, no artifact sub-grouping — just sort by date
            sorted_tickets = _topo_sort(spec_tickets)
            _emit_ticket_table(lines, sorted_tickets, phase)

        lines.append("---\n")

    # Footer
    lines.append(
        f"*Generated automatically. Re-run `generate-indexes.py` to update.*\n"
    )
    return "\n".join(lines)


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    repo_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()

    generated = 0
    skipped = 0

    for phase in ("planned", "prepared"):
        phase_dir = repo_root / phase
        if not phase_dir.is_dir():
            print(f"⚠  {phase}/ directory not found — skipping")
            continue

        for wg_dir in sorted(phase_dir.iterdir()):
            if not wg_dir.is_dir():
                continue

            # Derive a human-friendly WG name from the directory name
            wg_name = re.sub(r"([a-z])([A-Z])", r"\1 \2", wg_dir.name)
            wg_name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", wg_name)

            content = generate_index(wg_dir, phase, wg_name)
            if content is None:
                skipped += 1
                continue

            index_path = wg_dir / "index.md"
            index_path.write_text(content, encoding="utf-8")
            generated += 1
            print(f"✓  {phase}/{wg_dir.name}/index.md")

    print(f"\nDone. Generated {generated} index files, skipped {skipped} empty directories.")


if __name__ == "__main__":
    main()
