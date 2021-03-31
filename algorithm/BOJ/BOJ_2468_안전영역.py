# 안전영역
# 높이정보 => 물에 잠기지 않는 영역의 최대 개수
import copy

# 초기화
N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# area에서 최대 강우높이가 주어졌을 때, 잠기지 않는 구역의 개수 구하기
# DFS로 풀어보기
# 방문체크는 -1로 할 것
def DFS(area, max_rain):
    # 시작점 정하기
    cnt = 0  # 물에 잠기지 않는 구역의 개수
    for i in range(N):
        for j in range(N):
            if area[i][j] > max_rain:
                cnt += 1

                stack = []
                stack.append((i, j))

                while stack:
                    # DFS는 pop할떄 방문체크하고, BFS는 append할때 방문체크 한다
                    r, c = stack.pop(-1)
                    area[r][c] = -1  # 방문체크

                    for d in range(len(delta)):
                        nr = r + delta[d][0]
                        nc = c + delta[d][1]

                        # 조건
                        if nr < 0 or nr >= N or nc < 0 or nc >= N or area[nr][nc] <= max_rain:
                            continue
                        else:
                            stack.append((nr, nc))
    return cnt

max_rain = 0
for row in array:
    if max(row) >= max_rain:
        max_rain = max(row)

result = []
for i in range(max_rain+1):
    area = copy.deepcopy(array)
    result.append(DFS(area, i))

print(max(result))
