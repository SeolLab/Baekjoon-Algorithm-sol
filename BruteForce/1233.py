##Solustion1 1233 주사위
a,b,c = map(int,input().split())
res = [0]*81
for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            res[i+j+k] += 1 
print(res.index(max(res)))





##Solustion2 1233 주사위
from collections import Counter
def com(lst):
    counter = Counter(lst)
    com = counter.most_common(1)
    return com[0][0]
a,b,c = map(int,input().split())
lst = []
for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            lst.append(i+j+k)
n = com(lst)
print(n)
