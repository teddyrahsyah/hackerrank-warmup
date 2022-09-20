#!/bin/python3
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time_pm_to_am = {
      "12": "12",
      "01": "13",
      "02": "14",
      "03": "15",
      "04": "16",
      "05": "17",
      "06": "18",
      "07": "19",
      "08": "20",
      "09": "21",
      "10": "22",
      "11": "23",
      }
    new_format = s[:len(s) - 2]
    arr_new_format = new_format.split(":")

    if (s[-2:] == "PM"):
      arr_new_format[0] = time_pm_to_am[s[:2]]
      print(":".join(arr_new_format))
    elif(s[-2:] == "AM"):
      if(s[:2] == "12"):
        arr_new_format[0] = "00"
      print(":".join(arr_new_format))

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)