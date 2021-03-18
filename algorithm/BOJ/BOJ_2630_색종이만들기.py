# 색종이 만들기

# 정사각형 모양의 종이 -> 반절씩 나누어 한 장에 한 가지 색깔만 칠해져 있도록 한다


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]



# 한 공간 안에 한가지 수만 있는지 확인하는 함수
def check(r, c, k):  # r,c 시작 좌표, k는 면의 길이
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
        return -1

k = N
result = []
while k >= 1:
    # 시작점 찾기
    for r in range(0, N, k):
        for c in range(0, N, k):
            if paper[r][c] == 2:
                continue# 이미 한가지 색으로 정해졌다면 패스

            else:
                result.append(check(r, c, k))


    k //= 2


print(result.count(0))
print(result.count(1))