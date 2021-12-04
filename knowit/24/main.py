def read_input(filename):
    with open(filename, 'r') as f:
        route = ''
        for line in f:
            route = route + line.strip()
    return route

def travel(route):
    reach = 10
    visited = 0
    for house in route:
        if reach <= 0:
            return visited
        else:
            reach -= 1
        if int(house):
            reach += 2
        visited += 1
    

if __name__ == "__main__":
    route = read_input('knowit/24/rute.txt')
    result = travel(route)
    print(f'Result: {result}')