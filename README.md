# Bingo Card Generator

Generates randomized bingo cards (numbers 1–90, 25 per card) as print-ready HTML files. Used for live "Bingo Life" events in 2023, 2024, and 2025. Originally developed in 2025 with Claude (Anthropic).

## Quick Start

### Instalar dependencias

```
uv sync
```

### Ejecutar la generación (CLI)

```
uv run python3 bingo_generator.py \
      --template ./bingo_template_multipage.html \
      --title "Bingo Life 2026" \
      --numcards 200 \
      --layout 2x2 \
      --output "bingo_life_2026.html"
```

Layouts disponibles: `2x2` (4 cards/page, default), `3x2` (6 cards/page), `3x3` (9 cards/page).

### Ejecutar el GUI (Flask web app)

```
uv run python3 app.py
# Abre http://localhost:5001
```

### Simulación Monte Carlo

Estima cuántas bolas se necesitan sacar hasta que alguien gane:

```
uv run python3 bingo_simulation.py --nmax 90 --cmax 200 --simulations 10000
```

## Components

| File | Purpose |
|------|---------|
| `bingo_generator.py` | CLI card generator |
| `app.py` | Flask web UI (port 5001) |
| `bingo_simulation.py` | Monte Carlo win estimator |
| `bingo_template_multipage.html` | Recommended print template (4 cards/page) |
| `template_a4.html` | A4 format template |

## Event History

| Year | Event | Cards |
|------|-------|-------|
| 2023 | Bingo Life | — |
| 2024 | Bingo Life | — |
| 2025 | Bingo Life | 200 (see `200 Tarjetas Bingo Life A4 v2.pdf`) |
