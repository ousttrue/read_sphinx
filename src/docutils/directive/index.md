# directive

<https://www.sphinx-doc.org/ja/master/development/tutorials/helloworld.html>

* <https://docutils.sourceforge.io/docs/howto/rst-directives.html>

```py
class HelloWorld(Directive):
    def run(self):
        paragraph_node = nodes.paragraph(text='Hello World!')
        return [paragraph_node]
```

.. helloworld::
```{helloworld}
```

- [Sphinx ではどのようにラベルとキャプションを結びつけているのか](https://tk0miya.hatenablog.com/entry/2014/08/11/003957)

* Directive では独自ノードを作り
* visitor 関数で独自ノードを画像に変換する

しかし、キャプションをうまく扱うためには次のようなやり方をするとよいでしょう。

* Directive では figure ノード、caption ノードと画像を表す独自ノードを作る
* visitor 関数で独自ノードを画像に変換する

## `sphinx.ext.graphviz`

`sphinx/ext/graphviz.py`

```py
# setup.py

class graphviz(nodes.General, nodes.Inline, nodes.Element):
    pass

def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_node(graphviz,
                 html=(html_visit_graphviz, None), # 👈 graphviz node から html を出力する
                 latex=(latex_visit_graphviz, None),
                 texinfo=(texinfo_visit_graphviz, None),
                 text=(text_visit_graphviz, None),
                 man=(man_visit_graphviz, None))
    app.add_directive('graphviz', Graphviz) # 👈 graphviz node を作る
    app.add_directive('graph', GraphvizSimple)
    app.add_directive('digraph', GraphvizSimple)
    app.add_config_value('graphviz_dot', 'dot', 'html')
    app.add_config_value('graphviz_dot_args', [], 'html')
    app.add_config_value('graphviz_output_format', 'png', 'html')
    app.add_css_file('graphviz.css')
    app.connect('build-finished', on_build_finished) # 👈 copy css
    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}
```
