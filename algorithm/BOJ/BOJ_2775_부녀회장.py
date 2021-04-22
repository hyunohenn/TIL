# 부녀회장이 될테야

for tc in range(int(input())):
    K = int(input())  # 층 0층부터임
    n = int(input())  # 호수

    # 층수만큼 그 숫자대로 더하기
    f = [i for i in range(1, n+1)]  # 일단 0층

    for j in range(K):  # 각 층마다 돌면서
        print(f)
        for l in range(1, n): # 각 층의 방마다 돌면서
            f[l] += f[l-1]  # 누적합
    print(f)
    print(f[n-1])
