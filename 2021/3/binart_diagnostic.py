import os, sys

x = os.path.realpath(__file__)

print(x)

print("__file__ gives: \n" + __file__)

print("sys.path:")
y = sys.path
print(y[0] + "/input.txt")




with open(y[0] + "/input", 'r') as fp:
    n = len(line := fp.readline().rstrip())

    # digit_count[0] holds an n-length list to count zeros in each position
    # similarly, digit_count[1] counts ones
    digit_count = (n * [0], n * [0])

    while (line := fp.readline().rstrip()):
        for i in range(n):
            digit_count[int(line[i])][i] += 1

gamma = []
eps = []
for i in range(n):
    if digit_count[0] > digit_count[1]:
        gamma.append(0)
        eps.append(1)
    else:
        gamma.append(1)
        eps.append(0)

gamma_rslt = 0
eps_rslt = 0

for i in range(n):
    gamma_rslt += gamma[n-i-1] * 2^(i)
    eps_rslt += eps[n-i-1] * 2^(i)

print(gamma_rslt * eps_rslt)
