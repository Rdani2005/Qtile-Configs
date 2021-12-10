# ---------- Libraries ----------
from os import path
import json

qtile_path = path.join(path.expanduser('~'), ".config", "qtile")
#---------Methods-----------
# Method to call the colors
def my_theme():
    theme = "first-theme"
    
    configs = path.join(qtile_path, "config.json")
    if path.isfile(configs):
        with open(configs) as f:
            theme = json.load(f)["theme"]
    else:
        with open(config, "w") as f:
            f.write(f'{{"theme:": "{theme}" }}\n')

    theme_file = path.join(qtile_path, "themes", f'{theme}.json')
    if not path.isfile(theme_file):
        raise Exception(f'"{theme_file}" does not exist')

    with open(path.join(theme_file)) as f:
        return json.load(f)


if __name__ == "settings.theme":
    colors = my_theme()


