from graphviz import Digraph

import os
os.environ["PATH"] += os.pathsep + 'C:\Program Files (x86)\Graphviz2.38'

class Node:
    def __init__(self, name):
        self.edges = {}
        self.name = name

    def AddEdges(self, edge, child):
        self.edges[edge] = child


    def PrintNode(self):
        print("********************")
        print("nome =", self.name)
        print("edge =", self.edges)
        print("********************")

class Tree:
    def __init__(self):
        self.nodes = []

    def AddNode(self, node):
        self.nodes.append(node)

    def PrintTree(self):
        for node in self.nodes:
            node.PrintNode()     


    def PaintTree(self):        
        f = Digraph('G', filename='DecisionTree')
        
        for node in self.nodes:                      
            f.node(node.name)
            
            for edge in node.edges:
                f.edge(node.name, node.edges[edge], label=edge)
#            
        f.view()
       
        
