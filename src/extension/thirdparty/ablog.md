# ablog

<https://ablog.readthedocs.io/en/latest/>

<https://github.com/sunpy/ablog/blob/main/ablog/__init__.py#L65>

```python
def setup(app):
    """
    Setup ABlog extension.
    """

    for args in CONFIG:
        app.add_config_value(*args[:3])

    app.add_directive("post", PostDirective)
    app.add_directive("postlist", PostListDirective)

    app.connect("config-inited", config_inited)
    app.connect("doctree-read", process_posts)

    app.connect("env-purge-doc", purge_posts)
    app.connect("doctree-resolved", process_postlist)
    app.connect("missing-reference", missing_reference)
    app.connect("html-collect-pages", generate_archive_pages)
    app.connect("html-collect-pages", generate_atom_feeds)
    app.connect("html-page-context", html_page_context)

    app.add_transform(CheckFrontMatter)
    app.add_directive("update", UpdateDirective)
    app.add_node(
        UpdateNode,
        html=(lambda s, n: s.visit_admonition(n), lambda s, n: s.depart_admonition(n)),
        latex=(lambda s, n: s.visit_admonition(n), lambda s, n: s.depart_admonition(n)),
    )

    pkgdir = os.path.abspath(os.path.dirname(__file__))
    locale_dir = os.path.join(pkgdir, "locales")
    app.config.locale_dirs.append(locale_dir)

    return {"version": __version__}  # identifies the version of our extension
```
