import os,re,markdown
part = "\n\
    <article>\
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

article = "\
<!doctype html>\
<html>\
</html>"

root_path="D:/atarsei.github.io/"
""" 功能 """
def del_dom(path):#去掉文件名后缀
    list=os.listdir(path)
    for i in list:
        list.remove(i)
        i=i.strip(re.search(r'\..*',i).group())
        list.append(i)
    return list

def deal_dict(Dict,path):#1.在markdown中读取特殊符号,生成dict 2.分别把这些运用到xml和html中
    global dict,mdfile
    dict = Dict
    protection=["!S"]#不会被删除的内容的符号
    mdfile=open(path,"r",encoding="utf-8").read()
    for i in dict:
        if re.search(i+r'.*'+i,mdfile)!=None:
            pattern=re.search(i+r'.*'+i,mdfile).group()
            if i not in protection:
                mdfile=mdfile.replace(pattern,'')
            else:
                mdfile=mdfile.replace(i,'')
            dict[i]=pattern.strip(i)

def write_html(text,path):
    with open(path,'w',encoding='utf-8')as file:
        file.write(markdown.markdown(text,extensions=['extra']))
        file.close()

def write_xml(part,dict,path):
    for i in dict:
        part=part.replace(i,dict[i])
    xml = open(path,"r",encoding="utf-8").read()
    with open(path,"w",encoding="utf-8") as file:
        file.write(
            xml[:xml.find("<all>")+len("<all>")]+
            part+
            xml[xml.find("<all>")+len("<all>"):]
        )
        file.close()
""" 运行 """
page_list=del_dom(root_path+'article/page')
makedown_list=del_dom(root_path+'article/markdown')
for m in makedown_list:
    if m not in page_list:
        deal_dict(Dict,root_path+'article/markdown/'+m+'.md')
        write_html(mdfile,root_path+'article/page/'+m+'.html')
        write_xml(part,dict,root_path+"article/index.xml")

        
        




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