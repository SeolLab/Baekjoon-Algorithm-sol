import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10**9)
def dfs(first_node):
    for i in graph[first_node]:
        if visited[i] == 0 :
            visited[i] = 1 
            dfs(i)
    return 1

if __name__ == "__main__":
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
            cnt += dfs(i)
    print(cnt)
