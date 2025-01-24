# -*- coding: utf-8 -*-
"""
Created on thu Jan 22 00:42:10 2025

@author: hadee
"""
# creating two global values with a positive integer numbers that we will use to find their GCD
number1 = 55
number2 = 20
class Euclidean_Algorithm: 
    """ define a class called Euclidean_Algorithm to encapsulate it """
    
    def calculating_GCD(number1, number2):
        """ defining a method that calculate the 
        greatest common divisor  (GCD) 
        with number1 parameter and number2 parameter
        """
        #the while loope will iterate and it will stop when number2 became 0 
        while number2 != 0: # using a while loop to iterate and calculte the remainder 
            remainder = number1 % number2 # vairabl called remainder which is the remaining value when we divide number1 by number2
            number1 = number2 # updating number1 value with a value of number2
            number2 = remainder# updating number2 value with a value ofremainder 
        return number1 
    """ when the loop ends, it return number1 as the GCD """
    
GCD = Euclidean_Algorithm.calculating_GCD(number1, number2)
"""calling the calculating_GCD method and passing number1 and number2 as arguments"""
# printing the result 
print(f"the greatest common divisor of {number1} and {number2} is {GCD}")
