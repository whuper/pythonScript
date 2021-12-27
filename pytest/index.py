import os
import sys
import time
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
def tableFormat():
    try:
        for table in wordMain.ActiveDocument.Tables:
            # print(type("three_line1"))
            if(str(table.Style) == "three_line1"):
                print('不需要修改:' + str(table.Style))
            else:
                table.Style = "three_line1"
                print('修改成功')
    except:
        print('An exception occurred')
    else:
        print('表格样式无异常')


""" docMain.Close(False)
wordMain.Application.Quit()
sys.exit(0)  """


# 复制header文件并插入到头部
def copyHeader():
    word1 = win32com.client.DispatchEx('Word.Application')

    doc_header = word1.Documents.Open(currrent_path + "/header.docx")
    # 复制word文件的所有内容
    doc_header.Content.Copy()
    time.sleep(2)
    doc_header.Close()


    selection = wordMain.Selection
    selection.HomeKey(6, 0)
    selection.InsertBreak()
    selection.HomeKey(6, 0)
    selection.Paste()


# 复制footer文件并插入到尾部
def copyFooter():
    word2 = win32com.client.DispatchEx('Word.Application')

    # 打开word文件，经测试要是绝对路径
    doc_footer = word2.Documents.Open(currrent_path + "/footer.docx")
    # 复制word文件的所有内容
    doc_footer.Content.Copy()
    time.sleep(2)
    # 关闭小文件
    doc_footer.Close()

    # doc1.Range().Select()
    # doc.myRange.Selection.Paste()

    selection = wordMain.Selection
    # selection.MoveRight(1, docMain.Content.End) # 将光标移动到文末，就这一步试了我两个多小时
    # 使用EndKey更快一些
    selection.EndKey(6,0)
    selection.InsertBreak()
    selection.Paste()

tableFormat()
copyHeader()
copyFooter()

attempts = 0
success = False

toc_count = 0
ignoreOutline = False
while attempts < 3 and not success:
    try:
        toc_count = docMain.TablesOfContents.Count  # 判断是否有无目录，如果数量是1则代表已经有目录了,会尝试三次
        success = True
        print('获取目录成功')
        break
    except Exception as e:
        attempts += 1
        print('获取目录失败 ' + str(attempts) + '次，继续尝试..')
        # 暂停0.5秒
        time.sleep(0.5)

if not success:    
    ignoreOutline = True
    print('已忽略目录')
    print(e)

if toc_count == 0 and ignoreOutline == False:
    print('还没有目录')
    # for i, p in enumerate(docMain.Paragraphs):  # 遍历word中的内容
    for i in range(80):
        print('查找插入目录的段落...' + str(i))
        tempParagraph = docMain.Paragraphs[i]
        if '目录占位符' in tempParagraph.Range.Text:
            print('正在生成目录...')   
            placeholder = docMain.Paragraphs[i].Range            
            docMain.TablesOfContents.Add(Range=placeholder,
                                         UseHeadingStyles=True,
                                         UpperHeadingLevel=1,
                                         LowerHeadingLevel=3)  # 生成目录对象
           
            # 跳出
            break
        # 暂停 0.2秒
        time.sleep(0.2)

# placeholder.InsertBefore('\r\n')
# p.Range.InsertParagraphAfter()
# placeholder.InsertBreak()
# p.Range.InsertBreak()
# p.Range.InsertParagraphAfter()  # 添加新的段落 （容易出现 被呼叫方拒绝接收呼叫）
# p.Range.InsertAfter("---")
# p.Range.InsertBefore("---")

""" elif toc_count == 1:
    print('已经有目录了')
    toc = docMain.TablesOfContents(1)
    toc.Update() """


try:
    for i, p in enumerate(docMain.Paragraphs):  # 遍历word中的内容
        print('寻找分页符，再次查找段落...' + str(i))
        if '分页占位符' in p.Range.Text:
            # p.Range.Collapse()
            print('正在添加分页符...')
            p.Range.InsertBreak(7)
            time.sleep(0.5)
except Exception as e:
    print('插入分页符失败')
    print(e)


if(ignoreOutline == False and toc_count > 0):

    # 再更新一下目录，不然有时候没有...引导线
    outline = docMain.TablesOfContents(1)
    outline.Update()

wordMain.ActiveDocument.Save()
time.sleep(2)

docMain.Close(False)
wordMain.Application.Quit()
