import random


def generate_random():
    f1 = open('h.txt', 'w')
    for j in range(10000):
        x = ''
        y = ['H', 'T']
        for i in range(100):
            x += random.choice(y)
        f1.write(x + '\n')
