# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 13:53:58 2021

@author: Teresa
"""

"""
Write a program that writes to a file the numbers from 1 to 100, and their 
squares and square roots, as a table as shown below. Calculate the width of 
columns and use the appropriate format options when writing the numbers. 
Write the square root with 3 digits after the decimal point.
"""
# A program that writes to a file numbers 1 to 100, there squares
#       square roots as a table.(square root with 3 digits)


out_file = "power_solution.txt" # name of the file
afile = open(out_file, "w")
for i in range(1,101):
    line = str(i) + '\t'+ str(i**2)+ '\t' + str(format(i**(0.5),'.3f'))+'\n'
    afile.write(line)
    

afile.close()
