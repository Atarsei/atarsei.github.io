import os,re,markdown
from bs4 import BeautifulSoup
Part = "\n\
    <article id=\"!id!\">\
        <title>!T</title>\
        <summary>!S</summary>\
        <label>!L</label>\
        <date>\
            <year>!Y</year>\
            <month>!M</month>\
            <day>!D</day>\
        </date>\
    </article>"
Dict={'!T':'','!S':'','!L':'','!Y':'','!M':'','!D':''}

Article = "\
<!DOCTYPE html>\
<html lang='zh'>\
<head>\
    <meta charset='UTF-8'>\
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>\
    <title>无题</title>\
    <link rel='stylesheet' href='/assets/css/base.css'>\
    <link rel='stylesheet' href='/assets/css/article.css'>\
</head>\
<body>\
    <div class='topmeau'></div>\
    <div class='all'>\
        <div class='article'>\
            <div class='content'></div>\
        </div>\
<div class='space'></div>\
<div class='side'></div>\
</div>\
<script src='/assets/js/Load.js'></script>\
<script>LoadHtmlWrite('/assets/Module/nav.html', 'topmeau')</script>\
<script>LoadXmlForPage()</script>\
<script>PhotoStatus()</script>\
<iframe src='/assets/Module/musicplayer.html' style='position: fixed;right:0;top:60px;width:300px;height:40px;border-style:none;'></iframe>\
</body>\
</html>"

root_path="D:/atarsei.github.io/"
""" 功能 """
def del_dom(path):#去掉文件名后缀
    list=os.listdir(path)
    llist=[]
    for i in list:
        i=i.strip(re.search(r'\..*',i).group())
        llist.append(i)
    return llist

def open_file(path):
    global File
    File = open(path,"r",encoding="utf-8").read()

def deal_dict(filename):#1.在markdown中读取特殊符号,生成dict 2.分别把这些运用到xml和html中
    global dict,File
    dict = Dict
    protection=["!S"]#不会被删除的内容的符号
    dict['!T']=filename
    for i in dict:
        if re.search(i+r'.*'+i,File)!=None:
            pattern=re.search(i+r'.*'+i,File).group()
            if i not in protection:
                File=File.replace(pattern,'')
            else:
                File=File.replace(i,'')
            dict[i]=pattern.strip(i)#替换dict的默认值

def change_article(content):
    global article
    article=Article.replace("<div class='content'></div>",content)

def write_html(text,path):
    with open(path,'w',encoding='utf-8')as f:
        f.write(text)
        f.close()

def change_part_write_xml(path,filename):
    part=Part.replace("!id!",filename)
    for i in dict:
        part=part.replace(i,dict[i])
    xml = open(path,"r",encoding="utf-8").read()
    with open(path,"w",encoding="utf-8") as f:
        f.write(
            xml[:xml.find("<all>")+len("<all>")]+
            part+
            xml[xml.find("<all>")+len("<all>"):]
        )
        f.close()
""" 运行 """
def new_page():
    page_list=del_dom(root_path+'article/page')
    makedown_list=del_dom(root_path+'article/markdown')
    for m in makedown_list:
        if m not in page_list:
            open_file(root_path+'article/markdown/'+m+'.md')
            deal_dict(m)
            change_article("<div class='content'>"+markdown.markdown(File,extensions=['extra'])+"</div>")
            write_html(article,root_path+'article/page/'+m+'.html')
            change_part_write_xml(root_path+"article/index.xml",m)
def new_style():
    page_list=del_dom(root_path+'article/page')
    for m in page_list:
        try:
            open_file(root_path+'article/page/'+m+'.html')      
            change_article(str(BeautifulSoup(File,features="html.parser").find_all("div",class_="content")[0]))
            write_html(article,root_path+'article/page/'+m+'.html') 
        except:
            print(m)



#write_xml(part,"d:/atarsei.github.io/article/index.xml")
#blog_system.py
'''
from bs4 import BeautifulSoup
def write_nav():
    soup_bf = BeautifulSoup(open('d:/atarsei.github.io/assets/Module/nav.html', encoding='utf-8'),features='html.parser')
    soup=soup_bf.find_all('div')
    return soup[0]
def write(filename,text):    
    #'d:/atarsei.github.io/test_text.html'
    with open(filename, 'w',encoding='utf-8') as file_object:
        file_object.write(str(text))
write('d:/atarsei.github.io/test_text.html',write_nav())
'''