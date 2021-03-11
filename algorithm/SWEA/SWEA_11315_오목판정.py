# 오목 판정
# 가로, 세로, 대각선2개 방향으로 5개 체크

delta = [[0, 1], [1, 0], [1, 1], [-1, 1]]

def OMOK(board):
    ans = 'NO'

    for i in range(len(board)):
        for j in range(len(board[0])):

            if board[i][j] == 'o':
                # 방향을 돌아가면서 판정
                for d in range(len(delta)):
                    dis = 1
                    cnt = 1

                    nr = i + dis * delta[d][0]
                    nc = j + dis * delta[d][1]

                    while 0 <= nr and nr < len(board) and 0 <= nc and nc < len(board):
                        if board[nr][nc] == 'o':
                            cnt += 1
                            dis += 1

                            nr = i + dis * delta[d][0]
                            nc = j + dis * delta[d][1]

                            # 빈칸이면 누적 돌 개수 샌 다음 방향 전환
                            if cnt == 5:
                                ans = 'YES'
                                return ans

                        else:
                            if cnt == 5:
                                ans = 'YES'
                                return ans
                            else:
                                break
    return ans

# 테스트케이스 입력
for tc in range(int(input())):
    N = int(input())

    board = [list(input()) for _ in range(N)]

    print('#{} {}'.format(tc+1, OMOK(board)))
