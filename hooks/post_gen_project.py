"""cookiecutter-hatch-best-practices post-gen cookiecutter hook script."""

import os
import shutil

src_layout = "{{ cookiecutter.src_layout }}"
use_cli = "{{ cookiecutter.use_cli }}"
use_tests = "{{ cookiecutter.use_tests }}"
git_and_precommit_init = "{{ cookiecutter.git_and_precommit_init }}"

# Remove cli directory if not needed
if not use_cli:
    shutil.rmtree("{{ cookiecutter.__package_name }}/cli")

# Remove tests directory if not needed
if not use_tests:
    shutil.rmtree("tests")

# Move package to src directory
# *Must happen at the end of other file modifications
if src_layout:
    os.mkdir("src")
    shutil.move("{{ cookiecutter.__package_name }}", "src")

# Initialize git and install pre-commit hooks
if git_and_precommit_init:
    import subprocess

    subprocess.Popen(["git", "init"])
    subprocess.Popen(["hatch", "run", "lint:pre-commit", "install"])
