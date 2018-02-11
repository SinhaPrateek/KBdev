import os
import xml.dom.minidom as minidom

filedir = os.getcwd()+"/"+"files"+"/"+"A"+"/"+"A00"

def getText(nodelist):
    rc = []
    for node in nodelist:               # nodelist - [<DOM Element: title at 0x105fc7340>], node - <DOM Element: title at 0x105fc7340>
        onenodelist = node.childNodes   # onenodelist - [<DOM Text node "'The Effici'...">] "childNodes convert single Element obj to a single list of Textnode"
        for onenode in onenodelist:
            if onenode.nodeType == node.TEXT_NODE:
                rc.append(onenode.data)
    return '|'.join(rc)


i = 0
files = []
for file in os.listdir(filedir):
    i = i+1
    doc = minidom.parse(filedir + "/" + file)
    Elems = doc.getElementsByTagName('algorithm')
    for Elem in Elems:
        if Elem.getAttribute("name") == "ParsHed":
            title = Elem.getElementsByTagName("title")
            author = Elem.getElementsByTagName("author")
            abstract = Elem.getElementsByTagName("abstract")
            if len(title) == 1:
                print(file)
                print("\n")
                print(getText(title))
                print("\n")
                print(getText(author))
                print("\n")
                print(getText(abstract))
                print("-----------------------")
            else:
                files.append(file)

print(i)
print(files)