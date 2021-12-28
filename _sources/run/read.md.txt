# フェーズ 1: 読み込み

中間ファイルを書き出す

```
3. event.env-get-outdated(app, env, added, changed, removed)
4. event.env-before-read-docs(app, env, docnames)

for docname in docnames:
   5. event.env-purge-doc(app, env, docname)

   if doc changed and not removed:
      6. source-read(app, docname, source)
      7. run source parsers: text -> docutils.document
         - parsers can be added with the app.add_source_parser() API
      8. apply transforms based on priority: docutils.document -> docutils.document
         - event.doctree-read(app, doctree) is called in the middle of transforms,
           transforms come before/after this event depending on their priority.

9. event.env-merge-info(app, env, docnames, other)
   - if running in parallel mode, this event will be emitted for each process

10. event.env-updated(app, env)
```

## Environment

`sphinx.application.ENV_PICKLE_FILENAME`

`build/.doctrees/enviroment.pickle`

[Environment と Domain](https://www.ykrods.net/posts/2020/10/15/sphinx-docutils-extension/#environment-domain)

## .doctree

`build/.doctrees/*.doctree*`

[中間ファイル \*.doctree の内容をみてSphinxがどのようにreSTをparseしているか知りたい](https://sphinx-users.jp/reverse-dict/system/doctree.html)
