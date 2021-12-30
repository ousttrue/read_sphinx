# Theme

`StandaloneHTMLBuilder`

-   [テンプレート](https://www.sphinx-doc.org/ja/master/templating.html)
-   [テンプレートを作成する](https://sphinx-users.jp/cookbook/makingwebsite/template.html)
-   [Sphinxを使用しているプロジェクト](https://www.sphinx-doc.org/ja/master/examples.html)

## themes

| theme             |         | navigation                         |
| ----------------- | ------- | ---------------------------------- |
| alabaster         | default | toplevelのtoctree 固定                |
| basic系            | builtin | prev, next, table of contents, 現在地 |
| rtd               |         | toplevelのtoctree + 現在地, prev, next |
| sphinx_book_theme |         | toplevelのtoctree + 現在地, prev, next |

-   rtd の `toplevelのtoctree + 現在地` が使い易い


-   <https://sphinx-themes.org/>
-   <https://www.sphinx-doc.org/en/master/usage/theming.html>
-   <https://sphinx-users.jp/cookbook/changetheme/index.html>
-   <https://pypi.org/search/?c=Framework+%3A%3A+Sphinx+%3A%3A+Theme>

```{toctree}
basic
```

-   <https://sphinx-themes.org/sample-sites/sphinx-rtd-theme/>
-   <https://github.com/executablebooks/sphinx-book-theme>
-   <https://github.com/shiguredo/sphinx_shiguredo_theme>
-   <https://github.com/ryan-roemer/sphinx-bootstrap-theme>
-   <https://foss.heptapod.net/doc-utils/cloud_sptheme>

## customize

### sidebar

#### コンテンツを選ぶ

-   <https://www.sphinx-doc.org/en/master/usage/configuration.html>

conf.py

```python
html_sidebars = {
    '**': ['globaltoc.html', 'localtoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'],
}
```

#### カスタムのテンプレートを追加する

-   [Sphinxですべての目次をサイドバーに表示する](https://qiita.com/takakiku/items/99cf6505fb5c893a5168)
-   [サイドバーに全体目次を表示したい](http://www.areanine.gr.jp/~banjo/chocomemo/sphinx/sidebar.html)

<https://www.sphinx-doc.org/ja/master/templating.html#toctree>

`customtoc.html`

```html
<div id="toc" class="sidebarRow">
    <h3><a href="{{ pathto(master_doc) }}">{{ _('Table of Contents') }}</a></h3>
    {{ toctree (maxdepth=4, collapse=False, includehidden=False, titles_only=True) }}
</div>
```

#### 更に css を追加する

選択中の `<li><a>` に `current` class が付与されるので `css` で見た目が変わるようにすると見やすくなる。

```css
li.current > a {
    font-weight: bold;
}
```

### css

-   [Sphinx の sphinx_rtd_theme をカスタマイズする](https://kuttsun.blogspot.com/2016/11/sphinx-sphinxrtdtheme.html)

-   [sphinx で CSS の設定を追加する](https://qh73xebitbucketorg.readthedocs.io/ja/latest/1.Programmings/python/LIB/sphinx/addcss/)

### inherit

-   [Webサイトを作ろう(オリジナルテーマの作成)](https://sphinx-users.jp/cookbook/makingwebsite/index.html)
-   [Sphinx: 既存のテーマをカスタマイズする](https://blog.amedama.jp/entry/2016/01/06/122931)

#### 手順

-   テーマ名決める(仮に custom とする)
-   conf.py のあるフォルダに `custom` フォルダを作る
-   custom/theme.conf を作成


    [theme]
    inherit = basic
    stylesheet = main.css
    pygments_style = sphinx

    [option]
    nosidebar = false

-   conf.py が `custom` を使うように設定する

```python
html_theme = 'custom'
html_theme_path = ['.']
```

-   custom/static/main.css

```css
.body {
    background-color: silver;
}

.related {
    background-color: #a2e8fe;
}

.sphinxsidebar {
    background-color: #4b7afd;
}

.footer {
    background-color: #fcc1c1;
}
```
