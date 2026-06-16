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
from bingo_layouts import LAYOUTS, DEFAULT_LAYOUT, PAGE_SIZES, DEFAULT_PAGE_SIZE, MAX_NUMBERS, DEFAULT_MAX_NUMBER, VERSION
random.seed()

def generate_bingo_numbers(_sort=True, maxnum=DEFAULT_MAX_NUMBER):
    sample = random.sample(range(1, maxnum + 1), 25)
    if _sort:
        return sorted(sample)
    else:
        return sample


def main(args):
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    template = env.get_template('bingo_template.html')

    layout = LAYOUTS[args.layout]
    page_size = PAGE_SIZES[args.page_size]

    metadata = {
        "rango_tarjetas": f"1 al {args.numcards}",
        "fecha_produccion": datetime.now().strftime("%B %Y"),
        "rango_numeros": f"1 al {args.maxnum}",
    }

    cards_data = {i + 1: (args.title, generate_bingo_numbers(maxnum=args.maxnum)) for i in range(args.numcards)}

    rendered_html = template.render(cards=cards_data, metadata=metadata, layout=layout, page_size=page_size)

    with open(args.output, "w") as file:
        file.write(rendered_html)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Bingo Cards.')
    parser.add_argument('--version', action='version', version=f'bingo-generator {VERSION}')
    parser.add_argument('--title', default='Bingo Card', help='Title of the bingo cards.')
    parser.add_argument('--numcards', type=int, default=4, help='Number of bingo cards to generate.')
    parser.add_argument('--layout', default=DEFAULT_LAYOUT, choices=list(LAYOUTS.keys()),
                        help='Grid layout: 2x2 (default), 3x2, or 3x3.')
    parser.add_argument('--page-size', default=DEFAULT_PAGE_SIZE, choices=list(PAGE_SIZES.keys()),
                        dest='page_size', help='Paper size: a4 (default) or letter.')
    parser.add_argument('--maxnum', type=int, default=DEFAULT_MAX_NUMBER, choices=list(MAX_NUMBERS.keys()),
                        help='Highest number on cards: 90 (default) or 75.')

    default_output = "bingo_" + datetime.now().strftime('%y%m%d') + ".html"
    parser.add_argument('--output', default=default_output, help='Output file name.')

    args = parser.parse_args()
    main(args)

    print("Bingo generado exitosamente")
