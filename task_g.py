import numpy as np
import random

def score(aaa):
    r = aaa[range(8), range(8)]
    return np.mean(r) - np.mean(aaa)

def RandomPermutation():  
    perm = list(range(8))  
    random.shuffle(perm)  
    return perm  

def StupidPermutation():  
    partialSums = [0,1,8,35,111,285,  
        628,1230,2191,3606,5546,8039,11056,14506,18242,  
        22078,25814,29264,32281,34774,36714,38129,39090,  
        39692,40035,40209,40285,40312,40319,40320]  
    r = random.randint(0, partialSums[-1])  
    numInv = 0  
    while partialSums[numInv] < r:  
        numInv += 1  
    perm = list(range(8))  
    for step in range(numInv):  
        t1 = random.randint(0, 7)  
        t2 = random.randint(0, 7)  
        perm[t1], perm[t2] = perm[t2], perm[t1]  
    return perm

# dist = np.zeros((8, 8))
# for _ in range(10000):
#     b = RandomPermutation()
#     for index, el in enumerate(b):
#         dist[index, el] += 1
# print(dist)

# dist = np.zeros((8, 8))
# for _ in range(10000):
#     b = StupidPermutation()
#     for index, el in enumerate(b):
#         dist[index, el] += 1
# print(dist)

# exit()


with open("permutations.in", 'r') as f:
    n = int(f.readline())
    ans = []
    for _ in range(n):
        a = []
        dist = np.zeros((8, 8))
        for __ in range(1000):
            b = [int(x) for x in f.readline().split()]
            for index, el in enumerate(b):
                dist[index, el] += 1
            a.append(b)
        ans.append((_, score(dist)))
    
    ans = sorted(ans, key=lambda x: x[1])
    #print(ans)

    answ = [el[0] for el in ans]
    #answ = np.array(answ, dtype=int)
    np.savetxt("permutations.out", answ, fmt='%d')
    #for el in answ:
    #    print(el)