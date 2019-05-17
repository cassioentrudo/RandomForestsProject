from graphviz import Digraph

class Node:
    def __init__(self, name):
        self.edges = {}
        self.value = {}
        self.name = name

    def AddEdges(self, edge, child):
        self.edges[edge] = child
        
    def AddEdgesNumeric(self, edge, child, value):
        self.edges[edge] = child
        self.value[edge] = value
        
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
            
    def GetRootNode(self):
        return self.nodes[0]
    
    def GetNodeByName(self, name):
        nodeName = ""
        for node in self.nodes:
            try:
                if (node.name == name):
                    nodeName = node
            except:
                nodeName = ""
                print("return empty")
        return nodeName

    def PaintTree(self):        
        f = Digraph('G', filename='DecisionTree')
        
        for node in self.nodes:                      
            f.node(node.name)
            
            for edge in node.edges:
                f.edge(node.name, node.edges[edge], label=edge)    
        f.view()