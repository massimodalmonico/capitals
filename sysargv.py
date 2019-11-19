#! /usr/bin/env python3



from capitalspackage import checks


import sys


chosen_input = sys.argv[1]

checks.check_capital(str(chosen_input))
checks.check_state(str(chosen_input))
