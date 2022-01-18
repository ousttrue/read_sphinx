# Environment

`sphinx.environment.BuildEnvironment`

Enviroment にはサイト全体の情報が格納される。

`sphinx.application.Sphinx.__init__` 内 `_init_env` で初期化される。
`build/.doctree/environment.pickle` の有無で新規と更新に別れる。

| field      |                                                |
| ---------- | ---------------------------------------------- |
| all_docs   | Dict{docname: mtime}                           |
| found_docs | List{docname} @property: self.project.docnames |
| project    | `sphinx.project.Project`                       |
| domaindata | domain の dict                                 |
| tocs       |

```{toctree}
init
project
domaindata
collector
```
