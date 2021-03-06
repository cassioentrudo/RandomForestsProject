import pandas as pd
import numpy as np


#tablePath = "dadosBenchmark_validacaoAlgoritmoAD.csv"
isNumeric = True
#tablePath = "wdbc.data"
#tablePath = "wine.data"
tablePath = "ionosphere.data"

def DataRead(str1):
    if(isNumeric==True):
        dataTable = pd.read_csv("%s" % str1,header=None, sep="\s*\,",  engine='python') #PARA ATRIBUTOS NUMÉRICOS
    else:
        dataTable = pd.read_csv("%s" % str1, sep="\s*\;",  engine='python')
    return dataTable

table = DataRead(tablePath)

if (isNumeric == True):
    names = {}
    for x in range(len(table.columns)):
        number = x+65
        if (number>90):
            number = number+6
        names[x]=chr(number)
    table = table.rename(columns=names)

if(tablePath == "wdbc.data"):
    table = table.drop(columns="A")
    aux = table["B"]
    table = table.drop(columns="B")
    table["result"]=aux

if (tablePath == "wine.data"):
    aux = table["A"]
    table = table.drop(columns="A")
    for x in range(len(aux)):
       aux.iloc[x]=names.get(aux.iloc[x])
    table["result"]=aux
    
    
