# Hello World Contractor Demo

This repository is a small, dependency-free static web project used to
demonstrate Codex-led coordination of external contractor agents.

## Key Orchestration Concepts

To navigate this repository, you should understand the primary components of our workflow:
- **Codex**: the AI coding agent acting as architect, project manager, validator, and final integrator.
- **Beads (`bd`)**: a lightweight task tracking and durable state system used to model dependencies and record contractor evidence.
- **Outside model contractors**: external model tools, in this demo Google Antigravity and Claude Code, assigned to execute distinct tasks in isolation.
- **Patch branches**: dedicated Git branches where contractors carry out their work within strict file path boundaries, such as `agy/docs` or `claude/pages`.

For a deeper breakdown of the project architecture, terminology, and lifecycle
rules, see the [Project Guide](docs/project-guide.md).

Published Pages site:
<https://gprocunier.github.io/hello-world-contractor-demo/>

## Run Locally

Serving the files via a local server rather than opening the HTML file directly
keeps browser behavior close to the published GitHub Pages path.

Execute the following command to serve the application locally using Python's built-in HTTP server:

```bash
python3 -m http.server 8000
```

Once the server is running, open `http://localhost:8000`.

## Validate

Before committing code or submitting a contractor return, run the validation
checkpoint. The script parses the root landing page and the Pages entry point to
verify structure, stylesheet links, required content, and unresolved work
markers.

Execute the validator using:

```bash
python3 scripts/check_site.py
```

## Orchestration Model

This demo application is kept intentionally simple to allow easy inspection of the contractor workflow:

1. **Codex** creates and publishes the baseline project on `main`.
2. **Beads** records the task graph, dependencies, contractor packets, and return evidence.
3. **Codex PM** dispatches contractor packets to outside model contractors using commands like `agy -p` and `claude -p`.
4. **Outside Contractors** implement their assignments in isolated patch branches.
5. **Codex** evaluates the contractor returns and merges accepted patch branches into `main`.
6. **GitHub Pages** publishes the final integrated site.
