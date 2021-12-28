# 動作

## デバッグ

### vscode

launch.json

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

### venv

sphinx のソースをステップ実行したり、ブレイクポイントを置いたりするので、 `.venv` があった方がやりやすい。
`.venv/Lib/site-packages/sphinx` 内に潜ってゆく。

```python
> py -m venv .venv
> .\.venv\Scripts\Activate.ps1
(.venv) > pip install sphinx-autobuild myst-parser
```

## [ビルド・フェーズ](https://www.sphinx-doc.org/ja/master/extdev/index.html#build-phases)

* <https://www.sphinx-doc.org/ja/master/extdev/appapi.html#events>

```{toctree}
init.md
read.md
resolve.md
write.md
```
