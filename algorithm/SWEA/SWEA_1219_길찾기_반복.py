# 길찾기
# 단방향 DFS
# 탐색하다가 좀점인 99가 나오면 종료
# 탐색이 끝날때까지 99가 나오지 않으면 실패

for i in range(10):
    tc, E = map(int, input().split())
    routes = list(map(int, input().split()))

    # 인접 리스트 초기화
    adj_list = [[] for _ in range(100)]
    for j in range(E):
        adj_list[routes[j*2]].append(routes[j*2+1])

    # DFS 스택을 활용한 방법으로 구현해보기
    visited = [0] * 100
    stack = []
    def DFS_stack(v):
        stack.append(v)

        while len(stack) > 0:
            v = stack.pop()
            visited[v] = 1
            for i in range(len(adj_list[v])):
                if visited[adj_list[v][i]] == 0:
                    stack.append(adj_list[v][i])

        return visited[99]

    print('#{} {}'.format(tc, DFS_stack(0)))
