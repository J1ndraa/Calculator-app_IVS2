##
# @author: Halva Jindřich (xhalva05)
# @name: Math library
# @date: 2024/04/02
# @brief: This file includes implementation of class MathLib, that holds methods representing mathematical operations
#

import re

class MathLib():

    ##
    # @brief Adds two numbers
    # @return Sum of two numbers a and b
    @staticmethod
    def add(a, b):
        return a + b
    
    ##
    # @brief Difference of two numbers
    # @return Difference of two numbers a and b
    @staticmethod
    def sub(a, b):
        return a - b
    
    ##
    # @brief Multiply two numbers
    # @return Result of multiplying two numbers a and b
    @staticmethod
    def mul(a, b):
        return a * b
    
    ##
    # @brief Divides two numbers
    # @return Result of dividing two numbers a and b (a/b)
    @staticmethod
    def div(a, b):
        if(b == 0):
            exit(1) #dividing by zero
        return a / b
    
    ##
    # @brief Exponent operation
    # @return Number a power by b
    @staticmethod
    def expo(a, b):
        if b < 0:
            exit(1) #exponent cannot be negative number
        return a ** b 
    
    ##
    # @brief Square root
    # @return Square root of number a
    @staticmethod
    def sqrt(a):
        if a < 0:
            exit(1) #number in sqrt cannot be negative
        return a ** (1/2)
    
    ##
    # @brief Modulo operation
    # @return Returns the remainder after division of a by b
    @staticmethod
    def mod(a, b):
        return a % b
    
    ##
    # @brief Factorial of integer number 
    # @return Result is integer number
    @staticmethod
    def fact(a):
        if type(a) != int:
            exit(1) #factorial can be done only with decimal numbers
        if a == 0:
            return 1
        return a * MathLib.fact(a-1)
    
