#!/bin/python3
#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    alice = 0
    bob = 0
    result = []
    # Write your code here
    if a[0] > b[0]:
        alice += 1
    elif a[0] < b[0]:
        bob += 1

    if a[1] > b[1]:
        alice += 1
    elif a[1] < b[1]:
        bob += 1

    if a[2] > b[2]:
        alice += 1
    elif a[2] < b[2]:
        bob += 1

    result.append(alice)
    result.append(bob)
    return result

if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = print(compareTriplets(a, b))
