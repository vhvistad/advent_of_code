import math

def myFunc(r):
  return r[2]

def find_vn(state):
  vn = state['vn']
  votes = state['votes']

  total_votes = sum(votes)
  sum_vn = 0
  result = []

  for k, v in enumerate(votes):
    dist = v/total_votes * vn
    vn_floor = math.floor(dist)
    sum_vn += vn_floor
    rest = dist % 1

    result.append([k, vn_floor, rest])
  
  leftover_vn = vn - sum_vn
  result_copy = sorted(result, reverse=True, key=myFunc)

  while leftover_vn > 0:
    for k, _, r in result_copy:
      if leftover_vn == 0:
        break
      
      result[k][1] += 1
      leftover_vn -= 1

  return [result[0][1], result[1][1], result[2][1], result[3][1]]


if __name__ == '__main__':
  total_vn = [0, 0, 0, 0]
  candidates = []
  states = []

  with open('kandidater.txt', 'r') as f:
    for line in f.readlines():
      candidates.append(line.strip().split(' - '))

  with open('stater.txt', 'r') as f:
    for line in f.readlines():
      state, _, vn, k = line.strip().split(' - ')
      votes = [int(v[5:]) for v in k.split(', ')]
      states.append({
        'state': state,
        'vn': int(vn),
        'votes': votes
      })

  for s in states:
    result = find_vn(s)

    for i, k in enumerate(total_vn):
      total_vn[i] += result[i]
    
  winner = candidates[total_vn.index(max(total_vn))]

  # Answer: Donisse Tramp - 131
  print(f'{winner[1]} - {max(total_vn)}')
  