# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Environment Setup

This project uses Python with pipenv for dependency management:

```bash
# Install dependencies
pipenv install  # if Pipfile.lock exists
pipenv install -r requirements.txt  # starting from scratch

# Activate virtual environment
pipenv shell
```

## Common Commands

### Generate Bingo Cards
```bash
pipenv run python3 bingo_generator.py \
    --template ./bingo_template_multipage.html \
    --title "Bingo Life 2025" \
    --numcards 200 \
    --output "bingo_life_2025.html"
```

### Available Templates
- `bingo_template.html` - Basic single-page template
- `bingo_template_multipage.html` - Multi-page template with print formatting (recommended for large card sets)
- `template.html` - Alternative template
- `template_a4.html` - A4-specific template

## Architecture

This is a simple bingo card generator built with Python and Jinja2 templating.

### Core Components
- `bingo_generator.py` - Main generator script that creates randomized bingo cards
- HTML templates - Define the layout and styling for generated cards
- Uses Jinja2 for template rendering with card data

### Card Generation Logic
- Generates random numbers 1-90 for each card (25 numbers per card)
- Numbers are sorted by default but can be unsorted
- Each card gets a unique set of 25 numbers
- Supports bulk generation of multiple cards

### Template System
- Templates use CSS Grid for responsive card layouts
- Print-optimized styling with millimeter measurements
- Multi-page template includes page breaks for proper printing
- Cards display in 2-column grid layout per page