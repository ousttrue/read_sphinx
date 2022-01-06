# Extension

setup 関数をもつ python モジュール。

## setup

setup は 引数 `app: sphinx.application.Sphinx` をとる。

```python
def setup(app: sphinx.application.Sphinx):
    # ノードを登録する
    app.add_node(deleted, html=(visit_deleted, depart_deleted))

    # ロール
    app.add_role('del', deleted_role)

    # Directiveを登録する
    app.add_directive("helloworld", HelloWorld)

    # conf を追加する
    app.add_config_value('graphviz_dot', 'dot', 'html')

    # custom event
    app.add_event('todo-defined')
    # event handler
    app.connect('env-updated', create_nojekyll_and_cname)

    # transform
    app.add_transform(GlossaryDecorator)

    # 拡張のメタデータを返す
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
```

## 組み込み拡張

<https://www.sphinx-doc.org/ja/master/usage/extensions/index.html>


## 拡張の作り方

<https://www.sphinx-doc.org/ja/master/development/tutorials/index.html>

## サードパーティの拡張

* [(6日目) Sphinx 拡張の紹介](https://tk0miya.hatenablog.com/entry/20111206/p1)

```{toctree}
myst_parser
blockdiag
ablog
```

* <https://nbsphinx.readthedocs.io/en/0.8.8/>
