import math
import pandas as pd
from DadosTreinamento import table


def CalculaEntropia(valor1, valor2, total):
    p1 = (valor1/total) * math.log2(valor1/total)
    p2 = (valor2/total) * math.log2(valor2/total)

    return -p1-p2

def EntropiaTotal():
    gp_joga = table.groupby('Joga')
    total_inst = len(table)
    total_joga = len(gp_joga.get_group('Sim'))
    total_nao_joga = len(gp_joga.get_group('Nao'))

    return CalculaEntropia(total_joga, total_nao_joga, total_inst)

def CalculaGanhoValorAtributo(nome_atributo, valor_atributo, nome_atributo_alvo):
    gp_atributo = table.groupby(nome_atributo)
    gp_valor_atributo = gp_atributo.get_group(valor_atributo)
    gp_atributo_alvo = gp_valor_atributo.groupby(nome_atributo_alvo)

    try:
        total_atibuto_alvo_sim = len(gp_atributo_alvo.get_group("Sim"))
    except:
        total_atibuto_alvo_sim = 0

    try:
        total_atibuto_alvo_nao = len(gp_atributo_alvo.get_group("Nao"))
    except:
        total_atibuto_alvo_nao = 0

    if(total_atibuto_alvo_sim == 0 or total_atibuto_alvo_nao == 0):
        ganho_atributo = 0
    else:
        ganho_atributo = CalculaEntropia(valor1=total_atibuto_alvo_sim, valor2=total_atibuto_alvo_nao, total=len(gp_valor_atributo))

    return ganho_atributo

def CalculaGanhoTempo():
    gp_tempo = table.groupby(by="Tempo")
    total_tempo_ensolarado = len(gp_tempo.get_group("Ensolarado"))
    ganho_tempo_ensolarado = CalculaGanhoValorAtributo(nome_atributo="Tempo", valor_atributo="Ensolarado", nome_atributo_alvo="Joga")

    total_tempo_nublado = len(gp_tempo.get_group("Nublado"))
    ganho_tempo_nublado = CalculaGanhoValorAtributo(nome_atributo="Tempo", valor_atributo="Nublado", nome_atributo_alvo="Joga")

    total_tempo_chuvoso = len(gp_tempo.get_group("Chuvoso"))
    ganho_tempo_chuvoso = CalculaGanhoValorAtributo(nome_atributo="Tempo", valor_atributo="Chuvoso", nome_atributo_alvo="Joga")

    entropia = (total_tempo_ensolarado/len(table) * ganho_tempo_ensolarado) + (total_tempo_nublado/len(table) * ganho_tempo_nublado) + (total_tempo_chuvoso/len(table) * ganho_tempo_chuvoso)

    ganho_tempo = EntropiaTotal() - entropia

    return round(ganho_tempo, 3)

def CalculaGanhoTemperatura():
    gp_temperatura = table.groupby(by="Temperatura")
    total_temperatura_quente = len(gp_temperatura.get_group("Quente"))
    ganho_temperatura_quente = CalculaGanhoValorAtributo(nome_atributo="Temperatura", valor_atributo="Quente", nome_atributo_alvo="Joga")

    total_temperatura_fria = len(gp_temperatura.get_group("Fria"))
    ganho_temperatura_fria = CalculaGanhoValorAtributo(nome_atributo="Temperatura", valor_atributo="Fria", nome_atributo_alvo="Joga")

    total_temperatura_amena = len(gp_temperatura.get_group("Amena"))
    ganho_temperatura_amena = CalculaGanhoValorAtributo(nome_atributo="Temperatura", valor_atributo="Amena", nome_atributo_alvo="Joga")

    entropia = (total_temperatura_quente/len(table) * ganho_temperatura_quente) + (total_temperatura_fria/len(table) * ganho_temperatura_fria) + (total_temperatura_amena/len(table) * ganho_temperatura_amena)

    ganho_temperatura = EntropiaTotal() - entropia

    return round(ganho_temperatura, 3)

def CalculaGanhoUmidade():
    gp_umidade = table.groupby(by="Umidade")
    total_umidade_alta = len(gp_umidade.get_group("Alta"))
    ganho_umidade_alta = CalculaGanhoValorAtributo(nome_atributo="Umidade", valor_atributo="Alta", nome_atributo_alvo="Joga")

    total_umidade_normal = len(gp_umidade.get_group("Normal"))
    ganho_umidade_normal = CalculaGanhoValorAtributo(nome_atributo="Umidade", valor_atributo="Normal", nome_atributo_alvo="Joga")

    entropia = (total_umidade_alta/len(table) * ganho_umidade_alta) + (total_umidade_normal/len(table) * ganho_umidade_normal)

    ganho_umidade = EntropiaTotal() - entropia

    return round(ganho_umidade, 3)

def CalculaGanhoVentoso():
    gp_ventoso = table.groupby(by="Ventoso")
    total_ventoso_falso = len(gp_ventoso.get_group("Falso"))
    ganho_ventoso_falso = CalculaGanhoValorAtributo(nome_atributo="Ventoso", valor_atributo="Falso", nome_atributo_alvo="Joga")

    total_ventoso_verdadeiro = len(gp_ventoso.get_group("Verdadeiro"))
    ganho_ventosoo_verdadeiro = CalculaGanhoValorAtributo(nome_atributo="Ventoso", valor_atributo="Verdadeiro", nome_atributo_alvo="Joga")

    entropia = (total_ventoso_falso/len(table) * ganho_ventoso_falso) + (total_ventoso_verdadeiro/len(table) * ganho_ventosoo_verdadeiro)

    ganho_ventoso = EntropiaTotal() - entropia

    return round(ganho_ventoso, 3)

print("Ganho Tempo", CalculaGanhoTempo())
print("Ganho Temperatura", CalculaGanhoTemperatura())
print("Ganho Umidade", CalculaGanhoUmidade())
print("Ganho Ventoso", CalculaGanhoVentoso())
