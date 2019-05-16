import pandas as pd
import numpy as np


def DataRead(str1):
    dataTable = pd.read_csv("%s" % str1, sep="\s*\;",  engine='python')
    #dataTable = pd.read_csv("%s" % str1,header=None, sep="\s*\,",  engine='python') #PARA ATRIBUTOS NUMÉRICOS
    return dataTable

tablePath = "dadosBenchmark_validacaoAlgoritmoAD.csv"
#tablePath = "breast-cancer-wisconsin.data"



table = DataRead(tablePath)

