# https://habr.com/post/333426/
# terrible, but working code, do not repeat at home
with open("stump.in") as fin, open("stump.out", "w") as fout:
    data = []
    for line in fin.readlines()[1:]:
        a, b = [float(i) for i in line.split()]
        data.append([a, b])
    data.sort()
    a_c = 0.0
    a = 0.0
    b_c = len(data)
    b = sum([x[1] for x in data]) / b_c
    c = data[0][0]
    d1 = 0.0
    d2 = sum([(b - x[1]) ** 2 for x in data])
    best_d = d2
    best_params = (a, b, c)
    for i in range(len(data) - 1):
        x, y = data[i]
        a_c += 1
        a_d = a
        a += (y - a) / a_c
        
        b_c -= 1
        b_d = b
        b -= (y - b) / b_c
        d1 += (y - a_d) * (y - a)
        d2 -= (y - b_d) * (y - b)
        d = d1 + d2
        if d < best_d:
            c = (data[i + 1][0] + x) / 2
            best_d = d
            best_params = (a, b, c)
    a, b, c = best_params
    fout.write("{:0.6f} {:0.6f} {:0.6f}".format(a, b, c))