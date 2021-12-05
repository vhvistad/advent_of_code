import time
import matplotlib.pyplot as plt

start_time = time.time()

def position_near_target(step):
    diff = 8 + ((step-42) // 45) * 15
    start_step = 42 + 45*((step-42) // 45)
    x = (start_step + diff)//2
    y = (start_step - diff)//2
    return x, y, start_step
    
steps = 100000000000000000079
x, y, start_step = position_near_target(steps)
direction = 'north'
diff = []

for step in range(start_step, steps):
    if direction == 'north':
        y += 1
        if y % 3 == 0 and y % 5 != 0:
            direction = 'east'
    elif direction == 'east':
        x += 1
        if x % 5 == 0 and x % 3 != 0:
            direction = 'north'
    diff.append(x-y)

print(f'Final position: ({x}, {y})')
print("--- {:.6f} seconds ---".format(time.time() - start_time))
# plt.plot(diff)
# plt.show()