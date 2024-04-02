#!/bin/bash

# Import terminal colors
RED="\e[31m"
GREEN="\e[32m"
BLUE="\e[34m"
LIGHT_GRAY="\e[37m"
YELLOW="\e[33m"
PURPLE="\e[35m"
BOLD="\033[1m"
DEFAULT="\e[0m"

# Create variables to keep track of all the different test statistics
test_cnt=0
tests_passed=0

# Function to test the XML generated code
test_script_output(){
    test_description=$1  # The test description
    test_cnt=$2          # Test count
    test_file=$(pwd)$3   # Program input file 
    ref_output=$(pwd)$4  # Correct output

    printf "${LIGHT_GRAY}[Test $test_cnt] – $test_description\n" # Print information about the current test

    python3 "calc.py" < $test_file > "tmp_file.out" # Run the parse.py script

    diff -b "$(pwd)/tmp_file.out" "$ref_output"

    if [ $? -eq 0 ]; then
        printf "${BLUE}Expected $(cat $ref_output), recieved $(cat $(pwd)/tmp_file.out).\n"
        echo -e "${GREEN}Test passed ✓ ${DEFAULT}\n"
        # Increase the passed tests count
        tests_passed=$(($tests_passed + 1))
    else # The return code is not matching
        printf "${BLUE}Expected $(cat $ref_output), recieved $(cat $(pwd)/tmp_file.out).\n"
        echo -e "${RED}Test failed ⨯ ${DEFAULT}\n"
    fi

    # Increase the test count
    test_cnt=$(($test_cnt + 1))
}

clear

for file in "./tests"/*.input; do
    test_name=$(echo "$file" | rev | cut -d '.' -f2 | cut -d '/' -f1 | rev)
    test_script_output "Testing random calculator operations - $test_name test" $test_cnt "/tests/$test_name.input" "/tests/$test_name.output"
done

# Print the specific tests summary
echo ""
printf "${LIGHT_GRAY}/////////////////////////////////////\n"
printf "${LIGHT_GRAY}//             SUMMARY             //\n"
printf "${LIGHT_GRAY}/////////////////////////////////////\n\n"

# Print the total tests summary
printf "${BOLD}${GREEN}Total:\n\tTESTS PASSED = $tests_passed/$test_cnt\n\tTESTS FAILED = $(($test_cnt - $tests_passed))/$test_cnt\n"

# Author ~ Marek Čupr (xcuprm01)
