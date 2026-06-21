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
        colors = [
            {
                "name": "RED",
                "idx": 13,
                "convention": "R_*",
            },
            {
                "name": "BLUE",
                "idx": 6,
                "convention": "L_*",
            },
            {
                "name": "YELLOW",
                "idx": 22,
                "convention": None
            },
        ]
        buttons = []

        buttons.append(ColorAllButton(label="COLOR ALL",))
        for color in colors:
            button = ColorSelectionButton(label=color["name"],
                                          idx=color["idx"],)
            buttons.append(button)
        for button in buttons:
            self.layout.addWidget(button)
        self.layout.addStretch()


class Button(QtWidgets.QPushButton):

    def __init__(self, label="Button"):
        super().__init__()
        self.label = label
        self.setText(self.label)

        self.clicked.connect(self.do_btn_action)

    def do_btn_action(self):
        cmds.warning("ERROR: Base Button class, no functionality. ")


class ColorButton(Button):

    def do_btn_action(self):
        cmds.warning("ERROR: Base ColorButton class, no functionality.")


class ColorAllButton(ColorButton):

    def do_btn_action(self):
        # Define colors
        l_color = 6
        m_color = 17
        r_color = 13
        default_color = 22
        # Grab all controls
        cons = cmds.ls('*_CON')
        # Iterate through
        for con in cons:
            # Decide this con's color
            if con.startswith('L_'):
                color = l_color
            elif con.startswith('M_'):
                color = m_color
            elif con.startswith('R_'):
                color = r_color
            else:
                color = default_color
            # For shape in this con's relatives
            for s in cmds.listRelatives(con, s=True):
                # Enable override
                cmds.setAttr(s + '.overrideEnabled', 1)
                # set overrideColor
                cmds.setAttr(s + '.overrideColor', color)


class ColorSelectionButton(ColorButton):

    def __init__(self, label, idx):
        super().__init__(label)
        self.idx = idx

    def do_btn_action(self):
        selected_objs = cmds.ls(selection=True)
        all_curves = cmds.ls("*_CON")
        selected_curves = []

        if not selected_objs:
            cmds.warning("Nothing selected")
            return
        for curve in all_curves:
            if curve in selected_objs:
                selected_curves.append(curve)
        if not selected_curves:
            cmds.warning("No eligible curves selected")
            return
        for curve in selected_curves:
            for s in cmds.listRelatives(curve, s=True):
                cmds.setAttr(s + '.overrideEnabled', 1)
                cmds.setAttr(s + '.overrideColor', self.idx)
        cmds.select(clear=1)
