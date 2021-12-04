import time

def check_string(word, candidate):
  string = ""
  candidate = string.join(candidate)
  return candidate == word or candidate[::-1] == word

def scan(word, matrix):
  for y in range(len(matrix)):
    for x in range(len(matrix[y])-len(word)+1):
      candidate = matrix[y][x:x+len(word)]
      if check_string(word, candidate):
        return True
  return False

def diagonal_scan(word, matrix):
  for y in range(len(matrix)-len(word)+1):
    for x in range(len(word)-1, len(matrix[y])):
      candidate = []
      for char in range(len(word)):
        candidate.append(matrix[y+char][x-char])
      if check_string(word, candidate):
        return True
  return False

def diagonal_scan_reverse(word, matrix):
  for y in range(len(matrix)-len(word)+1):
    for x in range(len(matrix[y])-len(word)+1):
      candidate = []
      for char in range(len(word)):
        candidate.append(matrix[y+char][x+char])
      if check_string(word, candidate):
        return True
  return False

def transpose(matrix):
  transposed = []
  for i in range(len(matrix[0])):
    transposed.append([])
  for j in range(len(matrix)):
    for i in range(len(matrix[0])):
      transposed[i].append(matrix[j][i])
  return transposed

def print_matrix(m):
  for line in m:
    print(line)

def find_missing(wordlist, matrix):
  t_matrix = transpose(matrix)
  result = wordlist.copy()
  for word in wordlist:
    if scan(word, matrix):
      result.remove(word)
      print("Found word: " + word)
    if scan(word, t_matrix):
      result.remove(word)
      print("Found word: " + word)
    if diagonal_scan(word, matrix):
      result.remove(word)
      print("Found word: " + word)
    if diagonal_scan_reverse(word, matrix):
      result.remove(word)
      print("Found word: " + word)

  result = sorted(result)
  string = ""
  for word in result:
    string = string + word + ","
  return string

if __name__ == "__main__":
  start_time = time.time()
  matrix = []
  wordlist = []
  f = open("knowit/3/matrix.txt", "r", encoding="UTF-8")
  for line in f:
    matrix.append(list(line.strip()))
  f.close()
  f = open("knowit/3/wordlist.txt", "r", encoding="UTF-8")
  for line in f:
    wordlist.append(line.strip())
  f.close()

  missing = find_missing(wordlist, matrix)
  print("Missing words: " + missing)
  print("--- %s seconds ---" % (time.time() - start_time))