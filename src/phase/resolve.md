# RESOLVING

`フェーズ 3: 解決 `

```
# The updated-docs list can be builder dependent, but generally includes all new/changed documents,
# plus any output from `env-get-updated`, and then all "parent" documents in the ToC tree
# For builders that output a single page, they are first joined into a single doctree before post-transforms
# or the doctree-resolved event is emitted
for docname in updated-docs:
   13. apply post-transforms (by priority): docutils.document -> docutils.document
   14. event.doctree-resolved(app, doctree, docname)
       - In the event that any reference nodes fail to resolve, the following may emit:
       - event.missing-reference(env, node, contnode)
       - event.warn-missing-reference(domain, node)
```

## prepare_writing

```python
doctree = self.env.get_and_resolve_doctree(docname, self)
```
