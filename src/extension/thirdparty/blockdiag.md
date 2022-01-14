# blockdiag

```{blockdiag}
A -> B;
```

* <https://github.com/blockdiag/sphinxcontrib-blockdiag>
    * <https://github.com/blockdiag/sphinxcontrib-blockdiag/blob/master/sphinxcontrib/blockdiag.py#L299>
* <http://blockdiag.com/ja/blockdiag/index.html>

* <https://blog.interstellar.co.jp/2018/09/sphinxblockdiag/>

`pip install sphinxcontrib-blockdiag sphinxcontrib-seqdiag sphinxcontrib-actdiag sphinxcontrib-nwdiag`

```py
extensions = [
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.seqdiag',
    'sphinxcontrib.actdiag',
    'sphinxcontrib.nwdiag',
    'sphinxcontrib.rackdiag',
    'sphinxcontrib.packetdiag'
]
blockdiag_html_image_format = "SVG"
seqdiag_html_image_format = "SVG"
actdiag_html_image_format = "SVG"
nwdiag_html_image_format = "SVG"
rackdiag_html_image_format = "SVG"
packetdiag_html_image_format = "SVG"
```

```python
def setup(app):
    app.add_node(blockdiag_node,
                 html=(html_visit_blockdiag, html_depart_blockdiag))
    app.add_directive('blockdiag', Blockdiag)
    app.add_config_value('blockdiag_fontpath', None, 'html')
    app.add_config_value('blockdiag_fontmap', None, 'html')
    app.add_config_value('blockdiag_antialias', False, 'html')
    app.add_config_value('blockdiag_transparency', True, 'html')
    app.add_config_value('blockdiag_debug', False, 'html')
    app.add_config_value('blockdiag_html_image_format', 'PNG', 'html')
    app.add_config_value('blockdiag_tex_image_format', None, 'html')  # backward compatibility for 1.3.1
    app.add_config_value('blockdiag_latex_image_format', 'PNG', 'html')
    app.connect("builder-inited", on_builder_inited)
    app.connect("doctree-resolved", on_doctree_resolved)

    return {
        'version': pkg_resources.require('blockdiag')[0].version,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
```
