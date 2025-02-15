import random

def create_random_groups():

    # user_input = input('Enter a list of items, separated by a space:')
    # user_list= user_input.split()

    # NOTE: The above two lines can be combined into one line
    # NOTE: The split() method splits a string into a list with spaces as the default separator
    # NOTE: You can also specify the separator, like this: split(','), split(';'), etc.
    user_list = input('Enter a list of items, separated by a space:').split()

    # TODO: if the user doesn't enter an int
    group_size = int(input('Enter the number of groups:'))

    # NOTE: Uses the Fisher-Yates shuffle algorithm (aka Knuth Shuffle) to shuffle the list
    random.shuffle(user_list)



    print(user_list)

create_random_groups()