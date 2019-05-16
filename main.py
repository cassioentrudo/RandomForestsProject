#MAIN
from DadosTreinamento import table
import k_folds
import training
import ensemble

numFolds=4
nTrees=5

def main():
    folds = k_folds.k_folding(table, numFolds, training.GetTargetFeature())
    foldTeste=folds[numFolds-1]
    folds.pop(numFolds-1)
    forrest = ensemble.afforestation(folds, nTrees)

if __name__ == "__main__":
    main()