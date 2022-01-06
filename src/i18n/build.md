# build

動作

* `sphinx.locale.__init__.py`
* `sphinx.util.i18n.CatalogRepository`

`sphinx.application.Sphinx`

`mo` ファイルの更新

gettext の msgfmt コマンドを使い、バイナリ形式で効率良い バイナリカタログ

```py
    def compile_catalogs(self, catalogs: Set[CatalogInfo], message: str) -> None:
        if not self.config.gettext_auto_build:
            return

        def cat2relpath(cat: CatalogInfo) -> str:
            return relpath(cat.mo_path, self.env.srcdir).replace(path.sep, SEP)

        logger.info(bold(__('building [mo]: ')) + message)
        for catalog in status_iterator(catalogs, __('writing output... '), "darkgreen",
                                       len(catalogs), self.app.verbosity,
                                       stringify_func=cat2relpath):
            catalog.write_mo(self.config.language,
                             self.config.gettext_allow_fuzzy_translations)
```

## sphinx.transforms.i18n

read phase に

`sphinx.transforms.i18n.Locale` により翻訳を適用している？

`sphinx.io.SphinxI18nReader`

```py
def setup(app: "Sphinx") -> Dict[str, Any]:
    app.add_transform(PreserveTranslatableMessages)
    app.add_transform(Locale) # 👈 これ
    app.add_transform(RemoveTranslatableInline)

    return {
        'version': 'builtin',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
```
