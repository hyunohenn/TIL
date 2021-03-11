# 농작물 수확하기

# 크기는 항상 홀수
# 크기에 딱 맞는 정사각형 마름모 형태로 수확

for tc in range(int(input())):
    N = int(input())

    # 농장 입력받기
    farm = []
    for i in range(N):
        farm.append(list(map(int, input())))

    total = 0
    for i in range(N):
        diff = abs(N//2 - i)
        for j in range(diff, N-diff):
            total += farm[i][j]

    print('#{} {}'.format(tc+1, total))
