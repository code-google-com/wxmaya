#!/usr/bin/env python2.5

import app
del app
from app import *

import wx.py.shell

class pyshell(app):
    def OnInitUI(self):
        self.shell = wx.py.shell.Shell(self.panel)


if __name__ == '__main__':
    pyshell()
