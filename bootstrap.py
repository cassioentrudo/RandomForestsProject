import pandas as pd
import numpy as np
from DadosTreinamento import table


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





































