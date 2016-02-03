import argparse
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../lib'))

import mdparser

def _help():
    print(
    """
    {} [markdown file]
    """.format(sys.argv[0]))

def main():
    argparser = argparse.ArgumentParser(description='Convert markdown to confluence html.')
    argparser.add_argument('file', type=str)
    argparser.add_argument('--user')
    argparser.add_argument('--pass')
    argparser.add_argument('--id')
    argparser.add_argument('--parent-id')

    args = argparser.parse_args()
    # print(args.accumulate(args.integers))

    html = mdparser.parse(open(args.file).read())

    print(html)

def upload(html, id=None, pid=None, user=None, password=None):
    pass


main()
