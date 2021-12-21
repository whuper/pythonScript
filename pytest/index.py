import os
import win32com
import win32com.client
from win32com.client import Dispatch,DispatchEx

wordMain = Dispatch('Word.Application')
# 新建word文档
# doc = word.Documents.Add()

currrent_path = os.getcwd()

wordMain.Visible = False
# print(os.getcwd())
docMain = wordMain.Documents.Open(currrent_path + "/paper_part1.docx")
docMain.Activate()

# Accept all revisions
wordMain.ActiveDocument.Revisions.AcceptAll()

for table in wordMain.ActiveDocument.Tables:
  # table.Style = "three_line1"
  print(table.Style)

# 复制header文件并插入到头部

# 打开word文件，经测试要是绝对路径
word1 = win32com.client.DispatchEx('Word.Application')
doc_header = word1.Documents.Open(currrent_path + "/paper_part2.docx")
# 复制word文件的所有内容
doc_header.Content.Copy()
# 关闭小文件
doc_header.Close()

# doc1.Range().Select()
# doc.myRange.Selection.Paste()

selection = wordMain.Selection
selection.HomeKey(6,0)
selection.InsertBreak()
# selection.Paste()



# 复制footer文件并插入到尾部

word2 = win32com.client.DispatchEx('Word.Application')

# 打开word文件，经测试要是绝对路径
doc_footer = word2.Documents.Open(currrent_path + "/paper_part2.docx")
# 复制word文件的所有内容
doc_footer.Content.Copy()
# 关闭小文件
doc_footer.Close()

# doc1.Range().Select()
# doc.myRange.Selection.Paste()

selection = wordMain.Selection
# selection.MoveRight(1, docMain.Content.End) # 将光标移动到文末，就这一步试了我两个多小时
#使用EndKey更快一些
# selection.EndKey(6,0)
# selection.InsertBreak()
# selection.Paste()


wordMain.ActiveDocument.Save()
docMain.Close(False)
wordMain.Application.Quit()

