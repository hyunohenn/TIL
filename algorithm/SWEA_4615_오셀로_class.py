## 얘랑 오목판정 다시 보고 수업 내 코드도 다시 살펴보고, 정리해두기


def init():
    st = N // 2
    othello[st][st] = othello[st+1][st+1] = 2
    othello[st+1][st] = othello[st][st+1] = 1

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())  # N: 판의 크기, M: 돌을 놓는 횟수
    othello = [[0] * (N+1) for _ in range(N+1)]

    init()

    for i in range(M):
        c, r, color = map(int, in)
