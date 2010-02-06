#!/usr/bin/env python2.5


import sys
if 'darwin' in sys.platform:
    sys.path.append('/System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python/wx-2.8-mac-unicode/')
    sys.path.append('/Library/Python/2.6/site-packages/')
del sys

import wx

import pyshell
from pyshell import pyshell

import app
from app import wxmayaApps as appList, app

import m

import platform

import log
import log

import demos

import checkbox
from checkbox import checkbox

import button
from button import button



import mthread
from mthread import mthread

import callbackManager

