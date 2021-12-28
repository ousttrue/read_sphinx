# document

<https://docutils.sourceforge.io/>
  * https://docutils.sourceforge.io/docs/index.html#ref-reference-material-for-all-groups

Sphinx の記事 (rst) は、 doctree になって `build/.doctrees/*.doctree` に pickle 保存される。

`sphinx.addnodes.document` は、 `docutils.nodes.document` であり、`docutils.nodes.Node`。
root Node である。

myst-parser により markdown から doctree 化することができる。

## sphinx.addnodes.document

<https://www.sphinx-doc.org/en/master/_modules/sphinx/addnodes.html>

```python
class document(nodes.document):
    """The document root element patched by Sphinx.

    This fixes that document.set_id() does not support a node having multiple node Ids.
    see https://sourceforge.net/p/docutils/patches/167/

    .. important:: This is only for Sphinx internal use.  Please don't use this
                   in your extensions.  It will be removed without deprecation period.
    """

    def set_id(self, node: Element, msgnode: Element = None,
               suggested_prefix: str = '') -> str:
        from sphinx.util import docutils
        if docutils.__version_info__ >= (0, 16):
            ret = super().set_id(node, msgnode, suggested_prefix)  # type: ignore
        else:
            ret = super().set_id(node, msgnode)

        if docutils.__version_info__ < (0, 17):
            # register other node IDs forcedly
            for node_id in node['ids']:
                if node_id not in self.ids:
                    self.ids[node_id] = node
```

## docutils.nodes.document

<https://tristanlatr.github.io/apidocs/docutils/docutils.nodes.document.html>


```python
import sys
import pathlib
import pickle
import docutils.nodes


def traverse(node: docutils.nodes.Node, level=0):
    indent = '  ' * level
    print(f'{indent}{type(node)}')
    for child in node.children:
        traverse(child, level+1)


if __name__ == '__main__':
    document = pickle.loads(pathlib.Path(sys.argv[1]).read_bytes())
    traverse(document)

```

```
<class 'sphinx.addnodes.document'>
  <class 'docutils.nodes.section'>
    <class 'docutils.nodes.title'>
      <class 'docutils.nodes.Text'>
    <class 'docutils.nodes.compound'>
      <class 'sphinx.addnodes.toctree'>
    <class 'docutils.nodes.section'>
      <class 'docutils.nodes.title'>
        <class 'docutils.nodes.Text'>
      <class 'docutils.nodes.bullet_list'>
        <class 'docutils.nodes.list_item'>
          <class 'docutils.nodes.paragraph'>
            <class 'docutils.nodes.reference'>
              <class 'docutils.nodes.Text'>
    <class 'docutils.nodes.section'>
      <class 'docutils.nodes.title'>
        <class 'docutils.nodes.Text'>
      <class 'docutils.nodes.bullet_list'>
        <class 'docutils.nodes.list_item'>
          <class 'docutils.nodes.paragraph'>
            <class 'sphinx.addnodes.pending_xref'>
              <class 'docutils.nodes.inline'>
                <class 'docutils.nodes.Text'>
        <class 'docutils.nodes.list_item'>
          <class 'docutils.nodes.paragraph'>
            <class 'sphinx.addnodes.pending_xref'>
              <class 'docutils.nodes.inline'>
                <class 'docutils.nodes.Text'>
        <class 'docutils.nodes.list_item'>
          <class 'docutils.nodes.paragraph'>
            <class 'sphinx.addnodes.pending_xref'>
              <class 'docutils.nodes.inline'>
                <class 'docutils.nodes.Text'>
```