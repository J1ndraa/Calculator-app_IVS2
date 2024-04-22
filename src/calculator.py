##
# @author Marek Čupr (xcuprm01)
# @name Calculator class
# @subject IVS - Project 2
# @date 14. 03. 2024
#
# @brief This file includes implementation of Calculator class, that is used to create and evaluate infix expressions.
#

from math_library import MathLib
from stack import Stack

##
# @brief Calculator class
#
class Calculator:
    ##
    # @brief Constructor for the Calculator class.
    #
    def __init__(self):
        # Stack used for postfix conversion and evaluation
        self.__stack = Stack()
        # List to store postfix expression
        self.__postfix = []
        # List of operators and their precedence
        self.__precedence = [
            ('+', 1),
            ('-', 1),
            ('*', 2),
            ('/', 2),
            ('%', 2),
            ('^', 3),
            ('√', 4),
            ('!', 4)
        ]

    ##
    # @brief Convert infix expression to postfix expression.
    # @param equation Infix expression to be converted.
    #
    def postfix_convert(self, equation):
        # Iterate over the infix expression
        for char in equation:
            # Operand
            if isinstance(char, (int, float)):
                self.__postfix.append(char)
            # Left parenthesis
            elif char == '(':
                self.__stack.push(char)
            # Right parenthesis
            elif char == ')':
                self.untilLeftPar()
            # Operator / equal sign or invalid character 
            else:
                # Equal sign
                if char == '=':
                    self.pop_stack()
                # Operator
                elif any(char == operator[0] for operator in self.__precedence):
                    self.operatorPrecedence(char)
                # Invalid character
                else:
                    raise ValueError("Invalid character in equation")

    ##
    # @brief Clean the stack until a left parenthesis is found.
    #
    def untilLeftPar(self):
        # Pop the stack until a left parenthesis is found
        while self.__stack.top() != '(':
            self.__postfix.append(self.__stack.pop())
        
        # Pop the left parenthesis from the stack as well
        self.__stack.pop()

    ##
    # @brief Handle stack and postfix expression based on the operator precedence. 
    # @param operator Operator indicating what should be done based on its precedence.
    #
    def operatorPrecedence(self, operator):
        # Push the operator to the stack if it is empty
        if self.__stack.is_empty():
            self.__stack.push(operator)
        # Push the operator to the stack if left parenthesis is on the top of the stack
        elif self.__stack.top() == '(' or operator == '(':
            self.__stack.push(operator)
        # Push the operator to the stack if the operator has a higher precedence
        elif self.get_precedence(operator) > self.get_precedence(self.__stack.top()):
            self.__stack.push(operator)
        # Pop operators from the stack and append them to the postfix expression until the operator has a higher precedence
        else:
            self.__postfix.append(self.__stack.pop())
            self.operatorPrecedence(operator)

    ##
    # @brief Pop the stack and append the remaining operators to the postfix expression.
    #
    def pop_stack(self):
        while not self.__stack.is_empty():
            self.__postfix.append(self.__stack.pop())

    ##
    # @brief Evaluate the postfix expression.
    #
    def eval_expr(self):
        # Iterate over the postfix expression
        for char in self.__postfix:
            # Operand
            if isinstance(char, (int, float)):
                self.__stack.push(char)
            # Operator
            else:
                match char:
                    case '+':
                        val1, val2 = self.__stack.pop_multiple()
                        result = MathLib.add(float(val1), float(val2))
                        self.__stack.push(result)
                    case '-':
                        val1, val2 = self.__stack.pop_multiple()
                        result = MathLib.sub(float(val2), float(val1))
                        self.__stack.push(result)
                    case '*':
                        val1, val2 = self.__stack.pop_multiple()
                        result = MathLib.mul(float(val1), float(val2))
                        self.__stack.push(result)
                    case '/':
                        val1, val2 = self.__stack.pop_multiple()
                        result = MathLib.div(float(val2), float(val1))
                        self.__stack.push(result)
                    case '%':
                        val1, val2 = self.__stack.pop_multiple()
                        result = MathLib.mod(float(val2), float(val1))
                        self.__stack.push(result)
                    case '^':
                        val1, val2 = self.__stack.pop_multiple()
                        result = MathLib.expo(float(val2), float(val1))
                        self.__stack.push(result)
                    case '√':
                        val1, val2 = self.__stack.pop_multiple()
                        result = MathLib.sqrt(float(val1), float(val2))
                        self.__stack.push(result)
                    case '!':
                        val = self.__stack.pop()
                        # Check if the operand is an integer
                        if not isinstance(val, int):
                            raise ValueError("Invalid operand for factorial")
                        
                        result = MathLib.fact(int(val))
                        self.__stack.push(result)
                    case _  : 
                        raise ValueError("Invalid operator")

    ##
    # @brief Print the evaluation result.
    #
    def print_result(self):
        # Get the result from the stack
        result = self.__stack.pop()

        # Check if the result is an integer or a float
        if isinstance(result, float) and result.is_integer():
            print(int(result))
        else:
            print(result)

    ##
    # @brief Get the evaluation result.
    # @param decimal_places Number of decimal places to round the result to.
    # @return Evaluation result.
    #
    def get_result(self, decimal_places):
        # Get the result from the stack
        result = self.__stack.pop()

        # Check if the result is an integer or a float
        if isinstance(result, float) and result.is_integer():
            return int(result)
        else:
            return round(result, decimal_places)

    ##
    # @brief Get the precedence of the operator.
    # @param operator Operator to check the precedence of.
    # @return Precedence of the operator.
    #
    def get_precedence(self, operator):
        for op, prec in self.__precedence:
            if op == operator:
                return prec
            
        raise ValueError("Invalid operator")

# End of calculator.py