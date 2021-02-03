# 내꺼

def solution(n, lost, reserve):
    answer = 0

    # 이 부분이 문제였음
    # 여분을 가지고 있는 사람들 중 잃어버린 사람은 빼야함
    real_lost = list(set(lost) - set(reserve))
    real_reserve = list(set(reserve) - set(lost))

    answer = n - len(real_lost)
    for i in real_lost:
        for j in real_reserve:
            if abs(i-j) == 1:
                answer += 1
                real_reserve.remove(j)
                print( i, j)

    return answer




# -----


def solution(n, lost, reserve):
    answer = 0
    # set이용해서 중복제거
    reserve_list = sorted(list(set(reserve) - set(lost)))  # 2개있는 사람
    lost_students = sorted(list(set(lost)-set(reserve))) # 아예 없는 사람
    
    for res in reserve_list:  # 2개 있는 사람 순회
        if res-1 in lost_students:  # 왼쪽 먼저 줌
            lost_students.remove(res-1)  # 왼쪽에 없는 사람이면 체육복 빌려줌
        
        elif res+1 in lost_students:  # 왼쪽에 있는 사람이 체육복있으면 오른쪽 확인
            lost_students.remove(res+1)  # 오른쪽에 없는 사람이면 체육복 빌려줌
            
    answer = n - len(lost_students)    # n명 중 체육복 없는 사람 제외
    return answer



#------

def solution(n, lost, reserve) :
    real_reserve = set(reserve) - set(lost)
    real_lost = set(lost) - set(reserve)
    answer = n - len(real_lost)

    for loser in real_lost :
        if (loser-1) in real_reserve :
            answer += 1
            real_reserve -= {loser-1}
        elif (loser+1) in real_reserve :
            answer += 1
            real_reserve -={loser+1}
        else : continue

    return answer