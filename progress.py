#!/usr/bin/env python2.5
##########################################################################
#
#  Copyright (c) 2010, Roberto Hradec. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#
#     * Neither the name of Image Engine Design nor the names of any
#       other contributors to this software may be used to endorse or
#       promote products derived from this software without specific prior
#       written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
##########################################################################


from app import *
import m
import wx, time

class progress(app):
    def __init__(self, max=10, title="Go get a cofee! =)", msg="Please wait...", size=(250,220), onTop=False):
        self.max = max
        self.title = title
        self.msg = msg
        self.count = 0
        self.onTop = onTop
        app.__init__(self, title, size=size, hidden=True)

    @staticmethod
    def getCurrent():
        dlg = filter( lambda x: type(x) is progress, wxmayaApps)
        if dlg:
            return dlg[0]
        else:
            return None


    def MainLoop(self):
        self.runInMaya()
        
    def OnInit(self):
        if not hasattr(self, 'dlg'):
            self.dlg = wx.ProgressDialog(self.title,
                self.msg,
                maximum = self.max,
                parent=None,
                style = wx.PD_CAN_ABORT
                | wx.STAY_ON_TOP*self.onTop
                | wx.DIALOG_NO_PARENT
                | wx.PD_SMOOTH
                | wx.PD_ELAPSED_TIME
                | wx.PD_ESTIMATED_TIME
                | wx.PD_REMAINING_TIME
            )
        self.dlg.SetSize(self.size)
        self.dlg.CentreOnScreen()

        self.dlg.Show(True)
        self.dlg.Refresh()
        self.SetTopWindow(self.dlg)
        
        return True
    
    def checkMayaIsDone(self):
        if m.isMayaRunning:
            count = 0
            while(not hasattr(self,'dlg')):
                m.utils.processIdleEvents()
                count += 1 
                if count>10:
                    raise Exception("ERROR: wxmaya got stuck on progress class")

   
    def setMsg(self, msg):
        self.update( msg=msg )
        
    def update(self, msg=None, count=None):
        self.checkMayaIsDone()

        ret = True
        if count:
            self.count=count
        if msg:
            self.msg = msg
        else:
            self.count += 1
            
        if self.count<=self.max:
            ret = self.dlg.Update(self.count, newmsg=self.msg)
            if not ret[0]:
                self.close()
                raise Exception("Execution aborted by user!")
        else:
            self.close()
        
        
    def close(self):
        self.checkMayaIsDone()
        self.frame = self.dlg
        app.close(self)


if __name__ == '__main__':
    progress()
