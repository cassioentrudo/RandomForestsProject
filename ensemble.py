import pandas as pd
from bootstrap import bootstrap
from DadosTreinamento import table
from tree import Tree
import training

n=12;

#%%

def afforestation(dataTable, nTree):
    florest = []
    for x in range(nTree):
        data = bootstrap(table, n)
        decision_tree = Tree()
        training.GenerateDecisionTree(data, decision_tree)
        florest.append(decision_tree)
    return florest
        
#florest = afforestation(table, 5)