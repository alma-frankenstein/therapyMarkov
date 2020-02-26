#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from numpy import random
import input_to_dict
    
def main():
    statementLength = 60
    statement = createStatement(statementLength)
    print(capitalizer(statement))
    

def pickRandom(): ##if it's the first or the prev word's not an outer key, pick a random word
    wordList = ""
    with open('therapy_statements.txt') as file_object:
        for line in file_object:
            for word in line.split():
                wordList += word + " "
    return random.choice(wordList.split())


def weightedPick(word): #word is previous word in statement
    outer = input_to_dict.markovDict()
    addWord = ""
    subdict = outer[word]
    sum = 0 #sum is sum of values
    for occurance in subdict.values():
        sum = sum + occurance

    randRange = range(0,sum)
    rando = random.choice(randRange)
    
    #start with the first k,v pair. If rando - the v is less than 0, return
    #the key. Otherwise, move to the next k,v, pair and subtract the v from
    #rando again
    for word, frequency in subdict.items():
        rando = rando - frequency
        if rando < 0:
            addWord += word
            break
        else:
            continue

    return addWord


def createStatement(n):
    outer = input_to_dict.markovDict()
    statementString = ""
    counter = 0
    while counter < n:
        if counter == 0: #first word is random
            statementString += pickRandom() + " "
            counter += 1
        else: #if the previous word's in the outer dict, pick a word from its sudict
              #otherwise, pick a random word from the outer dict
            prevWord = statementString.split()[counter-1]
            if prevWord in outer:
                statementString += weightedPick(prevWord) + " "
                counter += 1
            else:
                statementString += pickRandom() + " "
                counter += 1
                
    return statementString


def capitalizer(statementString):
    statementString = statementString.split(" ")
    for index in range(len(statementString)):
        if index == 0:
            statementString[index] = statementString[index].title()
        elif statementString[index-1].endswith('.') or statementString[index-1].endswith('?') or statementString[index-1].endswith('!') or statementString[index] == "I" or statementString[index] == "I'm" or statementString[index] == "I'd" or statementString[index] == "I'll":
            statementString[index] = statementString[index].title()
        else:
            statementString[index] = statementString[index].lower()
    statementString = " ".join(statementString)
    if not statementString[len(statementString)-1].endswith('.'):
        statementString = statementString.rstrip() + "."
    return statementString
    
if __name__ == "__main__":
    main()
