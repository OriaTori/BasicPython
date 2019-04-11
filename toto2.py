#!user/bin/env python3
# -*- coding: utf-8 -*-

import random

try:
    numb = int(input("How many numbers will you want? "))
    maxNumb = int(input("Put max value of this number: "))
    if maxNumb < numb:
        print("You want to choose %s numbers from %s, which is not allowed because the numbers should be unique." % (numb, maxNumb))
        exit()
except ValueError:
    print("Incorrect data!")
    exit()


listNumb = []
i = 0
while i < numb:
    n = random.randint(1, maxNumb)
    if listNumb.count(n) == 0:
        listNumb.append(n)
        i = i + 1

for i in range(3):
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


    hitNumb = set(listNumb) & types
    if hitNumb:
        print("\nYou get: %s" % len(hitNumb))
        print("Hit numbers: ", hitNumb)
    else:
        print("You did not hit any number - try again.")

    print("\n" + "x" * 40 + "\n")

print("Select numbers: ", listNumb)
