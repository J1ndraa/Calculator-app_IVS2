import sys
from stack import OperatorStack
from calculator import Calculator
from args_handler import InputArgs

if __name__ == "__main__":
    inputArgs = InputArgs(sys.stdin)
    #inputArgs.print_equation()
    operatorStack = OperatorStack()
    exprStack = OperatorStack()
    calc = Calculator()
    calc.postfix_convert(operatorStack, inputArgs.get_equation())
    calc.eval_expr(exprStack)
    calc.print_result(exprStack)