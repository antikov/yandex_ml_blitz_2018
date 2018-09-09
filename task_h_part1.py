import numpy as np

def get_score(a, w1, w2, w3):
    def score(x, y):
        return w1 * x + w2 * np.log(y)

    _sum = 0
    _count = 0
    for i in range(len(a)):
        w, r1, r2, d1, d2 = a[i]
        if r1 != -1 and r2 != -1:
            if w == 0:
                _count += 1
                _sum += np.log1p(np.exp(score(r2, d2) - score(r1, d1)))
            elif w == 1:
                _count += 1
                _sum += np.log1p(np.exp(score(r1, d1) - score(r2, d2)))
            else:
                _count += 2
                _sum += np.log1p(np.exp(score(r1, d1) - score(r2, d2)))
                _sum += np.log1p(np.exp(score(r2, d2) - score(r1, d1)))
    return _sum / _count

a = []
_count = 0
with open("restaurants_train.txt", "r") as f:
    for _ in range(1000):
        w, r1, r2, d1, d2 = [float(x) for x in f.readline().split()]

        a.append([w, r1, r2, d1, d2])
a = np.array(a)
#preprocess
#a[:, 4] = 1 - a[:, 4]
#a[:, 3] = 1 - a[:, 3]
#mask1 = a[:, 1] == -1
#mask2 = a[:, 2] == -1

m = 6.944

for i in range(1000):
   if a[i, 1] == -1:
       a[i, 1] = m
   if a[i, 2] == -1:
       a[i, 2] = m

best_score = 1000
best_params = None
w1 = np.linspace(0.0, 0.6, 10)
w2 = np.linspace(-2, 0, 100)
w3 = np.linspace(-10, 0, 1)
for _w1 in w1:
    for _w2 in w2:
        for _w3 in w3:
            _s = get_score(a, _w1, _w2, _w3)
            if _s < best_score:
                best_score = _s
                best_params = _w1, _w2, _w3
                print(best_score, best_params)
