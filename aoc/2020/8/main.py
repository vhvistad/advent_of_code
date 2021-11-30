from copy import deepcopy

accumulator = 0

def acc(val):
  global accumulator 
  accumulator += val
  return 1

def jmp(offset):
  return offset

def nop(arg):
  return 1

OPS = {
  'acc': acc,
  'jmp': jmp,
  'nop': nop
}  

def exec(cmd, arg):
  return OPS[cmd](arg)

def run(program):
  global accumulator
  accumulator = 0
  i = 0
  while i < len(program):
    cmd = program[i][0]
    arg = program[i][1]
    visited = program[i][2]
    if visited:
      return False 
    else:
      program[i][2] = True
      i += exec(cmd, arg)
  return True

def find_jmp_nop(program):
  indexes = []
  i = 0
  for instruction in program:
    if instruction[0] == 'jmp' or instruction[0] =='nop':
      indexes.append(i)
    i += 1
  print(f'indexes = {indexes}')
  return indexes

def find_and_fix(program):
  indexes = find_jmp_nop(program)
  for i in indexes:
    new_prog = deepcopy(program)
    if new_prog[i][0] == 'jmp':
      new_prog[i][0] = 'nop'
    elif new_prog[i][0] == 'nop':
      new_prog[i][0] = 'jmp'
    completed = run(new_prog)
    if completed:
      return accumulator

if __name__ == "__main__":
  file = 'aoc/8/input.txt'
  with open(file, 'r')as f:
    program = []
    for line in f:
      line = line.split(' ')
      cmd = line[0]
      arg = int(line[1])
      instruction = [cmd, arg, False]
      program.append(instruction)
  finished = run(deepcopy(program))
  print(f'Result I: {accumulator}')
  result = find_and_fix(program)
  print(f'Result II: {result}')