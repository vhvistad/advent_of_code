from sympy import *

count = 0
found = []

def is_happy(n):
    sum_digits = 0
    for s in str(n):
        sum_digits += int(s)
    return n % sum_digits == 0

def checkHarshad(n):
    sum = 0
    temp = n
    while temp > 0:
        sum = sum + temp % 10
        temp = temp // 10

    # Return true if sum of digits is multiple of n
    return n % sum == 0
    
with open('C:/Users/vvistad/repos/advent_of_code/knowit/2025/8/input.txt', 'r') as f:
    for line in f.readlines():
        numbers = line.strip().split(' ')
        for num in numbers:
            n = int(num)
            if n in found:
                continue
            # if (n % 2 != 0 and checkHarshad(n)) or isprime(n):
            if checkHarshad(n) and isprime(n):
                count += 1
                found.append(n)
        # num = [int(s) for s in line.strip().split(' ')]
        # numbers.extend(num)

print(count)

# print(checkHarshad(35))