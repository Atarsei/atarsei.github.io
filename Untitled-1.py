# -*- coding:UTF-8 -*-
import markdown
input_file = open(file="D:/atarsei.github.io/assets/js/node_modules/marked/README.md", mode="r", encoding="utf-8")
text = input_file.read()
#text.replace()
""" print(text)
print(markdown.markdown(text)) """
with open("readme.html",'w',encoding='utf-8')as file:
    file.write(markdown.markdown(text,extensions=['extra']))
