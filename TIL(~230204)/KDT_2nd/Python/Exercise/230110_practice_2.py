# 2029. 
T = int(input())
for t in range(1, T + 1) :
    a, b = map(int, input().split())
    A = a // b # 몫 계산
    B = a % b # 나머지 계산

    print(f'#{t} {A} {B}')


# 2071. 
T = int(input())

for t in range(1, T + 1) :
    numbers = list(map(int, input().split()))
    result = sum(numbers)
    result /= len(numbers)
    print(f'#{t} {round(result)}')


# 1938. 
a,b = map(int,input().split())

# + - * /
print(a + b)
print(a - b)
print(a * b)
print(int(a / b))


# 2046.
number = int(input())

for i in range(number) : 
    print("#",end='')


# 2068.
T = int(input())

for t in range(1, T + 1) :
    numbers = list(map(int, input().split()))
    print(f'#{t} {max(numbers)}')
