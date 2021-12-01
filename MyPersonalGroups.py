# libraries
from libqtile import layout
from libqtile.config import Group


def init_groups():
    list_group = [
        Group("DEV", layout="monadtall"),
        Group("WEB", layout="monadtall"),
        Group("GFX", layout="monadtall"),
        Group("SYS", layout="monadtall"),
        Group("VBOX",layout="monadtall"),
        Group("DOC", layout="monadtall"),
        Group("VIDEOS",layout="monadtall"),
        Group("CHAT", layout="monadtall"),
        Group("GAMES", layout="monadtall")
    ]
    return list_group
