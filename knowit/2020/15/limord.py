def read_input(wlist, riddles):
  with open(wlist, 'r', encoding="UTF-8") as f:
    wordlist = f.read().split('\n')
  with open(riddles, 'r', encoding="UTF-8") as f:
    riddles = f.read().split('\n')
  return wordlist, riddles

def limord(w, wordlist):
  valid_words = []
  for word in wordlist:
    if len(word) > len(w):
      if word[:len(w)] == w:
        valid_words.append(word[len(w):])
      elif word[-len(w):] == w:
        valid_words.append(word[:-len(w)])
  return valid_words

def find_common(wordlist, words):
  print(f'checking words: {words}')
  result1 = limord(words[0], wordlist)
  result2 = limord(words[1], wordlist)
  # print(result1)
  # print(result2)
  return set(result1) & set(result2)


if __name__ == "__main__":
  wordlist, riddles = read_input('knowit/15/wordlist.txt', 'knowit/15/riddles.txt')
  s = set()
  for pairs in riddles:
    words = pairs.split(', ')
    s = s | find_common(wordlist, words)
    # print(s)
  s = s & set(wordlist)
  result = 0
  print(s)
  for word in s:
    result += len(word)
  print(f'Result: {result}')