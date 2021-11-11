# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 13:44:31 2021

@author: Teresa
"""
"""
Write a program that reads a grade between 1 and 5 (integer) and gives its 
description as follows: 1:Fail, 2:Poor, 3:Fair, 4:Good, 5:Excellent

EXTRA: Now modify your program so that it prints letters for grades between
 1 and 100 using the following table 
90–100:A, 80–89:B, 70–79:C, 60–69:D, 1–59:F
"""
#A program that reads a grade and gives its output
def grading():
    #request grade from user
    value = int(input( "Enter your Grade please(from 1 to 5): "))

    if value == 1:
        print("Fail")
    elif value == 2:
        print("Poor")
    elif value == 3:
        print("Fair")
    elif value == 4:
        print("Good")
    else:
        print("excellent")
        
              
grading()
