#!/usr/bin/env python3
from flask import Flask, render_template, request, send_file, make_response
from jinja2 import Environment, FileSystemLoader
import random
import os
import tempfile
from datetime import datetime
from bingo_generator import generate_bingo_numbers

app = Flask(__name__)

# Available templates
TEMPLATES = {
    'basic': 'bingo_template.html',
    'multipage': 'bingo_template_multipage.html',
    'a4': 'template_a4.html'
}

@app.route('/')
def index():
    return render_template('form.html', templates=TEMPLATES)

@app.route('/generate', methods=['POST'])
def generate_bingo():
    # Get form data
    title = request.form.get('title', 'Bingo Card')
    num_cards = int(request.form.get('numcards', 4))
    template_key = request.form.get('template', 'multipage')
    
    # Get the template filename
    template_file = TEMPLATES.get(template_key, 'bingo_template_multipage.html')
    
    # Load the template
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    template = env.get_template(template_file)
    
    metadata = {
        "rango_tarjetas": f"1 al {num_cards}",
        "fecha_produccion": datetime.now().strftime("%B %Y"),
        "rango_numeros": "1 al 90"
    }
    
    # Generate card data
    cards_data = {i+1: (title, generate_bingo_numbers()) for i in range(num_cards)}
    
    # Render the template
    rendered_html = template.render(cards=cards_data, metadata=metadata)
    
    # Create response
    response = make_response(rendered_html)
    response.headers['Content-Type'] = 'text/html'
    response.headers['Content-Disposition'] = f'attachment; filename=bingo_{datetime.now().strftime("%y%m%d")}.html'
    
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)