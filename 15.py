#Write a Python Program to Print all Prime Number till that number
#A prime number is a number greater than 1 that has only two factors: 1 and itself.
def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

a = int(input("Enter the number: "))

print(f"Prime numbers up to {a}:")
for number in range(2, a + 1):
    if check_prime(number):
        print(number)

