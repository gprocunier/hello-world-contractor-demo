# Hello World Contractor Demo

This repository is a small, dependency-free static web project used to demonstrate the coordination of external contractor agents by an autonomous orchestration system.

---

## Key Orchestration Concepts

To navigate this repository, you should understand the primary components of our workflow:
- **Codex**: The agentic AI orchestration system (developed by Google DeepMind) that acts as the principal architect, project manager, and validator.
- **Beads (`bd`)**: A lightweight task tracking and durable state management system used by Codex to define, model, and record task execution metadata.
- **Outside Model Contractors**: Autonomous agents (specifically Google Antigravity and Claude Code) assigned to execute distinct tasks in isolation.
- **Patch Branches**: Dedicated Git branches where contractors carry out their work within strict file path boundaries (e.g., `agy/docs` or `claude/pages`), keeping the work separated from the `main` branch.

For a comprehensive breakdown of the project architecture, terminology, and lifecycle rules, see the [Project Guide](file:///home/d00d/codex/hello-world-contractor-demo-agy/docs/project-guide.md).

---

## Run Locally

Serving the files via a local server rather than opening the HTML file directly ensures proper browser protocol alignment and routing. 

Execute the following command to serve the application locally using Python's built-in HTTP server:

```bash
python3 -m http.server 8000
```

Once the server is running, navigate your web browser to:
`http://localhost:8000`

---

## Validate

Before committing code or submitting a contractor return, you must execute the validation checkpoint. The validation script parses the landing page to verify the structure, stylesheet linkages, and required content while ensuring no unresolved placeholder markers remain.

Execute the validator using:

```bash
python3 scripts/check_site.py
```

---

## Orchestration Model

This demo application is kept intentionally simple to allow easy inspection of the contractor workflow:

1. **Codex** creates and publishes the baseline project on `main`.
2. **Beads** records the task graph, dependencies, contractor packets, and return evidence.
3. **Codex PM** dispatches contractor packets to outside model contractors using commands like `agy -p` and `claude -p`.
4. **Outside Contractors** implement their assignments in isolated patch branches.
5. **Codex** evaluates the contractor returns and merges accepted patch branches into `main`.
6. **GitHub Pages** publishes the final integrated site.


