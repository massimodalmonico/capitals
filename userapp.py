#! /usr/bin/env python3

'''importing the module checks from capitalspackage.
inside checks module there are the functions load_csv,
check_capital, check_state and get_country_data'''

from scripts import dbmanager
from capitalspackage import checks
from argparse import ArgumentParser

parser = ArgumentParser()

# add arguments to parser

parser.add_argument(
    "name",
    help="write name of European country or capital",
    type=str.upper)
parser.add_argument('-p', '--password', help="user's password (required)")
parser.add_argument('-u', '--username', help="username (required)")
parser.add_argument(
    "-v",
    "--verbosity",
    help="incrementally increase output verbosity up to -vv",
    action="count",
    default=0)
parser.add_argument(
    "-r",
    "--returnr",
    help="returns result to store it, instead of printing it",
    action='store_true')
parser.add_argument(
    "-c",
    "--choosecsv",
    help='''specify another csv file to use. make sure the format
          is CHINA;PECHINO/nGIAPPONE;TOKYO''',
    action='store')
parser.add_argument(
    "-e",
    "--extrainfo",
    help='''incrementally prints or returns (with -r) extra
          information about the country: population, area,
          currencies, languages''',
    action="count",
    default=0)

# call parse_args to retrieve input from user

args = parser.parse_args()

# check if username and password have been inserted

if args.username is None or args.password is None:
    print ('''username and password are required.
you may create a new user with bdmanager.py''')
    quit()

# run dbmanager to check if username and password are correct
# also create the database if not already existing
# this is neccesary for avoiding errors

dbmanager.open_and_create()
dbmanager.check_for_user(args.username, args.password)

# use standard Europe csv if -c is not called, otherwise load new csv

if args.choosecsv is not None:
    filename = args.choosecsv
else:
    filename = "capitalcsv"

list_of_capitals = checks.load_csv(filename)

# call functions to retrieve country/capital

checks.check_capital(list_of_capitals, args)
checks.check_state(list_of_capitals, args)

# if user asks for extra info run the function get_country_data

if args.extrainfo > 0:

    base_url = "https://restcountries.eu/rest/v2/name/{}?fullText=true"

# if the user inserted a country name, get_country_data may be run direclty
# otherwise call again check_state with parameters "name" and "-r" to get
# corresponding country name, and then run get_country_data

    if args.name in list_of_capitals.keys():
        checks.get_country_data(base_url, args.name, args)
    else:
        newargs = parser.parse_args([args.name, "--returnr"])
        countryname = checks.check_state(list_of_capitals, newargs)
        checks.get_country_data(base_url, countryname, args)
