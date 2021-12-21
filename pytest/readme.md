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