# 길찾기
# 최대 2개의 갈림길 & 일방통행
# 출발점 0 도착점 99

for i in range(10):
    tc, E = map(int, input().split())
    tmp = list(map(int, input().split()))

    adj = [[] for _ in range(100)]
    for i in range(0, len(tmp), 2):
        adj[tmp[i]].append(tmp[i+1])

    visited = [0] * 100

    def dfs(start):
        visited[start] = 1
        for i in range(len(adj[start])):
            if visited[adj[start][i]] == 0:
                dfs((adj[start][i]))
                # if adj[start][i] == 99:
                #     return 1
                # else:
                #     dfs(adj[start][i])
    dfs(0)
    print('#{} {}'.format(tc, visited[99]))