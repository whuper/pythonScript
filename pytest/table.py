from docx.enum.style import WD_STYLE_TYPE
from docx import Document
from docx.shared import Cm,Pt,RGBColor
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.enum.text import WD_ALIGN_PARAGRAPH


d=Document()
styles=d.styles
for s in styles:
    if s.type==WD_STYLE_TYPE.TABLE:
        print(s.name)

d.save('style.docx')