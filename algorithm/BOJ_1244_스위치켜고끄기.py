# 스위치 켜고 끄기

# 남학생의 경우 자연수의 배수 번호의 스위키 전환
# 여학생의 경우 최대 대칭 구간의 스위치 전환

# 스위치 전환하는 함수
def switch(idx):
    if light[idx] == 0:
        light[idx] = 1
    else:
        light[idx] = 0


N = int(input())  # 스위치 개수
light = [-1] + list(map(int, input().split()))  # 받은 자연수 사용 위해 -1 붙임

student = int(input())

for i in range(student):
    G, K = map(int, input().split())
    # 남학생의 경우
    if G == 1:
        for idx in range(len(light)):
            if idx % K == 0:
                switch(idx)

    # 여학생의 경우
    else:
        # 기준 자리 바꾸기
        switch(K)
        dis = 1
        while True:
            # 범위 안에 있을 경우에만 처리
            if 0 < K-dis and K+dis < len(light):
                # 대칭일때
                if light[K-dis] == light[K+dis]:
                    switch(K-dis)
                    switch(K+dis)
                    dis += 1
                else:
                    break
            else:
                break

for i in range(1, len(light)):
    print(light[i], end=' ')
    if i % 20 == 0:
        print()
