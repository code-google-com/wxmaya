

isMayaRunning = False
try:
    # if outside maya, init maya!
    #try:
    #    import maya.standalone maya.standalone.initialize( )
    #except:
    #    pass

    # now import the modules we need into m
    from maya.cmds import * 
    from maya import utils
    
    # trying to fix OSX
    import sys
    sys.stdin.write = lambda self, data: utils.executeDeferred(data)
    sys.stdin.flush = lambda self: None
    
    isMayaRunning = True
except:
    isMayaRunning = False
