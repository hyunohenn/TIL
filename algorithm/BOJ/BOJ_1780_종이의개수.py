# 종이의 개수
# 한 면이 같은 수로 되어 있다면 그대로 사용
# 아니라면 9개로 나누고 각각의 잘린 종이 확인 (3등분)

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]


# 한 공간 안에 한가지 수만 있는지 확인하는 함수
def check(r, c, k):  # r, c 시작 좌표, k는 면의 길이
    global paper
    color = []
    for i in range(k):
        for j in range(k):
            color.append(paper[r+i][c+j])

    if len(set(color)) == 1:
        for i in range(k):
            for j in range(k):
                paper[r+i][c+j] = 2
        return color[0]

    else:
        return -100


k = N
result = []
while k > 0:
    # 시작점 찾기
    for r in range(0, N, k):
        for c in range(0, N, k):
            if paper[r][c] == 2:
                continue  # 이미 한 가지 색으로 확인된 경우
            else:
                result.append(check(r, c, k))
    k //= 3


print(result.count(-1))
print(result.count(0))
print(result.count(1))