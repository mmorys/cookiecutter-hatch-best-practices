"""cookiecutter-hatch-best-practices post-gen cookiecutter hook script."""

import os
import shutil

src_layout = "{{ cookiecutter.src_layout }}"
use_cli = "{{ cookiecutter.use_cli }}"
use_tests = "{{ cookiecutter.use_tests }}"

# Remove cli directory if not needed
if not use_cli:
    shutil.rmtree("{{ cookiecutter.__package_name }}/cli")

# Remove tests directory if not needed
if not use_tests:
    shutil.rmtree("tests")

# Move package to src directory
# *Must happen af the end of other file modifications
if src_layout:
    os.mkdir("src")
    shutil.move("{{ cookiecutter.__package_name }}", "src")
