---
description: Workspace instructions for Soc Ops — a social bingo game for mixers and conferences
applyTo: "**"
---

# Soc Ops — Workspace Instructions

**Project:** Social Bingo game built with FastAPI, Jinja2, and HTMX  
**Status:** Active development with workshop checkpoint stages  
**Tech Stack:** Python 3.13+, FastAPI, Jinja2, HTMX, CSS (no framework)

## Project Overview

Soc Ops is a playful bingo experience designed for in-person mixers, conferences, and friendly gatherings. Players mark squares on a 5×5 board to spark conversations. The application is lightweight, runs locally, and emphasizes real human interaction over screen time.

**Key characteristics:**
- Single-page web app with shuffled boards
- Free space in center
- Instant UI feedback on mark/unmark
- Automatic bingo detection (rows, columns, diagonals)
- Multiple game modes (Bingo, Scavenger Hunt, Card Deck Draw)
- Cyberpunk Neon visual theme
- Built for quick play and local deployment

## Project Structure

```
app/
├── main.py              # FastAPI app setup, routes
├── models.py            # Data models (Game, Board, etc.)
├── game_logic.py        # Core bingo logic, board generation
├── game_service.py      # Higher-level game operations
├── data.py              # Question/prompt data for different themes
├── static/
│   ├── css/app.css      # Main stylesheet (Cyberpunk Neon theme)
│   └── js/htmx.min.js   # HTMX for dynamic interactions
└── templates/
    ├── base.html        # Base layout template
    ├── home.html        # Start screen
    └── components/
        ├── game_screen.html     # Active game view
        ├── bingo_board.html     # Board component
        ├── bingo_modal.html     # Win celebration modal
        └── start_screen.html    # Mode selection screen

tests/
├── test_api.py          # FastAPI route tests
└── test_game_logic.py   # Game logic unit tests

workshop/                # Multi-part workshop guide
├── GUIDE.md             # Full workshop instructions
├── 01-setup.md          # Part 1: Initial setup
├── 02-design.md         # Part 2: UI redesign
├── 03-quiz-master.md    # Part 3: Custom questions
└── 04-multi-agent.md    # Part 4: New features

.solutions/              # Checkpoint stages for workshop
└── step-XX-*/           # Each step with working code

pyproject.toml           # UV project config, dependencies, ruff rules
```

## Development Workflow

### Setup & Running

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **Run the application:**
   ```bash
   # Fast reload mode (default task)
   uv run uvicorn app.main:app --reload --port 8000
   ```
   Open: http://localhost:8000

3. **Run tests:**
   ```bash
   uv run pytest
   ```
   Tests should be comprehensive and test:
   - Board generation randomness
   - Bingo detection (rows, columns, diagonals)
   - Game state management
   - API responses

4. **Lint and format:**
   ```bash
   # Check for issues
   uv run ruff check .
   
   # Auto-format code
   uv run ruff format .
   ```

### Development Principles

- **Lightweight:** Minimize dependencies. No frontend framework — use vanilla CSS and HTMX.
- **Modular:** Game logic is separate from API/UI concerns.
- **Tested:** New features require unit tests before implementation (TDD approach available).
- **Accessible:** Ensure keyboard navigation and screen reader compatibility.
- **Local-first:** Designed to run on a single machine with minimal setup.

## Game Modes

The application supports multiple game modes (selectable on the start screen):

### 1. **Classic Bingo** (Original)
- 5×5 board with center free space
- Click squares to mark/unmark
- Bingo detection on rows, columns, diagonals
- Win modal celebration
- Default mode if none selected

### 2. **Scavenger Hunt** (New in step-06)
- Task/item checklist instead of board
- Checkboxes for marking completion
- Progress meter showing % complete
- Designed for finding people/activities at events
- Example: "Find someone with a tattoo," "Find a vegan"

### 3. **Card Deck Shuffle** (New in step-07)
- Single card draw interface
- Swipe left/right for Fail/Success feedback
- Card flip animations
- Quick rapid-fire interaction mode
- Visual feedback on interactions

**Note:** Game mode selection happens on the start screen. The `models.py` defines `GameMode` enum; routes in `main.py` initialize games accordingly.

## Theme & Styling

The project uses a **Cyberpunk Neon theme** with:
- **Color palette:** Cyan (#00FF41), Magenta (#FF10F0), Purple (#BF00FF), Dark background (#0a0e27)
- **Typography:** Futuristic, bold fonts
- **Effects:** Glowing text, animations, grid patterns
- **Accessibility:** High contrast for readability

**CSS Guidelines:**
- Use CSS variables defined at the top of `app.css` for colors
- No Tailwind or utility frameworks — plain CSS only
- Media queries for responsive design
- Animations use CSS keyframes (no JS animations in templates)

See [css-utilities.instructions.md](.github/instructions/css-utilities.instructions.md) for specific class patterns.

## Design Guide

### Design Principles

**Avoid "AI slop" aesthetics.** Create distinctive, intentional frontends that surprise and delight:
- **Typography:** Choose beautiful, unique fonts. Avoid generic choices (Arial, Inter, Roboto). Commit to fonts that elevate the aesthetic.
- **Color & Theme:** Use a cohesive, intentional color palette. Dominant colors with sharp accents outperform timid, even distributions. Draw from cultural/thematic inspiration.
- **Motion:** Use CSS-only animations for Jinja2 templates. Focus on high-impact moments — one well-orchestrated page load with staggered reveals (via `animation-delay`) beats scattered micro-interactions.
- **Backgrounds:** Create atmosphere and depth with layers. Use CSS gradients, geometric patterns, or contextual effects that match the aesthetic.
- **Implementation:** Match code complexity to the aesthetic vision. Maximalist designs need elaborate animations; minimalist designs need restraint and precision.

**Avoid:**
- Overused font families (Inter, Roboto, Arial, system fonts)
- Clichéd color schemes (e.g., purple gradients on white)
- Predictable layouts and cookie-cutter component patterns
- Designs lacking context-specific character

### CSS Utility Classes

The project provides custom CSS utilities (defined in `app/static/css/app.css`):

**Layout:**
```css
.flex, .flex-col, .flex-1
.grid, .grid-cols-5
.items-center, .justify-center, .justify-between
```

**Spacing:**
```css
.p-1, .p-3, .p-4, .p-6
.px-3, .px-4, .px-6, .px-8
.py-1\.5, .py-2, .py-3, .py-4
.mb-2, .mb-3, .mb-4, .mb-6, .mb-8, .mx-auto
.gap-1, .space-y-2
```

**Sizing:**
```css
.h-full, .w-full, .w-16, .min-h-full
.max-w-xs, .max-w-sm, .max-w-md
.aspect-square, .min-h-[60px]
```

**Colors (Cyberpunk Neon Theme):**
```css
/* CSS Variables in :root */
--color-cyan: #00FF41
--color-magenta: #FF10F0
--color-purple: #BF00FF
--color-dark-bg: #0a0e27

/* Utility classes */
.bg-dark, .text-cyan, .text-magenta, .text-purple
.glow (neon glow effect)
```

**Typography:**
```css
.text-xs, .text-sm, .text-lg, .text-3xl, .text-4xl, .text-5xl
.font-semibold, .font-bold
.text-center, .text-left
.leading-tight
```

**Borders & Shadows:**
```css
.border, .border-b
.rounded, .rounded-lg, .rounded-xl
.shadow-sm, .shadow-xl
.neon-border (glowing border)
```

**Animation:**
```css
.transition-all, .transition-colors
.duration-150
.animate-pulse, .animate-glow
```

### Component Design Patterns

**Start Screen:**
- Large, bold typography announcing the game
- Clear mode selection buttons with distinct visual states
- Cyberpunk aesthetic with neon accents and dark background

**Game Board:**
- 5×5 grid layout using `.grid-cols-5`
- Each square is clickable with mark/unmark feedback
- Center square is free space (visually distinct)
- Smooth transitions when marking/unmarking

**Game Controls:**
- Clear, accessible buttons with sufficient padding
- Hover states with color or glow changes
- Loading states for async operations

**Win Modal:**
- Full-screen overlay (`.fixed .inset-0 .z-50`)
- Celebration message with animations
- Prominent "Play Again" button

### Best Practices for This Project

1. **Use CSS variables for flexibility:** Define colors, spacing, and effects at `:root`
2. **Favor CSS-only animations:** Use `@keyframes` and `animation-delay` for staggered effects
3. **Compose utilities:** Combine multiple classes for complex layouts
4. **Keep specificity low:** Utility classes are single-purpose
5. **Test responsiveness:** Use media queries for mobile-first design
6. **Accessibility first:** High contrast, keyboard navigation, semantic HTML

### Cyberpunk Neon Theme Specifics

The Cyberpunk Neon aesthetic emphasizes:
- **Glowing effects:** Text shadows, box shadows with neon colors
- **Bold typography:** Futuristic, impactful fonts
- **High contrast:** Light text on dark backgrounds for readability
- **Grid & pattern backgrounds:** Geometric layers for atmosphere
- **Animations:** Smooth, fluid motion; avoid jarring transitions
- **Dark palette:** `#0a0e27` background with bright accents

When designing new components, commit fully to this aesthetic. Bold choices (unexpected font choices, unique color combinations) create more engaging experiences than timid, generic designs.

## Code Standards

### Python
- **Style:** PEP 8 via Ruff (configured in `pyproject.toml`)
- **Type hints:** Required for function parameters and returns
- **Naming:** 
  - Functions/variables: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_CASE`
- **Linting:** No unused imports, unused variables, or missing type hints

### Templates (Jinja2)
- Use `/components/` folder for reusable template partials
- `base.html` provides layout wrapper
- HTMX attributes for interactive elements (`hx-post`, `hx-get`, `hx-trigger`, etc.)
- Template names describe their purpose: `game_screen.html`, `bingo_board.html`

### Commits & PRs
- Descriptive commit messages: "Add scavenger hunt game mode" not "update code"
- Small, focused PRs (one feature per PR)
- Reference workshop steps or issue numbers when applicable

## Testing Approach

### Unit Tests
Located in `tests/test_game_logic.py`:
- Board generation correctness
- Bingo check logic (all row/column/diagonal combinations)
- Mark/unmark state changes

### Integration Tests
Located in `tests/test_api.py`:
- API endpoint responses
- Game initialization with different modes
- Board serialization

### Test Convention
- Test file names: `test_*.py`
- Test function names: `test_<feature>_<scenario>`
- Fixtures for common setup (boards, game states)
- Use `pytest` with verbose output

**Before submitting code:**
```bash
uv run pytest -v          # Run all tests with output
uv run ruff check .       # Check linting
uv run ruff format .      # Auto-format
```

## Common Development Tasks

### Adding a New Question Theme
1. Add questions to `app/data.py` in the appropriate category
2. Update `models.py` if adding a new `QuestionTheme` enum variant
3. Update `game_service.py` to load the new theme
4. Test with `uv run pytest`

### Updating the UI Theme
1. Modify color variables in `app/static/css/app.css`
2. Update background images or patterns in base template
3. Adjust animations/transitions in component files
4. Test locally: `uv run uvicorn app.main:app --reload`

### Adding a New Game Mode
1. Create tests first (TDD approach) in `tests/test_game_logic.py`
2. Add `GameMode` enum variant in `models.py`
3. Implement game logic in `game_logic.py`
4. Add API route in `main.py` for mode initialization
5. Create template component in `templates/components/`
6. Update start screen to show new mode option
7. Run full test suite before committing

### Creating a Checkpoint
Each workshop step has a corresponding `.solutions/step-XX-*` folder. When creating a new checkpoint:
```bash
# Copy current working app to solutions folder
cp -r app .solutions/step-08-description/app/
cp pyproject.toml .solutions/step-08-description/
# Update .solutions/README.md with new step description
```

## Workshop Reference

The `workshop/` folder contains a multi-part workshop guide:
- **Part 1 (01-setup.md):** Workspace setup, linting, README
- **Part 2 (02-design.md):** UI redesign (Cyberpunk theme)
- **Part 3 (03-quiz-master.md):** Custom question themes
- **Part 4 (04-multi-agent.md):** New game modes
- **Finished:** All features combined

See [GUIDE.md](../../workshop/GUIDE.md) for complete step-by-step instructions.

## Helpful AI Agent Modes

When using VS Code Copilot for development:

- **TDD Red/Green/Refactor:** Use when implementing new features with tests first
- **Pixel Jam:** Use when redesigning UI/styling
- **Quiz Master:** Use when creating new question themes
- **Explore:** Use for codebase navigation and understanding
- **python-dev-custom-mode:** Use for general Python development

## Quick Reference

| Task | Command |
|------|---------|
| Start app | `uv run uvicorn app.main:app --reload` |
| Run tests | `uv run pytest -v` |
| Format code | `uv run ruff format .` |
| Check linting | `uv run ruff check .` |
| Sync deps | `uv sync` |
| View docs | Open `/docs/` folder or visit live demo |

## Resources

- **Live Demo:** https://madebygps.github.io/vscode-github-copilot-agent-lab/
- **Workshop Guide:** `workshop/GUIDE.md`
- **Contributing:** See `CONTRIBUTING.md`
- **License:** See `LICENSE` file
- **Dev Container:** `.devcontainer/` for opinionated setup

---

**Remember:** Soc Ops is designed for human connection. Keep the experience lightweight, fun, and conversation-focused. Every feature should enhance the in-person interaction, not distract from it.
