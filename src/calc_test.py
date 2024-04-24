##
# @author Marek Čupr (xcuprm01)
# @name Calculator tests
# @subject IVS - Project 2
# @date 14. 03. 2024
#
# @brief This file runs the calculator tests.
#

import sys
from args_handler import InputArgs

# Run the calculator tests
if __name__ == "__main__":
    # Parse the input arguments
    inputArgs = InputArgs(sys.stdin)
    # Run the calculator tests
    inputArgs.run_calc_tests()

# End of calc_test.py