def fn(brd, elem):
    # 주어지는 인덱스를 파이썬 리스트에서 사용할 수 있도록 변형
    c, r = elem[0] - 1, elem[1] - 1
    brd[r][c] = elem[2]
    # 총 여덟방향 검사해야함
    delta = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    for d_r, d_c in delta:
        step = 1
        while 0 <= r + d_r * step < N and 0 <= c + d_c * step < N:
            # 한스텝 다음이 상대방 돌일 경우
            if brd[r + d_r * step][c + d_c * step] != elem[2] and brd[r + d_r * step][c + d_c * step] != 0:
                step += 1
            # 한스텝 다음이 내 돌일 경우
            # step >= 2 는 바로 다음 내돌이 나오는 경우를 제외하기 위함
            elif brd[r + d_r * step][c + d_c * step] == elem[2] and step >= 2:
                # 끝내기 전에 가운데 남의 돌을 모두 내것으로
                for k in range(1, 1 + step):
                    brd[r + d_r * k][c + d_c * k] = elem[2]
                break
            # 탐색중인 위치에 돌이 없는 경우
            else:
                break

    return brd


T = int(input())
for tc in range(1, T + 1):
    # N -> 게임판의 크기
    # M -> 총 돌을 놓은 횟수
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    # 게임판 초기화
    brd = [[0] * N for _ in range(N)]
    brd[N // 2 - 1][N // 2 - 1] = 2
    brd[N // 2 - 1][N // 2] = 1
    brd[N // 2][N // 2 - 1] = 1
    brd[N // 2][N // 2] = 2

    for elem in arr:
        brd = fn(brd, elem)

    # 개수세기
    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if brd[i][j] == 1:
                black += 1
            if brd[i][j] == 2:
                white += 1
    print('#{} {} {}'.format(tc, black, white))