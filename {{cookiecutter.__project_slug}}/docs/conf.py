"""Sphinx configuration."""
project = "{{cookiecutter.project_name}}"
author = "{{cookiecutter.author}}"
copyright = "{{cookiecutter.__copyright_year}}, {{cookiecutter.author}}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "myst_parser"
    {%- if cookiecutter.use_cli -%},
    "sphinx_click",
    {%- endif %}
]
autodoc_typehints = "description"
html_theme = "furo"
