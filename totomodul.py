#!user/bin/env python3
# -*- coding: utf-8 -*-

import random

def settings():
    """ Function in which we set proper value: numb, maxNumb, number of tries, degree of difficulty."""
    while True:
        try:
            numb = int(input("How many numbers will you want? "))
            maxNumb = int(input("Put max value of this number: "))
            if maxNumb < numb:
                print("You want to choose %s numbers from %s, which is not allowed because the numbers should be unique." % (numb, maxNumb))
                continue
            numberOfDraws = int(input("Enter the number of draws: "))
            return (numb, maxNumb, numberOfDraws)
        except ValueError:
                    print("Incorrect data!")
                    continue

def getNumbers(numb, maxNumb):
    """The function returns an unique integers from 1 to maxNumb """
    listNumb = []
    i = 0
    while i < numb:
        n = random.randint(1, maxNumb)
        if listNumb.count(n) == 0:
            listNumb.append(n)
            i = i + 1
    return listNumb

def getTypes(numb, maxNumb):
    """ The function gets types from the user. """
    print("Choose numbers %s from %s: " % (numb, maxNumb))
    types = set()
    i = 0
    while i < numb:
        try:
            typ = int(input("Enter the %s number: " % (i + 1)))
        except ValueError:
            print("Incorrect data format!")
            continue

        if 0 < typ <= maxNumb and typ not in types:
            types.add(typ)
            i = i + 1
    return types

def results(numbers, types):
    """ The function compers draws number and types number - returns number of hits."""
    hitNumb = set(numbers) & types
    if hitNumb:
        hitNumb = ", ".join(map(str, hitNumb))
        print("\nYou get: %s" % hitNumb)
    else:
        print("You did not hit any number - try again.")
    return len(hitNumb)
