# basicテーマ

basic 系

-   next, prev
-   path
-   table of contents

## 構成

`site-packages\sphinx\themes` に配置されている。

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
