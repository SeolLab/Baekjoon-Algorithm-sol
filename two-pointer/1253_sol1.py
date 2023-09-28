import sys 
input = sys.stdin.readline 
def point(lst):
    cnt = 0
    for i in range(len(lst)): 
        tmp = lst[:i] + lst[i+1:]
        left , right = 0, len(tmp) - 1 
        while left < right: 
            add = tmp[left] + tmp[right]
            if add == lst[i]: 
                cnt += 1 
                break
            elif add < lst[i]: left += 1 
            else: right -= 1
    print(cnt)
N = int(input())
lst = list(map(int,input().split()))
lst.sort()
point(lst)
