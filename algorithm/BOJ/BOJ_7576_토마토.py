# 2차원 토마토

# import 쓸줄 몰라 이번에 알아둘것 !!

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

# 또 BFS로 풀어본다
# 풀수 있는게 BFS밖에 없어

# 상하좌우
delta = [[-1, 0], [1, 0], [0, 1], [0, -1]]

def BFS(box):
    # 모든 토마토 익어있으면
    cnt = 0  # 안익은거의 개수
    for x in box:
        cnt += x.count(0)
    if cnt == 0:
        return 0

    # 기존에 하던대로 리스트로 풀면 터지므로 선형큐 구현
    q = [0] * 1000000
    head = 0  # pop 할때 +=1
    tail = 0  # append 할때 +=1
    day = 0

    # 시작점 몽땅 찾기
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                q[tail] = (i, j, day)
                tail += 1

    while head != tail:
        r, c, day = q[head]
        head += 1

        # 사방탐색 한다
        for d in range(len(delta)):
            nr = r + delta[d][0]
            nc = c + delta[d][1]

            if nr < 0 or nr >= N or nc < 0 or nc >= M or box[nr][nc] == 1 or box[nr][nc] == -1:
                continue
            else:
                q[tail] = (nr, nc, day+1)
                tail += 1
                # 방문체크 -> 익었다
                box[nr][nc] = 1
                cnt -= 1

                if cnt == 0:
                    return day+1

    return -1

print(BFS(box))