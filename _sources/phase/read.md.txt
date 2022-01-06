# READING

フェーズ 1: 読み込み

最初に翻訳カタログの処理。 {doc}`/i18n/index`

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

## read

```python
added, changed, removed = self.env.get_outdated_files(updated)
```

* docutils の Publisher で parse する。

`sphinx.io.py`

```python
def read_doc(app: "Sphinx", env: BuildEnvironment, filename: str) -> nodes.document:
    """Parse a document and convert to doctree."""
    # set up error_handler for the target document
    error_handler = UnicodeDecodeErrorHandler(env.docname)
    codecs.register_error('sphinx', error_handler)  # type: ignore

    reader = SphinxStandaloneReader() # これ
    reader.setup(app)
    filetype = get_filetype(app.config.source_suffix, filename)

    parser = app.registry.create_source_parser(app, filetype) # 👈 拡張子に応じて myst_parser になる

    if parser.__class__.__name__ == 'CommonMarkParser' and parser.settings_spec == ():
        # a workaround for recommonmark
        #   If recommonmark.AutoStrictify is enabled, the parser invokes reST parser
        #   internally.  But recommonmark-0.4.0 does not provide settings_spec for reST
        #   parser.  As a workaround, this copies settings_spec for RSTParser to the
        #   CommonMarkParser.
        parser.settings_spec = RSTParser.settings_spec

    pub = Publisher(reader=reader,
                    parser=parser,
                    writer=SphinxDummyWriter(),
                    source_class=SphinxFileInput,
                    destination=NullOutput())
    pub.process_programmatic_settings(None, env.settings, None)
    pub.set_source(source_path=filename)
    pub.publish() # 👈 myst parser が使われれる
    return pub.document
```

`sphinx.io.SphinxStandaloneReader`

```py
    def read(self, source: Input, parser: Parser, settings: Values) -> nodes.document:
        self.source = source

    def read_source(self, env: BuildEnvironment) -> str:
        """Read content from source and do post-process."""
        content = self.source.read()    
```

`SphinxFileInput`



```python
class MystParser(SphinxParser):
    def parse(self, inputstring: str, document: nodes.document) -> None:
        """Parse source text.

        :param inputstring: The source string to parse
        :param document: The root docutils node to add AST elements to

        """
        config = document.settings.env.myst_config
        parser = default_parser(config)
        parser.options["document"] = document
        env: dict = {}
        tokens = parser.parse(inputstring, env)
        if not tokens or tokens[0].type != "front_matter":
            # we always add front matter, so that we can merge it with global keys,
            # specified in the sphinx configuration
            tokens = [Token("front_matter", "", 0, content="{}", map=[0, 0])] + tokens
        parser.renderer.render(tokens, parser.options, env) # 👈 myst_parser.sphinx_renderer.SphinxRenderer
```

`myst_parser.docutils_renderer.DocutilsRenderer`

```python
    def render_front_matter(self, token: SyntaxTreeNode) -> None:
        """Pass document front matter data."""
```

`TocTreeCollector`

## Environment

`sphinx.application.ENV_PICKLE_FILENAME`

`build/.doctrees/enviroment.pickle`

[Environment と Domain](https://www.ykrods.net/posts/2020/10/15/sphinx-docutils-extension/#environment-domain)

## .doctree

`build/.doctrees/*.doctree*`

[中間ファイル \*.doctree の内容をみてSphinxがどのようにreSTをparseしているか知りたい](https://sphinx-users.jp/reverse-dict/system/doctree.html)
