# DFS와 BFS

# DFS로 그래프를 탐색한 결과와 BFS로 탐색한 결과를 출력

# 4, 5, 1 => 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V
# M개의 줄에는 간선이 연결하는 두 정점의 번호
# 정점이 여러개인 경우에는 정점 번호가 작은 것을 먼저 방문

n, m, v = map(int, input().split())
adj_list = list([] for _ in range(n+1))
for _ in range(m):
    a, b, = map(int, input().split())
    adj_list[a].append(b)  # 양방향임 ㅜㅜ
    adj_list[b].append(a)


# print(adj_list)


def DFS(v):
    stack = []
    ans = []

    stack.append(v)
    while stack:
        x = stack.pop()
        if x not in ans:
            ans.append(x)
            # 작은수부터 나오기 위해 정렬
            adj_list[x].sort(reverse=True)

            for i in adj_list[x]:
                stack.append(i)

    return ans

from collections import deque
def BFS(v):
    q = deque()
    ans = []

    q.append(v)
    while q:
        x = q.popleft()
        if x not in ans:
            ans.append(x)
            # 되돌리기
            adj_list[x].sort()

            for i in adj_list[x]:
                q.append(i)
    return ans

print(*DFS(v))
print(*BFS(v))

