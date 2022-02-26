from typing import Dict, Any, Tuple, Optional, List
from sphinx.application import Sphinx
from docutils import nodes
from docutils.nodes import Node
import sphinx
from sphinx.writers.html import HTMLTranslator
from sphinx.util.docutils import SphinxDirective, SphinxTranslator


class folium(nodes.General, nodes.Inline, nodes.Element):
    pass


def render_dot_html(self: HTMLTranslator, node: folium, code: str, options: Dict,
                    prefix: str = 'folium', imgcls: Optional[str] = None, alt: Optional[str] = None,
                    filename: Optional[str] = None) -> Tuple[str, str]:
    raise NotImplementedError()


def html_visit_folium(self: HTMLTranslator, node: folium) -> None:
    render_dot_html(
        self, node, node['code'], node['options'], filename=node.get('filename'))


class Folium(SphinxDirective):
    """
    Directive to insert arbitrary dot markup.
    """

    def run(self) -> List[Node]:
        raise NotImplementedError()


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_node(folium, html=(html_visit_folium, None))
    app.add_directive('folium', Folium)
    # app.add_css_file('graphviz.css')
    # app.connect('build-finished', on_build_finished)
    return {'version': '0.1.0', 'parallel_read_safe': True}
