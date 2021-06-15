# N과 M
# nPm
# 1 <= M <= N <= 8
# 한줄에 하나씩 문제의 조건 만족하는 수열 출력
# 중복되는 수열 출력 X 각 수열은 사전순으로 증가
# https://www.acmicpc.net/board/view/60497
# pypy에서는 Set, dict 모두 순서가 잇음
# https://doc.pypy.org/en/latest/cpython_differences.html (order로 검색)

import copy

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
sel = [0] * M
check = [0] * N
result = set()

def permu(idx):
    global sel, check, result
    if idx == M:
        # tmp tuple이 아니라 sel 리스트에 append그냥 하면 shallow copy가 됨
        tmp = tuple(sel)

        if tmp not in result:
            result.add(tmp)
            # 이래해도 됨****
            # print(*sel)

        return

    else:
        for i in range(N):
            # 사용했는지 체크
            if check[i] == 0:
                check[i] = 1
                sel[idx] = arr[i]
                permu(idx+1)
                #원상복귀
                check[i] = 0

permu(0)

# for r in result:
    # print(*r)
