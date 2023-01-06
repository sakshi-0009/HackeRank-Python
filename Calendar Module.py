'''Task :-

You are given a date. Your task is to find what the day is on that date.

Input Format :-

A single line of input containing the space separated month, day and year, respectively, in DD-MM-YYY format.'''

# Answer : 

import calendar
#calendar.Calendar(calendar.SUNDAY)
user_input = input().split()
month = int(user_input[0])
day = int(user_input[1])
year = int(user_input[2])
c = calendar.weekday(year, month, day)

if c == 0:
    print("MONDAY")
elif c == 1:
    print("TUESDAY")
elif c == 2:
    print("WEDNESDAY")
elif c==3:
    print("THURSDAY")
elif c==4:
    print("FRIDAY")
elif c== 5:
    print("SATURDAY")
elif c==6:
    print("SUNDAY")
