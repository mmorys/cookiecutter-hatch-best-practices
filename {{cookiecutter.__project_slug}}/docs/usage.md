# Usage

{% if cookiecutter.use_cli == "y" -%}
```{eval-rst}
.. click:: {{cookiecutter.__package_name}}.__main__:main
    :prog: hypermodern-python
    :nested: full
```
{%- endif %}
