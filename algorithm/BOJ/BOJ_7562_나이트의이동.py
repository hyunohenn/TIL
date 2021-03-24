# 나이트의 이동
# 최소 몇번만에 이동하는지 탐색 => BFS


for tc in range(int(input())):
    N = int(input())
    s_r, s_c = map(int, input().split())  # 현재 나이트가 있는 칸
    g_r, g_c = map(int, input().split())  # 나이트가 이동하려고 하는 칸

    # vistied array 초기화
    board = [[0] * N for _ in range(N)]
    board[s_r][s_c] = -1  # start = =1
    board[g_r][g_c] = 2  # goal == 2

    # 나이트 갈 수 있는 방향 delta 시계방향 순으로
    delta = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]

    def BFS(s_r, s_c):
        global board
        cnt = 1
        q = []
        q.append((s_r, s_c, cnt))
        while q:
            r, c, cnt = q.pop(0)
            board[r][c] = 1  # check visited
            for d in range(len(delta)):  # 탐색을 하면서
                n_r = r + delta[d][0]
                n_c = c + delta[d][1]

                if 0 > n_r or n_r >= N or 0 > n_c or n_c >= N:
                    continue

                if board[n_r][n_c] == 0:
                    q.append((n_r, n_c, cnt+1))
                    board[n_r][n_c] = 1

                if board[n_r][n_c] == 2:
                    return cnt

        return 0  # 다 돌아도 못찾았을 때

    print(BFS(s_r, s_c))