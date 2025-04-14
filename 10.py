# Write a Python program to solve quadratic equation
import math
a=float(input("enter the value of a "))
b=float(input("enter the value of b "))
c=float(input("enter the value of c "))
# ax^2 + bx + c = 0
# (−𝑏 ± (𝑏 − 4𝑎𝑐 )/(2𝑎)
d=b**2-4*a*c
if d>0:git branch -M main
    root1=(-b+math.sqrt(d))/(2*a)
    root2=(-b-math.sqrt(d))/(2*a)
    print(f"roots are real and different {root1} and {root2}")
elif d==0:
    root1=-b/(2*a)
    print(f"roots are real and same {root1}")
else:
    realpart=-b/(2*a)
    imaginarypart=math.sqrt(-d)/(2*a)
    print(f"roots are complex {realpart}+{imaginarypart}i and {realpart}-{imaginarypart}i")