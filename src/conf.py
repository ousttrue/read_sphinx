# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import sys
# sys.path.insert(0, os.path.abspath('.'))
import os
import pathlib
HERE = pathlib.Path(__file__).absolute().parent
# import sys
# sys.path.insert(0, os.path.abspath('.'))
if os.name == 'nt':
    os.environ['PATH'] = f"{os.environ['PATH']};C:\\Program Files\\Graphviz\\bin"
    os.environ['PATH'] = f"{os.environ['PATH']};C:\\Program Files\\Pandoc"

sys.path.append(str(HERE / "_ext"))

# -- Project information -----------------------------------------------------

project = 'read sphinx'
copyright = '2021, ousttrue'
author = 'ousttrue'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'helloworld',
    'folium_map',
    #
    "myst_parser",
    'sphinx.ext.autodoc',
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.seqdiag',
    'sphinxcontrib.actdiag',
    'sphinxcontrib.nwdiag',
    'sphinxcontrib.rackdiag',
    'sphinxcontrib.packetdiag',
    'sphinx.ext.graphviz',
    'nbsphinx',
]
graphviz_output_format = 'svg'
blockdiag_html_image_format = 'SVG'
seqdiag_html_image_format = 'SVG'
actdiag_html_image_format = 'SVG'
nwdiag_html_image_format = 'SVG'
rackiag_html_image_format = 'SVG'
packetdiag_html_image_format = 'SVG'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

language = "ja"
