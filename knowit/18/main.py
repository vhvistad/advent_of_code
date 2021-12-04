def read_input(filename):
    file = 'knowit/18/' + filename
    with open(file, 'r') as f:
        words = f.read().split('\n')
    return words

def is_palindrome(word):
    # word = list(word)
    for i in range(len(word) // 2):
        if word[i] != word[len(word)-1-i]:
            return False
    return True


if __name__ == "__main__":
    words = read_input('test.txt')
    for word in words:
        print(is_palindrome(word))
