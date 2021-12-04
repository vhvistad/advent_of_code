alpha = list('abcdefghijklmnopqrstuvwxyz')

def read_input(file):
  with open(file, 'r') as f:
    hints = f.read().strip().split('\n')
  return hints

def shift(word):
  word = list(word)
  for i in range(len(word)):
    letter = word[i]
    if letter == 'z':
      word[i] = 'a'
    else:
      word[i] = alpha[alpha.index(letter) + 1]
  return ''.join(word)  

def add_words(short, long):
  word_sum = ''
  for i in range(len(short)):
    lsum = (alpha.index(short[i]) + alpha.index(long[i])) % len(alpha)
    word_sum += alpha[lsum]
  return word_sum

def make_columns(hint):
  rows = [list(hint)]
  while len(hint) > 1:
    hint = add_words(shift(hint[1:]), hint)
    rows.append(list(hint))
  columns = []
  for i in range(len(rows[0])):
    columns.append([rows[0][i]])
  for i in range(1, len(rows)):
    for letter in range(len(rows[i])):
      columns[letter].append(rows[i][letter])
  return columns

def is_hint(password, hint):
  columns = make_columns(hint)
  for c in columns:
    c = ''.join(c)
    if password in c:
      return True
  return False

if __name__ == "__main__":
  words = read_input('knowit/11/hint.txt')
  password = 'eamqia'
  hint = None
  print(is_hint('rw', 'juletre'))
  for word in words:
    if is_hint(password, word):
      hint = word
      break
  print(f'Result: {hint}')