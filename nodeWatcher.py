#
# A class to monitor nodes in realtime
#
# it monitors nodes in maya, returning updated values everytime
# its accessed!
#

import os
import maya.cmds as m

class nodeWatcher:
    def __init__(self, nodetype, attribute):
        self.list = {}
        self.path = {}
        self.nodetype = nodetype
        self.attribute = attribute
        self.__listAll()

    def __cleanList__(self):
        for each in self.list:
            x = []
            x.extend(self.list[each])
            for index in x:
                self.list[each].remove(index)
        
    def __listAll(self):
        self.__cleanList__()
        for each in m.ls(type=self.nodetype):
            cgfx = m.getAttr('%s.%s' % (each, self.attribute) )
            cgfxName = os.path.basename(cgfx)
            if cgfxName not in self.list:
                self.list[cgfxName]=[]
            if each not in self.path:
                self.path[each]=cgfx
            if each not in self.list[cgfxName]:
                self.list[cgfxName].append(each)
            
    
    def refresh(self):
        self.__listAll()

    def __getitem__(self, key):
        self.__listAll()
        return self.list[key]

    def __str__(self):
        self.__listAll()
        return str(self.list)

    def attachedGeo(self, node):
        shapez = {}
        sgs = m.connectionInfo( "%s.outColor" % node, dfs=True )
        for sg in sgs:
            sg = sg.split('.')[0]
            for index in m.getAttr( "%s.dagSetMembers" % sg, mi=True ):
                shape = m.connectionInfo( "%s.dagSetMembers[%s]" % (sg,index), sfd=True ).split('.')[0]
                shapez[shape] = m.listRelatives( shape, p=True)
        return shapez


