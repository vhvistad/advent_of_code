alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alt(filename):
  with open(filename, 'r') as f:
    string = f.read()
  for i in range(len(alphabet)):
    letter1 = alphabet[i]
    count = 0
    j = 0
    while j < len(string):
      letter2 = string[j]
      if letter2 == letter1:
        count += 1
        if count != alphabet.index(letter1) + 1:
          string = string[:j] + string[j+1:]
        else:
          j += 1
      else:
        j += 1
  return string


if __name__ == "__main__":
  result = alt('knowit/13/text.txt')
  print(f'Result: {result}')