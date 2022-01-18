import pathlib
import logging
import sphinx.application
import sphinx.util.logging
import sphinx.util.build_phase
import sphinx.builders
import sphinx.builders.html

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
        # freshenv=True
    )

    env = app.env

    logger = logging.getLogger(sphinx.util.logging.NAMESPACE)
    logger.propagate = True
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # for t in sorted(app.registry.transforms, key=lambda x: x.default_priority):
    #     print(f'{t.default_priority:03d}: {t}')

    # app.build(force_all=True)
    # app.build(filenames=['src/index.md'])
    app.phase = sphinx.util.build_phase.BuildPhase.READING
    match app.builder:
        case sphinx.builders.html.StandaloneHTMLBuilder() as builder:
            builder.compile_update_catalogs()
            # app.builder.build_update()
            """Only rebuild what was changed or added since last build."""
            to_build = builder.get_outdated_docs()
            if isinstance(to_build, str):
                builder.build(['__all__'], to_build)
            else:
                from sphinx.locale import __
                to_build = list(to_build)
                builder.build(to_build,
                              summary=__('targets for %d source files that are out of date') %
                              len(to_build))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='[%(levelname)s]%(name)s:%(message)s')
    logging.lastResort = logging.NullHandler()
    main(HERE / 'src', HERE / 'build')
