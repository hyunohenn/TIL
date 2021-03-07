# 진기의 최고급 붕어빵

for tc in range(int(input())):
    N, M, K = map(int, input().split())
    arrival = list(map(int, input().split()))
    # 작은순서대로 정렬
    arrival.sort()

    # 선형시간 동안의 붕어빵의 누적 생산량은 시간//M * K
    # 따라서 방문 시점의 선형 시간의 누적 생산량에서 그 동안 방문한 손님의 수의
    # 차가 0이 되면 불가능
    result = 'Possible'
    for idx in range(N):
        if (arrival[idx] // M) * K - idx == 0:
            result = 'Impossible'
            break

    print('#{} {}'.format(tc+1, result))
