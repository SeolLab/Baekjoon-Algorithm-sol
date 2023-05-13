##암기왕 2776 
import sys
input = sys.stdin.readline
for i in range(int(input())):
    N = int(input())
    lst = list(map(int,input().split()))
    lst.sort()
    M = int(input())
    lst2 = list(map(int,input().split()))
    for x in lst2:
        left, right = 0, N-1 
        while left <= right:
            mid = (left + right) // 2
            if lst[mid] <= x: left = mid+1 
            else: right = mid -1
        if lst[right] == x: print(1)
        else: print(0)
