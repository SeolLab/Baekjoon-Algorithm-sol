## 예산
import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int,input().split()))
M = int(input())

left, right = 0, max(lst)
while left <= right: 
    mid = (left+right) // 2
    add = 0
    for i in lst:
        if mid < i: i = mid
        add += i 
    if add <= M: left = mid +1 
    else: right = mid - 1
print(right)
