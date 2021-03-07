# 퍼펙트 셔플

for tc in range(int(input())):
    N = int(input())

    cards = input().split()

    # 카드 장 수가 홀수일때는 교대로 놓을 때 먼저 놓는 쪽에 한장 더 들어간다
    if N % 2 == 1:
        A = cards[:N//2+1]
        B = cards[N//2+1:]
    else:
        A = cards[:N//2]
        B = cards[N//2:]

    ans = []
    for a, b in zip(A, B):
        ans.append(a)
        ans.append(b)

    if N % 2 == 1:
        ans.append(A[-1])

    print('#{}'.format(tc+1), end=' ')
    print(*ans)
