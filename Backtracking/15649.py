## backtracking
## 15649 N과 M(1)

import sys
input = sys.stdin.readline
def refunc(k):
    if k == M: 
        for i in range(M):
            print(lst[i],end=" ") 
        print()
    for i in range(1,N+1):
        if not isused[i]: 
            lst[k] = i 
            isused[i] = 1
            refunc(k+1)
            isused[i] = 0 
N,M = map(int,input().split())
lst = [0]*10
isused = [False]*10
refunc(0)
