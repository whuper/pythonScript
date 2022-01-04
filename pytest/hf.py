from docx import Document

doc = Document('paper_part1.docx')

AllSections = doc.sections
def setHFooter():
    # 设置页眉
        # 先取消"链接到前一页页眉"
    AllSections[1].header.is_linked_to_previous = False    
    # AllSections[1].header.paragraphs[0].text = "基于IPA分析的杭州HT酒店感知服务质量提升研究"
    
    #设置页脚
    for index in range(1,4):
        print("index %d"  %(index))
        AllSections[index].footer.is_linked_to_previous = False          

setHFooter()

doc.save('paper_part1.docx')