import numpy as np

class LR:
    def __init__(self, m):
        self.w = np.random.rand(m, 1)
    
    def fit(self, x, y):
        m, d = x.shape
        t = 1
        l = 1
        for i in range(10):
            #print(self.w)
            for i in range(m):
                if y[i] * (x[i] @ self.w)[0] < 1:
                    self.w = (1 - 1/t) * self.w + 1 / (l * t) * y[i]*x[i].reshape(-1,1)
                else:
                    self.w *= (1-1/t)
                t += 1
            #c1=1-(y*(x @ self.w))
            #c1[c1<0] = 0
            #cost = self.w.T @ self.w + l * sum(c1)
            #print(cost)
        
# t = 1;
# for (i=1:iterations)      % iterations over the full data
#     for (tau=1:m)      % pick a single data point
#         if (y(tau)*x(tau,:)*w < 1)  
#             w = (1-1/t)*w + 1/(lambda*t)*y(tau)*x(tau,:)';
#         else
#             w = (1-1/t)*w;
#         end
#         t=t+1;         % increment counter
#     end
#     c1=1-(y.*(x*w));
#     c1(c1<0)=0;  
#     cost = w'*w+ lambda*(sum(c1));
#     fprintf('Cost:%f\n',cost);
# end
    

n, m = [int(x) for x in input().split()]
x = []
y = []
for _ in range(n):
    temp = [float(x) for x in input().split()]
    x.append(temp[:-1])
    y.append(temp[-1])

x = np.array(x)
y = np.array(y)

lr = LR(m)
lr.fit(x, y)
print(*lr.w.reshape(-1))
