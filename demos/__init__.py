
import wxmaya

from dockingWindowDemo import  dockingWindowDemo


class controls(wxmaya.app):
    def OnInitUI(self):
        self.cb1 = wxmaya.checkbox(self.frame, 'testing wxmaya.checkbox', 'perspShape.renderable')
        self.cb1 = wxmaya.checkbox(self.frame, 'testing wxmaya.checkbox', 'perspShape.renderable')




# helloWorldGL need pyOpenGl to work, so if pyOpenGL is not installed, 
# we just ignore it. 
# TODO: add a class to initialize opengl using either Maya OpenMayaRender or Python OpenGL
try:
    import helloWorldGL
    reload(helloWorldGL)
    from helloWorldGL import helloWorldGL
except:
    pass
        


