##
# @author: Halva Jindřich (xhalva05)
# @name: Math library
# @subject: IVS - Project 2
# @date: 02. 04. 2024
#
# @brief: This file includes implementation of MathLib class, that holds methods representing mathematical operations
#

import re

##
# @brief MathLib class
#
class MathLib():
    ##
    # @brief Adds two numbers.
    # @param a First number for addition.
    # @param b Second number for addition.
    # @return Sum of two numbers a and b.
    #
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b
    
    ##
    # @brief Difference of two numbers.
    # @param a First number for subtraction.
    # @param b Second number for subtraction.
    # @return Difference of two numbers a and b.
    #
    @staticmethod
    def sub(a: float, b: float) -> float:
        return a - b
    
    ##
    # @brief Multiply two numbers.
    # @param a First number for multiplication.
    # @param b Second number for multiplication.
    # @return Result of multiplying two numbers a and b.
    #
    @staticmethod
    def mul(a: float, b: float) -> float:
        return a * b
    
    ##
    # @brief Divides two numbers.
    # @param a First number for division.
    # @param b Second number for division.
    # @return Result of dividing two numbers a and b.
    #
    @staticmethod
    def div(a: float, b: float) -> float:
        # Check if division by zero
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        
        return a / b
    
    ##
    # @brief Exponent operation.
    # @param a Base number.
    # @param b Exponent number.
    # @return Number a power by b.
    #
    @staticmethod
    def expo(a: float, b: float) -> float:
        # Check if the exponent is negative
        if b < 0:
            raise ValueError("Exponent cannot be a negative number")
        
        return a ** b 
    
    ##
    # @brief Square root operation.
    # @param a Number for square root.
    # @return Square root of number a.
    #
    @staticmethod
    def sqrt(a: float) -> float:
        # Check if the number is negative
        if a < 0:
            raise ValueError("Square root of a negative number")
        
        return a ** (1/2)
    
    ##
    # @brief Modulo operation.
    # @param a First number for modulo operation.
    # @param b Second number for modulo operation.
    # @return The remainder after division of a by b.
    #
    @staticmethod
    def mod(a: float, b: float) -> float:
        # Check if division by zero
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        
        return a % b
    
    ##
    # @brief Factorial of integer number.
    # @param a Number for factorial operation.
    # @return Result is integer number.
    #
    @staticmethod
    def fact(a: int) -> int:
        # Check if the number is negative
        if a < 0:
            raise ValueError("Factorial of a negative number")

        # Factorial of 0 is 1
        if a == 0:
            return 1

        # Recursive call of the factorial function        
        return a * MathLib.fact(a - 1)
    
# End of math_library.py