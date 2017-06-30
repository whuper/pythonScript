# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import wx

class InsertFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame With Button',
                size=(600, 400))
        panel = wx.Panel(self) #创建面板

        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five','six', 'seven', 'eight']
        self.choices = [u'中国', u'中文', u'中美', 'aunt', 'uncle', 'grandson', 'granddaughter']

        button = wx.Button(panel, label="Close", pos=(540, 10),
                size=(40, 20)) #将按钮添加到面板

         #定义普通样式的comboBox, 接受键盘输入，但不会改变Item
        commonLable = wx.StaticText(panel, -1, u"自动提示下拉框",pos=(100, 50),size=(150, -1))
        self.commonComboBox = wx.ComboBox(panel, -1, pos=(100, 80), size=(150, -1),value = "zero", choices = self.choices, style = wx.CB_DROPDOWN)

        #self.choices = choices
        #分别绑定多个事件，文本内容变化，字符输入
        self.commonComboBox.Bind(wx.EVT_TEXT, self.EvtText)
        self.commonComboBox.Bind(wx.EVT_CHAR, self.EvtChar)
        self.commonComboBox.Bind(wx.EVT_COMBOBOX, self.EvtCombobox) 
        self.commonComboBox.ignoreEvtText = False



        #绑定按钮的单击事件
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        #绑定窗口的关闭事件
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)



    def OnCloseMe(self, event):
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy()

    def EvtCombobox(self, event):
        self.commonComboBox.ignoreEvtText = True
        event.Skip()

    def EvtChar(self, event):
        #这里需要注意一点事，回车键如果不过滤掉的话，EvtText会类似于进入死循环，这里还不太清楚到底是为什么
        if event.GetKeyCode() == 8:
            self.commonComboBox.ignoreEvtText = True
        event.Skip()

    def EvtText(self, event):

        currentText = event.GetString()
        #这里先判断内容是否为空，如果为空的话，需要让下拉菜单隐藏起来
        if currentText=='':
            self.commonComboBox.SetItems(self.choices)
            self.commonComboBox.Dismiss()
        if self.commonComboBox.ignoreEvtText:
            self.commonComboBox.ignoreEvtText = False
            return

        currentText = event.GetString()
        found = False
        choiceTemp = []
        for choice in self.choices :
            if choice.startswith(currentText):
                self.commonComboBox.ignoreEvtText = True
                found = True
                choiceTemp.append(choice)
        #进行文本匹配后，如果存在的话，就将combobox的内容置为匹配到的列表,再弹出下拉菜单
        if found:
            print choiceTemp[0]
            self.commonComboBox.SetItems(choiceTemp)
            self.commonComboBox.Popup()
            self.commonComboBox.SetValue(currentText)
            self.commonComboBox.SetInsertionPoint(len(currentText))
            self.commonComboBox.ignoreEvtText = False
        if not found:
            self.commonComboBox.Dismiss()
            self.commonComboBox.SetInsertionPoint(len(currentText))
            event.Skip()

    def derivedRelatives(self, relative):
        return [relative, 'step' + relative, relative + '-in-law']


if __name__ == '__main__':
    app = wx.App()
    frame = InsertFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
