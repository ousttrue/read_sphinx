# READING

フェーズ 1: 読み込み

```{blockdiag}
blockdiag {
    read -> "docutils(transform)" -> "write(.doctree & env)"
}
```

## prepare

更新ファイルのチェック。

| event                      |                                   |
|----------------------------|-----------------------------------|
| event.env-get-outdated     | app, env, added, changed, removed |
| event.env-before-read-docs | app, env, docnames                |

```python
added, changed, removed = self.env.get_outdated_files(updated)
```

## foreach docname

| event               |                   |
|---------------------|-------------------|
| event.env-purge-doc | app, env, docname |

###  if doc changed and not removed

| event       |                      |
|-------------|----------------------|
| source-read | app, docname, source |

* {doc}`/docutils/transform`
* {doc}`/i18n/index`

### run source parsers: text -> docutils.document

parsers can be added with the app.add_source_parser() API

{doc}`/extension/myst_parser`

### apply transforms based on priority: docutils.document -> docutils.document

transforms come before/after this event depending on their priority.

| event              |              |
|--------------------|--------------|
| event.doctree-read | app, doctree |

## merge(if running in parallel mode, this event will be emitted for each process)

| event                |                           |
|----------------------|---------------------------|
| event.env-merge-info | app, env, docnames, other |

## updated

| event             |          |
|-------------------|----------|
| event.env-updated | app, env |

## 中間ファイル
### Environment

`sphinx.application.ENV_PICKLE_FILENAME`

`build/.doctrees/enviroment.pickle`

[Environment と Domain](https://www.ykrods.net/posts/2020/10/15/sphinx-docutils-extension/#environment-domain)

### .doctree

`build/.doctrees/*.doctree*`

[中間ファイル \*.doctree の内容をみてSphinxがどのようにreSTをparseしているか知りたい](https://sphinx-users.jp/reverse-dict/system/doctree.html)
