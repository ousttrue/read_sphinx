# inheritance_diagram

<https://www.sphinx-doc.org/en/master/usage/extensions/inheritance.html>

クラスの継承図。
{doc}`graphviz` に依存するのでそっちの設定もしておくこと。

conf.py

```py
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.graphviz',
    'sphinx.ext.inheritance_diagram',
]
autodoc_default_options = {
    'member-order': 'bysource',
}
```

## apidoc と連携する例

{doc}`/command/index` の template を改造する。

`sphinx-apidoc -t TEMPLATE_DIR` で指定する。

* <https://stackoverflow.com/questions/59307596/how-to-add-inheritance-diagram-to-all-modules-in-sphinx>
