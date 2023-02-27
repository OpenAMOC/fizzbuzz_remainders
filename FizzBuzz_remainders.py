# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 14:01:44 2022

"""
#starts loop for 1 through 100
for n in range (1,101):
    # % gives the remainder of a division
    X = (n%5)
    Y = (n%3)
    #sets up empty output to be added to
    output = ""
    if Y==0:
        output += "fizz"
    if X==0:
        output += "buzz"
    if output == "":
        #prints n if output remains empty
        print(n)
    else:
        #prints the output if it has been filled by fizz, buzz or both
        print(output)
