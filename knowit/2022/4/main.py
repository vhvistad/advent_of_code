def numberToBase(n, b):
    if n == 0:
        return 0
    digits = []
    while n:
        digits.append(str(n % b))
        # digits += str(n % b)# + digits
        n //= b
    return ''.join(digits[::-1])
    # return digits

def is_palindrome(n):
    n = str(n)
    # return n[:len(n)//2] == n[len(n)//2 + len(n)%2:][::-1]

    if int(len(n)) % 2 == 0:
        first, second = n[:len(n)//2], n[len(n)//2:]
    else:
        first, second = n[:len(n)//2], n[len(n)//2+1:]

    return first == second[::-1]

def is_multipalindrome(n):
    count = 0
    palindromes = []
    for base in range(2, 17):
        if is_palindrome(numberToBase(n, base)):
            # palindromes.append('Base ' + str(base) + ': ' + str(numberToBase(n, base)))
            count += 1
        if count == 3:
            # print(f'Number: {n}')
            # print(f'Palindromes: {palindromes}\n')
            return True
    return False




if __name__ == "__main__":

    sum_of_multipalindromes = 0

    for n in range(10_000_000):
    # for n in range(1_000):
        if is_multipalindrome(n):
            sum_of_multipalindromes += n
    
    print(sum_of_multipalindromes - 991)