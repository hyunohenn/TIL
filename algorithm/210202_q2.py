# 소수 찾기
#1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, 
# solution을 만들어 보세요.
# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)

def solution(n):
    answer = 0
    for i in range(2, n+1):
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count += 1
                
        if count == 0:
            answer += 1
        
    
    return answer


## 두번째 고친 코드

    def solution(n):
    answer = 0
    r = []
    for i in range(2, n+1):
        count = 0
        for j in r:
            if i % j == 0:
                count = 1
                break
                
        if count == 0:
            r.append(i)
        
    answer = len(r)
    return answer



def solution(n):
    if n == 2:
        return 1
    
    answer = 1 
    for i in range(2, n+1):
        for j in range(2, int(i**(1/2))+2):
            if i % j == 0:
                break
        else:
            answer +=1
    
    return answer