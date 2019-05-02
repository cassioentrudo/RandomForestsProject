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
