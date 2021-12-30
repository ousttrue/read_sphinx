# basic

basic 系

-   next, prev
-   path
-   table of contents

## 動作

### init

-   {doc}`ビルドフェーズ0 </run/init>`
-   sphinx.builders.Builder#create_template_bridge
-   sphinx.jinja2glue.BuiltinTemplateLoader#init
-   `builder-inited`

### write

-   {doc}`ビルドフェーズ4 </run/write>`
-   sphinx.builders.Builder#buile
-   sphinx.builders.Builder#write
-   sphinx.builders.StandaloneHTMLBuilder#write_doc
-   sphinx.jinja2glue.BuiltinTemplateLoader#handle_page

```python
    # page.html がエントリーポイント
    def handle_page(self, pagename: str, addctx: Dict, templatename: str = 'page.html',
                    outfilename: str = None, event_arg: Any = None) -> None:
```

-   sphinx.jinja2glue.BuiltinTemplateLoader#render

```python
output = self.templates.render(templatename, ctx)
```

## 構成

-   page.html

```html
{%- extends "layout.html" %}
{% block body %}
  {{ body }}
{% endblock %}
```

-   layout.html

| block    | content   | class                 |
| -------- | --------- | --------------------- |
| relbar1  | relbar()  | class="related"       |
| body     | page.html | class="body"          |
| sidebar2 | sidebar() | class="sphinxsidebar" |
| relbar2  | relbar()  | class="related"       |
| footer   | footer()  | class="footer"        |

## basic を継承するテーマ

### agogo

### bizstyle

    [theme]
    inherit = basic
    stylesheet = bizstyle.css
    pygments_style = friendly

    [options]
    rightsidebar = false
    sidebarwidth = 210

    maincolor = #336699

### classic

### default

### epub

### haiku

### nature

### nonav

### pyramid

### scrolls

-   next, prev が無い

### sphinxdoc

### traditional
