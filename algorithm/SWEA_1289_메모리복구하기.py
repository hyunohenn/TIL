# 원재의 메모리 복구하기
# 메모리 bit중 하나를 골라 0,1을 결정하면 해당 값이
# 메모리 끝까지 덮어씌우는 문제 -> 최소 수정 횟수 구하기

for tc in range(int(input())):
    arr = list(map(int, input()))
    # 초기화상태 메모리
    temp = [0] * len(arr)

    count = 0
    for i in range(len(arr)):
        if arr[i] != temp[i]:
            count += 1
            for j in range(i, len(arr)):
                temp[j] = arr[i]

    print('#{} {}'.format(tc+1, count))