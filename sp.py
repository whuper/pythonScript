#coding:utf-8

import re, urllib

strTitle = ""
strTxtTmp = ""
strTxtOK = ""

f = open("163News.txt", "w+")

m = re.findall(r"news\.163\.com/\d.+?<\/a>",urllib.urlopen("http://www.163.com").read(),re.M)

for i in m:
    testUrl = i.split('"')[0]
    if testUrl[-4:-1]=="htm":

    
        strTitle = strTitle + "\n" + i.split('"')[0] + i.split('"')[1]  # 合并标题头内容

        okUrl = i.split('"')[0] # 重新组合链接
        UrlNews = ''
        UrlNews = "http://" + okUrl
        
        print UrlNews

        n = re.findall(r"<P style=.TEXT-INDENT: 2em.>(.*?)<\/P>",urllib.urlopen(UrlNews).read(),re.M)
        for j in n:
            if len(j)<>0:
                j = j.replace("&nbsp","\n")
                j = j.replace("<STRONG>","\n_____")
                j = j.replace("</STRONG>","_____\n")
                strTxtTmp = strTxtTmp + j + "\n"
                strTxtTmp = re.sub(r"<a href=(.*?)>", r"", strTxtTmp)
                strTxtTmp = re.sub(r"<\/[Aa]>", r"", strTxtTmp)
    
        strTxtOK = strTxtOK + "\n\n\n===============" + i.split('"')[0] + i.split('"')[1] + "===============\n" + strTxtTmp


        strTxtTmp = "" # 组合链接标题和正文内容
        print strTxtOK


f.write(strTitle + "\n\n\n" + strTxtOK)# 全部分析完成后，写入文件
f.close()#关闭文件
