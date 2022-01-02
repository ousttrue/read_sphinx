# CONSISTENCY_CHECK

## document isn't included in any toctree

`WARNING: document isn't included in any toctree`

`sphinx.environment.BuildEnvironment`

```python
    def check_consistency(self) -> None:
        """Do consistency checks."""
        included = set().union(*self.included.values())  # type: ignore
        for docname in sorted(self.all_docs):
            if docname not in self.files_to_rebuild:
                if docname == self.config.root_doc:
                    # the master file is not included anywhere ;)
                    continue
                if docname in included:
                    # the document is included from other documents
                    continue
                if 'orphan' in self.metadata[docname]:
                    continue
                logger.warning(__('document isn\'t included in any toctree'),
                               location=docname)
```
