# 보물섬
# 최단 거리가 제일 먼 두 육지의 이동 시간을 출력

N, M = map(int, input().split())  # 세로 가로

tmap = [list(input()) for _ in range(N)]

delta = [[-1, 0], [1, 0], [0, 1], [0, -1]]
def bfs(sr, sc):
    max_dis = 0
    visited = [[0] * M for _ in range(N)]
    q = []
    dis = 0
    q.append((sr, sc, dis))
    visited[sr][sc] = 1  # 방문처리

    while q:
        r, c, dis = q.pop(0)
        dis += 1
        for d in range(4):
            nr = r + delta[d][0]
            nc = c + delta[d][1]

            if nr >= 0 and nr < N and nc >= 0 and nc < M and tmap[nr][nc] == 'L' and visited[nr][nc] == 0:
                q.append((nr, nc, dis))
                visited[nr][nc] = 1

                if dis > max_dis:
                    max_dis = dis
    return max_dis

found = 0
for i in range(N):
    for j in range(M):
        if tmap[i][j] == 'L':
            candidate = bfs(i,j)
            if found < candidate:
                found = candidate
print(found)