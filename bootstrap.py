import pandas as pd
import numpy as np


def DataRead(str1, useCols, tablenames):
    dataTable = pd.read_csv("%s" % str1, header=None, sep="\s*\;",usecols=useCols, names=tablenames,  engine='python')
    dataTable.drop(dataTable.index[[0]], inplace=True)
    return dataTable


tablePath = "D:/git/randomTree/dadosBenchmark_validacaoAlgoritmoAD.csv"


useColls = [0, 1, 2, 3, 4]
tableCollumns = ['Tempo','Temperatura','Umidade','Ventoso','Joga'] 
table = DataRead(tablePath, useColls , tableCollumns)


#%%

def bootstrap(aux, n):

    randArray = np.floor(np.random.rand(n)*len(aux)).astype(int)
    auxDataframe = pd.DataFrame(index=range(n), columns=aux.columns)
    for i in range(n):
        auxDataframe.iloc[i,:] = aux.iloc[randArray[i],:]
        
    return auxDataframe


conjTreino = pd.DataFrame()
conjTreino = bootstrap(table, len(table))

conjTeste = pd.DataFrame()
conjTeste = bootstrap(table, np.random.randint(14))





































