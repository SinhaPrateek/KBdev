import networkx as nx

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

    def create_subgraph(self):
        ####### create paper subgraph , since Au-T,Au-Au,T-T,Au-Ti,T-Ti are possble nodes,
        # so they were taken in one list. Then they will be added as nodes and edges can be geerated between all combination of these nodes at once
        combinedList = self.authors + self.topics
        combinedList.append(self.title)
        # print("full list" + str(combinedList))
        paperSG = nx.complete_graph(combinedList)
        print("number of nodes is " + str(paperSG.number_of_nodes()) + " number of edges is " + str(paperSG.number_of_edges()) + " and edges are: " + str(list(paperSG.edges)) + "\n")

        ######## adding Ti-Ci edges
        # citations = Paper_obj.citpapers
        # for citation in citations:
        #     paperSG.add_edge(Paper_obj.title,citation)
        #     print("After adding citations ,number of nodes is " + str(paperSG.number_of_nodes()) + " number of edges is " + str(paperSG.number_of_edges()) + "and edges are: " + str(list(paperSG.edges)))

        return paperSG



