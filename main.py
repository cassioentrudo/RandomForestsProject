#MAIN
from DadosTreinamento import table, isNumeric
import k_folds
import training
import ensemble
import votation

numFolds=10
nTrees=3


#%%

def main():
    folds = k_folds.k_folding(table, numFolds, training.GetTargetFeature())
    testFold=folds[numFolds-1]
    folds.pop(numFolds-1)
    forrest = ensemble.afforestation(folds, nTrees)
    mostVoted=votation.categoricVotation(forrest, testFold, training.GetTargetFeature())
    print(testFold)
    print(mostVoted)
    
    
if __name__ == "__main__":
    main()