# BuildPhase

* <https://www.sphinx-doc.org/ja/master/extdev/index.html#build-phases>
* <https://www.sphinx-doc.org/ja/master/extdev/appapi.html#events>

```python
from enum import IntEnum


class BuildPhase(IntEnum):
    """Build phase of Sphinx application."""
    INITIALIZATION = 1
    READING = 2
    CONSISTENCY_CHECK = 3
    RESOLVING = 3
    WRITING = 4
```

```{toctree}
init
```

## Reading

```{blockdiag}
blockdiag {
    rst -> sphinx
    md -> myst_parser -> sphinx
    
    sphinx -> doctree
    sphinx -> environment

    rst, md [stacked];
    doctree [shape = "flowchart.database", stacked];
    environment [shape = "flowchart.database"];
}
```

```{toctree}
read
```

## Check, Resolve, Writing

```{blockdiag}
blockdiag {
    environment -> HtmlBuilder
    doctree -> HtmlBuilder
    theme -> HtmlBuilder -> html, css, js

    doctree [shape = "flowchart.database", stacked];
    environment [shape = "flowchart.database"];
}
```

```{toctree}
consistency_check
resolve
write
```
