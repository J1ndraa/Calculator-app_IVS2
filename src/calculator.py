##
# @author Marek Čupr (xcuprm01)
# @name Calculator class
# @subject IVS - Project 2
# @date 14. 03. 2024
#
# @brief This file includes implementation of Calculator class, that is used to create and evaluate infix expressions.
#

# Importing the math_library module
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
        self.stack = Stack()
        # List to store postfix expression
        self.postfix = []
        # List of operators and their precedence
        self.precedence = [
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
                self.postfix.append(char)
            # Left parenthesis
            elif char == '(':
                self.stack.push(char)
            # Right parenthesis
            elif char == ')':
                self.untilLeftPar()
            # Operator / equal sign or invalid character 
            else:
                # Equal sign
                if char == '=':
                    self.pop_stack()
                # Operator
                elif any(char == operator[0] for operator in self.precedence):
                    self.operatorPrecedence(char)
                # Invalid character
                else:
                    raise ValueError("Invalid character in equation")

    ##
    # @brief Clean the stack until a left parenthesis is found.
    #
    def untilLeftPar(self):
        # Pop the stack until a left parenthesis is found
        while self.stack.top() != '(':
            self.postfix.append(self.stack.pop())
        
        # Pop the left parenthesis from the stack as well
        self.stack.pop()

    ##
    # @brief Handle stack and postfix expression based on the operator precedence. 
    # @param operator Operator indicating what should be done based on its precedence.
    #
    def operatorPrecedence(self, operator):
        # Push the operator to the stack if it is empty
        if self.stack.is_empty():
            self.stack.push(operator)
        # Push the operator to the stack if left parenthesis is on the top of the stack
        elif self.stack.top() == '(' or operator == '(':
            self.stack.push(operator)
        # Push the operator to the stack if the operator has a higher precedence
        elif self.get_precedence(operator) > self.get_precedence(self.stack.top()):
            self.stack.push(operator)
        # Pop operators from the stack and append them to the postfix expression until the operator has a higher precedence
        else:
            self.postfix.append(self.stack.pop())
            self.operatorPrecedence(operator)

    ##
    # @brief Pop the stack and append the remaining operators to the postfix expression.
    #
    def pop_stack(self):
        while not self.stack.is_empty():
            self.postfix.append(self.stack.pop())

    ##
    # @brief Evaluate the postfix expression.
    #
    def eval_expr(self):
        # Iterate over the postfix expression
        for char in self.postfix:
            # Operand
            if isinstance(char, (int, float)):
                self.stack.push(char)
            # Operator
            else:
                match char:
                    case '+':
                        val1, val2 = self.stack.pop_multiple()
                        result = MathLib.add(float(val1), float(val2))
                        self.stack.push(result)
                    case '-':
                        val1, val2 = self.stack.pop_multiple()
                        result = MathLib.sub(float(val2), float(val1))
                        self.stack.push(result)
                    case '*':
                        val1, val2 = self.stack.pop_multiple()
                        result = MathLib.mul(float(val1), float(val2))
                        self.stack.push(result)
                    case '/':
                        val1, val2 = self.stack.pop_multiple()
                        result = MathLib.div(float(val2), float(val1))
                        self.stack.push(result)
                    case '%':
                        val1, val2 = self.stack.pop_multiple()
                        result = MathLib.mod(float(val2), float(val1))
                        self.stack.push(result)
                    case '^':
                        val1, val2 = self.stack.pop_multiple()
                        result = MathLib.expo(float(val2), float(val1))
                        self.stack.push(result)
                    case '√':
                        val1, val2 = self.stack.pop_multiple()
                        result = MathLib.sqrt(float(val1), float(val2))
                        self.stack.push(result)
                    case '!':
                        val = self.stack.pop()
                        # Check if the operand is an integer
                        if not isinstance(val, int):
                            raise ValueError("Invalid operand for factorial")
                        
                        result = MathLib.fact(int(val))
                        self.stack.push(result)
                    case _  : 
                        raise ValueError("Invalid operator")

    ##
    # @brief Print the evaluation result.
    #
    def print_result(self):
        # Get the result from the stack
        result = self.stack.pop()

        # Check if the result is an integer or a float
        if isinstance(result, float) and result.is_integer():
            print(int(result))
        else:
            print(result)

    ##
    # @brief Get the precedence of the operator.
    # @param operator Operator to check the precedence of.
    # @return Precedence of the operator.
    #
    def get_precedence(self, operator):
        for op, prec in self.precedence:
            if op == operator:
                return prec
            
        raise ValueError("Invalid operator")

# End of calculator.py