import json
import os

import maya.cmds as cmds
import maya.OpenMayaUI as omui
from PySide6 import QtWidgets, QtCore
from shiboken6 import wrapInstance


def get_maya_main_win():
    """Return the Maya main window"""
    main_win_addr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_win_addr), QtWidgets.QWidget)


class Window(QtWidgets.QDialog):

    def __init__(self):
        super().__init__(parent=get_maya_main_win())
        self.setWindowTitle("Crystal Rig Helper")
        self.resize(300, 450)
        self.colors = [
            {
                "label": "RED",
                "idx": 13,
            },
            {
                "label": "BLUE",
                "idx": 6,
            },
            {
                "label": "YELLOW",
                "idx": 22,
            },
        ]
        self.mk_layout()

    def mk_layout(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        for color in self.colors:
            self.mk_button(color)
        self.layout.addStretch()

    def mk_button(self, color):
        button = Button(color)
        self.layout.addWidget(button)
        return button


class Button(QtWidgets.QPushButton):

    def __init__(self, color):
        super().__init__(color["label"])
        self.clicked.connect(self.behavior)
        self.label = color["label"]
        self.idx = color["idx"]

    def behavior(self):
        print("test")
