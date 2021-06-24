import sys
import os 

sys.path.insert(0, os.path.abspath('../../'))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    'sphinx_click'
]
