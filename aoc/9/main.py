def read_input(filename):
    with open('aoc/9/'+filename, 'r') as f:
        numbers = f.read().split('\n')
        numbers = [int(n) for n in numbers]
    return numbers

if __name__ == "__main__":
    numbers = read_input('test.txt')
    print(numbers)