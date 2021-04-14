# 과제
# 16지수 문자로 이루어진 1차 배열이 주어질 때 암호비트패턴을 찾아 차례대로 출력하시오.
# 암호는 연속되어있다.

pattern = {
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9
}

# binary = '00010111100011010111011001100101110110111011011101100110010000000000000000000000'
#binary = '00000001100101000110100011010111101101110010011001001101110110000000000'
def decode(binary):
    codes = []
    i = 0
    while i < len(binary):
        sub = binary[i:i+7]
        if sub not in pattern:
            i += 1
            continue
        codes.append(pattern[sub])
        i += 7
    return codes
# print(decode(binary))

def check(code):
    odd = code[0] + code[2] + code[4] + code[6]
    even = code[1] + code[3] + code[5]

    if (odd * 3 + even + code[7]) % 10 == 0:
        return sum(code)

    return 0

n = int(input())
for tc in range(n):
    r, c = map(int,input().split())
    # found = False
    line = ''
    for i in range(r):
        l = input()
        line += l

    for j in range(len(line)-1, -1, -1):
        if line[j] == '1':
            # print(j)
            line = line[j-56:j+1]
            # print(line)
            break
        # # if len(line) != c or found:
        #     continue

    code = decode(line)
    if len(code) == 8:
        print('#{} {}'.format(tc + 1, check(code)))
        # found = True


