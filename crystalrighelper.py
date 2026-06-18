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
        self.mk_layout()

    def mk_layout(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.color_all_button = self.mk_button("ALL")
        self.red_button = self.mk_button("RED")
        self.blue_button = self.mk_button("BLUE")
        self.yellow_button = self.mk_button("YELLOW")
        self.layout.addStretch()

    def mk_button(self, name=""):
        button = QtWidgets.QPushButton(name)
        self.layout.addWidget(button)
        return button
