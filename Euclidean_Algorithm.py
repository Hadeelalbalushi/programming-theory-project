# -*- coding: utf-8 -*-
"""
Created on thu Jan 22 00:42:10 2025

@author: hadee
"""
 


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
   

try :
   # The two numbers that we want to get their GCD
   number1 = int(input("please enter the first positive integer:"))#asking the user to enter the first number
   number2 = int(input("please enter the second positive integer:"))#asking the user to enter the second number
   
   # using the if Condition to check if the user input are  positive integer numbers
   #so if the user input is less than or equal to zero 
   if number1<= 0 or number2<= 0 :
       # so if the input numbers are negative then it will raise(appear) this message 
           raise ValueError("Both numbers must be positive integers!!")

   GCD = Euclidean_Algorithm.calculating_GCD(number1, number2)
   """calling the calculating_GCD method and passing number1 and number2 as arguments"""
    # printing the result 
   print(f"the greatest common divisor of {number1} and {number2} is {GCD}")
#this message will appear if the user entered invalid input, and also the program will stop       
except ValueError as e:
    print(f"\nInvalid input:{e}")
    print("\nThis program is stopped because of the invalid input ")
   
     