# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 13:34:59 2021

@author: NjeriMacharia
"""
"""
Write a program that reads two numbers from the user and prints the product 
digit by digit. Each digit should be printed on a separate line. Hint:
There are various ways to do this (e.g. using mathematical operations).
But with our current programming knowledge, the best way would be to use 
the str() conversion function."""

# Question 3

# A program that reads two numbers and prints out the product
#   but with each digit of the product in its own line.

# prompt user to input two digits

first_no =int(input("Kindly input any number: "))
second_no = int(input("Kindly input another number: "))

#calculate the product:
product = first_no * second_no

#display the output
product =str(product)
for i in product:
    print(i)
    
    
