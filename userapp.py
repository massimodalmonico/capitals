#! /usr/bin/env python3

'''importing the module checks from capitalspackage. 
inside checks module there are the functions load_csv,
check_capital and check_state'''

from capitalspackage import checks

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("name", help = "write name of European country or capital", type= str.upper)
parser.add_argument("-v", "--verbosity", help="incrementally increase output verbosity up to -vv", action="count", default=0)
parser.add_argument("-r", "--return", help="returns result to store it, instead of printing it", action='store_true')

args = parser.parse_args()

filename = "capitalcsv"

list_of_capitals = checks.load_csv(filename)

checks.check_capital(args.name, list_of_capitals, args)
checks.check_state(args.name, list_of_capitals, args)
