# sphinx-autobuild

-   <https://github.com/executablebooks/sphinx-autobuild>

> Rebuild Sphinx documentation on changes, with live-reload in the browser.

`pip install sphinx-autobuild`

わりと、シンプルな実装。
フォルダを監視して、変更を検知したら sphinx-build をキックする。
sphinx-build は中間ファイルをキャッシュして、差分をビルドする能力があるので
部分的にビルドされる。
sphinx-build のビルド結果も監視されており、ビルド結果の変更を検知して livereload を発動させている。
賢い。


```
# 空いているポートの自動選択
> sphinx-autobuild doc build --open-browser --port=0
```
