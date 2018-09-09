import numpy as np

with open("task_O.txt", 'w') as fin:
    k = 5
    m = 10000
    u = 10000
    d = 1000000
    t = 10000
    fin.write("{} {} {} {} {}\n".format(k, u, m, d, t))
    for _ in range(d):
        user = np.random.randint(0, u)
        movie = np.random.randint(0, m)
        rating = 1 + user % k
        fin.write("{} {} {}\n".format(user, movie, rating))
    for _ in range(t):
        user = np.random.randint(0, u)
        movie = np.random.randint(0, m)
        fin.write("{} {}\n".format(user, movie))
