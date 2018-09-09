import numpy as np

with open("coins.in") as f:
    i = 0
    a = []
    for line in f.readlines()[1:]:
        _k ,_m = [float(x) for x in line.split()]
        _k += 2
        _m += 1
        p = _m / _k
        q = 1 - p
        ml = p ** _m * q ** (_k - _m)
        a.append((i, _m / _k, ml))
        i += 1
    
    a.sort(key=lambda x: x[1])

    b = []
    for i in a:
        b.append(i[0])
    np.savetxt("coins.out", b, fmt='%d')