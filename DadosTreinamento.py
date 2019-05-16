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

<<<<<<< HEAD
table = DataRead(tablePath)




=======
tablePath = "dadosBenchmark_validacaoAlgoritmoAD.csv"
>>>>>>> 17d7ec42c6fce7e4577d1a7ed879e93372e19b9e
#tablePath = "breast-cancer-wisconsin.data"





