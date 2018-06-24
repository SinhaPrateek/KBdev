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
    def __init__(self,title_id,authors_id,topics_id,cit_paper_id):
        self.title = title_id
        self.authors = authors_id
        self.topics = topics_id
        self.citpapers = cit_paper_id
