from math import sqrt
from sympy.ntheory import factorint
import time

def divisor_sum(num):
  factors = factorint(num)
  div_sum = 1
  for f in factors:
    s = 1
    for p in range(1, factors[f]+1):
      s += f**p
    div_sum *= s
  return div_sum

def quad_diff(num):
  div_sum = divisor_sum(num)
  if div_sum > 2*num:
    diff = div_sum - 2*num
    if diff % sqrt(diff) == 0:
      return True
  return False


if __name__ == "__main__":
  start_time = time.time()
  result = 0
  for i in range(1, 1_000_000):
    if quad_diff(i):
      result += 1
  print(f'Result: {result}')
  print("--- %s seconds ---" % (time.time() - start_time))