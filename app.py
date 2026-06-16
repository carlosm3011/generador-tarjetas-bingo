#!/usr/bin/env python3
from flask import Flask, render_template, request, make_response
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from bingo_generator import generate_bingo_numbers
from bingo_layouts import LAYOUTS, DEFAULT_LAYOUT, PAGE_SIZES, DEFAULT_PAGE_SIZE

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html',
                           layouts=LAYOUTS,
                           default_layout=DEFAULT_LAYOUT,
                           page_sizes=PAGE_SIZES,
                           default_page_size=DEFAULT_PAGE_SIZE)

@app.route('/generate', methods=['POST'])
def generate_bingo():
    title = request.form.get('title', 'Bingo Card')
    num_cards = int(request.form.get('numcards', 4))
    layout_key = request.form.get('layout', DEFAULT_LAYOUT)
    page_size_key = request.form.get('page_size', DEFAULT_PAGE_SIZE)

    layout = LAYOUTS.get(layout_key, LAYOUTS[DEFAULT_LAYOUT])
    page_size = PAGE_SIZES.get(page_size_key, PAGE_SIZES[DEFAULT_PAGE_SIZE])

    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    template = env.get_template('bingo_template.html')

    metadata = {
        "rango_tarjetas": f"1 al {num_cards}",
        "fecha_produccion": datetime.now().strftime("%B %Y"),
        "rango_numeros": "1 al 90",
    }

    cards_data = {i + 1: (title, generate_bingo_numbers()) for i in range(num_cards)}

    rendered_html = template.render(cards=cards_data, metadata=metadata, layout=layout, page_size=page_size)

    response = make_response(rendered_html)
    response.headers['Content-Type'] = 'text/html'

    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
