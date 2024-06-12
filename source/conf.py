# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Research IT Technical Document Store'
copyright = '2024, University of Liverpool'
author = 'Ian Smith, Cliff Addison, Manhui Wang, Max Birkett'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []


# >>>>>>>>>>>>>>>> sphinx_rtd_theme: see https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html
# These folders are copied to the documentation's HTML output
html_static_path = ['_static']
html_logo = '_static/img/ResIT-techDocs.png'

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css'
]


html_show_sourcelink = False
html_theme_options = {
    'logo_only': True
}

# <<<<<<<<<<<<<<<<

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# my see: https://www.sphinx-doc.org/en/master/usage/theming.html#themes
# theme not 'alabaster', classic, sphinxdoc, sphinx_rtd_theme[install pip], scrolls, agogo, traditional, nature, haiku, bizstyle, pyramid
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']