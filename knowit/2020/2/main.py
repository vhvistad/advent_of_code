def is_prime(n):
  if n == 1:
    return "1 is invalid"
  for i in range(2, n // 2 + 1):
    if n % i == 0:
      return False
  return True

def has_digit_7(n):
  n = str(n)
  for digit in n:
    if digit == "7":
      return True
  return False

def find_prime(n):
  while True:
    if is_prime(n):
      return n
    n -= 1

def how_many(n):
  i = 0
  result = 0
  while i < n:
    if has_digit_7(i):
      i += find_prime(i) + 1
    else:
      i += 1
      result += 1
  return result

print(how_many(5433000))