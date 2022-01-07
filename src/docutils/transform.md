# Transform

`sphinx.application.Sphinx`

```py
    def add_transform(self, transform: Type[Transform]) -> None:
        """Register a Docutils transform to be applied after parsing.

        Add the standard docutils :class:`Transform` subclass *transform* to
        the list of transforms that are applied after Sphinx parses a reST
        document.

        :param transform: A transform class

        .. list-table:: priority range categories for Sphinx transforms
           :widths: 20,80

           * - Priority
             - Main purpose in Sphinx
           * - 0-99
             - Fix invalid nodes by docutils. Translate a doctree.
           * - 100-299
             - Preparation
           * - 300-399
             - early
           * - 400-699
             - main
           * - 700-799
             - Post processing. Deadline to modify text and referencing.
           * - 800-899
             - Collect referencing and referenced nodes. Domain processing.
           * - 900-999
             - Finalize and clean up.

        refs: `Transform Priority Range Categories`__

        __ https://docutils.sourceforge.io/docs/ref/transforms.html#transform-priority-range-categories
        """  # NOQA
        self.registry.add_transform(transform)
```

## app.registry.transforms

| default_priority | transform                                                        |
|------------------|------------------------------------------------------------------|
| 010              | sphinx.transforms.ApplySourceWorkaround                          |
| 010              | sphinx.transforms.ExtraTranslatableNodes                         |
| 010              | sphinx.transforms.i18n.PreserveTranslatableMessages              |
| 020              | sphinx.transforms.i18n.Locale                                    |
| 100              | sphinx.transforms.compact_bullet_list.RefOnlyBulletListTransform |
| 200              | sphinx.transforms.UnreferencedFootnotesDetector                  |
| 210              | sphinx.transforms.DefaultSubstitutions                           |
| 210              | sphinx.transforms.MoveModuleTargets                              |
| 210              | sphinx.transforms.HandleCodeBlocks                               |
| 210              | sphinx.transforms.AutoNumbering                                  |
| 210              | sphinx.transforms.AutoIndexUpgrader                              |
| 261              | sphinx.transforms.SortIds                                        |
| 500              | sphinx.transforms.DoctestTransform                               |
| 619              | sphinx.domains.citation.CitationDefinitionTransform              |
| 619              | sphinx.domains.citation.CitationReferenceTransform               |
| 700              | sphinx.builders.latex.transforms.FootnoteDocnameUpdater          |
| 750              | sphinx.transforms.SphinxSmartQuotes                              |
| 850              | sphinx.transforms.references.SphinxDanglingReferences            |
| 850              | sphinx.transforms.references.SphinxDomains                       |
| 880              | sphinx.transforms.DoctreeReadEvent                               |
| 880              | sphinx.versioning.UIDTransform                                   |
| 999              | sphinx.transforms.FilterSystemMessages                           |
| 999              | sphinx.transforms.ManpageLink                                    |
| 999              | sphinx.transforms.i18n.RemoveTranslatableInline                  |

## reading

`sphinx.io`

```py
def read_doc(app: "Sphinx", env: BuildEnvironment, filename: str) -> nodes.document:
    """Parse a document and convert to doctree."""
    # set up error_handler for the target document
    error_handler = UnicodeDecodeErrorHandler(env.docname)
    codecs.register_error('sphinx', error_handler)  # type: ignore

    reader = SphinxStandaloneReader()
    reader.setup(app) # 👈 setup transforms
    filetype = get_filetype(app.config.source_suffix, filename)
    parser = app.registry.create_source_parser(app, filetype)
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
    pub.publish() # 👈 apply transforms
    return pub.document
```

```{inheritance-diagram} sphinx.io.SphinxStandaloneReader
```

```py
class SphinxStandaloneReader(SphinxBaseReader):
    """
    A basic document reader for Sphinx.
    """

    def setup(self, app: "Sphinx") -> None:
        self.transforms = self.transforms + app.registry.get_transforms() # 👈 app.registry.transforms
        super().setup(app)
```
