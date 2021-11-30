from sympy import isprime

def sequence(length):
  length += 1
  primes = 0
  seq = [0, 1]
  content = {0, 1}
  for n in range(2, length):
    a = seq[-2] - n
    if a < 0 or a in content:
      a = seq[-2] + n
    seq.append(a)
    content.add(a)
    if isprime(a):
      primes += 1
  return primes
    
if __name__ == "__main__":
  primes = sequence(1800813)
  print(f'Primes: {primes}')