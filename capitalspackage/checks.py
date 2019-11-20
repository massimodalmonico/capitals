# function to check if the capital inserted is present in the list
def check_capital(state_name):

    if state_name in list_of_capitals:
        print("The capital of {} is {}".format(state_name,
              list_of_capitals[state_name]))

# function to check if the state inserted is present in the list
def check_state(capital_name):

    for state, capital in list_of_capitals.items():
        if capital == capital_name:
            print("The European state whose capital is {} is {}".
                  format(capital_name, state))


    if capital_name not in list_of_capitals and
    capital_name not in list_of_capitals.values():

        print("Sorry, {} does not seem to be an European state or capital".
              format(capital_name))
