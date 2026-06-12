# Repository Guidelines

This repository is a public demonstration of Codex-managed external contractor
work. Keep the app intentionally small and dependency-free so the orchestration
story remains easy to inspect.

## Work Tracking

Use Beads (`bd`) for durable task state. Contractor-only beads with
`contractor-only`, `local-worker-only`, or `no-codex-exec` labels are not normal
Codex pickup work. Codex may coordinate, dispatch, review, and merge contractor
work, but must not impersonate the assigned contractor.

Do not commit raw contractor packets, contractor returns, local Beads databases,
or orchestration audit files.

## Branches

- `main`: Codex-owned integration branch.
- `agy/docs`: Google Antigravity documentation contractor branch.
- `claude/pages`: Claude Code GitHub Pages contractor branch.

Contractors must not commit directly to `main`.

## Validation

Run this before handoff, merge, or publish:

```bash
python3 scripts/check_site.py
```

Before any formal GitHub publication step, also check that the worktree contains
no local paths, secrets, raw packet files, or transient orchestration artifacts.

