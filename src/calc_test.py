import sys
from args_handler import InputArgs

if __name__ == "__main__":
    inputArgs = InputArgs(sys.stdin)
    inputArgs.run_calc_tests()