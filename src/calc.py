import sys
from calculator import Calculator
from args_handler import InputArgs

if __name__ == "__main__":
    inputArgs = InputArgs(sys.stdin)
    #inputArgs.print_equation()
    calc = Calculator()
    calc.postfix_convert(inputArgs.get_equation())
    calc.eval_expr()
    calc.print_result()