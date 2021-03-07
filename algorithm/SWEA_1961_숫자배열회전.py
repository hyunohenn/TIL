# 숫자 배열 회전
# NxN 배열을 90, 180, 270도 회전

for tc in range(int(input())):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    print('#{}'.format(tc+1))

    for i in range(N):
        # 90도
        for j in range(N):
            print(arr[N-1-j][i], end='')

        print(' ', end='')

        # 180도
        for j in range(N):
            print(arr[N-1-i][N-1-j], end='')

        print(' ', end='')

        # 270도
        for j in range(N):
            print(arr[j][N-1-i], end='')

        print(' ', end='')

        print()