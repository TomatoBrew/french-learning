#!/bin/bash
# shitty script building the svgs, to be replaced with cmake or something else offering build targets and file types for output
if [[ ! -d $1 ]]; then
    echo "not a valid path"
    exit 1
fi

for template in $1/*.dot.j2; do
    out="$(cut -d'.' -f1 <<< $(basename "$template")).svg"
    python3 ../scripts/parse_jinja.py -d ../scripts/vars.json -t $template | dot -Tsvg > $out
done