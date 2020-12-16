def generation_size(filename):
  with open(filename, 'r') as f:
    gen_list = [0]
    generation = 0
    prev_char = ''
    string = f.read()
    for char in string:
      if char == ' ' and prev_char != ')':
        gen_list[generation] += 1
      elif char == '(':
        generation += 1
        if len(gen_list) == generation:
          gen_list.append(0)
      elif char == ')' and prev_char != ')':
        gen_list[generation] += 1
        generation -= 1
      elif char == ')':
        generation -= 1
      prev_char = char
  return max(gen_list)


if __name__ == "__main__":
  result = generation_size('knowit/12/family.txt')
  print(f"Result: {result}")