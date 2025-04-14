# Write a Python Program to Check Leap Year.

#a % 4 == 0 ➝ Year is divisible by 4
# a % 100 != 0 ➝ Not a century year
# OR a % 400 == 0 ➝ Century year, but divisible by 400 (which makes it leap)

a= int(input("enter the year "))
if(a%4==0 and a%100!=0 or a%400==0):
    print(f"{a} is leap year")
else:
    print(f"{a} is not leap year")