# AC
# 보기엔 쉬워보이는데 뭐가 어려운점일까?
# Delete / Reverse

for tc in range(int(input())):

    functions = input()
    N = int(input())
    tmp = input()

    if tmp == '[]':
        arr = []
    else:
        arr = list(map(int, tmp[1:-1].split(',')))

    # print(arr)

    # 루프는 한번만 돌려야할것 같음
    # 따라서 인덱스 접근을 하자
    def AC(functions, arr):
        head = 0
        tail = N - 1
        direction = True  # 정방향일때 True, 아닐때 False
        for f in functions:
            if f == 'R':
                direction = not direction
                head, tail = tail, head

            elif f == 'D':
                # 삭제 가능한지부터 확인
                if direction == True and head > tail:
                    return 'error'

                if direction == False and tail > head:
                    return 'error'

                # 그 담에 지운다다
                if direction == True:
                    head += 1
                else:
                    head -= 1

        # 확인
        if direction == True:
            return arr[head:tail+1]
        else:
            return list(reversed(arr[tail:head+1]))


    ans = AC(functions, arr)
    # 으아아아아아아 짜증나
    # 이건 아니지 쫌
    if ans == 'error':
        print(ans)
    else:
        print('[', end='')
        for i in range(len(ans)):
            if i == len(ans) -1:
                print(str(ans[i]), end='')
            else:
                print(str(ans[i]), end=',')
        print(']')
