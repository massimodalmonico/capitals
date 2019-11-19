#! /usr/bin/env python3

'''importing the module checks from capitalspackage 
inside check module there are the two functions 
check_capital and check_state'''


from capitalspackage import checks

# perform tests

checks.check_capital("Germany")
checks.check_capital("Honduras")
checks.check_state("Rome")
checks.check_state("Tokyo")

