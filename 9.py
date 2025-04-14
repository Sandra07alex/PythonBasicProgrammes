# Write a Python program to display calendar for the current year.
import calendar
import datetime

current_year= datetime.datetime.now().year
cal=calendar.TextCalendar(calendar.SUNDAY)
print(f"Calander of the year{current_year} \n")
for i in range(1,13):
    print(cal.formatmonth(current_year, i ))
