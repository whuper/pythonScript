import os
import sys
import time
import win32com
import win32com.client
from win32com.client import Dispatch


wordMain = Dispatch('Word.Application')
currrent_path = os.getcwd()

wordMain.Visible = False
docMain = wordMain.Documents.Open(currrent_path + "/20020181225-王文豪.docx")
docMain.Activate()

# Accept all revisions
wordMain.ActiveDocument.Revisions.AcceptAll()


# 插入页眉
def setPageHeader():
    AllSections = wordMain.ActiveDocument.Sections
    sectionQuantity = len(AllSections)
    print("共有 %d 节" %(sectionQuantity))
    
    # 为第二个节设置页眉
    headersCollection = AllSections[1].Headers
    for header in headersCollection:
        header.Range.Text = "基于IPA分析的杭州HT酒店感知服务质量提升研究"

setPageHeader()