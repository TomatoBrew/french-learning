#!/usb/bin/env python3
import json
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
    return parser.parse_args()



if __name__ == '__main__':
    args = parse_args()
    data = get_data("./vars.json")
    data = data | get_data(args.data)
    template = Template(get_template(args.template))
    temp = template.render(data)
    print(args.data)

    #s = Source(source=temp, filename="file1234HAHA")
    #s.render(directory=args.output, format='jpg')