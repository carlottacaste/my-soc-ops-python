# Soc Ops — Social Bingo for Real People

Welcome to Soc Ops, a playful Social Bingo experience built for in-person mixers, conferences, and friendly meetups. Spark conversations, break the ice, and celebrate the small wins: first to five in a row wins!

Why it’s fun
- Quick to play: a single page web app with a shuffled 5x5 bingo board.
- Designed for conversation: prompts encourage real human interaction, not just screen time.
- Lightweight: runs locally with minimal dependencies — ideal for demos and workshops.

Live demo & docs
- Play the live demo: https://madebygps.github.io/vscode-github-copilot-agent-lab/
- Workshop and design guide: see the `workshop/` folder or the docs link above.

Features
- Shuffled boards with a FREE SPACE center
- Mark/unmark squares with instant UI feedback
- Bingo detection (rows, columns, diagonals)
- Test coverage and linting preconfigured for development

Quick start
1. Install: Python 3.13+ is required.
2. Sync dependencies: `uv sync` (uses the provided uv project manager)
3. Run locally: `uv run uvicorn app.main:app --reload`
4. Open: http://localhost:8000

Development
- Tests: `uv run pytest`
- Lint & format: `uv run ruff check .` and `uv run ruff format .`
- A devcontainer is included at `.devcontainer/` for an opinionated developer experience.

Contributing
Contributions, bug reports, and ideas are very welcome. Please read CONTRIBUTING.md for guidelines and opening a PR.

License
This project is open source under the terms of the included LICENSE file.

Thanks for checking out Soc Ops — go find someone who loves karaoke and mark that square!
