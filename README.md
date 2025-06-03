# Bingo Card Generator

## Quick Start

### Crear el virtual environment

```
pipenv install # si ya esta el pipfile.lock
pipenv install -r requirements.txt # si estamos empezando de cero
```

### Ejecutar la generación

```
 pipenv run python3 bingo_generator.py \
       --template ./bingo_template_multipage.html \
       --title "Bingo Life 2025" \
       --numcards 200 \
       --output "bingo_life_2025.html"
```

### Ejecutar el gui

```
pipenv run python3 app.py
```
