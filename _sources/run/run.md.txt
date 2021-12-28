# 動作

## venv

sphinx のソースにステップ実行するので、 `.venv` あった方がやりやすい。

```python
> py -m venv .venv
> .\.venv\Scripts\Activate.ps1
(.venv) > pip install sphinx-autobuild myst-parser
```

## sphinx.application.Sphinx

```python
app = Sphinx()

    self.create_builder(buildername)
```

## sphinx.registry.SphinxComponentRegistry.create_builder

## sphinx.builders.StandaloneHTMLBuilder

### __init__

template ( `alabaster` など ) で初期化する。

```python
    def init_templates(self) -> None:
        theme_factory = HTMLThemeFactory(self.app)
        themename, themeoptions = self.get_theme_config()
        self.theme = theme_factory.create(themename)
        self.theme_options = themeoptions.copy()
        self.create_template_bridge()
        # self.templates: sphinx.jijja2glue.BuiltinTemplateLoader
        self.templates.init(self, self.theme)
```

### prepare_writing

```python
doctree = self.env.get_and_resolve_doctree(docname, self)
```
### handle_page

## sphinx.jijja2glue.BuiltinTemplateLoader

`jinja2.environment.get_template` `page.html`

### render

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
