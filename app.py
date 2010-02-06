#!/usr/bin/env python2.5

import sys, os
import wx
import threading, time
import log

import m, platform

import callbackManager

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
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Hello from wxPython", size=(400,300))

class app(wx.App):
    def __init__(self, title="Hello from wxPython", size=(800,500), frameClass=frame ):
        self.size = size
        self.title = title
        self.__frameClass = frameClass
        if m.isMayaRunning :
            m.utils.executeDeferred(wx.App.__init__,self,0)
            self.runInMaya()
        else:
            wx.App.__init__(self,0)
            self.MainLoop()
        wxmayaAppsAdd(self)
        
    def setTitle(self, title):
        self.title = title

    def setFrameClass(self, frameClass):
        self.__frameClass = frameClass

    def setSize(self, size):
        self.size = size
        
    def OnInit(self):
        #self.menu_bar  = wx.MenuBar()
        #self.frame = wx.Frame(None, -1, "Hello from wxmaya", size=self.size)
        self.frame = self.__frameClass(None)
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
        
        #wx events
        self.frame.Bind(wx.EVT_CLOSE, self.close) 
        
        if hasattr(self, 'idle'):
            self.frame.Bind(wx.EVT_IDLE, self.idle) 
        
        #maya events
        if hasattr(self, 'connectionCallback'):
            def connectionCallback(*args):
                self.connectionCallback(args)
            self.__connectionCallbackOBJ = callbackManager.mayaConnectionCallback(connectionCallback)

        #if hasattr(self, 'nodeAddedCallback'):
        #    def nodeAddedCallback(*args):
        #        self.nodeAddedCallback(args)
        #    self.__nodeAddedCallbackOBJ = callbackManager.mayaNodeAddedCallback(nodeAddedCallback, 'mesh')

        #if hasattr(self, 'nodeRemovedCallback'):
        #    def nodeRemovedCallback(*args):
        #        self.nodeRemovedCallback(args)
        #    self.__nodeRemovedCallbackOBJ = callbackManager.mayaNodeRemovedCallback(nodeRemovedCallback, 'mesh')
            
        if hasattr(self, 'forceUpdateCallback'):
            def forceUpdateCallback(*args):
                self.forceUpdateCallback(args)
            self.__forceUpdateCallbackOBJ = callbackManager.mayaAddForceUpdateCallback(forceUpdateCallback)
            
        if hasattr(self, 'addTimeChangeCallback'):
            def addTimeChangeCallback(*args):
                self.addTimeChangeCallback(args)
            self.__forceUpdateCallbackOBJ = callbackManager.mayaAddTimeChangeCallback(addTimeChangeCallback)
    
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
        self.frame.DestroyChildren()
        if event:
            event.Skip()
        if hasattr(self, 'connectionCallback'):
            self.__connectionCallbackOBJ.remove()
            
        wxmayaAppsDel(self)

if __name__ == '__main__':
    app()
