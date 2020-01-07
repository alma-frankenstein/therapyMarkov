#!/usr/bin/env python3
# -*- coding: utf-8 -*-
    
def main():
    statementLength = 20
    pickNext()
    statement = createStatement(statementLength)
    print(capitalizer(statement))

def pickNext():
    
    from numpy import random
    import best_tester
    outer = best_tester.markovDict()
    
    addWord = ""
    for randKey, subdict in outer.items():
        randouterKey = random.choice(list(outer.keys()))
        subdict = outer[randouterKey]
    
        sum = 0 #sum is sum of values
        for occurance in subdict.values():
            sum = sum + occurance
        randRange = range(0,sum)
        rando = random.choice(randRange)

        for word, frequency in subdict.items():
            rando = rando - frequency
            if rando < 0:
                addWord += word
                break
            else:
                continue

        return addWord


def createStatement(n):
    statementString = ""
    counter = 0
    while counter < n:
        statementString += pickNext() + " "
        counter += 1
    return statementString
    
def capitalizer(statementString):
    statementString = statementString.split(" ")
    for index in range(len(statementString)):
        if index == 0:
            statementString[index] = statementString[index].title()
        elif statementString[index-1].endswith('.') or statementString[index] == "i":
            statementString[index] = statementString[index].title()
        else:
            statementString[index] = statementString[index].lower()
    statementString = " ".join(statementString)
    return statementString
    
if __name__ == "__main__":
    main()
