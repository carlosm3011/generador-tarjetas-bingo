#!/usr/bin/env python3
from flask import Flask, render_template, request, make_response
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from bingo_generator import generate_bingo_numbers
from bingo_layouts import LAYOUTS, DEFAULT_LAYOUT, PAGE_SIZES, DEFAULT_PAGE_SIZE, MAX_NUMBERS, DEFAULT_MAX_NUMBER, VERSION

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html',
                           layouts=LAYOUTS,
                           default_layout=DEFAULT_LAYOUT,
                           page_sizes=PAGE_SIZES,
                           default_page_size=DEFAULT_PAGE_SIZE,
                           max_numbers=MAX_NUMBERS,
                           default_max_number=DEFAULT_MAX_NUMBER,
                           version=VERSION)

@app.route('/generate/<layout>/<page_size>/<int:numcards>/<int:maxnum>', methods=['GET'])
def generate_bingo(layout, page_size, numcards, maxnum):
    if layout not in LAYOUTS:
        return f"Invalid layout '{layout}'. Valid options: {', '.join(LAYOUTS)}", 400
    if page_size not in PAGE_SIZES:
        return f"Invalid page size '{page_size}'. Valid options: {', '.join(PAGE_SIZES)}", 400
    if not (1 <= numcards <= 1000):
        return "numcards must be between 1 and 1000", 400
    if maxnum not in MAX_NUMBERS:
        return f"Invalid maxnum '{maxnum}'. Valid options: {', '.join(str(k) for k in MAX_NUMBERS)}", 400

    title = request.args.get('title', 'Bingo Card')
    download = request.args.get('download', 'false').lower() == 'true'

    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    template = env.get_template('bingo_template.html')

    metadata = {
        "rango_tarjetas": f"1 al {numcards}",
        "fecha_produccion": datetime.now().strftime("%B %Y"),
        "rango_numeros": f"1 al {maxnum}",
    }

    cards_data = {i + 1: (title, generate_bingo_numbers(maxnum=maxnum)) for i in range(numcards)}

    rendered_html = template.render(
        cards=cards_data,
        metadata=metadata,
        layout=LAYOUTS[layout],
        page_size=PAGE_SIZES[page_size],
    )

    response = make_response(rendered_html)
    response.headers['Content-Type'] = 'text/html'

    if download:
        filename = f'bingo_{datetime.now().strftime("%y%m%d")}.html'
        response.headers['Content-Disposition'] = f'attachment; filename={filename}'

    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
