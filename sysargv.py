#! /usr/bin/env python3

'''importing the module checks from capitalspackage. 
inside checks module there are the two functions 
check_capital and check_state'''

from capitalspackage import checks

# sys is necessary to use method sys.argv

import sys


# store the first parameter passed by the user in chosen_input
# after checking if exacly one argument has been passed by the user

if len (sys.argv) == 2:
    chosen_input = sys.argv[1]


# perform the checks on chosen_input and return results

    checks.check_capital(str(chosen_input))
    checks.check_state(str(chosen_input))


# produce meaningful error if argument passed != 1

else: print ("wrong number of arguments" +
              "\nplease insert exacly one argument: country or capital name")




