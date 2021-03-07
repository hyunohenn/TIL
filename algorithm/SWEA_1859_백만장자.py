# 백만장자 프로젝트

for tc in range(int(input())):
    N = int(input())

    # 매매가 리스트
    price = list(map(int, input().split()))

    # 망한 코드라 한다
    # sold = 0
    # def max_profit(price):
    #     global sold
    #     if len(price) == 0:
    #         return sold
    #
    #     maxprice= max(price)
    #     idx = 0
    #     while price[idx] != maxprice:
    #         sold += maxprice - [price[idx]]
    #         idx += 1
    #
    #     price = price[idx+1:]
    #     max_profit(price)
    maxprice = price[-1]
    sold = 0
    for i in range(len(price)-1, -1, -1):
        if price[i] < maxprice:
            sold += maxprice-price[i]

        elif price[i] > maxprice:
            maxprice = price[i]

    print('#{} {}'.format(tc+1, sold))