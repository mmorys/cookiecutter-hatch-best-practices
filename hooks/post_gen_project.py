src_layout = "{{ cookiecutter.src_layout }}"

if src_layout:
    import os
    import shutil

    os.mkdir("src")
    shutil.move("{{ cookiecutter.package_name }}", "src")
