#!/bin/python3
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive_elements = []
    negative_elements = []
    zero_elements = []

    for i in arr:
      if i > 0:
        positive_elements.append(i)
      elif i < 0:
        negative_elements.append(i)
      else:
        zero_elements.append(i)

    print("{:.6f}".format(len(positive_elements) / len(arr)))
    print("{:.6f}".format(len(negative_elements) / len(arr)))
    print("{:.6f}".format(len(zero_elements) / len(arr)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
