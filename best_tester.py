#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Alma, Justin
"""
#creates dictionary of words in the text as keys, followed by a nested 
#dictionary of the words that follow it as keys and the number of times
#they follow it as values

def markovDict():
    wordSequences = {}
    
    with open('therapy_statements.txt') as file_object:
        #pastword is key in outer dict
        pastWord = ""
        for line in file_object:
            #nextWord is the word you're on
            for nextWord in line.split():
                if pastWord in wordSequences:
                    frequency = wordSequences[pastWord]
                else:
                    frequency = {}
                    wordSequences[pastWord] = frequency
                if nextWord in frequency:
                     occurrances = frequency[nextWord]
                     #value; either the number that's already there or the one we just put there
                else:
                    occurrances = 0
                frequency[nextWord] = occurrances + 1
                pastWord = nextWord
        return wordSequences

