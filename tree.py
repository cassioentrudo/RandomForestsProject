class Node:
    def __init__(self, name, father, edge):
        self.childs = []
        self.name = name
        self.father = father
        self.edge = edge

    def AddChilds(self, childs):
        self.childs.append(childs)

    def PrintNode(self):
        print("********************")
        print("nome =", self.name)
        print("father =", self.father)
        print("childs =", self.childs)
        print("edge =", self.edge)
        print("********************")

class Tree:
    def __init__(self):
        self.nodes = []

    def AddNode(self, node):
        self.nodes.append(node)

    def PrintTree(self):
        for node in self.nodes:
            node.PrintNode()
