import pathlib
import logging
import sphinx.application
import sphinx.util.logging

logger = logging.getLogger(__name__)
HERE = pathlib.Path(__file__).absolute().parent


def main(src: pathlib.Path, build: pathlib.Path):
    static = src / '_static'
    static.mkdir(exist_ok=True)

    app = sphinx.application.Sphinx(
        srcdir=str(src),
        confdir=str(src),
        outdir=str(build),
        doctreedir=str(build / '.doctrees'),
        buildername='html',
        freshenv=True
    )

    logger = logging.getLogger(sphinx.util.logging.NAMESPACE)
    logger.propagate = True
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # for t in sorted(app.registry.transforms, key=lambda x: x.default_priority):
    #     print(f'{t.default_priority:03d}: {t}')

    # app.build(force_all=True)
    app.build(filenames=['src/index.md'])


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='[%(levelname)s]%(name)s:%(message)s')
    logging.lastResort = logging.NullHandler()
    main(HERE / 'src', HERE / 'build')
