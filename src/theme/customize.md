# customize

## sidebar

### コンテンツを選ぶ

-   <https://www.sphinx-doc.org/en/master/usage/configuration.html>

conf.py

```python
html_sidebars = {
    '**': ['globaltoc.html', 'localtoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'],
}
```

### カスタムのテンプレートを追加する

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

### 更に css を追加する

選択中の `<li><a>` に `current` class が付与されるので `css` で見た目が変わるようにすると見やすくなる。

```css
li.current > a {
    font-weight: bold;
}
```

## css

-   [Sphinx の sphinx_rtd_theme をカスタマイズする](https://kuttsun.blogspot.com/2016/11/sphinx-sphinxrtdtheme.html)

-   [sphinx で CSS の設定を追加する](https://qh73xebitbucketorg.readthedocs.io/ja/latest/1.Programmings/python/LIB/sphinx/addcss/)

## inherit

-   [Webサイトを作ろう(オリジナルテーマの作成)](https://sphinx-users.jp/cookbook/makingwebsite/index.html)
-   [Sphinx: 既存のテーマをカスタマイズする](https://blog.amedama.jp/entry/2016/01/06/122931)

### 手順

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
