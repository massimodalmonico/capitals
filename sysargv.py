#! /usr/bin/env python3

'''importing the module checks from capitalspackage 
inside check module there are the two functions 
check_capital and check_state'''

from capitalspackage import checks

# sys is necessary to use method sys.argv

import sys

# store the first parameter passed by the user in chosen_input

chosen_input = sys.argv[1]

# perform the checks on chosen_input and return results

checks.check_capital(str(chosen_input))
checks.check_state(str(chosen_input))
