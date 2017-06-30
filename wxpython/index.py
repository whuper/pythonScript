#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx 
 
app = wx.App() 
window = wx.Frame(None, title = "wxPython - haohao", size = (400,300)) 
panel = wx.Panel(window) 
label = wx.StaticText(panel, label = "Hello World Wangwenhao", pos = (100,100)) 
window.Show(True) 
app.MainLoop() 
