from DadosTreinamento import table
import training
import pandas as pd


#%%

def k_folding(kTable, kN, kTarget):
    
    totalSize = len(kTable)
    foldSize = totalSize//kN
    folds = []
    count=0
    if (totalSize%kN>0):
        foldSize = foldSize + 1
    #shufTable = table.sample(frac=1).reset_index(drop=True)
    orderedTable = kTable.sort_values(kTarget)
    stratified = pd.DataFrame();
    for x in range(kN):
        for y in range (0, totalSize, kN):
            if (y+x<totalSize):
                #print(y+x)
                pdobject = pd.DataFrame(orderedTable.iloc[y+x])
                pdobject = pdobject.transpose()
                stratified = stratified.append(pdobject)
    x=0
    while(x<totalSize):
        count = count + 1
        if (count<=totalSize%kN):
            folds.append(stratified[x:x+foldSize])
            x = x + foldSize
        else:
            folds.append(stratified[x:x+foldSize-1])
            x = x + foldSize - 1
    return folds

#%%

n=4
target=training.GetTargetFeature()
fold = k_folding(table, n, target)