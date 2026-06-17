# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Background

Bingo card generator used for live "Bingo Life" events (2023, 2024, 2025). Originally developed by Carlos Martinez in 2025 with assistance from Claude (Anthropic). Numbers range 1–90, 25 per card — standard Spanish/Latin American bingo format.

## Development Environment Setup

This project uses Python with uv for dependency management:

```bash
uv sync
```

## Common Commands

### Generate Bingo Cards (CLI)
```bash
uv run python3 bingo_generator.py \
    --title "Bingo Life 2026" \
    --numcards 200 \
    --layout 2x2 \
    --page-size a4 \
    --maxnum 90 \
    --output "bingo_life_2026.html"
```

### Run the Web UI
```bash
uv run python3 app.py
# Opens at http://localhost:5001
```

### Run Monte Carlo Simulation
```bash
uv run python3 bingo_simulation.py --nmax 90 --cmax 200 --simulations 10000
# Use --kmax to simulate cards with fewer numbers (must be ≤ nmax)
uv run python3 bingo_simulation.py --nmax 90 --kmax 16 --cmax 200
```

## Architecture

Single-template bingo card generator built with Python, Jinja2, and Flask.

### Core Components
- `bingo_generator.py` — CLI script; renders `bingo_template.html` with card data
- `bingo_layouts.py` — single source of truth for layout specs (`LAYOUTS`, `PAGE_SIZES`)
- `app.py` — Flask web UI on port 5001; exposes layout/page-size options and returns rendered HTML
- `bingo_template.html` — the one Jinja2 template; handles all layouts and page sizes
- `bingo_simulation.py` — standalone Monte Carlo simulator (uses `typer`)

### Layout System (`bingo_layouts.py`)
Layouts are defined as `rows × cols` (e.g. `3x2` = 3 rows, 2 columns = 6 cards/page).
All measurements are in mm, pre-calculated for A4/Letter so nothing is left to the browser.

| Layout | Cols | Rows | Cards/page | Cell size |
|--------|------|------|-----------|-----------|
| `2x2`  | 2    | 2    | 4         | 13mm      |
| `3x2`  | 2    | 3    | 6         | 10mm      |
| `3x3`  | 3    | 3    | 9         | 9mm       |

### Template System
- Single template: `bingo_template.html`
- `@page { size: ...; margin: 15mm }` declares paper size and printer margins
- Body padding (15mm) is stripped on print via `@media print` to avoid doubling the margin
- Cards group into pages via a Jinja loop using `layout.cols * layout.rows`
- `page-break-after: always` on each group; last group uses `auto` to avoid a blank final page
- Number grid is centered in the card box via `justify-content: center` / `align-content: center`

### Web UI
- `templates/form.html` — form with title, card count, layout, and page size selectors
- Two `type="button"` buttons; JS builds the REST URL and either calls `window.open(..., '_blank')` or `window.location.href`
- No form submission; JS is scoped to the form page and has no effect on the generated output

### REST API
```
GET /generate/<layout>/<page_size>/<numcards>/<maxnum>?title=...&download=true
```
- Path params validated against `LAYOUTS` / `PAGE_SIZES` / `MAX_NUMBERS`; `numcards` must be 1–1000
- `download=true` adds `Content-Disposition: attachment`; omitting it renders inline
