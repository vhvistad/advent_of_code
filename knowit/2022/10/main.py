import time

R_max = 1_000_000
a = 0.2
g = 0.000075
l = 83
b = 0.1

R_n = 125000
U_n = 3500
n = 10
# test = []


start_time = time.time()
for i in range(n):
    R_new = int(R_n + (a*R_n*(R_max-R_n))/R_max - g*U_n*R_n)
    U_new = int(U_n + (g*U_n*R_n)/l - b*U_n)
    R_n = R_new
    U_n = U_new
    # if i % 1_000_000 == 0:
    #     print(f'n = {i}')

print(f'n = {n}\nR_n = {R_n}\nU_n = {U_n}')
# print(test)

duration = time.time() - start_time
print("--- Finished in %s seconds " % (int(duration)), end='')
print(f'({int(duration//60)}m {int(duration%60)}s)')

#for i in range(1_000_000_000_000):
#    if i % 1_000_000 == 0:
#        print(i)