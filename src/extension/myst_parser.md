# myst_parser

```python
def setup(app):
    """Initialize Sphinx extension."""
    from myst_parser.sphinx_parser import MystParser

    app.add_source_suffix(".md", "markdown")
    app.add_source_parser(MystParser)

    setup_sphinx(app)

    return {"version": __version__, "parallel_read_safe": True}


def setup_sphinx(app: "Sphinx"):
    """Initialize all settings and transforms in Sphinx."""
    # we do this separately to setup,
    # so that it can be called by external packages like myst_nb
    from myst_parser.directives import FigureMarkdown, SubstitutionReferenceRole
    from myst_parser.main import MdParserConfig
    from myst_parser.mathjax import override_mathjax
    from myst_parser.myst_refs import MystReferenceResolver

    app.add_role("sub-ref", SubstitutionReferenceRole())
    app.add_directive("figure-md", FigureMarkdown)

    app.add_post_transform(MystReferenceResolver)

    for name, default in MdParserConfig().as_dict().items():
        if not name == "renderer":
            app.add_config_value(f"myst_{name}", default, "env")

    app.connect("builder-inited", create_myst_config)
    app.connect("builder-inited", override_mathjax)
```

## MystParser

`docutils.readers.Reader`

```python
    def parse(self):
        """Parse `self.input` into a document tree."""
        self.document = document = self.new_document()
        self.parser.parse(self.input, document)
        document.current_source = document.current_line = None
```

`myst_parser.sphinx_parser.MystParser`

```python
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
        parser.renderer.render(tokens, parser.options, env)
```

`myst_parser.sphinx_renderer.SphinxRenderer`

```python
    def render(
        self, tokens: Sequence[Token], options, md_env: MutableMapping[str, Any]
    ) -> nodes.document:
        self._render_tokens(list(tokens))
        
    def _render_tokens(self, tokens: List[Token]) -> None:
        # render
        for child in node_tree.children:
            # skip hidden?
            if f"render_{child.type}" in self.rules:
                self.rules[f"render_{child.type}"](child)
            else:
                self.create_warning(
                    f"No render method for: {child.type}",
                    line=token_line(child, default=0),
                    subtype="render",
                    append_to=self.current_node,
                )

# child.type
front_matter
inline
inline
heading

# child.type
front_matter
inline
inline
paragraph
```
