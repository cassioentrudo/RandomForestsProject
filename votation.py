from training import Classify
from DadosTreinamento import isNumeric

def categoricVotation(forrest, testFold, targetFeature):
    mostVoted = []
    for i in range(len(testFold)):
        answers = {}
        for tree in forrest:
            vote = Classify(tree, testFold.iloc[i,:],isNumeric)
            if vote in answers:
                answers[vote] = answers[vote] + 1
            else:
                answers[vote] = 1
        values = list(answers.values())
        keys = list(answers.keys())
        mostVoted.append(keys[values.index(max(values))])
    return mostVoted

def numericVotation(forrest, testFold, targetFeature):
    mostVoted = []
    for i in range(len(testFold)):
        answers = 0
        countAnswers = 0
        for tree in forrest:
            answers = answers + Classify(tree, testFold.iloc[i,:],isNumeric)
            countAnswers = countAnswers + 1
        mostVoted.append(answers/countAnswers)
    return mostVoted
        
            