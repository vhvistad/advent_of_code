def read_rules(file):
  rules = []
  with open(file, 'r') as f:
    for line in f:
      rule = line.strip().split(' bags contain ')
      rule[1] = rule[1].split(', ')
      # Remove trailing "bag." and "bags.": 
      rule[1][-1] = rule[1][-1][:-5].strip()
      if len(rule[1]) > 1:
        # Remove trailing "bag" and "bags":
        for i in range(len(rule[1][:-1])):
          rule[1][i] = rule[1][i][:-4].strip()
      rules.append(rule)
  return rules

def find_content_size(color, rules):
  contains = 0
  for rule in rules:
    if color == rule[0]:
      if rule[1][0] == 'no other':
        return contains
      else:
        for content in rule[1]:
          amount = int(content[0])
          contains += amount + amount * find_content_size(content[2:], rules)
      break
  return contains

def find_outermost(color, rules):
  outermost = []
  for rule in rules:
    for inner_bag in rule[1]:
      if inner_bag[2:] == color:
        outermost.append(rule[0])
        tmp = find_outermost(rule[0], rules)
        for t in tmp:
          if t not in outermost:
            outermost.append(t)
  return outermost

if __name__ == "__main__":
  rules = read_rules('aoc/7/input.txt')
  color = 'shiny gold'
  result = len(find_outermost(color, rules))
  print(f'Part I result: {result}')
  result = find_content_size(color, rules)
  print(f'Part II result: {result}')