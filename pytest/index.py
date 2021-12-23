import os
import sys
import win32com
import win32com.client
from win32com.client import Dispatch, DispatchEx

wordMain = Dispatch('Word.Application')
# 新建word文档
# doc = word.Documents.Add()

currrent_path = os.getcwd()

wordMain.Visible = True
# print(os.getcwd())
docMain = wordMain.Documents.Open(currrent_path + "/paper_part1.docx")
docMain.Activate()

# Accept all revisions
wordMain.ActiveDocument.Revisions.AcceptAll()

# 修改所有表格样式为三线表
try:
  for table in wordMain.ActiveDocument.Tables:
    # print(type("three_line1"))
    if(str(table.Style) == "three_line1"):
        print('不需要修改' + str(table.Style))
    else:
        print('已修改')
except:
  print('An exception occurred')
else:
    print('修改完成')



""" docMain.Close(False)
wordMain.Application.Quit()
sys.exit(0)  """


# 复制header文件并插入到头部

word1 = win32com.client.DispatchEx('Word.Application')

doc_header = word1.Documents.Open(currrent_path + "/header.docx")
# 复制word文件的所有内容
doc_header.Content.Copy()
doc_header.Close()

""" selection = wordMain.Selection
selection.HomeKey(6, 0)
selection.InsertBreak()
selection.HomeKey(6, 0)
selection.Paste() """


# 复制footer文件并插入到尾部

word2 = win32com.client.DispatchEx('Word.Application')

# 打开word文件，经测试要是绝对路径
doc_footer = word2.Documents.Open(currrent_path + "/footer.docx")
# 复制word文件的所有内容
doc_footer.Content.Copy()
# 关闭小文件
doc_footer.Close()

# doc1.Range().Select()
# doc.myRange.Selection.Paste()

selection = wordMain.Selection
# selection.MoveRight(1, docMain.Content.End) # 将光标移动到文末，就这一步试了我两个多小时
# 使用EndKey更快一些
# selection.EndKey(6,0)
# selection.InsertBreak()
# selection.Paste()


# 在目录二字下，生成目录
toc_count = docMain.TablesOfContents.Count  # 判断是否有无目录，如果数量是1则代表已经有目录了
if toc_count == 0:
    print('还没有目录')
    for i, p in enumerate(docMain.Paragraphs):  # 遍历word中的内容
        print('查找目录...')
        if '目录' in p.Range.Text:  # 用于指定目录页面，看下面提示
            print('正在生成目录...')
            p.Range.InsertBreak()
            p.Range.InsertBreak()
            # p.Range.InsertParagraphAfter()  # 添加新的段落 （容易出现 被呼叫方拒绝接收呼叫）
            # p.Range.InsertAfter("---")
            parag_range = docMain.Paragraphs(i+2).Range
            docMain.TablesOfContents.Add(Range=parag_range,
                                         UseHeadingStyles=True,
                                         UpperHeadingLevel=1,
                                         LowerHeadingLevel=3)  # 生成目录对象
            # p.Range.InsertParagraphAfter()
            # 跳出
            break

elif toc_count == 1:
    print('已经有目录了')
    toc = docMain.TablesOfContents(1)
    toc.Update()


wordMain.ActiveDocument.Save()
docMain.Close(False)
# wordMain.Quit()
wordMain.Application.Quit()
