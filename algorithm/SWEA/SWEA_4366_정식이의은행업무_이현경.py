# 정식이의 은행업무

# n진수 str => 10진수로
def todec(bs, n):
    result = 0
    for i in range(len(bs)-1, -1, -1):
            result += int(bs[i]) * (n ** (len(bs) -1 - i))
    return result

# 한자리씩 바꾸는 모든 경우의 수
def change(bs, n):
    result = []
    for i in range(len(bs)):
        for j in range(n):
            result.append(bs[:i] + str(j) + bs[i+1:])
    return result

# 두개 리스트에서 같은 수 찾으면 리턴
def findnum(l1, l2):
    for i in l1:
        for j in l2:
            if i == j:
                return i

for tc in range(int(input())):
    bs = input()
    ts = input()

    binlist = change(bs, 2)
    terlist = change(ts, 3)

    l1 = []
    l2 = []
    for bs in binlist:
        l1.append(todec(bs, 2))
    for ts in terlist:
        l2.append(todec(ts, 3))

    print('#{} {}'.format(tc+1, findnum(l1, l2)))
