# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 13:49:38 2021

@author: Teresa
"""
"""
EXTRA: Now modify your program so that it prints letters for grades between
 1 and 100 using the following table 
90–100:A, 80–89:B, 70–79:C, 60–69:D, 1–59:F
"""
# programa that prints the grade given the marks attained
def grading2():

    # input the marks attained
    marks = int(input("Enter your marks (from 1-100): "))
    if marks in range(1,60):
        print("E")
    elif marks in range(60,70):
        print("D")
    elif marks in range(70,80):
        print("C")
    elif marks in range(80,90):
        print("B")
    else:
        print("A")
grading2()


