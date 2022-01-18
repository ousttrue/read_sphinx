# READING

フェーズ 1: 読み込み

```{blockdiag}
blockdiag {
    read -> "docutils(transform)" -> "write(.doctree & env)"
}
```

## sphinx.util.i18n.CatalogRepository

* compile_update_catalogs. mo ファイルの生成

## prepare

更新ファイルのチェック。

### conf.py の更新チェック

`build/.buildinfo`

`sphinx.StandaloneHTMLBuilder`

```py
    def get_outdated_docs(self) -> Iterator[str]:
        try:
            with open(path.join(self.outdir, '.buildinfo')) as fp:
                buildinfo = BuildInfo.load(fp)
            if self.build_info != buildinfo:
                logger.debug('[build target] did not match: build_info ')
                yield from self.env.found_docs
                return                
```

`.buildinfo`

```
# Sphinx build info version 1
# This file hashes the configuration used when building these files. When it is not found, a full rebuild will be done.
config: 21b9b62534fd766965fac5345c71c03e
tags: 645f666f9bcd5a90fca523b33c5a78b7
```

### template の更新チェック

### env の更新チェック

```py
    def get_outdated_docs(self) -> Iterator[str]:
        # 続き・・・

        for docname in self.env.found_docs:
            if docname not in self.env.all_docs:
                logger.debug('[build target] did not in env: %r', docname)
                yield docname
                continue
            targetname = self.get_outfilename(docname)
            try:
                targetmtime = path.getmtime(targetname)
            except Exception:
                targetmtime = 0
            try:
                srcmtime = max(path.getmtime(self.env.doc2path(docname)),
                               template_mtime)
                if srcmtime > targetmtime:
                    logger.debug(
                        '[build target] targetname %r(%s), template(%s), docname %r(%s)',
                        targetname,
                        datetime.utcfromtimestamp(targetmtime),
                        datetime.utcfromtimestamp(template_mtime),
                        docname,
                        datetime.utcfromtimestamp(path.getmtime(self.env.doc2path(docname))),
                    )
                    yield docname
            except OSError:
                # source doesn't exist anymore
                pass

```

## event

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

{doc}`/extension/thirdparty/myst_parser`

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
