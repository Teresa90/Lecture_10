# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 13:22:01 2021

@author: Teresa
"""
"""
Write a program that prints a table as shown below which lists powers of 
2 and 1/x for numbers 1 to 10. Column alignment, space between columns, and 
digit formats should be as shown below. """


for x in range(1,11):
    print(x,"\t",2**x, "\t",format(1/x, '.3f'))
    

