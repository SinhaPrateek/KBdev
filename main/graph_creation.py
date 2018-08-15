from poc1.main.classFiles import Paper
import os
import json
import networkx as nx
import matplotlib.pyplot as plt

final_paper_class_file = os.getcwd()+ "/" + "files" + "/db_creation" + "/final_paper_class.json"
graph_file_gml = os.getcwd()+ "/" + "files" + "/db_creation" + "/graph_file_gml.json"  #gml format
graph_file_adj = os.getcwd()+ "/" + "files" + "/db_creation" + "/graph_file_adj.json"  #adjacency list format:  https://networkx.github.io/documentation/latest/reference/readwrite/generated/networkx.readwrite.adjlist.write_adjlist.html#networkx.readwrite.adjlist.write_adjlist

fullGraph = nx.Graph()         #initializing fullGraph object

# read the paper class json file and save each paper class json to a list
with open(final_paper_class_file) as f:
    paper_class_json_list_unstripped = f.readlines()

paper_class_json_list = [x.strip() for x in paper_class_json_list_unstripped]


for paper_class_json in paper_class_json_list:   #paper_class_json is for each paper
    paper_class_json_obj = json.loads(paper_class_json)
    Paper_obj = Paper(paper_class_json_obj['title'],paper_class_json_obj['authors'],paper_class_json_obj['topics'],paper_class_json_obj['citpapers'])

    ####### create paper subgraph , since Au-T,Au-Au,T-T,Au-Ti,T-Ti are possble nodes,
    # so they were taken in one list. Then they will be added as nodes and edges can be geerated between all combination of these nodes at once
    paperSG = Paper_obj.create_subgraph()
    ######### keep adding each paper subgraph to full graph
    fullGraph = nx.compose(fullGraph,paperSG)
    # print("number of nodes is " + str(fullGraph.number_of_nodes()) + " number of edges is " + str(fullGraph.number_of_edges()) + " and edges are: " + str(list(fullGraph.edges))  + "\n")

nx.write_gml(fullGraph, graph_file_gml)      #gml(graph modelling language) format,recommended format for saving graph
nx.write_adjlist(fullGraph, graph_file_adj)  #saving in adjacency list format
print("number of nodes in full graph is " + str(fullGraph.number_of_nodes()) + " number of edges is " + str(fullGraph.number_of_edges()) + " and edges are: " + str(list(fullGraph.edges))  + "\n")

################ to visualize the graph
# nx.draw(fullGraph,with_labels=True, font_weight='bold')
# plt.show()


