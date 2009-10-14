#
# mthread - a class to create proper python threads in maya.
#
# just derive this class to your own to create a custom threaded class
# that does realtime updates in maya.
#
#


import time, threading, sys
import maya.cmds as m
import maya.utils


global __objects
global __thread

try: 
    __objects
    __objects=[]
    time.sleep(1.1) # wait so all old threads can finish if module has being reloaded!
except:
    __objects=[]    
    

def startPumpThread():
    global __thread
    try: 
        __thread
    except:
        __thread = threading.Thread(target = threadPumpObjects, args = ())
        __thread.start() 

def addObjects(obj):
    global __objects
    if obj not in __objects:
        __objects.append(obj)
    startPumpThread()
    
def removeObjects(obj, all=False):
    global __objects
    if all:
        __objects=[]
    elif obj in __objects:
        del __objects[ __objects.index(obj) ]    

def threadObjects():
    global __objects
    return __objects

def threadPumpObjects():
    global __objects
    global __thread
    while(__objects):
        time.sleep(1)
        for each in __objects:
            def runScriptJob():
                m.scriptJob( runOnce=True,  idleEvent=each.thread )
            maya.utils.executeInMainThreadWithResult( runScriptJob )
    del __thread


class mthread():
    def __init__(self):
        self.start()

    def thread(self):
        print '\n'.join( 
            filter(lambda x: str(self.__init__).split('<')[2].strip('>>') in x, m.scriptJob( listJobs=True ))
        ).strip()
        
    @staticmethod
    def threadList():
        return threadObjects()

    @staticmethod
    def stopAll():
        removeObjects(None,True)

    def start(self):
        addObjects(self)

    def stop(self,all=False):
        removeObjects(self,all)

    def __del__(self):
        self.stop()
