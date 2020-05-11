import os,sys
path="D:/atarsei.github.io/CubismSdkForWeb-4-r.1/Samples/TypeScript/Demo/node_modules"
for i in os.listdir(path):
    if os.path.exists(path+"/"+i+"/readme.md"):
        os.remove(path+"/"+i+"/readme.md")
    if os.path.exists(path+"/"+i+"/Readme.md"):
        os.remove(path+"/"+i+"/Readme.md")
    if os.path.exists(path+"/"+i+"/README.md"):
        os.remove(path+"/"+i+"/README.md")
    if os.path.exists(path+"/"+i+"/CHANGELOG.md"):
        os.remove(path+"/"+i+"/CHANGELOG.md")