import numpy as np
def score(a, b):
    w1 = 0.4
    w2 = -0.8
    return w1 * a + w2 * np.log(b)

with open("restaurants.in", "r") as f, open("restaurants.out", "w") as f2:
    n = int(f.readline())
    for _ in range(n):
        r, d  = [float(x) for x in f.readline().split()]
        if r < 0 :
            r = 6.944
        answ = float(score(r, d))
        f2.write("{:.7f}\n".format(answ))