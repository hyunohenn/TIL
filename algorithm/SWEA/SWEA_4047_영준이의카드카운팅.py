# 영준이의 카드 카운팅

# 카드 덱 맞추는 알고리즘

def deck(string):
    # 카드 카운팅을 위한 리스트 초기화
    # S D H C
    cards = [[0] *13 for _ in range(4)]

    for i in range(0, len(string), 3):
        row_idx = 0
        col_idx = 0
        # 카드의 무늬 판별
        if string[i] == 'D':
            row_idx = 1
        elif string[i] == 'H':
            row_idx = 2
        elif string[i] == 'C':
            row_idx = 3

        # 카드 숫자 판별
        if string[i+1] == '1':  # 10 보다 클 경우
            col_idx += 10 * int(string[i+1])

        col_idx += int(string[i+2])
        col_idx -= 1  # 인덱스는 0부터 시작하므로

        # 카드 확인
        if cards[row_idx][col_idx] == 1:  # 이미 겹치는 카드가 있다면
            return 'ERROR'

        else:
            cards[row_idx][col_idx] = 1

    # 카드 카운팅
    cnt = []
    for i in range(4):
        total = 0
        for j in range(13):
            if cards[i][j] == 0:
                total += 1
        cnt.append(total)

    return cnt


# 데이터 인풋
for tc in range(int(input())):
    string = input()

    ans = deck(string)
    print('#{}'.format(tc+1), end=' ')
    if type(ans) == str:
        print(ans)

    else:
        print(*ans)