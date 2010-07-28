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



import log
import m
import app
import wx

import controlBase 
from controlBase import controlBase

class checkbox(controlBase):
    def __init__(self, panel, name='teste', attr=None):
        controlBase.__init__(self, panel, attr)
        self.control = wx.CheckBox(self.panel, -1, attr)#, (65, 40), (150, 20), wx.NO_BORDER)
        self.control.SetValue( bool(self.getAttr()) )

        self.control.Bind(wx.EVT_CHECKBOX, self.callback, self.control)

    def refresh(self, event):
        log.write('checkbox.refresh: %d' % event)
        if self.attr and m.isMayaRunning:
            value = self.getAttr()
            if self.attrValue != value:
                self.control.SetValue( bool(value) )
                self.attrValue = value

    def callback(self, event):
        log.write('checkbox.callback: %d' % event.IsChecked())
        if self.attr and m.isMayaRunning:
            self.setAttr( int(event.IsChecked()) )
            
    def attrCallback(self, *args):
        if self.attr and m.isMayaRunning:
            value = self.getAttr()
            if self.attrValue != value:
                log.write( 'checkbox.attrCallback: attr %s changed outside %s to %d' % (self.attr, __name__, value) )
                self.control.SetValue( bool(value) )
                self.attrValue = value
