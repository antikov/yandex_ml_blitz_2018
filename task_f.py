import bisect
from collections import defaultdict

with open("input.txt") as fin, open("output.txt","w") as fout:
    d = defaultdict(list)
    brr = []
    for line in fin.readlines()[1:]:
        a, b = [float(x) for x in line.split()]
        d[a].append(b)
        brr.append(b)
    brr.sort()
    _sum = 0
    _count = 0
    for a in sorted(d.keys(), reverse=True):
        for el in d[a]:
            del brr[bisect.bisect_left(brr, el)]
        for el in d[a]:
            _sum += bisect.bisect_left(brr, el)
            _sum += (bisect.bisect_right(brr, el) - bisect.bisect_left(brr, el)) / 2
        _count += len(brr) * len(d[a])

    answer = _sum / _count
    fout.write("{:0.6f}".format(answer))
