"""cookiecutter-hatch-best-practices post-gen cookiecutter hook script."""

src_layout = "{{ cookiecutter.src_layout }}"
use_cli = "{{ cookiecutter.use_cli }}"
use_tests = "{{ cookiecutter.use_tests }}"

if src_layout:
    import os
    import shutil

    # Remove cli directory if not needed
    if not use_cli:
        shutil.rmtree("{{ cookiecutter.__package_name }}/cli")

    if not use_tests:
        shutil.rmtree("tests")

    # Move package to src directory
    # *Must happen af the end of other file modifications
    os.mkdir("src")
    shutil.move("{{ cookiecutter.__package_name }}", "src")
