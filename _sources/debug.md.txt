# デバッグ

## vscode

### launch.json

<https://srbrnote.work/archives/4231>

```json
{
    "name": "Sphinx",
    "type": "python",
    "request": "launch",
    "module": "sphinx",
    "args": [
        ".",
        "build"
    ],
    "justMyCode": false
}
```

とすることで `F5` で sphinx を実行できる。
`"justMyCode": false` がみそで、これがあると外部ライブラリの中でもブレイクできる。

### problemMatcher

```js

```

## venv

sphinx のソースをステップ実行したり、ブレイクポイントを置いたりするので、 `.venv` があった方がやりやすい。
`.venv/Lib/site-packages/sphinx` 内に潜ってゆく。

```python
> py -m venv .venv
> .\.venv\Scripts\Activate.ps1
(.venv) > pip install sphinx-autobuild myst-parser
```

.venv も search 対象に入れる。

`.vscode/settings.json`

```js
 "search.useIgnoreFiles": false
```

## mod
### phase

```py
    @property
    def phase(self):
        return self._phase

    @phase.setter
    def phase(self, value: BuildPhase):
        from .util.console import colorize
        color_phase = colorize('yellow', value.name)
        logger.info(f'phase: {color_phase}')
        self._phase = value
```

```py
    def emit(self, name: str, *args: Any,
             allowed_exceptions: Tuple[Type[Exception], ...] = ()) -> List:
        """Emit a Sphinx event."""
        try:            
            from .util.console import colorize
            logger.debug(f'[app] emitting event: {colorize("green", name)}{repr(args)[:100]}')
        except Exception:
            # not every object likes to be repr()'d (think
            # random stuff coming via autodoc)
            pass
```
