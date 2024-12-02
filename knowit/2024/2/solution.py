import sympy

def digit_sum(s):
    return sum([int(n) for n in str(s)])

n = 2
primes = 0
special_primes = 0
sum_primes = 0

while special_primes < 10_000:
    if sympy.isprime(n):
        primes += 1
        if digit_sum(n) == digit_sum(primes):
            sum_primes += n
            special_primes += 1
    n += 1

success = 'Success' if sum_primes == 18857085298 else 'Failed'

print(f'sum_primes: {sum_primes} - {success}')

# Ansver is 18857085298