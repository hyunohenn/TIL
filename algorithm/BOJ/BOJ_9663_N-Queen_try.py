# N-Queen

# n*n의 정사각형 안에 n개의 queen 배치
# 자신의 일직선상 및 대각선상에 아무 것도 놓이지 않아야 함

N = int(input())
board = [list() for _ in range(N)]
delta = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [-1, -1]]

# 현재 판에 올려진 모든 말 체크 DFS 재귀
board[0][0] = 1

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            c = i
            r = j
            if check(c, r) == True:
                cnt += 1





def check(c, r):
    for d in range(4):
        nc = c + delta[d][0]
        nr = r + delta[d][1]
        if nc >= 0 and nc < N and nr >= 0 and nr < N and board[nc][nr] == 0:
            check(nc, nr)
        if board[nc][nr] == 1:
            return False
    return True

def check(c, r):
    for i in range(N):
        if board[c][i] == 1 and i != r:
            return False
    for i in range(N):
        if board[i][r] == 1 and i != c:
            return False

    for i in range(1, N):
        nc = c - i
        nr = r - i
        if  nc >= 0 and nc < N and nr >= 0 and nr < N and board[nc][nr] == 1:
            return False

        nc = c - i
        nr = r + i
        if  nc >= 0 and nc < N and nr >= 0 and nr < N and board[nc][nr] == 1:
            return False

        nc = c + i
        nr = r + i
        if  nc >= 0 and nc < N and nr >= 0 and nr < N and board[nc][nr] == 1:
            return False

        nc = c + i
        nr = r - i
        if  nc >= 0 and nc < N and nr >= 0 and nr < N and board[nc][nr] == 1:
            return False
    return True