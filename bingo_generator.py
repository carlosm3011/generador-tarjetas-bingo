#!/usr/bin/env python3
##########################################
# Generador de tarjetas de Bingo
# (c) Carlos M. Martinez
# carlos@xt6.us
# 20230811
##########################################


from jinja2 import Environment, FileSystemLoader
import random
import argparse
from datetime import datetime
random.seed()

## def
def generate_bingo_numbers(_sort = True):
    sample = random.sample(range(1,91), 25) # 91 is exclusive, so the range is 1-90
    if _sort:
        return sorted(sample)
    else:
        return sample
## end


def main(args):
    # Load the template from file
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    template = env.get_template(args.template)

    metadata = {
        "rango_tarjetas": "1 al 4",
        "fecha_produccion": "junio 2025",
        "rango_numeros": "1 al 90"
    }

    # Generate card data
    # cards_data = {}

    # Generate card data
    cards_data = {i+1: (args.title, generate_bingo_numbers()) for i in range(args.numcards)}

    rendered_html = template.render(cards=cards_data, metadata=metadata)

    # Write the rendered HTML to an output file
    with open(args.output, "w") as file:
        file.write(rendered_html)
## end def main


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Bingo Cards.')
    parser.add_argument('--template', default='bingo_template.html', help='Template file name.')
    parser.add_argument('--title', default='Bingo Card', help='Title of the bingo cards.')
    parser.add_argument('--numcards', type=int, default=4, help='Number of bingo cards to generate.')
    
    # Formatting current date to YYMMDD format
    default_output = "bingo_" + datetime.now().strftime('%y%m%d') + ".html"
    parser.add_argument('--output', default=default_output, help='Output file name.')
    
    args = parser.parse_args()
    main(args)
    
    print("Bingo generado existosamente")
## end if
