import win32com
import win32com.client
import os

path = os.getcwd()
file_mode = path + r'\第一个文档.docx'
# document = Document(file_mode)
# # 读取word中的所有表格
# tables = document.tables
# document.tables[1].add_row()
app =win32com.client.Dispatch('Word.Application')
# 打开word，经测试要是绝对路径
doc = app.Documents.Open(file_mode)
# 复制word的所有内容
doc.Content.Copy()
# 关闭word
doc.Close()

word = win32com.client.DispatchEx('Word.Application')

doc1 = word.Documents.Open(path + r'\第二个文档.docx')
# myRange = doc1.Range(doc1.Content.End-1, doc1.Content.End-1)

# doc1.Range().Select()
#
# doc.myRange.Selection.Paste()
s = word.Selection
s.MoveRight(1, doc1.Content.End) # 将光标移动到文末，就这一步试了我两个多小时
s.Paste()
doc1.Close()