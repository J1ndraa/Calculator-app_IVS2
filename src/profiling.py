##
# @author Marek Čupr (xcuprm01)
# @name StandardDeviation class
# @subject IVS - Project 2
# @date 24. 04. 2024
#
# @brief This file includes implementation of StandardDeviation class, that is used to calculate the standard deviation of input numbers.
#

from math_library import MathLib
import sys

##
# @brief StandardDeviation class
#
class StandardDeviation:
    ##
    # @brief Constructor for the StandardDeviation class.
    #
    def __init__(self):
        # List to store the numbers
        self.__nums = []
        # Length of the list
        self.__len = 0
        # Sum of the numbers
        self.__sum = 0
        # Sum of the numbers squared
        self.__sum_expo = 0
        # Parse the input
        for line in sys.stdin.readlines():
            self.__nums.extend([float(num) for num in line.split()])

    ##
    # @brief Calculate the standard deviation of the input numbers.
    #
    def calculate(self):
        # Calculate the length of the list
        self.calculate_len()
        # Calculate the sum of the numbers
        self.calculate_sum()
        # Calculate the sum of the numbers squared
        self.calculate_sum_expo()
        # Print the result
        print(MathLib.sqrt(MathLib.mul(MathLib.div(1, MathLib.sub(self.__len, 1)), MathLib.sub(self.__sum_expo, MathLib.mul(self.__len, MathLib.expo(float(MathLib.div(self.__sum, self.__len)), 2)))), 2))

    ##
    # @brief Calculate the length of the list.
    #
    def calculate_len(self):
        for num in self.__nums:
            self.__len = MathLib.add(self.__len, 1)
    
    ##
    # @brief Calculate the sum of the numbers.
    #
    def calculate_sum(self):
        for num in self.__nums:
            self.__sum = MathLib.add(self.__sum, num)

    ##
    # @brief Calculate the sum of the numbers squared.
    #
    def calculate_sum_expo(self):
        for num in self.__nums:
            self.__sum_expo = MathLib.add(self.__sum_expo, MathLib.expo(num, 2))

# Run the standard deviation calculation
if __name__ == '__main__':
    # Create a new StandardDeviation object
    stddev = StandardDeviation()
    # Calculate the standard deviation
    stddev.calculate()

# End of profiling.py