#!/usr/bin/env python2.5

import maya.OpenMaya as OpenMaya
import log

global callbacks
try: 
    callbacks
except:
    callbacks=[]


def MObject(node):
    list = OpenMaya.MSelectionList()
    list.add( node )
    mobj = OpenMaya.MObject()
    list.getDependNode( 0, mobj )
    return mobj

def MPlug(nodeAttr):
    node, attr = nodeAttr.split('.')
    mobj  = __MObject(node)
    mplug = OpenMaya.MPlug( mobj, __MObject(nodeAttr) )
    return  mobj, mplug

class mayaCallBack:
    def __init__(self, callbackID = None):
        if type(callbackID)==type([]):
            self.callbackID = callbackID
        else:
            self.callbackID = [callbackID]
    def remove(self):
        for each in self.callbackID:
            if each:
                callbacks.append(each) # add callback ID here so swig object memory doesnt leak!
                OpenMaya.MMessage.removeCallback(each)
                log.write("mayaRemoveCallback: callbackID %d removed" % each)
                

class mayaConnectionCallback(mayaCallBack):
    def __init__(self, func):
        mayaCallBack.__init__(self, OpenMaya.MDGMessage.addConnectionCallback( func ) )

class mayaTimeChangeCallback(mayaCallBack):
    def __init__(self, func):
        mayaCallBack.__init__(self, OpenMaya.MDGMessage.addTimeChangeCallback( func ) )

class mayaNodeAddedCallback(mayaCallBack):
    def __init__(self, func, nodetype = "dependNode"):
        mayaCallBack.__init__(self, OpenMaya.MDGMessage.addNodeAddedCallback( func, nodetype ) )

class mayaNodeRemovedCallback(mayaCallBack):
    def __init__(self, func, nodetype = "dependNode"):
        mayaCallBack.__init__(self, OpenMaya.MDGMessage.addNodeRemovedCallback( func, nodetype ) )

class mayaNodeRemovedCallback(mayaCallBack):
    def __init__(self, func, nodetype = "dependNode"):
        mayaCallBack.__init__(self, OpenMaya.MDGMessage.addNameChangedCallback( func, nodetype ) )

class mayaAddForceUpdateCallback(mayaCallBack):
    def __init__( self, func ):
        mayaCallBack.__init__(self, OpenMaya.MDGMessage.addForceUpdateCallback( func ) )

class mayaAddTimeChangeCallback(mayaCallBack):
    def __init__( self, func ):
        mayaCallBack.__init__(self, OpenMaya.MDGMessage.addTimeChangeCallback( func ) )





class mayaNodeChangeCallback(mayaCallBack):
    def __init__(self, nodeAttr, callbackFunc):
        node, attr = nodeAttr.split('.')
        mobj = MObject(node)
        self.node = node
        self.attr = attr
        self.callbackFunc = callbackFunc

        callbackIDs = [
            OpenMaya.MNodeMessage.addAttributeChangedCallback( mobj, mayaNodeChangeCallback.attrChangedCallback, self ),
            OpenMaya.MNodeMessage.addNameChangedCallback(      mobj, mayaNodeChangeCallback.nameChangedCallback, self ),
            OpenMaya.MNodeMessage.addNodeAboutToDeleteCallback(   mobj, mayaNodeChangeCallback.deleteCallback, self  ),
        ]
        # add the callback list to be removed automatically when the class is deleted.
        mayaCallBack.__init__(self, callbackIDs)
    
    @staticmethod
    def attrChangedCallback( *args ):
        msg         = args[0]
        mplug       = args[1]
        otherMPlug  = args[2]
        self        = args[3]
        node, attr = mplug.name().split('.')
        
        logMsg = 'mayaNodeChangeCallback.attrChangedCallback: '
        
        # if attr changed
        if msg & OpenMaya.MNodeMessage.kAttributeSet:
            logMsg += '%s.%s -> OpenMaya.MNodeMessage.kAttributeSet' % (node, attr)
            self.callbackFunc()
        
        ''' TODO: add callbacks for all the possivel changes in a node, so the controls can reflect that change of state automatically 
            msg Mask for all possible change types:
              kConnectionMade = 0x01, kConnectionBroken = 0x02, kAttributeEval = 0x04, kAttributeSet = 0x08,
              kAttributeLocked = 0x10, kAttributeUnlocked = 0x20, kAttributeAdded = 0x40, kAttributeRemoved = 0x80,
              kAttributeRenamed = 0x100, kAttributeKeyable = 0x200, kAttributeUnkeyable = 0x400, kIncomingDirection = 0x800,
              kAttributeArrayAdded = 0x1000, kAttributeArrayRemoved = 0x2000, kOtherPlugSet = 0x4000, kLast = 0x8000
        '''
        
        log.write(logMsg)

    @staticmethod
    def nameChangedCallback( *args ):
        print 'nameChangedCallback:',args
        
 
    @staticmethod
    def deleteCallback( *args ):
        print 'deleteCallback:',args
        
     
     
     
     