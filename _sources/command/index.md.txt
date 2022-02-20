# Command

## builtin
### sphinx-quickstart

ひな型になる conf.py の生成など。

index.rst
```rst
.. tmp documentation master file, created by
   sphinx-quickstart on Sat Feb 19 18:06:59 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to tmp's documentation!
===============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

> Sphinxはいくつかのドキュメント名を、自分で使用するために予約済み

<https://www.sphinx-doc.org/ja/master/usage/restructuredtext/directives.html?highlight=modindex#special-names>

* genindex

> index ディレクティブ

* modindex

autodoc の一覧を表示。
> モジュールインデックスには rst:dir:module ディレクティブで指定されたエントリーが含まれます

* search

conf.py
```py
project = 'tmp'
copyright = '2022, me'
author = 'me'
extensions = [
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'alabaster'
html_static_path = ['_static']
```

### sphinx-build

html の生成など

### sphinx-apidoc

{doc}`/extension/builtin/autodoc` の記事を自動生成するコマンド。
`python` のソースからAPIドキュメントになる `rst` を生成する。

例

`sphinx-autodoc -o docs/autodoc src/module_path -f --separate`

* <https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html>

* [reST を書かずに autodoc だけで Sphinx する](https://qiita.com/satamame/items/65abd04e74b341ed1e80)
* [sphinx で cython モジュールのapiを自動生成](https://ymd_h.gitlab.io/ymd_blog/posts/cython_sphinx_api/)

#### template

* <https://stackoverflow.com/questions/29385564/customize-templates-for-sphinx-apidoc>
* <https://stackoverflow.com/questions/59307596/how-to-add-inheritance-diagram-to-all-modules-in-sphinx>

<https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#module-sphinx.ext.autodoc>

## 外部コマンド

```{toctree}
sphinx-autobuild
```
