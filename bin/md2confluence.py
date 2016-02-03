import argparse
import mistune
import re
import sys
import textwrap


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

    html = mistune.markdown(open(args.file).read(), renderer=ConfluenceRenderer())

    print(html)


def upload(html, id=None, pid=None, user=None, password=None):
    pass


class ConfluenceRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        return textwrap.dedent('''\
            <ac:structured-macro ac:name="code" ac:schema-version="1">
                <ac:parameter ac:name="language">{l}</ac:parameter>
                <ac:plain-text-body><![CDATA[{c}]]></ac:plain-text-body>
            </ac:structured-macro>
        ''').format(c=code, l=lang or '')

    def linebreak(self):
        return '<br />\n'


main()
