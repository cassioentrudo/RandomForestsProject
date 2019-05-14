import pandas as pd
import numpy as np


def DataRead(str1, useCols, tablenames):
    dataTable = pd.read_csv("%s" % str1, header=None, sep="\s*\;",usecols=useCols, names=tablenames,  engine='python')
    dataTable.drop(dataTable.index[[0]], inplace=True)
    return dataTable


tablePath = "dadosBenchmark_validacaoAlgoritmoAD.csv"


useColls = [0, 1, 2, 3, 4]
tableCollumns = ['Tempo','Temperatura','Umidade','Ventoso','Joga'] 
table = DataRead(tablePath, useColls , tableCollumns)
df =  DataRead(tablePath, useColls , tableCollumns)

test=np.floor(np.random.rand(14)*14).astype(int)
#%%
olar = np.floor(np.random.rand(14)*14).astype(int)
oi=np.array(olar)


#%%

def bootstrap_resample(X, n):

    resample_i = np.floor(np.random.rand(n)*len(X)).astype(int)
    auxDataframe = pd.DataFrame(index=X.index, columns=X.columns)
    for i in range(len(df)):
        auxDataframe.iloc[i,:] = X.iloc[resample_i[i],:]
        
    
    #X_resample = np.array(X[resample_i])  
    return auxDataframe


df_resampled = pd.DataFrame()

df_resampled = bootstrap_resample(df, 14)

#for rows in df.len():
  # df_resampled.iloc[rows,:] = bootstrap_resample(df.iloc[rows,:], 14)













#%%

def CalculaEntropiaTotal():
    countSim = 0
    countNao = 0
    countInstancias = len(instancias)
    for instancia in instancias:
        print(instancia.joga)
        if(instancia.joga.rstrip() == "Sim"):
            countSim += 1
        if(instancia.joga.rstrip() == "Nao"):
            countNao += 1

    sim = (countSim/countInstancias) * math.log2(countSim/countInstancias)
    nao = (countNao/countInstancias) * math.log2(countNao/countInstancias)
    entropiaTotal = round(- sim - nao, 3)
    print(entropiaTotal)

    return sim

























#%%

class Instancia:

    tempo = ""
    temperatura = ""
    umidade = ""
    tempo = ""
    tempo = ""

    def __init__(self, tempo, temperatura, umidade, ventoso, joga):
        self.tempo = tempo
        self.temperatura = temperatura
        self.umidade = umidade
        self.ventoso = ventoso
        self.joga = joga


class DadosTreinamento:

    def CarregaInstanciasTreinamento(self):
        manipulador = open('dadosBenchmark_validacaoAlgoritmoAD.csv', 'r')
        linhas = manipulador.readlines()
        instancias = []

        for i in range(len(linhas)):
            if(i == 0):
                continue

            atributos = linhas[i].split(';')

            tempo = atributos[0]
            temperatura = atributos[1]
            umidade = atributos[2]
            ventoso = atributos[3]
            joga = atributos[4]

            instancia = Instancia(
                tempo, temperatura, umidade, ventoso, joga)

            instancias.insert(i, instancia)

        manipulador.close()
        return instancias
