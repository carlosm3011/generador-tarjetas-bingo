# Bingo Card Generator

Generates randomized bingo cards (numbers 1–90, 25 per card) as print-ready HTML files. Used for live "Bingo Life" events in 2023, 2024, and 2025. Originally developed in 2025 with Claude (Anthropic).

## Quick Start

```bash
uv sync
```

### CLI

```bash
uv run python3 bingo_generator.py \
      --title "Bingo Life 2026" \
      --numcards 200 \
      --layout 2x2 \
      --page-size a4 \
      --output "bingo_life_2026.html"
```

### Web UI

```bash
uv run python3 app.py
# Opens at http://localhost:5001
```

The web UI lets you fill in the options and either open the result in a new tab or download it.

### Monte Carlo Simulation

Estimates how many draws until the first card wins:

```bash
uv run python3 bingo_simulation.py --nmax 90 --cmax 200 --simulations 10000
```

## Options

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `--layout` | `2x2`, `3x2`, `3x3` | `2x2` | Cards per page (rows × cols): 4, 6, or 9 |
| `--page-size` | `a4`, `letter` | `a4` | Paper size |
| `--numcards` | 1–1000 | 4 | Number of cards to generate |
| `--title` | string | `Bingo Card` | Title printed on each card |
| `--output` | filename | `bingo_YYMMDD.html` | Output file |

## Components

| File | Purpose |
|------|---------|
| `bingo_generator.py` | CLI card generator |
| `bingo_layouts.py` | Layout and page size definitions |
| `app.py` | Flask web UI (port 5001) |
| `bingo_simulation.py` | Monte Carlo win estimator |
| `bingo_template.html` | Single Jinja2 template (handles all layouts) |

## Event History

| Year | Event | Cards |
|------|-------|-------|
| 2023 | Bingo Life | — |
| 2024 | Bingo Life | — |
| 2025 | Bingo Life | 200 (see `200 Tarjetas Bingo Life A4 v2.pdf`) |
