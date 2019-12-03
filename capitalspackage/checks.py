import csv

import requests

import json

def load_csv(filename):

    list_of_capitals = {}
    with open (filename) as csvfile:
        reader = csv.reader (csvfile, delimiter = ';')
        for row in reader:
            list_of_capitals[row[0]] = row[1]

    return list_of_capitals

# function to check if the capital inserted is present in the list
def check_capital(checklist, args):
    if args.name in checklist:
        if args.verbosity >= 2:
            if args.returnr == True:
                print("args.name is passed to check functions. in those the dictionary passed as checklist is checked, previously loaded by function load_csv. the result returned is > ", checklist[args.name])
                return checklist[args.name]
            else:
                print("args.name is passed to check functions. in those the dictionary passed as checklist is checked, previously loaded by function load_csv. the match found is > ", checklist[args.name])
        elif args.verbosity >= 1:
            if args.returnr == True:
                print("Returning {}, capital of {}".format(checklist[args.name], args.name))
                return checklist[args.name]
            else:
                print("The capital of {} is {}".format(args.name,
                  checklist[args.name]))
        else:
            if args.returnr == True:
                return checklist[args.name]
            else:
                print(checklist[args.name])


# function to check if the state inserted is present in the list
def check_state(checklist, args):

    for state, capital in checklist.items():
        if capital == args.name:
            if args.verbosity >= 2:
                if args.returnr == True:
                    print("args.name is passed to check functions. in those the dictionary passed as checklist is checked, previously loaded by function load_csv. the result returned is > ", state)
                    return state
                else:
                    print("args.name is passed to check functions. in those the dictionary passed in checklist is checked, previously loaded by function load_csv. the match found is > ", state)
            elif args.verbosity >= 1:
                if args.returnr == True:
                    print("Returning {}, the state which capital is {}".format(state, args.name))
                    return state
                else:
                    print("{} is the capital of {}".format(args.name, state))
            else:
                if args.returnr == True:
                    return state
                else:
                    print (state)
    if args.name not in checklist and args.name not in checklist.values():
        print("Sorry, {} does not seem to be a state or capital present in the checklist".
              format(args.name))


#function to fetch extra information about countries from REST api
def get_country_data (base_url, countryname, args):

    url= base_url.format(countryname)
    response= requests.get(url)
    if response.status_code == 200:
        result = json.loads(response.text)  # parse json to dict

        if args.extrainfo >= 4:

            if args.verbosity >= 2:
                if args.returnr == True:
                    print ("succesfully fetched api data from REST Countries. returning list with population, area (km^2), currencies list and languages list of {}".format(countryname))
                    elist=[]
                    elistc=[]
                    elistl=[]
                    for r in result:
                        elist.append(r['population'])
                        elist.append(r['area'])
                        for n in range(len(r['currencies'])):
                            elistc.append(r['currencies'][n]['name'])
                        for n in range(len(r['languages'])):
                            elistl.append(r['languages'][n]['name'])
                    elist.append(elistc)
                    elist.append(elistl)
                    return elist
                else:
                    print ("succesfully fetched api data from REST Countries")
                    elistc=[]
                    elistl=[]
                    for r in result:
                        print (countryname, "'s population= ", r['population'])
                        print (countryname, "'s area (km^2) = ", r['area'])
                        for n in range(len(r['currencies'])):
                            elistc.append(r['currencies'][n]['name'])
                        print (countryname, "'s currencies= ", elistc)
                        for n in range(len(r['languages'])):
                            elistl.append(r['languages'][n]['name'])
                        print (countryname, "'s languages= ", elistl)

            elif args.verbosity >= 1:
                if args.returnr == True:
                    print ("returning list with population, area (km^2), currencies list and languages list of {}".format(countryname))
                    elist=[]
                    elistc=[]
                    elistl=[]
                    for r in result:
                        elist.append(r['population'])
                        elist.append(r['area'])
                        for n in range(len(r['currencies'])):
                            elistc.append(r['currencies'][n]['name'])
                        for n in range(len(r['languages'])):
                            elistl.append(r['languages'][n]['name'])
                    elist.append(elistc)
                    elist.append(elistl)
                    print (elist)
                    return elist
                else:
                    elistc= []
                    elistl= []
                    for r in result:
                        print (countryname, "'s population= ", r['population'])
                        print (countryname, "'s area (km^2) = ", r['area'])
                        for n in range(len(r['currencies'])):
                            elistc.append(r['currencies'][n]['name'])
                        print (countryname, "'s currencies= ", elistc)
                        for n in range(len(r['languages'])):
                            elistl.append(r['languages'][n]['name'])
                        print (countryname, "'s languages= ", elistl)

            else:
                if args.returnr == True:
                    elist= []
                    elistc= []
                    elistl= []
                    for r in result:
                        elist.append(r['population'])
                        elist.append(r['area'])
                        for n in range(len(r['currencies'])):
                            elistc.append(r['currencies'][n]['name'])
                        for n in range(len(r['languages'])):
                            elistl.append(r['languages'][n]['name'])
                    elist.append(elistc)
                    elist.append(elistl)
                    return elist
                else:
                    elistc= []
                    elistl= []
                    for r in result:
                        print (r['population'])
                        print (r['area'], " km^2")
                        for n in range(len(r['currencies'])):
                            elistc.append(r['currencies'][n]['name'])
                        print (elistc)
                        for n in range(len(r['languages'])):
                            elistl.append(r['languages'][n]['name'])
                        print (elistl)


        elif args.extrainfo >= 3:
            if args.verbosity >= 2:
                if args.returnr == True:
                    print ("succesfully fetched api data from REST Countries. returning list with population, area (km^2) and currencies list of {}".format(countryname))
                    elist=[]
                    elistc=[]
                    for r in result:
                        elist.append(r['population'])
                        elist.append(r['area'])
                        for n in range(len(r['currencies'])):
                            elistc.append(r['currencies'][n]['name'])
                    elist.append(elistc)
                    return elist
                else:
                    print ("succesfully fetched api data from REST Countries")
                    elistc=[]
                    for r in result:
                        print (countryname, "'s population= ", r['population'])
                        print (countryname, "'s area (km^2) = ", r['area'])
                        for n in range(len(r['currencies'])):
                            elistc.append(r['currencies'][n]['name'])
                        print (countryname, "'s currencies= ", elistc)
            elif args.verbosity >= 1:
                if args.returnr == True:
                    print ("returning list with population, area (km^2) and currencies list of {}".format(countryname))
                    elist=[]
                    elistc=[]
                    for r in result:
                        elist.append(r['population'])
                        elist.append(r['area'])
                        for n in range(len(r['currencies'])):
                            elistc.append(r['currencies'][n]['name'])
                    elist.append(elistc)
                    print (elist)
                    return elist
                else:
                    elistc= []
                    for r in result:
                        print (countryname, "'s population= ", r['population'])
                        print (countryname, "'s area (km^2) = ", r['area'])
                        for n in range(len(r['currencies'])):
                            elistc.append(r['currencies'][n]['name'])
                        print (countryname, "'s currencies= ", elistc)

            else:
                if args.returnr == True:
                    elist= []
                    elistc= []
                    for r in result:
                        elist.append(r['population'])
                        elist.append(r['area'])
                        for n in range(len(r['currencies'])):
                            elistc.append(r['currencies'][n]['name'])
                    elist.append(elistc)
                    return elist
                else:
                    elistc= []
                    for r in result:
                        print (r['population'])
                        print (r['area'], " km^2")
                        for n in range(len(r['currencies'])):
                            elistc.append(r['currencies'][n]['name'])
                        print (elistc)

        elif args.extrainfo >= 2:
            if args.verbosity >= 2:
                if args.returnr == True:
                    print ("succesfully fetched api data from REST Countries. returning list with population and area (km^2) of {}".format(countryname))
                    elist=[]
                    for r in result:
                        elist.append(r['population'])
                        elist.append(r['area'])
                    return elist
                else:
                    print ("succesfully fetched api data from REST Countries")
                    for r in result:
                        print (countryname, "'s population = ", r['population'])
                        print (countryname, "'s area (km^2) = ", r['area'])
            elif args.verbosity >= 1:
                if args.returnr == True:
                    print ("returning list with population and area (km^2) of {}".format(countryname))
                    elist=[]
                    for r in result:
                        elist.append(r['population'])
                        elist.append(r['area'])
                    print (elist)
                    return elist
                else:
                    for r in result:
                        print (countryname, "'s population= ", r['population'])
                        print (countryname, "'s area (km^2) = ", r['area'])
            else:
                if args.returnr == True:
                    elist=[]
                    for r in result:
                        elist.append(r['population'])
                        elist.append(r['area'])
                    return elist
                else:
                    for r in result:
                        print (r['population'])
                        print (r['area'], " km^2")

        elif args.extrainfo >= 1:
            if args.verbosity >= 2:
                if args.returnr == True:
                    print ("succesfully fetched api data from REST Countries. returning population of {}".format(countryname))
                    for r in result:
                        return r['population']
                else:
                    print ("succesfully fetched api data from REST Countries")
                    for r in result:
                        print (countryname, "'s population = ", r['population'])
            elif args.verbosity >= 1:
                if args.returnr == True:
                    print ("returning population of {}".format(countryname))
                    for r in result:
                        print (r['population'])
                        return r['population']
                else:
                    for r in result:
                        print (countryname, "'s populatio = ", r['population'])
            else:
                if args.returnr == True:
                    for r in result:
                        return r['population']
                else:
                    for r in result:
                        print (r['population'])
    else:
        print ("sorry, something went wrong with the API request. check your internet connection and country/capital name and try again")
        raise requests.exceptions.RequestException
