#!/usr/bin/env python2.5

import sys, os
import wx
import threading, time
import log

import m, platform


class __applist(list):
    def killall(self):
        for each in self:
            each.close()

global wxmayaApps
try: 
    wxmayaApps 
except:
    wxmayaApps = __applist()

class __cleanClass__:
    pass

def wxmayaAppsAdd(app):
    global wxmayaApps 
    try: 
        wxmayaApps 
    except:
        wxmayaApps = __applist()
    wxmayaApps.append(app)

def wxmayaAppsDel(app):
    global wxmayaApps 
    try: 
        del wxmayaApps[wxmayaApps.index(app)]
    except:
        pass
    del app

class frame(wx.Frame):
    def __init__(self, title, size):
        wx.Frame.__init__(self, None, -1, "Hello from wxPython", size=size)

class app(wx.App):
    def __init__(self, title="Hello from wxPython", size=(800,500) ):
        self.size = size
        self.title = title
        if m.isMayaRunning :
            m.utils.executeDeferred(wx.App.__init__,self,0)
            self.runInMaya()
        else:
            wx.App.__init__(self,0)
            self.MainLoop()
        wxmayaAppsAdd(self)
        
    def setTitle(self, title):
        self.title = title

    def setSize(self, size):
        self.size = size
        
    def OnInit(self):
        self.menu_bar  = wx.MenuBar()
        #self.frame = wx.Frame(None, -1, "Hello from wxmaya", size=self.size)
        self.frame = frame(self.title, size=self.size)
        self.panel = wx.Panel(self.frame, -1)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.gap = 0
        
        if hasattr(self,'OnInitUI'):
            self.OnInitUI()

        panelChildren = self.panel.GetChildren()
        if len(panelChildren):
            for each in panelChildren:
                self.sizer.Add( each, 1, wx.EXPAND |wx.ALL, self.sizer.gap )
            self.panel.SetSizer(self.sizer)
        else:
            self.frame.RemoveChild(self.panel)

        self.frame.SetSize(self.size)
        self.frame.SendSizeEvent()
        self.frame.SetLabel(self.title)
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        sys.displayhook = self.displayHook
        
        self.frame.Bind(wx.EVT_CLOSE, self.close) 
        
        if hasattr(self, 'idle'):
            self.frame.Bind(wx.EVT_IDLE, self.idle) 
            
        return True
    
    def displayHook(self, o):
        print o
        
        
    def runInMaya(self):
        evtloop = self
        # this fixes threading problems in OSX, but causes exceptions in Windows
        # so, its a OSX only feature.
        if platform.osx:
            evtloop    = wx.EventLoop()
            oldEvtloop = wx.EventLoop.GetActive()
        self.keepGoing=True
        def process():
                if evtloop != self:
                    wx.EventLoop.SetActive(evtloop)
                while evtloop.Pending():
                    evtloop.Dispatch()
                self.ProcessIdle()
                if evtloop != self:
                    wx.EventLoop.SetActive(oldEvtloop)
                        
        def thread():
            while self.keepGoing:
                time.sleep(0.2)
                m.utils.executeDeferred(process)
            
        self.pumpedThread = threading.Thread(target = thread, args = ())
        self.pumpedThread.start() 

        
    def close(self, event=None):
        log.write('app.close: %s' % str(event))
        self.keepGoing=False
        self.frame.Destroy()
        if event:
            event.Skip()
        wxmayaAppsDel(self)

if __name__ == '__main__':
    app()
