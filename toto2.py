#!user/bin/env python3
# -*- coding: utf-8 -*-

import random

numb = int(input("How many numbers will you want? "))
maxNumb = int(input("Put max value of this number: "))

print("Chose %s from %s numbers: " % (numb, maxNumb))

listNumb = []
#for i in range(numb):
i = 0
while i < numb:
    n = random.randint(1, maxNumb)
    if listNumb.count(n) == 0:
        listNumb.append(n)
        i = i + 1
#    print(n)
print("Select numbers: ", listNumb)
