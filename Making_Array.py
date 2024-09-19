# import numpy as np
# array=np.array([1,3,4,5,6,6,7,7,8,8,34])
# print(type(array))
# print(array)
# print(array)

# def waleed():
#     print(3+4)

# waleed()

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = 6
print(f"{number} is prime:", is_prime(number))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
number=int(input("Enter Number"))
print(f"{number} is Prime:",is_prime(number))