#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 20:02:53 2019

@author: alma
"""

wordSequences = {}

with open('greenEggs.txt') as file_object:
    word = ""
    for line in file_object:
        #nextWord is the word you're on
        for nextWord in line.split():
            if word in wordSequences:
                frequency = wordSequences[word]
            else:
                frequency = {}
                wordSequences[word] = frequency
            if nextWord in frequency:
                 occurrances = frequency[nextWord]
                 #value; either the number that's already there or the one we just put there
            else:
                occurrances = 0
            frequency[nextWord] = occurrances + 1
            word = nextWord
print(wordSequences)
     

#dict = {'meow':'cat', 'sup':'bro'}

#print(dict['cat'])