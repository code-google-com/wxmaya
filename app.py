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


class app(wx.App):
    def __init__(self, size=(800,500) ):
        self.size = size
        if isMayaRunning :
            maya.utils.executeDeferred(wx.App.__init__,self,0)
            self.runInMaya()
        else:
            wx.App.__init__(self,0)
            self.MainLoop()
    def OnInit(self):
        self.menu_bar  = wx.MenuBar()
        self.frame = wx.Frame(None, -1, "Hello from wxPython", size=self.size)
        
        try: self.OnInitUI()
        except: pass
        
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
            
        pumpedThread = threading.Thread(target = thread, args = ())
        pumpedThread.start() 

    def Close(self, event=None):
        self.keepGoing=False
        self.frame.Destroy()
        if event:
            event.Skip()

if __name__ == '__main__':
    app()
