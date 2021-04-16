# 격자판의 숫자 이어붙이기

delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def DFS(r, c, distance, num):
    num += arr[r][c]
    distance += 1

    if distance == 7:
        nums.append(num)
        return

    for d in range(4):
        nr = r + delta[d][0]
        nc = c + delta[d][1]

        if nr >= 0 and nr < 4 and nc >= 0 and nc < 4:
            DFS(nr, nc, distance, num)

for tc in range(int(input())):
    arr = [list(input().split()) for _ in range(4)]

    nums = []
    for i in range(4):
        for j in range(4):
            DFS(i, j, 0, '')
    print('#{} {}'.format(tc+1, len(set(nums))))
    # print(set(nums))