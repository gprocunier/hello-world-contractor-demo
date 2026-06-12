# Hello World Contractor Demo

This repository is a small static web project used to demonstrate a Codex-led
external contractor workflow.

Codex owns the architecture, project management, validation, and final merge
decisions. Outside model contractors receive bounded Beads assignments and work
on patch branches:

- Google Antigravity documents the project on `agy/docs`.
- Claude Code creates the GitHub Pages site on `claude/pages`.

## Run Locally

Open `index.html` in a browser, or serve the directory with Python:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Validate

```bash
python3 scripts/check_site.py
```

The validation script checks that the static page has the expected title,
stylesheet link, primary content, and no unresolved contractor placeholders.

## Orchestration Model

This demo intentionally keeps the application simple so the workflow is easy to
inspect:

1. Codex creates and publishes the baseline project.
2. Beads records the work graph, dependencies, contractor packets, and return
   evidence.
3. Codex PM dispatches contractor packets with `agy -p` and `claude -p`.
4. Codex evaluates contractor returns and merges only accepted patch branches.
5. GitHub Pages publishes the final documentation site.

