import time

directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]

def read_input(wordlist, matrix):
  w = []
  m = []
  with open(wordlist, "r", encoding="UTF-8") as f:
    for line in f:
      w.append(line.strip())
  with open(matrix, "r", encoding="UTF-8") as f:
    for line in f:
      m.append(list(line.strip()))
  return w, m

def scan(word, matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] == word[0]:
        if check_word(word, matrix, (i,j)):
          return True

def check_word(word, matrix, pos):
  for d in directions:
    if scan_out(word, matrix, pos, d):
      return True
  return False

def scan_out(word, matrix, pos, direction):
  i = pos[0]
  j = pos[1]
  if edge_too_close(word, matrix, pos, direction):
    return False
  for char in range(1, len(word)):
    i += direction[0]
    j += direction[1]
    if matrix[i][j] != word[char]:
      return False
  return True

def edge_too_close(word, matrix, pos, direction):
  fin_i = pos[0] + (len(word)-1)*direction[0]
  fin_j = pos[1] + (len(word)-1)*direction[1]
  if fin_i > len(matrix)-1 or fin_i < 0:
    return True
  if fin_j > len(matrix[0])-1 or fin_j < 0:
    return True
  return False

def print_matrix(m):
  for line in m:
    print(line)

def main(wordlist, matrix):
  result = wordlist.copy()
  for word in wordlist:
    if scan(word, matrix):
      result.remove(word)
      print("Found word: " + word)
  result = sorted(result)
  string = ""
  i = 0
  for word in result:
    i += 1
    if i < len(result):
      string = string + word + ","
    else:
      string = string + word
  return string

if __name__ == "__main__":
  start_time = time.time()
  wordlist, matrix = read_input("knowit/3/wordlist.txt", "knowit/3/matrix.txt")
  missing = main(wordlist, matrix)
  print("Missing words: " + missing)
  print("--- %s seconds ---" % (time.time() - start_time))