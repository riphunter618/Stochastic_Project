import numpy as np
import matplotlib.pyplot as plt

def draw_histogram():
    f1 = open('h.txt', 'r')
    x1 = f1.readlines()
    y = ['H', 'T']
    res2 = []
    for x in x1:
        res1 = []
        for k in y:
            c1 = 0
            res = 0
            for j in x:
                if j == k:
                    c1 += 1
                else:
                    res = max(res, c1)
                    c1 = 0
            res = max(res, c1)
            res1.append(res)
        res2.append(max(res1))
    print(res2)
    hist = np.histogram(res2, bins=50)
    counts, bins = hist
    plt.stairs(counts, bins)
    plt.show()
