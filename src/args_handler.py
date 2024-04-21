##
# @author Marek Čupr (xcuprm01)
# @name InputArgs class
# @subject IVS - Project 2
# @date 14. 03. 2024
#
# @brief This file includes implementation of InputArgs class, that is used to parse input arguments and run the calculator.
#

from calculator import Calculator

##
# @brief InputArgs class
#
class InputArgs:
    ##
    # @brief Constructor for the InputArgs class.
    # @param input String to be parsed.
    #
    def __init__(self, input):
        # List to store the equation
        self.__equation = []
        # Calculator used to evaluate the equation
        self.__calc = Calculator()
        # Temporary string used to store numbers
        self.__tmp_string = ""

        # Parse the input
        for line in input:
            # Remove whitespaces
            for string in line.split():
                # Iterate over the string
                for char in string:
                    if char:
                        # Save integers and floats to the temporary string 
                        if char.isdigit() or char == '.':
                            self.__tmp_string += char
                        # Handle the saved operand and add the current operator to the equation
                        else:
                            self.handle_char()
                            self.__equation.append(char)

        # Handle the last operand and add the equal sign
        self.handle_char()
        self.__equation.append('=')

    ##
    # @brief Validate operands in the temporary string and add them to the equation.
    #
    def handle_char(self):
        # Validate the temporary string
        if len(self.__tmp_string) != 0:
            # Float value
            if '.' in self.__tmp_string:
                # Invalid float
                if self.__tmp_string.count('.') > 1:
                    raise ValueError("Invalid equation")
                # Valid float
                else:
                    self.__equation.append(float(self.__tmp_string))
            # Integer value
            else:
                self.__equation.append(int(self.__tmp_string))

            # Clear the temporary string
            self.__tmp_string = ""

    ##
    # @brief Get the equation.
    # @return List of the equation.
    #
    def get_equation(self):
        return self.__equation

    ##
    # @brief Run the calculator.
    #
    def run_calc(self):
        # Convert the infix expression to postfix
        self.__calc.postfix_convert(self.get_equation())
        # Evaluate the postfix expression
        self.__calc.eval_expr()
        # Print the result
        self.__calc.print_result()

# End of args_handler.py