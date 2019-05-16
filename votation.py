

def categoricVotation(forrest, testFold, targetFeature):
    mostVoted = []
    for line in testFold:
        answers = {}
        for tree in forrest:
            vote = classify(tree, testFold[line], targetFeature)
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
    for line in testFold:
        answers = 0
        countAnswers = 0
        for tree in forrest:
            answers = answers + classify(tree, testFold[line], targetFeature)
            countAnswers = countAnswers + 1
        mostVoted.append(answers/countAnswers)
    return mostVoted
        
            