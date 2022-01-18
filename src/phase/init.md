
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


```
1. event.config-inited(app,config)
```

## sphinx.application.Sphinx._init_env

```py
    def _init_env(self, freshenv: bool) -> None:
        # build/.doctree/environment.pickle
        filename = path.join(self.doctreedir, ENV_PICKLE_FILENAME)
        if freshenv or not os.path.exists(filename):
            self.env = BuildEnvironment(self)
            self.env.find_files(self.config, self.builder)
        else:
            try:
                with progress_message(__('loading pickled environment')):
                    with open(filename, 'rb') as f:
                        self.env = pickle.load(f)
                        self.env.setup(self)
            except Exception as err:
                logger.info(__('failed: %s'), err)
                self._init_env(freshenv=True)
```

{doc}`/environment/index`

### sphinx.application.Sphinx._init_builder

```
2. event.builder-inited(app)
```
