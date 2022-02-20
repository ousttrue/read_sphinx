# autodoc

python モジュールから docstring を抜き出してドキュメント化する。
`sphinx-apidoc` コマンド で rst を生成できる。

* <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>
  * <https://autoapi.readthedocs.io/>

## 設定

`conf.py` に設定が必要

```py
# todo
sys.path.append(PATH_TO_IMPORT_MODULE) # sphinx が import して docstring を生成するのに必要かも(対象が sys.path に含まれない場合)

extensinos = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon', # docstring syle 拡張(google 書式, numpy 書式)
]
# 設定
autodoc_default_options = {
    'imported-members': True, # __all__ 無しでも出るが余計なものも出る。
}
```

## docstring

* <https://www.python.org/dev/peps/pep-0257/>
* [Python入門］docstringの書き方](https://atmarkit.itmedia.co.jp/ait/articles/1912/06/news025.html)

## docstring の style

* [GoogleスタイルのPython Docstringの入門](https://qiita.com/11ohina017/items/118b3b42b612e527dc1d)
* <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>
* <https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>
