# 스도쿠 검증



def sudoku(arr):
    # 가로 세로 검증
    for i in range(9):
        garo = []
        sero = []
        for j in range(9):
            # 세로 줄 안에 중복된 수가 있는지 검사
            if arr[i][j] not in garo:
                garo.append(arr[i][j])

            else:
                return 0

            if arr[j][i] not in sero:
                sero.append(arr[j][i])

            else:
                return 0
    # 9칸 검증
    for i in range(0, 9, 3):   # 3x3 칸의 시작점 지정
        for j in range(0, 9, 3):
            sr = i
            sc = j
            diagonal = []
            for k in range(3):
                for j in range(3):
                    if arr[sr + k][sc + j] not in diagonal:
                        diagonal.append(arr[sr + k][sc + j])

                    else:
                        return 0
    return 1





for tc in range(int(input())):
    arr = [list(map(int, input().split())) for _ in range(9)]


    print('#{} {}'.format(tc+1, sudoku(arr)))