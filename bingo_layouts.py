#!/usr/bin/env python3
# All measurements in mm, calculated for A4 (180mm x 267mm usable area after 15mm body padding).

LAYOUTS = {
    '2x2': {
        'cols': 2, 'rows': 2,
        'card_gap': 10, 'card_padding': 5,
        'cell_gap': 2, 'cell_size': 13,
        'cell_font': 8, 'title_font': 9,
    },
    '3x2': {
        'cols': 3, 'rows': 2,
        'card_gap': 6, 'card_padding': 3,
        'cell_gap': 1, 'cell_size': 9,
        'cell_font': 5, 'title_font': 6,
    },
    '3x3': {
        'cols': 3, 'rows': 3,
        'card_gap': 6, 'card_padding': 3,
        'cell_gap': 1, 'cell_size': 9,
        'cell_font': 5, 'title_font': 5,
    },
}

DEFAULT_LAYOUT = '2x2'
