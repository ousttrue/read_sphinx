# BuildPhase.WRITING

フェーズ 4: 書き出し

```
15. Generate output files
16. event.build-finished(app, exception)
```
## write

```python
for docname in status_iterator(docnames, __('writing output... '), "darkgreen",
                                len(docnames), self.app.verbosity):
    self.app.phase = BuildPhase.RESOLVING
    # doctree を env から得る
    doctree: docutils.nodes.document = self.env.get_and_resolve_doctree(docname, self)
    self.app.phase = BuildPhase.WRITING
    # doctree を write する
    self.write_doc_serialized(docname, doctree)
    self.write_doc(docname, doctree)
```

HTML builder の場合、 {doc}`basic teheme の動作 </builder/html/theme/basic>` に続く。
