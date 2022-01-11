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
|----------|-----------|-----------------------|
| relbar1  | relbar()  | class="related"       |
| body     | page.html | class="body"          |
| sidebar2 | sidebar() | class="sphinxsidebar" |
| relbar2  | relbar()  | class="related"       |
| footer   | footer()  | class="footer"        |

## basic を継承するテーマ

| theme       | html_sidebars | comment           |
|-------------|---------------|-------------------|
| aoggo       |               |                   |
| bizstyle    | enable        |                   |
| classic     | enable        |                   |
| default     | enable        | classic と同じ    |
| pyramid     | enable        |                   |
| nature      | enable        |                   |
| sphinxdoc   | enable        |                   |
| traditional | enable        |                   |
| haiku       | no sidebar    |                   |
| scrolls     | no sidebar    | next, prev が無い |
| epub        |               |                   |
| nonav       |               |                   |
