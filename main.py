#MAIN
from DadosTreinamento import table
import k_folds
import training
import ensemble
import votation

numFolds=10
nTrees=3


#%%

def main():
    folds = k_folds.k_folding(table, numFolds, training.GetTargetFeature())
    for x in range(len(folds)):
        trainingFolds=folds
        testFold=folds[x]
        trainingFolds.pop(x)
        forrest = ensemble.afforestation(folds, nTrees)
        mostVoted=votation.categoricVotation(forrest, testFold, training.GetTargetFeature())
        print(testFold)
        print(mostVoted)
        print("####################################   NOVA FOLD   ######################################################")
    
    
if __name__ == "__main__":
    main()