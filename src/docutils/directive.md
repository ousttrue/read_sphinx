# directive

<https://www.sphinx-doc.org/ja/master/development/tutorials/helloworld.html>

* <https://docutils.sourceforge.io/docs/howto/rst-directives.html>

```py
class HelloWorld(Directive):
    def run(self):
        paragraph_node = nodes.paragraph(text='Hello World!')
        return [paragraph_node]
```

.. helloworld::
```{helloworld}
```

- [Sphinx ではどのようにラベルとキャプションを結びつけているのか](https://tk0miya.hatenablog.com/entry/2014/08/11/003957)

* Directive では独自ノードを作り
* visitor 関数で独自ノードを画像に変換する

しかし、キャプションをうまく扱うためには次のようなやり方をするとよいでしょう。

* Directive では figure ノード、caption ノードと画像を表す独自ノードを作る
* visitor 関数で独自ノードを画像に変換する

`sphinx.ext.graphviz`
