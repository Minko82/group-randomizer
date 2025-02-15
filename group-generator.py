import random

def create_random_groups():

    # user_input = input('Enter a list of items, separated by a space:')
    # user_list= user_input.split()

    user_list = input('Enter a list of items, separated by a space:').split()

    group_size = int(input('Enter the number of groups:'))

    print(user_list)

create_random_groups()