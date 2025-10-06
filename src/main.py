import os
import sys

import ctypes
import wx
import hostEditor
import home

if __name__ == '__main__':
    App = wx.App(False)
    frame = home.main(None)
    frame.Show(True)
    App.MainLoop()