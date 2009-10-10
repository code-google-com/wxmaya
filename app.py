#!/usr/bin/env python2.5

import sys, os
import wx
import threading, time

isMayaRunning = False
try:
    import maya
    isMayaRunning = True
except:
    isMayaRunning = False


global wxmayaApps
try: 
    wxmayaApps 
except:
    wxmayaApps = []

 
def wxmayaAppsAdd(app):
    global wxmayaApps 
    try: 
        wxmayaApps 
    except:
        wxmayaApps = []
    wxmayaApps.append(app)

def wxmayaAppsDel(app):
    global wxmayaApps 
    try: 
        del wxmayaApps[wxmayaApps.index(app)]
    except:
        pass

class frame(wx.Frame):
    def __init__(self, title, size):
        wx.Frame.__init__(self, None, -1, "Hello from wxPython", size=size)

class app(wx.App):
    def __init__(self, size=(800,500) ):
        self.size = size
        if isMayaRunning :
            maya.utils.executeDeferred(wx.App.__init__,self,0)
            self.runInMaya()
        else:
            wx.App.__init__(self,0)
            self.MainLoop()
        wxmayaAppsAdd(self)
        
        
    def OnInit(self):
        self.menu_bar  = wx.MenuBar()
        #self.frame = wx.Frame(None, -1, "Hello from wxmaya", size=self.size)
        self.frame = frame("Hello from wxPython", size=self.size)
        
        if hasattr(self,'OnInitUI'):
            self.OnInitUI()
        
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        sys.displayhook = self.displayHook
        
        self.frame.Bind(wx.EVT_CLOSE, self.Close) 
        return True
    
    def displayHook(self, o):
        print o
        
        
    def runInMaya(self):
        self.keepGoing=True
        def process():
                while self.Pending():
                    self.Dispatch()
                self.ProcessIdle()
                        
        def thread():
            while self.keepGoing:
                time.sleep(0.1)
                maya.utils.executeDeferred(process)
            
        self.pumpedThread = threading.Thread(target = thread, args = ())
        self.pumpedThread.start() 

    def Close(self, event=None):
        self.keepGoing=False
        self.frame.Destroy()
        if event:
            event.Skip()
        wxmayaAppsDel(self)

if __name__ == '__main__':
    app()
