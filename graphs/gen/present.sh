#!/bin/bash
python3 ../scripts/parse_jinja.py -d ../scripts/vars.json -t ../le_present.dot.j2 | dot -Tsvg > present.svg