

pip3 install python-docx



https://www.cnblogs.com/deepwaterplan/articles/6664796.html

### Python操作Word（Win32com）
https://zhuanlan.zhihu.com/p/67543981


table.style='Medium Grid 1 Accent 1' 
or
document.add_table(3,4,style='Medium Grid 1 Accent 1')

windows 安装 pip install --user python_docx


output = word.Documents.Add()

output.Application.Selection.Range.InsertFile('second.doc')
output.Application.Selection.Range.InsertBreak()
output.Application.Selection.Range.InsertFile('first.doc')



# https://bbs.csdn.net/topics/390966063?list=262329

wordapp.Selection.endkey(6,0) wdStory 为 6 wdMove 为0

这样试试 
Selection.EndKey (6) Selection.InsertNewPage() Selection.TypeText ("456")

myRange.InsertBefore(translate_results) myRange.InsertBefore('\r\n')



### Python 使用 win32com 模块对 word 文件进行操作
https://www.cnblogs.com/zhuminghui/p/11765401.html


for x in wb.paragraphs:
​ x.text=x.text.replace(‘ABC’,‘DEF’)



## Word 中的 WdBreakType (枚举)


指定分隔符的类型。

| 名称                       | 值  | 说明                                                               |
|--------------------------|----|------------------------------------------------------------------|
| wdColumnBreak            | 8  | 插入点处的分栏符。                                                        |
| wdLineBreak              | 6  | 换行符。                                                             |
| wdLineBreakClearLeft     | 9  | 换行符。                                                             |
| wdLineBreakClearRight    | 10 | 换行符。                                                             |
| wdPageBreak              | 7  | 插入点处的分页符。                                                        |
| wdSectionBreakContinuous | 3  | 新节不包含相应分页符。                                                      |
| wdSectionBreakEvenPage   | 4  | 使下一节从下一偶数页开始的分节符。 如果分节符落入偶数页，则 Word 将下一奇数页留为空白。                  |
| wdSectionBreakNextPage   | 2  | 分节符在下一页。                                                         |
| wdSectionBreakOddPage    | 5  | 使下一节从下一奇数页开始的分节符。 如果分节符落入奇数页，则 Word 将下一偶数页留为空白。                  |
| wdTextWrappingBreak      | 11 | 结束当前行，并强制文字在图片、表格或其他项目的下方继续。 文字将在下一个空行（且该空行不包含与左边距或右边距对齐的表格）上继续。 |


# 在文档开头添加内容
myRange1 = doc.Range(0,0)
myRange1.InsertBefore('Hello word')

# 在文档末尾添加内容
myRange2 = doc.Range()
myRange2.InsertAfter('Bye word') 


# 在文档i指定位置添加内容
myRange3= doc.Range(0, insertPos) # insertPos为数字
myRange3.InsertAfter('what's up, bro?')

Python 使用 win32com 模块对 word 文件进行操作
https://www.cnblogs.com/zhuminghui/p/11765401.html