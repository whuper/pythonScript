#-*- encoding:UTF-8 -*-
import wx
import sys, glob

class DemoFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1,
                          "wx.ListCtrl in wx.LC_ICON mode",
                          size=(600,400))

        # load some images into an image list
        il = wx.ImageList(32,32, True)#创建图像列表
        for name in glob.glob("icon??.png"):
            bmp = wx.Bitmap(name, wx.BITMAP_TYPE_PNG)
            il_max = il.Add(bmp)

        # create the list control
        #创建列表窗口部件
        self.list = wx.ListCtrl(self, -1, 
                style=wx.LC_ICON | wx.LC_AUTOARRANGE)

        # assign the image list to it
        self.list.AssignImageList(il, wx.IMAGE_LIST_NORMAL)

        # create some items for the list
        #为列表创建一些项目
        for x in range(25):
            img = x % (il_max+1)
            self.list.InsertImageStringItem(x, 
                    "This is item %02d" % x, img)

app = wx.PySimpleApp()
frame = DemoFrame()
frame.Show()
app.MainLoop()
