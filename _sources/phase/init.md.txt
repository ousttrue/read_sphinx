
# INITIALIZATION

フェーズ 0: 初期化

## sphinx.application.Sphinx

```python
    app = sphinx.application.Sphinx(
        srcdir=str(src),
        confdir=str(src),
        outdir=str(build),
        doctreedir=str(build / '.doctrees'),
        buildername='html'
    )
```

```
1. event.config-inited(app,config)
2. event.builder-inited(app)
```

## extension の import と setup

<https://www.sphinx-doc.org/ja/master/_modules/sphinx/application.html?highlight=builtin_extensions#>

```python
        # load all built-in extension modules
        for extension in builtin_extensions:
            self.setup_extension(extension)

        # conf.py の extensions の初期化
        # load all user-given extension modules
        for extension in self.config.extensions:
            self.setup_extension(extension)            
```

* 各 extensoin を import して setup を呼ぶ

例えば、

<https://github.com/bitprophet/alabaster/blob/master/alabaster/__init__.py#L18>


{doc}`/extension/index`
