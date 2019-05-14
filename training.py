import pandas as pd
import math
from DadosTreinamento import table


def GetFeatures(table_file):
    features = []
    for col in table:
        features.append(col)
    return features


def GetTargetFeature():
    features = GetFeatures(table)
    return features[-1]


def EntropyCalculate():
    feature_target = GetTargetFeature()
    gp_target = table.groupby(feature_target)
    feature_values = table[feature_target].unique().tolist()
    total_instances = len(table)
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
    gr_target_feature = _table.groupby(feature_target)

    entropy = 0
    gain = 0
    for feature_value in feature_values:
        entropy = 0
        for feature_target_value in feature_target_values:
            gp_valor_atributo = gp_feature.get_group(feature_value)
            gp_valor_atributo_target = gp_valor_atributo.groupby(feature_target)

            try:
                count_gp_atributo_target = len(gp_valor_atributo_target.get_group(feature_target_value))
            except:
                count_gp_atributo_target = 0

            if(count_gp_atributo_target != 0):
                entropy -= (((count_gp_atributo_target/len(gp_valor_atributo))) * (math.log2(count_gp_atributo_target/len(gp_valor_atributo))))
            else:
                 entropy = 0

        entropy = round(entropy, 3)

        total_instances = len(_table)
        total_valor_atributo = len(gp_valor_atributo)

        gain += (total_valor_atributo/total_instances * entropy)

    gain = EntropyCalculate() - gain

    return round(gain, 3)


def FindNode(_table):
    gain_dict = {}
    for feature in GetFeatures(_table):
        if feature != GetTargetFeature():
            gain_dict[feature] = GainCalculate(feature, _table)
            print(feature, "= ", gain_dict[feature])

    return max(gain_dict, key=gain_dict.get)


def GenerateDecisionTree():
    #root node
    rootNode = FindNode(table)
    print("\nrootName= " , rootNode)

    galhos = table[rootNode].unique().tolist()
    print("\ngalhos= " , galhos)

    for galho in galhos:
        gp_rootNode = table.groupby(rootNode)
        gp_galho = gp_rootNode.get_group(galho)
        print("\n\n",gp_galho)

        FindNode(gp_galho)




GenerateDecisionTree()
