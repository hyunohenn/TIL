# 나누어 떨어지는 숫자 배열
# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            answer.sort()
            
        if len(answer) == 0:
            answer.append(-1)
            
    return answer


## 수정코드(정확도)

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            
    if len(answer) == 0:  # 루프를 돌릴 필요가 없는데 넣었더니 정확도 떨어짐
        answer.append(-1)

    answer.sort()    
    return answer