# 組み込み拡張

<https://www.sphinx-doc.org/ja/master/usage/extensions/index.html>

```{toctree}
autodoc
```

## graphviz


```{warning}
dot.exe に PATH を通す必要あり
```

`conf.py`

```py
import os
if os.name == 'nt':
    # windows で dot.exe にパスを通してやる例
    os.environ['PATH'] = f"{os.environ['PATH']};C:\\Program Files\\Graphviz\\bin"

extensions = [
    'sphinx.ext.graphviz',
]
graphviz_output_format = 'svg'    
```

```{digraph} G
rankdir="BT"
B->A
C->A
```

### dot 言語

* [DOT 言語でグラフの方向を変えるには](https://www.johf.com/log/20121228a.html)
* [クラス図を自動生成する](https://qiita.com/kenichi-hamaguchi/items/c0b947ed15725bfdfb5a)

## autodoc

