import pathlib
import logging
import sphinx.application
import sphinx.util.logging

logger = logging.getLogger(__name__)
HERE = pathlib.Path(__file__).absolute().parent


def main():
    app = sphinx.application.Sphinx(
        srcdir=str(HERE),
        confdir=str(HERE),
        outdir=str(HERE / 'build'),
        doctreedir=str(HERE / 'build/.doctree'),
        buildername='html'
    )

    logger = logging.getLogger(sphinx.util.logging.NAMESPACE)
    logger.propagate = True
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    app.build(force_all=True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(levelname)s]%(name)s:%(message)s')
    logging.lastResort = logging.NullHandler()
    main()
