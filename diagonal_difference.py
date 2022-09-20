#!/bin/python3
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr, n):
    # Write your code here
    asc_diagonal = 0
    desc_diagonal = 0

    # Diagonal Ascending
    for i in range(n):
      asc_diagonal += arr[i][i]

    # Diagonal Ascending
    x = 0
    for i in range(n-1, -1, -1):
      desc_diagonal += arr[x][i]
      x += 1
    return abs(asc_diagonal - desc_diagonal)


if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = print(diagonalDifference(arr, n))
