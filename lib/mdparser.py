import textwrap
import mistune

def parse(markdown):
    return mistune.markdown(markdown, renderer=ConfluenceRenderer())


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
