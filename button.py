

import log
import m
import app
import wx

from controlBase import controlBase

class button(controlBase):
    def __init__(self, panel, name='teste', default=False, attr=None, pos=[0,0], size=[10,200], style=0, validator=wx.Validator()):
        controlBase.__init__(self, panel, attr)
        self.name = name
        self.control = wx.Button(self.panel, -1, name, pos, size, style, validator, name)#, (65, 40), (150, 20), wx.NO_BORDER)
        
        #self.control.SetDefault(default)
        
        self.panel.Bind(wx.EVT_BUTTON, self.callback, self.control)


    def callback(self, event):
        log.write('button.callback: %s' % (self.name) )
        if self.attr and m.isMayaRunning:
            self.setAttr( int(event.IsChecked()) )
            

