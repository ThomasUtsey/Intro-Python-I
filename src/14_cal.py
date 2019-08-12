"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# Write a program that accepts user input of the form
input_month = input("Enter a month: ")
input_year = input("Enter a year:")

input_month = int(input_month)
input_year = int(input_year)


today = datetime.today()
now_month = today.month
now_year = today.year


def month_year(input_month=now_month, input_year=now_year):
    c = calendar.TextCalendar(calendar.SUNDAY)
    display_calendar = c.formatmonth(input_year, input_month)
    print(display_calendar)


month_year(input_month, input_year)
