numbers = {
    '': 0,
    'en': 1,
    'to': 2,
    'tre': 3,
    'fire': 4,
    'fem': 5,
    'seks': 6,
    'sju': 7,
    'åtte': 8,
    'ni': 9,
    'ti': 10,
    'elleve': 11,
    'tolv': 12,
    'tretten': 13,
    'fjorten': 14,
    'femten': 15,
    'seksten': 16,
    'sytten': 17,
    'atten': 18,
    'nitten': 19,
    'tjue': 20,
    'tretti': 30,
    'førti': 40,
    'femti': 50
}

if __name__ == "__main__":
    file = 'knowit/2021/1/tall.txt'
    with open(file, 'r', encoding="UTF-8") as f:
        string = f.read().strip()
    
    result = 0
    while len(string) > 0:
        candidate = ''
        for num_str in numbers.keys():
            if len(num_str) <= len(string) and num_str == string[0:len(num_str)]:
                if numbers[num_str] > numbers[candidate]:
                    candidate = num_str
        result += numbers[candidate]
        string = string[len(candidate):]


    print(f'Result = {result}')