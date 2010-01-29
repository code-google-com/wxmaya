#!/usr/bin/env python2.5

import maya.OpenMaya as OpenMaya
import log
reload( log )

global callbacks
try: 
    callbacks
except:
    callbacks={}


def __MObject(node):
    list = OpenMaya.MSelectionList()
    list.add( node )
    mobj = OpenMaya.MObject()
    list.getDependNode( 0, mobj )
    return mobj

def __MPlug(nodeAttr):
    node, attr = nodeAttr.split('.')
    mobj  = __MObject(node)
    mplug = OpenMaya.MPlug( mobj, __MObject(nodeAttr) )
    return  mobj, mplug


def addCallback(nodeAttr, callbackFunc):
    node, attr = nodeAttr.split('.')
    mobj = __MObject(node)

    if callbacks.has_key(node):
        callbacks[ node ][ attr ] = callbackFunc
    else:
        callbacks[ node ] = {
            attr       : callbackFunc,
            'callbacks' : {
                'attr'   : OpenMaya.MNodeMessage.addAttributeChangedCallback( mobj, attrChangedCallback ),
                'node'   : OpenMaya.MNodeMessage.addNameChangedCallback(      mobj, nameChangedCallback ),
                'delete' : OpenMaya.MNodeMessage.addNodePreRemovalCallback(   mobj, deleteCallback ),
            },
        }
            
def attrChangedCallback( *args ):
    msg         = args[0]
    mplug       = args[1]
    otherMPlug  = args[2]
    node, attr = mplug.name().split('.')
    
    logMsg = '__calbackManager.attrChangedCallback: '
    
    # if attr changed
    if msg & OpenMaya.MNodeMessage.kAttributeSet:
        logMsg += '%s.%s -> OpenMaya.MNodeMessage.kAttributeSet' % (node, attr)
        callbacks[ node ][ attr ]()
    
    ''' TODO: add callbacks for all the possivel changes in a node, so the controls can reflect that change of state automatically 
        msg Mask for all possible change types:
          kConnectionMade = 0x01, kConnectionBroken = 0x02, kAttributeEval = 0x04, kAttributeSet = 0x08,
          kAttributeLocked = 0x10, kAttributeUnlocked = 0x20, kAttributeAdded = 0x40, kAttributeRemoved = 0x80,
          kAttributeRenamed = 0x100, kAttributeKeyable = 0x200, kAttributeUnkeyable = 0x400, kIncomingDirection = 0x800,
          kAttributeArrayAdded = 0x1000, kAttributeArrayRemoved = 0x2000, kOtherPlugSet = 0x4000, kLast = 0x8000
    '''
    
    log.write(logMsg)
        
def nameChangedCallback( *args ):
    msg         = args[0]
    mplug       = args[1]
    otherMPlug  = args[2]
    node, attr = mplug.name().split('.')
    
    
def deleteCallback( *args ):
    msg         = args[0]
    mplug       = args[1]
    otherMPlug  = args[2]
        
        
     
     
     
     