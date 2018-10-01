import numpy as np

class LinearSeparateBoundary:
    def __init__(self, m):
        self.w = np.random.rand(m, 1)
    
    def fit(self, x, y):
        for i in range(len(x)):
            if np.sign(self.w.T @ x[i]) != y[i]:
                self.w += x[i] * y[i]

    def get_weights(self):
        return self.w.reshape(-1)

n, m = [int(x) for x in input().split()]
x = []
y = []
for _ in range(n):
    temp = [float(x) for x in input().split()]
    x.append(temp[:-1])
    y.append(temp[-1])

x = np.array(x)
y = np.array(y)

lr = LinearSeparateBoundary(m)
lr.fit(x, y)
print(*lr.get_weights())
