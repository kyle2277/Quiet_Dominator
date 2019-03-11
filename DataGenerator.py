import os
import random


def __init__():
    # todo write game generator
    file = input("Enter name for new file: ")
    while os.path.isfile(file):
        print("File %s already exists." % file)
        file = input("Enter name for new file: ")
    f = open(file, 'w')
    f.write(generate_data())


def generate_data():
    data = ""
    com = []
    user = []
    o = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(5):
        rand = random.randint(1, len(o)-1)
        com.append(o[rand])
        o.pop(rand)

    print('com (X)= ', com)

    for j in range(3):
        rand = random.randint(1, len(o)-1)
        user.append(o[rand])
        o.pop(rand)
    user.append(o[0])
    o.pop(0)
    print('user (O)= ', user)
    return data

def generate_game():
    first = goes_first()
    if first == 'com':
        # com first
    else:
        # user first


def generate_single_game():
    pass


def goes_first():
    rand = random.randint(0, 1)
    if rand == 0:
        return 'com'
    else:  # console == 1
        return 'user'


__init__()

