from DadosTreinamento import table
import training
import pandas as pd


#%%

def k_folding(kTable, kN, kTarget):
    
    totalSize = len(kTable)
    foldSize = totalSize//kN
    if (totalSize%kN>0):
        foldSize = foldSize + 1
    #shufTable = table.sample(frac=1).reset_index(drop=True)
    orderedTable = kTable.sort_values(kTarget)
    stratified = pd.DataFrame();
    for x in range(kN):
        for y in range (0, totalSize, kN):
            #print(y+x)
            if (y+x<totalSize):
                pdobject = pd.DataFrame(orderedTable.iloc[y+x])
                pdobject = pdobject.transpose()
                stratified = stratified.append(pdobject)
    folds = [stratified[x:x+foldSize] for x in range (0, totalSize, foldSize)]
    return folds

#%%

n=2
target=training.GetTargetFeature()
fold = k_folding(table, n, target)