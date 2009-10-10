#!/usr/bin/env python2.5


import sys
if 'darwin' in sys.platform:
    sys.path.append('/System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python/wx-2.8-mac-unicode/')
    sys.path.append('/Library/Python/2.6/site-packages/')

import wx

import pyshell
reload(pyshell)
from pyshell import pyshell

import app
reload(app)
from app import wxmayaApps as appList, app

# helloWorldGL need pyOpenGl to work, so if pyOpenGL is not installed, 
# we just ignore it. 
# TODO: add a class to initialize opengl using either Maya OpenMayaRender or Python OpenGL
try:
    import helloWorldGL
    reload(helloWorldGL)
    from helloWorldGL import helloWorldGL
except:
    pass
