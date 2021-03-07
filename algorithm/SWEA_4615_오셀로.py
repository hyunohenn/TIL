# 오셀로

for tc in range(int(input())):
    # N: 한변의 길이
    # M: 플레이어가 돌을 놓는 횟수
    N, M = map(int, input().split())

    # 판 초기화 1: 흑돌 2: 백돌
    # 인덱스 에러를 피하고 입력 위치를 그대로 사용하기 위해 상하좌우 1칸씩 벽을 만든다
    tmp = [list([-1] + [0] * N) + [-1] for _ in range(N)]
    board = [[-1] * (N + 2)] + tmp + [[-1] * (N + 2)]

    board[N // 2][N // 2] = 2
    board[N // 2 + 1][N // 2 + 1] = 2
    board[N // 2][N // 2 + 1] = 1
    board[N // 2 + 1][N // 2] = 1

    # 방향
    # 상하좌우 대각선 시계방향
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [1, 1], [1, -1], [-1, -1]]

    for num in range(M):
        c, r, color = map(int, input().split())
        board[r][c] = color


        reverse = []  # 뒤집어야 되는 칸
        # 8 방향을 순차적으로 돈다
        for dir in range(8):
            nc = c + delta[dir][0]  # 바꿀 좌표
            nr = r + delta[dir][1]
            while True:
                # 빈칸을 만나거나 범위를 벗어나거나 같은 색을 만났을 때
                if nr < 0 or nr > N or nc < 0 or nc > N:
                    reverse = []
                    break

                if board[nr][nc] == -1 or board[nr][nc] == 0:
                    reverse = []
                    break

                if board[nr][nc] == color:
                    break

                else:
                    tmp = [nr, nc]
                    reverse.append(tmp)

                    nc += delta[dir][0]
                    nr += delta[dir][1]

            # 뒤집어주기
            for position in reverse:
                if color == 1:
                    board[position[0]][position[1]] = 1
                else:
                    board[position[0]][position[1]] = 2

    black = 0
    white = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                black += 1

            elif board[i][j] == 2:
                white += 1

    print('#{} {} {}'.format(tc+1, black, white))
