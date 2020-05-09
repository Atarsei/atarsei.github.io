from bs4 import BeautifulSoup
outside ="<div><div id='div'></div></div><span></span>"
out_bf =BeautifulSoup(outside,features="html.parser")
print(out_bf)
inside = "<i>hhh<b>hhhh</b></i>"
in_bf =BeautifulSoup(inside,features="html.parser")
out_bf.find_all('div',id="div")[0].append(in_bf)
print(out_bf)