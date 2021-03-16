# 단지 번호 붙이기

# 데이터 입력
N = int(input())

complex = [list(map(int, input())) for _ in range(N)]

# 상하좌우
delta = [[0, -1], [0, 1], [-1, 0], [1, 0]]
v = []

def BFS(complex, r, c):
    cnt = 1
    q = []
    q.append((r, c))
    complex[r][c] = visitied
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr = r + delta[d][0]
            nc = c + delta[d][1]

            if nc >= 0 and nc < N and nr >= 0 and nr < N and complex[nr][nc] == 1:
                q.append((nr, nc))
                # 방문처리 1이 기본이므로 2부터 방문처리
                complex[nr][nc] = visitied
                cnt += 1
    v.append((visitied, cnt))


# 시작점 찾기
visitied = 2
for i in range(N):
    for j in range(N):
        if complex[i][j] == 1:
            BFS(complex, i, j)
            visitied += 1

v.sort(key=lambda x:x[1])
print(len(v))
for i in range(len(v)):
    print(v[i][1])

for i in complex:
    print(i)
