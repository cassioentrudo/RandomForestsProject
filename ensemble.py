import pandas as pd
from bootstrap import bootstrap
from DadosTreinamento import isNumeric
from tree import Tree
import training


#%%

def afforestation(dataTable, nTree):
    #print("[ENSEMBLE] afforestation(). isNumeric=", isNumeric)
    florest = []
    trainTable = pd.concat(dataTable)
    n=len(trainTable)
    for x in range(nTree):
        data = bootstrap(trainTable, n)
        decision_tree = Tree()
        #print("[ENSEMBLE] Generating decision tree [",x+1,"] of" ,  nTree)
        training.GenerateDecisionTree(data, decision_tree, isNumeric)
        #print("[ENSEMBLE] Adding decision_tree in florest")
        florest.append(decision_tree)
    return florest
        
#florest = afforestation(table, 5)