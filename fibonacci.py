# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 16:27:09 2022

@author: abelw
"""

"""A function that produces the xth (after 0 for convinience) element of the Fibonacci sequence"""

def fibonacci(limit, index = 1, precede2 = 0, precede1 = 0):
    #Function accepts 4 arguments:
    #   - limit: The index of the fibonacci sequence the user seeks to identify
    #   - index: The current index of the sequence
    #   - precede2: The item of the sequence from index-2
    #   - precede1: The item of the sequence from index-3 

    new = precede2 + precede1
    #The next element of the sequence is calculated
    if new == 0:
        new = 1
        #If the generated value is 0, it is set to 1 as this is only possible as the first element in the sequence
        
    if index == limit:
        print(new)
        return(new)
        #When the specified index is reached the value is printed and returned to the user
    else:
        fibonacci(limit, index+1, precede1, new)
        #If the value is not reached then the function is called with updated arguments



