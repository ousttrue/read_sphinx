# HTMLBuilder

-   [Sphinxにひっそり存在するビルダー "dirhtml"の使い勝手を知る](https://zenn.dev/attakei/articles/sphinx-make-dirhtml)

## 動作

### init

-   `StandaloneHTMLBuilder`

`sphinx.jinja2glue.BuiltinTemplateLoader` をセットアップする。

-   {doc}`ビルドフェーズ0 </run/init>`
-   sphinx.builders.Builder#create_template_bridge
-   sphinx.jinja2glue.BuiltinTemplateLoader()
-   sphinx.jinja2glue.BuiltinTemplateLoader#init
-   `builder-inited`

### write

`sphinx.jinja2glue.BuiltinTemplateLoader` を使う。

-   {doc}`ビルドフェーズ4 </run/write>`
-   sphinx.builders.Builder#buile
-   sphinx.builders.Builder#write
-   sphinx.builders.StandaloneHTMLBuilder#write_doc
-   sphinx.jinja2glue.BuiltinTemplateLoader#handle_page

```python
    # page.html がエントリーポイント
    def handle_page(self, pagename: str, addctx: Dict, templatename: str = 'page.html',
                    outfilename: str = None, event_arg: Any = None) -> None:
```

-   sphinx.jinja2glue.BuiltinTemplateLoader#render

```python
output = self.templates.render(templatename, ctx)
```

#### sidebar のメカニズム

```python
# StandaloneHTMLBuilder
    def add_sidebars(self, pagename: str, ctx: Dict) -> None:
        def has_wildcard(pattern: str) -> bool:
            return any(char in pattern for char in '*?[')

        sidebars = None
        matched = None
        customsidebar = None

        # default sidebars settings for selected theme
        if self.theme.name == 'alabaster':
            # provide default settings for alabaster (for compatibility)
            # Note: this will be removed before Sphinx-2.0
            try:
                # get default sidebars settings from alabaster (if defined)
                theme_default_sidebars = self.theme.config.get('theme', 'sidebars')
                if theme_default_sidebars:
                    sidebars = [name.strip() for name in theme_default_sidebars.split(',')]
            except Exception:
                # fallback to better default settings
                sidebars = ['about.html', 'navigation.html', 'relations.html',
                            'searchbox.html', 'donate.html']
        else:
            theme_default_sidebars = self.theme.get_config('theme', 'sidebars', None)
            if theme_default_sidebars:
                sidebars = [name.strip() for name in theme_default_sidebars.split(',')]

        # user sidebar settings
        html_sidebars = self.get_builder_config('sidebars', 'html')
        for pattern, patsidebars in html_sidebars.items():
            if patmatch(pagename, pattern):
                if matched:
                    if has_wildcard(pattern):
                        # warn if both patterns contain wildcards
                        if has_wildcard(matched):
                            logger.warning(__('page %s matches two patterns in '
                                              'html_sidebars: %r and %r'),
                                           pagename, matched, pattern)
                        # else the already matched pattern is more specific
                        # than the present one, because it contains no wildcard
                        continue
                matched = pattern
                sidebars = patsidebars

        if sidebars is None:
            # keep defaults
            pass

        ctx['sidebars'] = sidebars # 👈
        ctx['customsidebar'] = customsidebar
```

## sphinx.jinja2glue.BuiltinTemplateLoader

### render

```python
    def render(self, template: str, context: Dict) -> str:  # type: ignore
        return self.environment.get_template(template).render(context)
```

-   template: `page.html`, `genindex.html`, `search.html` 等が入力する。
-   context: は jinja template に渡す変数

```python
# StandaloneHTMLBuilder
        ctx = self.globalcontext.copy()

    def prepare_writing(self, docnames: Set[str]) -> None: 
        # 省略

        self.globalcontext = {
            'embedded': self.embedded,
            'project': self.config.project, # 👈 conf.py
            'release': return_codes_re.sub('', self.config.release),  # 👈 conf.py
            'version': self.config.version,  # 👈 conf.py
            'last_updated': self.last_updated, 
            'copyright': self.config.copyright, # 👈 conf.py
            'master_doc': self.config.root_doc, # 👈 conf.py
            'root_doc': self.config.root_doc,  # 👈 conf.py
            'use_opensearch': self.config.html_use_opensearch, # 👈 conf.py
            'docstitle': self.config.html_title,  # 👈 conf.py
            'shorttitle': self.config.html_short_title,  # 👈 conf.py
            'show_copyright': self.config.html_show_copyright,  # 👈 conf.py
            'show_sphinx': self.config.html_show_sphinx, # 👈 conf.py
            'has_source': self.config.html_copy_source, # 👈 conf.py
            'show_source': self.config.html_show_sourcelink, # 👈 conf.py
            'sourcelink_suffix': self.config.html_sourcelink_suffix, # 👈 conf.py
            'file_suffix': self.out_suffix,
            'link_suffix': self.link_suffix,
            'script_files': self.script_files,
            'language': self.config.language, # 👈 conf.py
            'css_files': self.css_files,
            'sphinx_version': __display_version__,
            'sphinx_version_tuple': sphinx_version,
            'style': self._get_style_filename(),
            'rellinks': rellinks,
            'builder': self.name,
            'parents': [],
            'logo': logo,
            'favicon': favicon,
            'html5_doctype': html5_ready and not self.config.html4_writer, # 👈 conf.py
        }
        if self.theme:
            # 👇 global context に theme.conf の option 項の値が追加される
            # [options]
            # rightsidebar = false
            # sidebarwidth = 210
            # maincolor = #336699
            self.globalcontext.update(
                ('theme_' + key, val) for (key, val) in
                self.theme.get_options(self.theme_options).items())
        self.globalcontext.update(self.config.html_context)        
```

```{toctree}
:maxdepth: 1
theme/index
```
