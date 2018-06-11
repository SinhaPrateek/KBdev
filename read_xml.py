import xml.dom.minidom as minidom

class Read_XML:
    def __init__(self,file_path):
        self.doc = minidom.parse(file_path)
        self.Elems = self.doc.getElementsByTagName('algorithm')

    def getText(self,nodelist):                  # always need to pass a list of node elements
        rc = []
        for node in nodelist:               # nodelist - [<DOM Element: title at 0x105fc7340>], node - <DOM Element: title at 0x105fc7340>
            onenodelist = node.childNodes   # onenodelist - [<DOM Text node "'The Effici'...">] "childNodes convert single Element obj to a single list of Textnode"
            for onenode in onenodelist:
                if onenode.nodeType == node.TEXT_NODE:
                    rc.append(onenode.data)
        return '|'.join(rc)

    def parseCitations(self):
        if self.parseable() == "parseable":
            for Elem in self.Elems:
                if Elem.getAttribute("name") == "ParsCit":
                    citations = Elem.getElementsByTagName('citation')
                    j = 0
                    for citation in citations:
                        j = j + 1
                        cit_authors = citation.getElementsByTagName('author')
                        cit_title = citation.getElementsByTagName("title")
                        date = citation.getElementsByTagName("date")
                        print("\n")
                        print(self.getText(cit_title))
                        print("\n")
                        print(self.getText(date))
                        print("\n")
                        print(self.getText(cit_authors))
                    print(j)

    def parseHeading(self):
        if self.parseable() == "parseable":
            for Elem in self.Elems:
                if Elem.getAttribute("name") == "ParsHed":
                    title = Elem.getElementsByTagName("title")
                    author = Elem.getElementsByTagName("author")
                    abstract = Elem.getElementsByTagName("abstract")
                    print(self.getText(title))
                    print("\n")
                    print(self.getText(author))
                    print("\n")
                    print(self.getText(abstract))

    def getTitle(self):
        if self.parseable() == "parseable":
            for Elem in self.Elems:
                if Elem.getAttribute("name") == "ParsHed":
                    title = Elem.getElementsByTagName("title")
                    return self.getText(title)

    def getAuthors(self):
        if self.parseable() == "parseable":
            for Elem in self.Elems:
                if Elem.getAttribute("name") == "ParsHed":
                    author = Elem.getElementsByTagName("author")
                    return self.getText(author).split("|")

    def getAbstract(self):
        if self.parseable() == "parseable":
            for Elem in self.Elems:
                if Elem.getAttribute("name") == "ParsHed":
                    abstract = Elem.getElementsByTagName("abstract")
                    return self.getText(abstract)

    def getCitationTitle(self):
        if self.parseable() == "parseable":
            for Elem in self.Elems:
                if Elem.getAttribute("name") == "ParsCit":
                    citations = Elem.getElementsByTagName('citation')
                    citTitle = []
                    for citation in citations:
                        cit_title = citation.getElementsByTagName("title")
                        citTitle.append(self.getText(cit_title))
                    return citTitle


    def parseable(self):
        for Elem in self.Elems:
            if Elem.getAttribute("name") == "ParsHed":
                title = Elem.getElementsByTagName("title")
                if len(title) == 1:
                    return "parseable"
                else:
                    return "not_parseable"


