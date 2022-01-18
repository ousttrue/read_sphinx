# 初期化

```py
    def _init_env(self, freshenv: bool) -> None:
        filename = path.join(self.doctreedir, ENV_PICKLE_FILENAME)
        if freshenv or not os.path.exists(filename):
            # 新規
            self.env = BuildEnvironment(self)
            self.env.find_files(self.config, self.builder)
        else:
            try:
                with progress_message(__('loading pickled environment')):
                    with open(filename, 'rb') as f:
                        # picke ロード
                        self.env = pickle.load(f)
                        # 更新
                        self.env.setup(self)
            except Exception as err:
                logger.info(__('failed: %s'), err)
                self._init_env(freshenv=True)
```

## 新規: sphinx.environment.BuildEnvironment

### find_files

## 更新: sphinx.environment.BuildEnvironment

### setup
