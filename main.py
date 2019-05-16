#MAIN
from DadosTreinamento import table, isNumeric
import k_folds
import training
import ensemble
import votation

numFolds=4
nTrees=5


#%%

def main():
    folds = k_folds.k_folding(table, numFolds, training.GetTargetFeature())
    testFold=folds[numFolds-1]
    folds.pop(numFolds-1)
    forrest = ensemble.afforestation(folds, nTrees)
    if(isNumeric==False):
        mostVoted=votation.categoricVotation(forrest, testFold, training.GetTargetFeature())
    else:
        mostVoted=votation.numericVotation(forrest, testFold, training.GetTargetFeature())

if __name__ == "__main__":
    main()