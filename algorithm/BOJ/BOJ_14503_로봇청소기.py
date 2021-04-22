# 로봇 청소기
# 얘가 보는 방향을 항상 확인해야 한다

# 턴한 횟수에 따라 mode연산?
delta = {
    0: [-1, 0],
    1: [0, 1],
    2: [1, 0],
    3: [0, -1],
}
# delta = {
#     0: [0, 1],
#     1: [1, 0],
#     2: [0, -1],
#     3: [-1, 0],
# }

def robot(r, c, d):
    global arr
    # 처음 출발점 청소체크
    arr[r][c] = 2
    cnt = 1
    while True:
        flag = False  # 1번을 마치고 cd로 갈때
        for i in range(4):
            # 왼쪽으로 돌아본다
            d = (d + 3) % 4  # 2번 실행
            nr = r + delta[d][0]
            nc = c + delta[d][1]
            # 청소하지 않은 공간 존재
            if nr >= 0 and nr < N and nc >= 0 and nc < M and arr[nr][nc] == 0:
                # 이동했을 때 위치
                r = nr
                c = nc
                arr[r][c] = 2  # 2-a 전진하고 1번부터 진행
                cnt += 1
                flag = True
                break

        # 2-a 만족
        if flag:
            continue
        # 4방향 탐색이 끝난 후
        rd = (d + 2) % 4  # 후진 체크
        nr = r + delta[rd][0]
        nc = c + delta[rd][1]
        if nr >= 0 and nr < N and nc >= 0 and nc < M and arr[nr][nc] == 2:
            r = nr
            c = nc
        else:
            break
    return cnt

N, M = map(int, input().split())
r, c, d = map(int, input().split())
# d -> 0 북쪽, 1 동쪽, 2 남쪽, 3 서쪽
arr = [list(map(int, input().split())) for _ in range(N)]
print(robot(r, c, d))