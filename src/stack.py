##
# @author Marek Čupr (xcuprm01)
# @name Stack class
# @subject IVS - Project 2
# @date 14. 03. 2024
#
# @brief This file includes implementation of Stack class, that is used for infix to postfix conversion and postfix expression evaluation
#

##
# @brief Stack class
#
class Stack:
    ##
    # @brief Constructor for the Stack class.
    #
    def __init__(self):
        self.__stack = []

    ##
    # @brief Push new item to the top of the stack.
    # @param item Item to be pushed onto the stack.
    #
    def push(self, item):
        self.__stack.append(item)

    ##
    # @brief Pop the top item from the stack.
    # @return The top item from the stack.
    #
    def pop(self):
        # Check if the stack is empty
        if self.is_empty():
            raise IndexError("Attempted to pop item from an empty stack.")
        
        return self.__stack.pop()
    
    ##
    # @brief Pop multiple top items from the stack.
    # @return The top two items from the stack.
    #
    def pop_multiple(self):
        return float(self.__stack.pop()), float(self.__stack.pop())

    ##
    # @brief Get the top item from the stack.
    # @return The top item from the stack.
    #
    def top(self):
        return self.__stack[-1] if not self.is_empty() else ''

    ##
    # @brief Check if the stack is empty.
    # @return True if the stack is empty, False otherwise.
    #
    def is_empty(self):
        return (len(self.__stack) == 0)

# End of stack.py