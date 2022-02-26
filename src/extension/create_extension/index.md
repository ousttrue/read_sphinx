# 拡張の作り方

- <https://www.sphinx-doc.org/ja/master/development/tutorials/index.html>
- [Sphinxのプラグインの作り方を学ぶ](https://note.gosyujin.com/2013/10/02/sphinx-plugin/)

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

```{toctree}
directive
```
