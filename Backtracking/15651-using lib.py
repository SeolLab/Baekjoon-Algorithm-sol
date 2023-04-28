from itertools import product
n, m = map(int, input().split())
lst = [(i+1) for i in range(n)]
for i in list(map(' '.join, product(map(str, lst), repeat=m))):
    print(i)
