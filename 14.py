#Write a Python Program to Check Prime Number
#A prime number is a number greater than 1 that has only two factors: 1 and itself.


a=int(input("enter the number "))
flag=True
if (a==1) :
    flag=False
else:
    for i in range (2,a):
        if(a%i==0):
            flag=False
            break
if (flag==True):
    print(f"{a}is a Prime Number")
else:
    print(f"{a}is  Not a Prime Number")
