import sys
input = sys.stdin.readline 
from collections import deque 
def bfs(first_node):
    deq = deque([first_node])
    while deq: 
        tmp = deq.popleft()
        for i in graph[tmp]:
            if visited[i] == 0 :
                deq.append(i)
                visited[i] = 1 
    return 1

N, M = map(int,input().split())
graph = [[] for i in range(N+1)]
visited = [0] * (N+1)
cnt = 0 
for i in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)    
    graph[b].append(a)    
for i in range(1,N+1):
    if visited[i] == 0: 
        bfs(i)
        cnt += 1 
print(cnt)
