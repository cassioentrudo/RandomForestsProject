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
        print("******************** PRINTING TREE ********************")
        for node in self.nodes:
            node.PrintNode()
