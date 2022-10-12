# Usage

{% if cookiecutter.use_cli -%}
```{eval-rst}
.. click:: {{cookiecutter.__package_name}}.__main__:main
    :prog: hypermodern-python
    :nested: full
```
{%- endif %}
