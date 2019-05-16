import pandas as pd
from bootstrap import bootstrap
from DadosTreinamento import table, isNumeric
from tree import Tree
import training


#%%

def afforestation(dataTable, nTree):
    florest = []
    trainTable = pd.concat(dataTable)
    n=len(trainTable)
    for x in range(nTree):
        data = bootstrap(trainTable, n)
        decision_tree = Tree()
        training.GenerateDecisionTree(data, decision_tree, isNumeric)
        florest.append(decision_tree)
    return florest
        
#florest = afforestation(table, 5)