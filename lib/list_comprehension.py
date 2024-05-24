#!/usr/bin/env python3

#Function takes a list of numbers
def return_evens(num_list):
    return [v for v in num_list if v%2==0] #returns a new list containg only eve numbers

def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list] #return new list containing same strings but with an exclamation mark added on each at the end