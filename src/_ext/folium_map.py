from typing import Dict, Any, Tuple, Optional, List
from sphinx.application import Sphinx
from docutils import nodes
from docutils.nodes import Node
from docutils.parsers.rst import Directive, directives
import sphinx
from sphinx.writers.html import HTMLTranslator
from sphinx.util.docutils import SphinxDirective, SphinxTranslator
from sphinx.util.typing import OptionSpec
from sphinx.util.nodes import set_source_info


class folium(nodes.General, nodes.Inline, nodes.Element):
    pass


def render_dot_html(self: HTMLTranslator, node: folium, code: str, options: Dict,
                    prefix: str = 'folium', imgcls: Optional[str] = None, alt: Optional[str] = None,
                    filename: Optional[str] = None) -> Tuple[str, str]:
    raise NotImplementedError()


def html_visit_folium(self: HTMLTranslator, node: folium) -> None:
    render_dot_html(
        self, node, '', node['options'], filename=node.get('filename'))


def figure_wrapper(directive: Directive, node: folium, caption: str) -> nodes.figure:
    figure_node = nodes.figure('', node)
    if 'align' in node:
        figure_node['align'] = node.attributes.pop('align')

    inodes, messages = directive.state.inline_text(caption, directive.lineno)
    caption_node = nodes.caption(caption, '', *inodes)
    caption_node.extend(messages)
    set_source_info(directive, caption_node)
    figure_node += caption_node
    return figure_node


def float2(argument):
    return [float(n) for n in argument.split(',')]


class Folium(SphinxDirective):
    """
    Directive to insert arbitrary dot markup.
    """
    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec: OptionSpec = {
        'location': float2,
        'caption': directives.unchanged,
    }

    def run(self) -> List[Node]:
        node = folium()
        node['options'] = {'docname': self.env.docname}
        node['location'] = self.options['location']
        if 'caption' not in self.options:
            self.add_name(node)
            return [node]
        else:
            figure = figure_wrapper(self, node, self.options['caption'])
            self.add_name(figure)
            return [figure]


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_node(folium, html=(html_visit_folium, None))
    app.add_directive('folium', Folium)
    # app.add_css_file('graphviz.css')
    # app.connect('build-finished', on_build_finished)
    return {'version': '0.1.0', 'parallel_read_safe': True}
