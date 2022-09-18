#!/bin/python3
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive_elements = 0
    negative_elements = 0
    zero_elements = 0

    for i in arr:
      if i > 0:
        positive_elements += 1
      elif i < 0:
        negative_elements += 1
      else:
        zero_elements += 1

    print("{:.6f}".format(positive_elements / len(arr)))
    print("{:.6f}".format(negative_elements / len(arr)))
    print("{:.6f}".format(zero_elements / len(arr)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
