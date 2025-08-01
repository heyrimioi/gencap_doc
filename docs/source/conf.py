# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))  # Go up from source -> docs -> MEDCAP
import gencap 

project = 'GENCAP'
copyright = '2025, Hye-Lim LEE (Epione team, Inria)'
author = 'Hye-Lim LEE (Epione team, Inria)'
release = '0.9.0-dev'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',    # auto-generate API docs
    'sphinx.ext.napoleon',   # Google/NumPy style docstrings
    'sphinx.ext.viewcode',   # add links to source code
    'myst_parser'            # Enable MyST Markdown parsing
]

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

myst_enable_extensions = [
    "deflist",                # English comment: Enable definition list syntax
    "colon_fence",            # English comment: Enable ::: fenced code blocks
]

html_theme = 'sphinx_rtd_theme'

autodoc_default_options = {
    "members": True,             
    "show-inheritance": True,   
    "exclude-members": "_*"
}


napoleon_google_docstring = True
napoleon_numpy_docstring = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
