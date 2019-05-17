#MAIN
from DadosTreinamento import table
import k_folds
import training
import ensemble
import votation

numFolds=10
nTrees=1


#%%

def main():
    folds = k_folds.k_folding(table, numFolds, training.GetTargetFeature())
    originalResults = []
    mostVotes = []
    for x in range(len(folds)):
        trainingFolds=folds.copy()
        testFold=folds[x]
        trainingFolds.pop(x)
        forrest = ensemble.afforestation(folds, nTrees)
        mostVoted=votation.categoricVotation(forrest, testFold, training.GetTargetFeature())
        originalResults.append(testFold[training.GetTargetFeature()])
        mostVotes.append(mostVoted)
        print(testFold)
        print(mostVoted)
        print("####################################   NOVA FOLD   ######################################################")

    print("Original: ", originalResults)    
    print("Most Voted: ", mostVotes)
    
if __name__ == "__main__":
    main()