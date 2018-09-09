import numpy as np
from collections import defaultdict

k, u, m, d, t = [int(i) for i in input().split()]

mul = 0.01
ratings = []
users = np.random.randn(u) * mul
movies = np.random.randn(m) * mul
mean_rating = 0
for _ in range(d):
    user, movie, rating = [int(i) for i in input().split()]
    #rating /= k
    mean_rating += rating
    ratings.append([user, movie, rating])
mean_rating /= d
predict = []
for _ in range(t):
    predict.append([int(i) for i in input().split()])
dim = 10
w = np.random.randn(u, dim) * mul
x = np.random.randn(m, dim) * mul

#import time

lr = 0.02
lmbda = 0.0
for i in range(10):
    #start_time = time.time()
    #cost = 0
    for user, movie, rating in ratings:
        temp = w[user] @ x[movie].T - rating + users[user] + movies[movie] + mean_rating
        #cost += temp ** 2
        x[movie] -= lr * (temp * w[user])# + lmbda * x[movie])
        w[user] -= lr * (temp * x[movie])# + lmbda * w[user])
        movies[movie] -= lr * (temp)# + lmbda * movies[movie])
        users[user] -= lr * (temp)# + lmbda * users[user])
    #cost += lmbda * (np.sum(x ** 2) + np.sum(w ** 2) + np.sum(movies ** 2) + np.sum(users **2))
    #print(cost, time.time() - start_time)

for user, movie in predict:
    score = sum(w[user] * x[movie]) + users[user] + movies[movie] + mean_rating
    #score *= k
    score = max(0, min(score, k))
    print(score)