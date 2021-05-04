# 아기상어
# 약간 잔인
# 귀찮아도 변수명을 길게 써버릇해보자...

from collections import deque
from copy import deepcopy
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def find_food(size):
    for i in range(N):
        for j in range(N):
            if 0 < sea[i][j] < size:
                return True
    return False

def BFS(sr, sc, cnt, dis, size):
    global result_time
    # 먹을게 아에 없으면 짤라!
    flag = find_food(size)

    while flag:
        q = deque()
        q.append((sr, sc, cnt, dis, size))
        v = deepcopy(origin_v)
        min_dis = 999999999
        target_r = 999999999
        target_c = 999999999

        while q:
            sr, sc, cnt, dis, size = q.popleft()
            dis += 1
            # 움직인다
            for d in range(4):
                nr = sr + delta[d][0]
                nc = sc + delta[d][1]
                # 일단 갈 수 있으면 간다 // min_dis 보다 거리 길어지면 갈 필요 없음
                if 0 <= nr < N and 0 <= nc < N and sea[nr][nc] <= size and v[nr][nc] == 0 and dis <= min_dis:
                    v[nr][nc] = 1
                    q.append((nr, nc, cnt, dis, size))
                    # 먹을 수 있으면
                    if 0 < sea[nr][nc] < size:
                        # 거리가 가장 짧은 것들 중에서 제일 위, 제일 왼쪽을 고른다
                        if dis < min_dis:
                            min_dis = dis
                            target_r = nr
                            target_c = nc
                        elif dis == min_dis:
                            if nr < target_r:
                                target_r = nr
                                target_c = nc
                            elif target_r == nr and nc <= target_c:
                                target_c = nc

        # 골랐으면 먹자
        if target_r == 999999999:
            return
        sea[target_r][target_c] = 0
        cnt += 1
        result_time += min_dis
        # 많이 먹었는지 확인
        if cnt == size:
            size += 1
            cnt = 0

        # 먹었으니 초기화 다시 bfs를 시작한다
        # 새로운 시작을 위한 변수 설정
        sr = target_r
        sc = target_c
        dis = 0
        flag = find_food(size)

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]

# 잡아먹는 데 성공할 때까지 누적 시간
result_time = 0

# 잡아먹을때마다 갱신해주어야 할 visited list
origin_v = [[0] * N for _ in range(N)]

# while문 두개 있어야 되네...
# 먼저 상어 위치 확인
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            sr = i
            sc = j
            sea[sr][sc] = 0  # 출발점도 초기화

BFS(sr, sc, 0, 0, 2)
print(result_time)