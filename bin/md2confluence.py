import sys
import mistune
import argparse


def _help():
    print(
    """
    {} [markdown file]
    """.format(sys.argv[0]))

def main():
    parser = argparse.ArgumentParser(description='Convert markdown to confluence html.')
    parser.add_argument('file', type=str)
    parser.add_argument('--user')
    parser.add_argument('--pass')
    parser.add_argument('--id')
    parser.add_argument('--parent-id')
    args = parser.parse_args()
    # print(args.accumulate(args.integers))
    html = mistune.markdown(open(args.file).read())
    print(html)

def upload(html, id=None, pid=None, user=None, pass=None):
    pass

main()
