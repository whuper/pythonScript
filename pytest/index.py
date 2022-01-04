import os
import sys
import time
import win32com
import win32com.client
from win32com.client import Dispatch, DispatchEx


def print_obj(obj): 
  print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))


try:
 # 脚本名后面接收一个参数，通过sys.argv[1] 获取，参数为1(默认，number)，2，3，4, 等于4的时候会从 【插入目录，分页符】开始, 5的时候从页眉页脚开始
  start_step = int(sys.argv[1])
except:
  start_step = 1

# print(type(start_step))
# print(start_step)


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
sys.exit(0) """


# 复制header文件并插入到头部
def copyHeader():
    word1 = win32com.client.DispatchEx('Word.Application')

    doc_header = word1.Documents.Open(currrent_path + "/header.docx")
    # 复制word文件的所有内容
    doc_header.Content.Copy()
    time.sleep(2)
    doc_header.Close()
    time.sleep(1)

    selection = wordMain.Selection
    # selection.HomeKey(6, 0)
    # selection.InsertBreak()
    selection.HomeKey(6, 0)
    time.sleep(1)
    selection.Paste()
    time.sleep(1)

# 插入页眉
def setPageHeader():
    doc = wordMain.ActiveDocument       
    sections = doc.Sections
    for section in sections:
        headersCollection = section.Headers
        for header in headersCollection:
            header.Range.Text = "基于IPA分析的杭州HT酒店感知服务质量提升研究"

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
    time.sleep(1)

    # doc1.Range().Select()
    # doc.myRange.Selection.Paste()

    selection = wordMain.Selection
    # selection.MoveRight(1, docMain.Content.End) # 将光标移动到文末，就这一步试了我两个多小时
    # 使用EndKey更快一些
    time.sleep(0.5)
    selection.EndKey(6,0)
    selection.InsertBreak()
    time.sleep(0.5)
    selection.Paste()
    time.sleep(1)

# 查找是否已经插入过头部了
""" mainRange = docMain.Content
if mainRange.find.Execute('论文题目'):
    hasHeader = True

if mainRange.find.Execute('访谈记录'):
    hasFooter = True 

"""


if(start_step <= 1):
    tableFormat()

if(start_step <= 2):
    copyHeader()
if(start_step <= 3):
    copyFooter()


# strHello = "the length of (%s) is %d" %('Hello World',len('Hello World'))




# 插入分节符
lst = iter(range(100))
for i in lst:
    print('查找分节符的段落%d...' %(i))
    tempParagraph = docMain.Paragraphs[i]
    if '分节符在下一页占位符' in tempParagraph.Range.Text:
        print('正在插入分节符...')
        tempParagraph.Range.InsertBreak(2)
        # tempParagraph.Delete()
        tempParagraph.Range.InsertBreak(6)
        time.sleep(0.5)
        # lst.__next__() # 跳过下次循环

time.sleep(1)


print('尝试插入目录')
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
        print('获取目录失败 %d 次，继续尝试..' %(attempts))
        # 暂停0.5秒
        time.sleep(0.5)

if not success:    
    ignoreOutline = True
    print('已忽略目录')
    print(e)

if toc_count == 0 and ignoreOutline == False:
    print('还没有目录')
    # for i, p in enumerate(docMain.Paragraphs):  # 遍历word中的内容
    for i in range(100):
        print('查找插入目录的段落%d...' %(i))
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


# 插入分页符
try:
    for i, p in enumerate(docMain.Paragraphs):  # 遍历word中的内容
        print('寻找分页符，再次查找段落%d ...'  %(i))
        if '分页占位符' in p.Range.Text:
            # p.Range.Collapse()
            print('正在添加分页符...')
            p.Range.InsertBreak(7)
            time.sleep(0.5)
            continue
except Exception as e:
    print('插入分页符失败')
    print(e)

time.sleep(0.5)


if(ignoreOutline == False and toc_count > 0):

    # 再更新一下目录，不然有时候没有...引导线
    outline = docMain.TablesOfContents(1)
    outline.Update()

wordMain.ActiveDocument.Save()
time.sleep(2)


# 为每一节设置页眉和页脚
AllSections = wordMain.ActiveDocument.Sections
sectionQuantity = len(AllSections)
print("共有 %d 节" %(sectionQuantity))


wordMain.ActiveDocument.Save()
time.sleep(2)

docMain.Close(False)
wordMain.Application.Quit()

