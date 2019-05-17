import pandas as pd
import math
from DadosTreinamento import table
from tree import Tree
from tree import Node

def GetFeatures(table_file):
    features = []
    for col in table_file:
        features.append(col)
    return features


def GetTargetFeature():
    features = GetFeatures(table)
    return features[-1]


def EntropyCalculate(_table):
    feature_target = GetTargetFeature()
    gp_target = _table.groupby(feature_target)
    feature_values = _table[feature_target].unique().tolist()
    total_instances = len(_table)
    entropy = 0

    for feature_value in feature_values:
        value = len(gp_target.get_group(feature_value))
        entropy += -((value/total_instances)) * (math.log2(value/total_instances))

    return round(entropy, 3)


def GainCalculate(feature_name, _table):
    feature_target = GetTargetFeature()
    feature_target_values = _table[feature_target].unique().tolist()
    gp_feature = _table.groupby(feature_name)
    feature_values = _table[feature_name].unique().tolist()

    info = 0
    gain = 0
    for feature_value in feature_values:
        info = 0
        for feature_target_value in feature_target_values:
            gp_valor_atributo = gp_feature.get_group(feature_value)
            gp_valor_atributo_target = gp_valor_atributo.groupby(feature_target)

            try:
                count_gp_atributo_target = len(gp_valor_atributo_target.get_group(feature_target_value))
            except:
                count_gp_atributo_target = 0

            if(count_gp_atributo_target != 0):
                info -= (((count_gp_atributo_target/len(gp_valor_atributo))) * (math.log2(count_gp_atributo_target/len(gp_valor_atributo))))
            else:
                 info = 0

        info = round(info, 3)

        total_instances = len(_table)
        total_valor_atributo = len(gp_valor_atributo)

        gain += (total_valor_atributo/total_instances * info)

    gain = EntropyCalculate(_table) - gain

    return round(gain, 3)


def FindNode(_table):
    gain_dict = {}

    for feature in GetFeatures(_table):
        gain = GainCalculate(feature, _table)
        if(gain == 0 and feature == GetTargetFeature()):
            return feature
        else:
            if (feature != GetTargetFeature()):
                gain_dict[feature] = gain

    node = max(gain_dict, key=gain_dict.get)

    return node


def GenerateDecisionTree(_table, tree, isNumeric, name=None):
    rootNodeName = FindNode(_table)
    if (name != None):
        node = Node(name)
    else:
        node = Node(rootNodeName)
    tree.AddNode(node)
    _table = _table.reset_index(drop=True)



    if(isNumeric==False):
        galhos = _table[rootNodeName].unique().tolist()
    
        for galho in galhos:
    
            gp_rootNode = _table.groupby(rootNodeName)
            gp_galho = gp_rootNode.get_group(galho)
            nodeName = FindNode(gp_galho)
            if (nodeName == GetTargetFeature()):
                folha = gp_galho[nodeName].unique().tolist()[0]
                node.AddEdges(galho, folha)
            else:
                node.AddEdges(galho, nodeName)
                GenerateDecisionTree(gp_galho, tree, isNumeric)
    else:
        tableMean = _table[rootNodeName].mean()
        biggerGalho = pd.DataFrame()
        smallerGalho = pd.DataFrame()
        
        for i in range(len(_table)):
            #print(_table.loc[i,rootNodeName])
            if(_table.loc[i,rootNodeName]>tableMean):
                biggerGalho = biggerGalho.append(_table.iloc[i])
            else:
                smallerGalho = smallerGalho.append(_table.iloc[i])

        biggerGalho = biggerGalho.drop(columns=rootNodeName)
        smallerGalho = smallerGalho.drop(columns=rootNodeName)
        
        nodeNameBig = FindNode(biggerGalho)
        nodeNameSmall = FindNode(smallerGalho)
        
        if (nodeNameBig == GetTargetFeature()):
                folha = biggerGalho[nodeNameBig].unique().tolist()[0]
                node.AddEdgesNumeric("big", folha, tableMean)
        else:
            node.AddEdgesNumeric("big", "big" + rootNodeName + nodeNameBig, tableMean)
            GenerateDecisionTree(biggerGalho, tree, isNumeric, "big" + rootNodeName + nodeNameBig)
            
        if (nodeNameSmall == GetTargetFeature()):
                folha = smallerGalho[nodeNameSmall].unique().tolist()[0]
                node.AddEdgesNumeric("small", folha, tableMean)
        else:
            node.AddEdgesNumeric("small", "small" + rootNodeName + nodeNameSmall, tableMean)
            GenerateDecisionTree(smallerGalho, tree, isNumeric, "small" + rootNodeName + nodeNameSmall)
            
def GetIndexFeatureByName(featurename):
    features = GetFeatures(table)
    for i in range(len(features)-1):
        if(featurename == features[i]):
            return i
#%%

def Classify(decision_tree, instance, isNumeric):
#    instance = "Ensolarado;Quente;Alta;Falso;Nao"
#    instance = "Ensolarado;Quente;Alta;Verdadeiro;Nao"
#    instance = "Nublado;Quente;Alta;Falso;Sim"
#    instance = "Chuvoso;Amena;Alta;Falso;Sim"
#    instance = "Chuvoso;Fria;Normal;Falso;Sim"
#    instance = "Chuvoso;Fria;Normal;Verdadeiro;Nao"
#    instance = "Nublado;Fria;Normal;Verdadeiro;Sim"
#    instance = "Ensolarado;Amena;Alta;Falso;Nao"
#    instance = "Ensolarado;Fria;Normal;Falso;Sim"
#    instance = "Chuvoso;Amena;Normal;Falso;Sim"
#    instance = "Ensolarado;Amena;Normal;Verdadeiro;Sim"
#    instance = "Nublado;Amena;Alta;Verdadeiro;Sim"
#    instance = "Nublado;Quente;Normal;Falso;Sim"
#    instance = "Chuvoso;Amena;Alta;Verdadeiro;Nao"
    
#    decision_tree = Tree()
#    GenerateDecisionTree(table, decision_tree, isNumeric)
#    decision_tree.PrintTree()    
        
#    attributes = instance.split(";")
    
    next_node = decision_tree.GetRootNode()
    result = ""
    #print(instance)
    if (isNumeric == False):
        while(next_node != ""):
            #print ("next_node=", next_node.name)
            index = GetIndexFeatureByName(next_node.name)
            edge = instance.iloc[index]
            #print("edge=", edge)
            #print("next_node.edges", next_node.edges)
            
            result = next_node.edges[edge]
            next_node = decision_tree.GetNodeByName(next_node.edges[edge])       
    
    else:
        while(next_node != ""):
            if(next_node.name[0]=='b' and next_node.name[1]=='i'):
                value = instance.loc[next_node.name[4]]
            elif(next_node.name[0]=='s' and next_node.name[1]=='m'):
                value = instance.loc[next_node.name[6]]
            else:
                value = instance.loc[next_node.name]
            if (value>next_node.value["big"]):
                result=next_node.edges["big"]
            else:
                result=next_node.edges["small"]
            next_node = decision_tree.GetNodeByName(result)
                
        
    #print(result)
    return result
    