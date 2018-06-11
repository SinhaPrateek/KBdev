from main.read_xml import Read_XML
class Author:
    def __init__(self,author_id,author_name):
        self.author_id = author_id
        self.author_name = author_name

class Title:
    def __init__(self,title_id,title_name):
        self.title_id = title_id
        self.title = title_name

class Topic:
    def __init__(self,topic_id,topic_name):
        self.topic_id = topic_id
        self.topic = topic_name

class Paper:
    def __int__(self,title,authors,topics,papers):
        self.title = title
        self.authors = authors
        self.topics = topics
        self.papers = papers
        self.read_xml_obj = Read_XML(file)