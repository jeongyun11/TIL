# 2072. 홀수만 더하기 # sum에다가 더하는 식으로
T = int(input())

for t in range(1, T+1):
    numbers = map(int,input().split())
    holls = []
    for number in numbers :
        if 1 == number % 2 :
            holls.append(number)

    print(f'#{t} {sum(holls)}')


# 2056. 연월일 달력 # 잘한듯?
T = int(input())

for t in range(1, T+1):
    nal = input()

    year_str = nal[0:4]
    year = int(nal[0:4])
    month_str = nal[4:6]
    month = int(nal[4:6])
    date_str = nal[6:8]
    date = int(nal[6:8])

    is_Year = year > 0
    is_Month = 1 <= month <= 12
    is_Date = 1 <= date <= 31

    if (month == 2) and (28 < date) or ((month==4 or month==6 or month==9 or month== 11) and (30 < date)):
        is_Date = False

    print(f'#{t}',end=' ')

    if(is_Date and is_Month and is_Year) :
        print(year_str,month_str,date_str,sep='/')
    else :
        print(-1)


# 2043. 서랍의 비밀번호
P, K = map(int,input().split())
print(P-K+1)


# 1933. 간단한 N의 약수
N = int(input())
numbers = []
for index in range(1, N+1):
    if 0 == (N % index):
        numbers.append(index)
print(*numbers)


# 1288. 새로운 불면증 치료법
T = int(input())

for t in range(1, T+1):
    N = int(input())
    num_list = set()
    cnt = 1

    while 10 > len(num_list) :
        number = str(N * cnt)
        for num_one in number:
            num_list.add(num_one)
        result = N * cnt
        cnt += 1 
    print(f'#{t} {result}')
