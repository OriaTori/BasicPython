#!user/bin/env python3
# -*- coding: utf-8 -*-

from totomodul import settings, getNumbers, getTypes, results

def main(args):
    # game settings
    numb, maxNumb, numbDraws = settings()

    # get numbers
    numbers = getNumbers(numb, maxNumb)

    # get types
    for i in range(numbDraws):
        types = getTypes(numb, maxNumb)
        numberOfHits = results(numbers, types)

        print("Hit numbers: ", numberOfHits)
        print("\n" + "x" * 40 + "\n")

    print("Select numbers: ", numbers)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
