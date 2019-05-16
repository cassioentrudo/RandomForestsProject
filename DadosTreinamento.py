import pandas as pd
import numpy as np


tablePath = "dadosBenchmark_validacaoAlgoritmoAD.csv"
isNumeric = False

def DataRead(str1):
    if(isNumeric==True):
        dataTable = pd.read_csv("%s" % str1,header=None, sep="\s*\,",  engine='python') #PARA ATRIBUTOS NUMÉRICOS
    else:
        dataTable = pd.read_csv("%s" % str1, sep="\s*\;",  engine='python')
    return dataTable

table = DataRead(tablePath)




#tablePath = "breast-cancer-wisconsin.data"
