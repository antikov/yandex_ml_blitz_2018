n, m = [int(x) for x in input().split()]

p = {}
for i in range(n):
    p[i] = [0] * n

for _ in range(m):
    a, b = [int(x) - 1 for x in input().split()]
    p[a][b] += 1

best_arr = []
added = set()

while len(best_arr) < n:
    _min = 999999
    for i in range(n):
        if i not in added:
            _sum = sum(p[i])
            if _sum < _min:
                _min = _sum
                el = i
    best_arr.append(el)
    added.add(el)
    for i in range(n):
        p[i][el] = 0

for el in best_arr[::-1]:
    print(el + 1)
