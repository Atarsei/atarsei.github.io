import markdown
input_file = open("d:atarsei.github.io/hhh.md", mode="r", encoding="utf-8")
text = input_file.read()
#text.replace()
print(text)
print(markdown.markdown(text))