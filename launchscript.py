# Add this to your Maya shelf, or run it with the Maya Script Editor
import CrystalRigHelper.crystalrighelper as CRigHelper
import importlib

importlib.reload(CRigHelper)
win = CRigHelper.Window()
win.show()
