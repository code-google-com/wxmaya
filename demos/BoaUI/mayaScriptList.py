#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1TREECTRL1, 
] = [wx.NewId() for _init_ctrls in range(2)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(520, 321), size=wx.Size(280, 464),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self.SetClientSize(wx.Size(272, 437))

        self.treeCtrl1 = wx.TreeCtrl(id=wxID_FRAME1TREECTRL1, name='treeCtrl1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(272, 437),
              style=wx.TR_HAS_BUTTONS)
        self.treeCtrl1.Bind(wx.EVT_TREE_ITEM_ACTIVATED,
              self.OnTreeCtrl1TreeItemActivated, id=wxID_FRAME1TREECTRL1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTreeCtrl1TreeItemActivated(self, event):
        event.Skip()
