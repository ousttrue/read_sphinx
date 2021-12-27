# Builder

`sphinx.builders.__init__.py:Builder`

## read

中間ファイルを書き出す

### Environment

`sphinx.application.ENV_PICKLE_FILENAME`

`build/.doctrees/enviroment.pickle`

[Environment と Domain](https://www.ykrods.net/posts/2020/10/15/sphinx-docutils-extension/#environment-domain)

### .doctree

`build/.doctrees/*.doctree*`

[中間ファイル *.doctree の内容をみてSphinxがどのようにreSTをparseしているか知りたい](https://sphinx-users.jp/reverse-dict/system/doctree.html)


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
