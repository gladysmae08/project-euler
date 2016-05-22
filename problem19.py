# counting sundays
'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

month_days = {
              'jan' : 31,
              'feb' : 28,
              'mar' : 31,
              'apr' : 30,
              'may' : 31,
              'jun' : 30,
              'jul' : 31,
              'aug' : 31,
              'sep' : 30,
              'oct' : 31,
              'nov' : 30,
              'dec' : 31
}
month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 366%7 = 2; 1 jan 1901 = wed
year = 1901
sunday_count = 0
day_count = 1

is_sunday = lambda x : (x % 7 == 6) 
while (year < 2001):
    for month in month_lengths:
        if month == 28 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            month += 1
        day_count += month
        if is_sunday(day_count):
            sunday_count += 1
    year += 1
if is_sunday(day_count):
    sunday_count -= 1

print(sunday_count)
        
