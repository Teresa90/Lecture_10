# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 13:38:58 2021

@author: NjeriMacharia
"""
"""
Assume that we number the lower-case letters starting from 1: ‘a’=1, ‘b’=2, 
etc. Write a program that finds the sum of the number values of the letters
of a word that the user enters"""

# A program that  finds the sum of values represented by letters

# prompt the user to enter to enter a word

word = input("Kindly key in any word: ")

# convert the words to lower-case
l_word = word.lower()

# look up table
alphabet_key = ("abcdefghijklmnopqrstuvwxyz")

# find position of letters in the word
total = 0
for i in l_word:
    pos =alphabet_key.index(i)+1
    #sum the values representing the alphabets
    total = total + pos
print(total)

