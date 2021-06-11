#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    """
    """
    
    moto = a
    domo = b

    moto_points = 0
    domo_points = 0

    if moto[0] != domo[0]:

        if moto[0] > domo[0]:
            moto_points += 1

        else:
            domo_points += 1

    else:
        pass

    if moto[1] != domo[1]:

        if moto[1] > domo[1]:
            moto_points += 1

        else:
            domo_points += 1

    else:
        pass

    if moto[2] != domo[2]:

        if moto[2] > domo[2]:
            moto_points += 1

        else:
            domo_points += 1

    else:
        pass

    return moto_points, domo_points

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
