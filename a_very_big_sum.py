#!/bin/python3
#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
  result = 0
  for i in ar:
    result += i

  return result


if __name__ == '__main__':

  ar_count = int(input().strip())

  ar = list(map(int, input().rstrip().split()))

  result = print(aVeryBigSum(ar))
