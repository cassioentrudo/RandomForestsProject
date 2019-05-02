import math
from DadosTreinamento import DadosTreinamento


dados = DadosTreinamento()
instancias = dados.CarregaInstanciasTreinamento()


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


def

entropia = CalculaEntropiaTotal()
