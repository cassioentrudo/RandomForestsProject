#MAIN
from DadosTreinamento import table, tablePath
import k_folds
import training
import ensemble
import votation

numFolds=10
nTrees=3


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
        originalResults.append(testFold[training.GetTargetFeature()].as_matrix())
        mostVotes.append(mostVoted)
        print(testFold)
        print(mostVoted)
        print("####################################   NOVA FOLD   ######################################################")

    print("Original: ", originalResults)    
    print("Most Voted: ", mostVotes)
    VP=0
    VN=0
    FP=0
    FN=0
    if (tablePath == "wdbc.data"):
        for x in range(len(mostVotes)):
            for y in range(len(mostVotes[x])):
                if (mostVotes[x][y]=="=B"):
                    if(originalResults[x][y]=="B"):
                        VP=VP+1
                    else:
                        FP=FP+1
                else:
                    if(originalResults[x][y]=="B"):
                        FN=FN+1
                    else:
                        VN=VN+1
        print("VP: ", VP, " VN: ", VN, " FP: ", FP, " FN: ", FN)
    
    if (tablePath == "ionosphere.data"):
        for x in range(len(mostVotes)):
            for y in range(len(mostVotes[x])):
                if (mostVotes[x][y]=="=g"):
                    if(originalResults[x][y]=="g"):
                        VP=VP+1
                    else:
                        FP=FP+1
                else:
                    if(originalResults[x][y]=="g"):
                        FN=FN+1
                    else:
                        VN=VN+1
        print("VP: ", VP, " VN: ", VN, " FP: ", FP, " FN: ", FN)
        
if __name__ == "__main__":
    main()