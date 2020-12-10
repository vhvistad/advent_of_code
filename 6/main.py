def count_yes(filename):
  counts = []
  with open(filename, 'r') as f:
    unique = ''
    for line in f:
      if line != '\n':
        for letter in line.strip():
          if letter not in unique:
            unique += letter
      else: 
        counts.append(len(unique))
        unique = ''
    counts.append(len(unique))
    unique = ''
  result = 0
  for c in counts:
    result += c
  # print(counts)
  return result


if __name__ == "__main__":
  filename = '6/input.txt'
  result = count_yes(filename)
  print(result)

