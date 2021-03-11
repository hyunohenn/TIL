# 현주의 상자 바꾸기

for tc in range(int(input())):
    N, Q = map(int, input().split())

    box = [0] * N

    for i in range(Q):
        start, end = map(int, input().split())
        for x in range(start-1, end):
            box[x] = i+1

    print('#{}'.format(tc+1), end=' ')
    print(*box)
