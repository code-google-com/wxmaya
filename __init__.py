#!/usr/bin/env python2.5


import sys
if 'darwin' in sys.platform:
    sys.path.append('/System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python/wx-2.8-mac-unicode/')
    sys.path.append('/Library/Python/2.6/site-packages/')
del sys

import wx

import pyshell
reload(pyshell)
from pyshell import pyshell

import app
reload(app)
from app import wxmayaApps as appList, app

import mthread
reload(mthread)
from mthread import mthread


import m
reload(m)

import platform
reload(platform)

import log
reload(log)

import demos
reload(demos)

import checkbox
reload(checkbox)
from checkbox import checkbox

