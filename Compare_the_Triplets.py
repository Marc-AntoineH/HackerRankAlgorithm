#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b): # a and b are the list of number taken
    alice = 0
    bob = 0
    totalInput = len(a) 

    for i in range(totalInput):
        if (a[i] > b[i]):
            alice += 1
        if (a[i] < b[i]):
            bob += 1
        if (a[i] == b[i]):
            alice += 0
            bob += 0    
    return (alice, bob)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
