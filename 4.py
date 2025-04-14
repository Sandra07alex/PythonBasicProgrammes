# Write a Python program to swap two variables.
a=int(input("enter the 1st number "))
b=int(input("enter the 2nd number "))
print(f'before swapping a={a} and b={b}')
temp=a
a=b
b=temp
print(f'After swapping a={a} and b={b}')

# to swap two variables without temp variable.
a, b = b, a

print(f'After 2nd swapping a={a} and b={b}')