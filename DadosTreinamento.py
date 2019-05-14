import pandas as pd
import numpy as np


def DataRead(str1):
    dataTable = pd.read_csv("%s" % str1, sep="\s*\;",  engine='python')
    dataTable.drop(dataTable.index[[0]], inplace=True)
    return dataTable


tablePath = "dadosBenchmark_validacaoAlgoritmoAD.csv"



table = DataRead(tablePath)

