---
name: generate-indexes
description: >
  Regenerate index.md files for all work-group directories under planned/ and
  prepared/. Each index lists tickets grouped by specification and artifact
  (repository), sorted by date and dependency order, with summaries for each
  grouping and dependency explanations.
---

# Generate WG Index Files

Run the `generate-indexes.py` script from the repository root to regenerate all
`index.md` files under `planned/` and `prepared/`.

## Steps

1. Run the generator:
   ```
   python generate-indexes.py
   ```
2. The script will scan every work-group directory, parse ticket metadata from
   each `FHIR-*.md` file, and write an `index.md` per non-empty directory.
3. Review the output — it prints which files were generated and how many were
   skipped (empty directories).

## What the index files contain

- **Planned indexes** group tickets by **Specification → Artifact (repository)**
  and sort by date with dependency ordering (prerequisites first).
- **Prepared indexes** group tickets by **Specification** and sort by date
  (oldest first).
- Dependency groups show which tickets must be completed before others, with
  explanatory summaries.

## When to run

Run this skill whenever:
- New ticket files are added to planned/ or prepared/
- Ticket metadata changes (title, spec, status, dependencies)
- Work-group directories are added or reorganized
