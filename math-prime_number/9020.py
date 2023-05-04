##골드바흐의 추측 9020번 python
def gold(a,b):
    if not is_prime(a) or not is_prime(b): 
        return gold(a-1,b+1)
    else: return a,b 

def is_prime(a):
    for i in range(2,int(a**0.5)+1):
        if not a%i: return False
    return True 
import sys 
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
for i in range(int(input())): 
    x = int(input())
    x >>= 1
    if is_prime(x):
        print(x,x)
    else: 
        t = gold(x,x)
        print(*t)    
