def read_input(file):
  with open(file, 'r') as f:
    games = []
    for line in f:
      games.append(line.strip().split(','))
  return games

def find_winner(games):
  players = {}
  for game in games:
    max_points = len(game) - 1
    for p in range(len(game)):
      player = game[p]
      if player not in players:
        players[player] = max_points - p
      else:
        players[player] += max_points - p
  winner = max(players, key=players.get)
  return f'{winner}-{players[winner]}'


if __name__ == "__main__":
  games = read_input('knowit/10/leker.txt')
  print(find_winner(games))