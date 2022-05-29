#!/usb/bin/env python3
import json
import os
from graphviz import Source
from argparse import ArgumentParser
from jinja2 import Template


def get_data(datafile):
    with open(datafile, 'r') as fh:
        data = json.load(fh)
        return data

def get_template(templatefile):
    with open(templatefile, 'r') as fh:
        template = fh.read()
        return template

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-d", "--data", dest="data",
        help="json file containing the variables", required=True)
    parser.add_argument("-t", "--template", dest="template",
        help="template file to be parsed", required=True)
    parser.add_argument("-o", "--output", dest="output",
        help="location to write the result to default=./graphs", default="./graphs")
    parser.add_argument("-c", "--clean", dest="clean",
        help="cleanup generated dot file after graph creation", default=True)
    parser.add_argument("-f", "--format", dest="format",
        help="output format of graphs", default="jpg")
    return parser.parse_args()



if __name__ == '__main__':
    args = parse_args()
    var_file = os.path.dirname(os.path.realpath(__file__)) + "/vars.json"
    data = get_data(var_file)
    data = data | get_data(args.data)

    template = Template(get_template(args.template))
    temp = template.render(data)

    fname = os.path.splitext(os.path.basename(args.data))[0]

    s = Source(source=temp, filename=fname)
    s.render(directory=args.output, cleanup=args.clean, format=args.format)