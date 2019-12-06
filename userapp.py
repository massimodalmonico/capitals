#! /usr/bin/env python3

'''importing the module checks from capitalspackage.
inside checks module there are the functions load_csv,
check_capital and check_state'''

from scripts import dbmanager
from capitalspackage import checks
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("name", help = "write name of European country or capital", type= str.upper)
parser.add_argument('-p', '--password', help="user's password (required)",
                    required=True)
parser.add_argument('-u', '--username', help="username (required)",
                    required=True)
parser.add_argument("-v", "--verbosity", help= "incrementally increase output verbosity up to -vv", action= "count", default= 0)
parser.add_argument("-r", "--returnr", help= "returns result to store it, instead of printing it", action= 'store_true')
parser.add_argument("-c", "--choosecsv", help= "specify another csv file to use. make sure the format is CHINA;PECHINO/nGIAPPONE;TOKYO", action= 'store')
parser.add_argument("-e", "--extrainfo", help= "incrementally prints or returns (with -r) extra information about the country: population, area, currencies, languages", action= "count", default= 0)


args = parser.parse_args()

dbmanager.open_and_create()
dbmanager.check_for_user(args.username, args.password)

if args.choosecsv != None:
    filename= args.choosecsv
else: filename = "capitalcsv"

list_of_capitals = checks.load_csv(filename)

checks.check_capital(list_of_capitals, args)
checks.check_state(list_of_capitals, args)

if args.extrainfo > 0:
    
    base_url = "https://restcountries.eu/rest/v2/name/{}?fullText=true"
    if args.name in list_of_capitals.keys():
        checks.get_country_data(base_url, args.name, args)
    else:
        newargs= parser.parse_args([args.name, "--returnr"])
        countryname= checks.check_state(list_of_capitals, newargs)
        checks.get_country_data(base_url, countryname, args)
