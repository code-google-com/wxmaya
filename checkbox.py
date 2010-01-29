

import log
import m
import app
import wx

import controlBase 
reload(controlBase)
from controlBase import controlBase

class checkbox(controlBase):
    def __init__(self, panel, name='teste', attr=None):
        controlBase.__init__(self, panel, attr)
        self.control = wx.CheckBox(self.panel, -1, attr)#, (65, 40), (150, 20), wx.NO_BORDER)
        self.control.SetValue( bool(self.getAttr()) )

        self.panel.Bind(wx.EVT_CHECKBOX, self.callback, self.control)

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
