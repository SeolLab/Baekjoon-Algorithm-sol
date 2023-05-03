##simulation 
## 1547 python 
import sys
input = sys.stdin.readline 
lst = []
tar = 1
for i in range(int(input())):
    a, b = map(int,input().split())
    if tar == a: tar = b
    elif tar == b: tar = a
print(tar)
