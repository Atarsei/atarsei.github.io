# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import os
def write_nav():
    soup_bf = BeautifulSoup(open('d:/atarsei.github.io/assets/Module/nav.html', encoding='utf-8'),features='html.parser')
    soup=soup_bf.find_all('div')
    return soup[0]
def write(filename,text):    
    #'d:/atarsei.github.io/test_text.html'
    with open(filename, 'w',encoding='utf-8') as file_object:
        file_object.write(str(text))
write('d:/atarsei.github.io/test_text.html',write_nav())