#MAIN
from DadosTreinamento import table
import k_folds
import training
import ensemble
import votation

numFolds=4
nTrees=5
isNumeric=0

#%%

def main():
    folds = k_folds.k_folding(table, numFolds, training.GetTargetFeature())
    testFold=folds[numFolds-1]
    folds.pop(numFolds-1)
    forrest = ensemble.afforestation(folds, nTrees)
    if(isNumeric==0):
        mostVoted=votation.categoricVotation(forrest, testFold, training.GetTargetFeature())
    else:
        mostVoted=votation.numericVotation(forrest, testFold, training.GetTargetFeature())

if __name__ == "__main__":
    main()