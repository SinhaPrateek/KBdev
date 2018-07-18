import os
import xml.dom.minidom as minidom

filedir = os.getcwd()+"/"+"files"+"/Anew"

def getText(nodelist):                  # always need to pass a list of node elements
    rc = []
    for node in nodelist:               # nodelist - [<DOM Element: title at 0x105fc7340>], node - <DOM Element: title at 0x105fc7340>
        onenodelist = node.childNodes   # onenodelist - [<DOM Text node "'The Effici'...">] "childNodes convert single Element obj to a single list of Textnode"
        for onenode in onenodelist:
            if onenode.nodeType == node.TEXT_NODE:
                rc.append(onenode.data)
    return '|'.join(rc)

def parseCitations(Elem):
    if Elem.getAttribute("name") == "ParsCit":
        citations = Elem.getElementsByTagName('citation')
        j = 0
        for citation in citations:
            j = j + 1
            cit_authors = citation.getElementsByTagName('author')
            cit_title = citation.getElementsByTagName("title")
            date = citation.getElementsByTagName("date")
            print("\n")
            print(getText(cit_title))
            print("\n")
            print(getText(date))
            print("\n")
            print(getText(cit_authors))
        print(j)

def parseHeading(Elem):
    if Elem.getAttribute("name") == "ParsHed":
        title = Elem.getElementsByTagName("title")
        author = Elem.getElementsByTagName("author")
        abstract = Elem.getElementsByTagName("abstract")
        print(getText(title))
        print("\n")
        print(getText(author))
        print("\n")
        print(getText(abstract))

        print("-----------------------")





i = 0
files = []
for file in os.listdir(filedir):
    i = i+1
    try:
        doc = minidom.parse(filedir + "/" + file)
        Elems = doc.getElementsByTagName('algorithm')
        for Elem in Elems:
            if Elem.getAttribute("name") == "ParsHed":
                title = Elem.getElementsByTagName("title")
                if len(title) == 1:
                    print(file)
                    print("\n")
                    parseHeading(Elem)
                else:
                    files.append(file)
                    break
            parseCitations(Elem)
    except:
        print(file)


print(i)
print(files)


