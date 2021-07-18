# 카드2

# 1. 맨 뒤에 있는 카드 버림
# 2. 제일 위에 있는 카드를 제일 밑으로
# 가장 마지막에 남는 카드는?

## deque 없이 풀기

N = int(input())

queue = [0] * 9999999
for i in range(N+1):
    queue[i] = i

start_idx = 1
end_idx = N
how_many = N

while how_many > 1:
    # 1번 조건
    start_idx += 1
    how_many -= 1
    # 2번 조건
    end_idx += 1
    queue[end_idx] = queue[start_idx]
    start_idx += 1

print(queue[end_idx])