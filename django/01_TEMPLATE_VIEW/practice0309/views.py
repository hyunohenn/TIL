from django.shortcuts import render
from django.http.response import HttpResponse
import random
import requests

# 사용자가 입력할 form & input용 **HTML을 제공**
# 종이 한 장 마련해주는게 끝
def ping(request):
    return render(request, 'practice0309/ping.html')


# 사용자 입력 데이터를 활용하는 view 함수
def pong(request):
    request.GET # <QueryDict: {'kor-name': ['이현경'], 'eng-name': ['hyun']}>
    
    kr_name = request.GET.get('kor-name')  # <input name="kor-name">
    en_name = request.GET.get('eng-name')
    fullname = kr_name + en_name
    context = {
        'fullname': fullname,
    }
    return render(request, 'practice0309/pong.html', context)

def var_route(request, value):
    print(type(value))
    return HttpResponse

def lotto(request, no):
#     # 1. 현실 로또 번호를 가져온다.
#     # 2. 1000번 
#         # 3. 현실 번호와 내가 추첨한 번호를 비교한다.
#         # 4. 등수 결과를 어딘가에 저장한다. 
#     # 5. 잘 context 에 비벼서 내보낸다

    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={no}'

    r = requests.get(url)
    r.json()
    
    real_lotto = []
    # 로또 번호 리스트 생성
    for i in range(1, 7):
        real_lotto.append(r.json()[f'drwtNo{i}'])
    # 로또 보너스번호 확인
    bonus = r.json()['bnusNo']

    prize = [0] * 6

    for i in range(1000):
        total = 0
        bonus_total = 0
        my_lotto = random.sample(range(1, 46), 6)
        
        for num in my_lotto:
            if num in real_lotto:
                total += 1
            if num == bonus:
                bonus_total += 1
        
        if total == 6:
            prize[0] += 1
        elif total == 5 and bonus_total == 1:
            prize[1] += 1
        elif total == 5:
            prize[2] += 1
        elif total == 4:
            prize[3] += 1
        elif total == 3:
            prize[4] += 1
        else:
            prize[5] += 1

        result = {}
        for idx in range(len(prize)):
            if idx == len(prize)-1:
                result['꽝'] = prize[idx]
            else:
                result[f'{idx+1}등'] = prize[idx]


        context = {
            'result': result,
            'real_lotto': real_lotto,
            'bonus': bonus,
        }

    return render(request, 'practice0309/lotto.html', context)