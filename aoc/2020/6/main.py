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

def count_same_answers(answers, group_size):
  total = 0
  for a in answers:
    if answers[a] == group_size:
      total += 1
  return total

def count_yes_everyone(filename):
  with open(filename, 'r') as f:
    answers = {}
    group_size = 0
    total = 0
    for line in f:
      if line != '\n':
        group_size += 1
        for letter in line.strip():
          if letter in answers:
            answers[letter] += 1
          else:
            answers[letter] = 1
      else:
        total += count_same_answers(answers, group_size)
        group_size = 0
        answers = {}
    total += count_same_answers(answers, group_size)
    return total
    # counts.append(len(unique))
    # unique = ''
  # result = 0
  # for c in counts:
  #   result += c
  # # print(counts)
  # return result


if __name__ == "__main__":
  filename = '6/input.txt'
  result = count_yes(filename)
  print(result)
  total = count_yes_everyone(filename)
  print(total)