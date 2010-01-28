
import wxmaya
import wx

from dockingWindowDemo import  dockingWindowDemo


class controls(wxmaya.app):
    def OnInitUI(self):
        self.cb1 = wxmaya.checkbox(self.panel, 'testing wxmaya.checkbox', 'perspShape.renderable')
        self.b1  = wxmaya.button(self.panel, 'testing wxmaya.checkbox')
        




# helloWorldGL need pyOpenGl to work, so if pyOpenGL is not installed, 
# we just ignore it. 
# TODO: add a class to initialize opengl using either Maya OpenMayaRender or Python OpenGL
try:
    import helloWorldGL
    reload(helloWorldGL)
    from helloWorldGL import helloWorldGL
except:
    pass
        


