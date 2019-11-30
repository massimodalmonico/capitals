import csv

def load_csv(filename):

    list_of_capitals = {}
    with open (filename) as csvfile:
        reader = csv.reader (csvfile, delimiter = ';')
        for row in reader:
            list_of_capitals[row[0]] = row[1]

    return list_of_capitals

# function to check if the capital inserted is present in the list
def check_capital(state_name, checklist, args):
    if state_name in checklist:
        if args.verbosity >= 2:
            if args.returnr == True:
                print("args.name is passed to check functions. in those the dictionary passed as checklist is checked, previously loaded by function load_csv. the result returned is > ", checklist[state_name])
                return checklist[state_name]
            else:
                print("args.name is passed to check functions. in those the dictionary passed as checklist is checked, previously loaded by function load_csv. the match found is > ", checklist[state_name])
        elif args.verbosity >= 1:
            if args.returnr == True:
                print("Returning {}, capital of {}".format(checklist[state_name], state_name))
                return checklist[state_name]
            else:
                print("The capital of {} is {}".format(state_name,
                  checklist[state_name]))
        else:
            if args.returnr == True:
                return checklist[state_name]
            else:
                print(checklist[state_name])


# function to check if the state inserted is present in the list
def check_state(capital_name, checklist, args):

    for state, capital in checklist.items():
        if capital == capital_name:
            if args.verbosity >= 2:
                if args.returnr == True:
                    print("args.name is passed to check functions. in those the dictionary passed as checklist is checked, previously loaded by function load_csv. the result returned is > ", state)
                    return state
                else:
                    print("args.name is passed to check functions. in those the dictionary passed in checklist is checked, previously loaded by function load_csv. the match found is > ", state)
            elif args.verbosity >= 1:
                if args.returnr == True:
                    print("Returning {}, the state which capital is {}".format(state, capital_name))
                    return state
                else:
                    print("{} is the capital of {}".format(capital_name, state))
            else:
                if args.returnr == True:
                    return state
                else:
                    print (state)
    if capital_name not in checklist and capital_name not in checklist.values():
        print("Sorry, {} does not seem to be a state or capital present in the checklist".
              format(capital_name))


