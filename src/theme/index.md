# Theme

{doc}`/builder/html/index` の見た目のカスタマイズ。

-   rtd の `toplevelのtoctree + 現在地` が使い易い

| theme             |         | navigation                         |
| ----------------- | ------- | ---------------------------------- |
| alabaster         | default | toplevelのtoctree 固定                |
| basic系            | builtin | prev, next, table of contents, 現在地 |
| rtd               |         | toplevelのtoctree + 現在地, prev, next |
| sphinx_book_theme |         | toplevelのtoctree + 現在地, prev, next |

-   [Sphinxを使用しているプロジェクト](https://www.sphinx-doc.org/ja/master/examples.html)
-   <https://sphinx-themes.org/>
-   <https://www.sphinx-doc.org/en/master/usage/theming.html>
-   <https://sphinx-users.jp/cookbook/changetheme/index.html>
-   <https://pypi.org/search/?c=Framework+%3A%3A+Sphinx+%3A%3A+Theme>

[alabaster](https://github.com/bitprophet/alabaster) も含めて `builtin` のテーマはすべて basic テーマを継承している。

```{toctree}
:maxdepth: 1
basic
```

## その他のテーマ

```{toctree}
furo
```
-   <https://sphinx-themes.org/sample-sites/sphinx-rtd-theme/>
-   <https://github.com/executablebooks/sphinx-book-theme>
-   <https://github.com/shiguredo/sphinx_shiguredo_theme>
-   <https://github.com/ryan-roemer/sphinx-bootstrap-theme>
-   <https://foss.heptapod.net/doc-utils/cloud_sptheme>

## テーマのカスタマイズ

```{toctree}
customize
create
```
