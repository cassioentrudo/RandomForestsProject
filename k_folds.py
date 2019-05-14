from DadosTreinamento import table
import pandas as pd
import numpy as np

n=2
answer="Joga"

#%%

foldSize = foldSize=len(table)/n
#shufTable = table.sample(frac=1).reset_index(drop=True)
orderedTable = table.sort_values(answer)
stratified = pd.DataFrame();
for x in range(n):
    for y in range (0, len(orderedTable), n):
        pdobject = pd.DataFrame(orderedTable.iloc[y+x])
        pdobject = pdobject.transpose()
        #print pdobject
        stratified = stratified.append(pdobject)
folds = [stratified[x:x+foldSize] for x in range (0, len(stratified), foldSize)]