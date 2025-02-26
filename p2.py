import math

def derangement(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (n - 1) * (derangement(n - 1) + derangement(n - 2))

n1 = 10
for i in range(3, 23):
    x = derangement(i)
    print(f'the number of derangements of {i} items is {x}')
    print(f'prob of derangement of {i} items is {x/math.factorial(i)}\n')
