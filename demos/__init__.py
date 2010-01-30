
import wxmaya
import wx

from dockingWindowDemo import  dockingWindowDemo


class controls(wxmaya.app):
    def OnInitUI(self):
        self.title = "Controls Demo!"
        self.cb1 = wxmaya.checkbox(self.panel, 'testing wxmaya.checkbox', 'perspShape.renderable')
        
        
        def button(arg):
            wxmaya.m.mel('select perspShape')
        self.b1  = wxmaya.button(self.panel, 'select perspShape', button)
        
        self.setTitle("Controls Demo!")
        self.setSize( (300,80) )
        




# helloWorldGL need pyOpenGl to work, so if pyOpenGL is not installed, 
# we just ignore it. 
# TODO: add a class to initialize opengl using either Maya OpenMayaRender or Python OpenGL
try:
    import helloWorldGL
    reload(helloWorldGL)
    from helloWorldGL import helloWorldGL
except:
    pass
        


