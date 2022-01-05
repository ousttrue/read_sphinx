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
read
consistency_check
resolve
write
```
