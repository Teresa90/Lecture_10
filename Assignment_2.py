# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 13:27:52 2021

@author: Teresa
"""
"""
A simple type of secret code can be done by replacing each character with a 
corresponding different character. Let’s assume we want to replace each 
character with the character that is 5 ahead of it in the ASCII code 
table (e.g: ord(‘A’)=65; 65+5=70; chr(70)=’F’. So, we will replace character 
‘A’ with character ‘F’ in our code). Write a program that reads 
a sentence from the user and outputs a new string that is produced using 
the secret code described above (there shouldn’t be any extra space between
characters in the output)."""
# Question 2
# A program to encode a users information


def secret_coder():
    # prompt user to input the message to encode
    message = input("Input the message to be encode: ")

    # Loop through the message to and print out the unicode values
    for i in message:
        code = ord(i) + 5
        
        #convert the new unicode to a new message
        new_message = chr(code)
        print(new_message,end = "")

secret_coder()#call the function


