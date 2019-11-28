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
            print("args.name is validated by function input_validation then passed to check functions. in those the dictionary 'list_of_capitals' is checked, previously loaded by function load_csv. the match found is > ", checklist[state_name])
        elif args.verbosity >= 1:
            print("The capital of {} is {}".format(state_name,
              checklist[state_name]))
        else:
            print(checklist[state_name])


# function to check if the state inserted is present in the list
def check_state(capital_name, checklist, args):

    for state, capital in checklist.items():
        if capital == capital_name:
            if args.verbosity >= 2:
                print("args.name is validated by function input_validation then passed to check functions. in those the dictionary 'list_of_capitals' is checked, previously loaded by function load_csv. the match found is > ", state)
            elif args.verbosity >= 1:
                print("The European state whose capital is {} is {}".
                  format(capital_name, state))
            else:
                print (state)
    if capital_name not in checklist and capital_name not in checklist.values():
        print("Sorry, {} does not seem to be an European state or capital".
              format(capital_name))


