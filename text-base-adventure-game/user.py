from options import*

def get_comand() -> None:
    """function for managing the user input"""

    user_input = get_user_input()
    action = user_input[0]
    action = action.lower()

    # quit the game
    if action == 'q':
        quit()
        return

    # options - first word
    if action in action_dictionary:
        user_action = action_dictionary[action]

        # options - second word
        if len(user_input) >= 2:
            print(user_action(user_input[1]))
        else:
            print(user_action("nothing"))

    # wrong option
    else:
        print("{} dosent work in this game".format(action))
        print("Possible options: ")
        for k in action_dictionary.keys():
            print("{}".format(k))
        return

def get_user_input() -> list[str] :
    """Getting the user input as a list"""
    return input("Your comand (q/Q to quit): ").split()