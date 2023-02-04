# import sys
# # sys.stdin = open("C:/Users/uwn10/Downloads/input.txt", "r")
# sys.stdin = open("input.txt", "r")


# 2047. 신문 헤드라인
string = input()
print(string.upper())


# 2025. N줄덧셈
sum = 0
number = int(input())

for i in range(1,number + 1) : 
    sum += i

print(sum)


# 1936. 1대1 가위바위보
A, B = map(int,input().split())

if ((A == 2) and (B == 1)) or ((A == 3) and (B == 2)) or ((A == 1) and (B == 3)) : # 2 1, 3 2, 1 3
    print('A')
else : # 1 2, 2 3, 3 1
    print('B')


# 2027. 대각선 출력하기
# for i in range(5) :
#     for j in range(5) : 
#         if j == i : 
#             print('#', end='')
#         else : 
#             print('+', end='')
#     print()

for i in range(5) :
    print('+'*i, '#', '+'*(4-i), sep='')


# 2058. 자릿수 더하기
# number = int(input())
# sum = 0

# while number >= 1 :
#     sum += number % 10
#     number //= 10

# print(sum)

# number = int(input())
# sum = 0

# while number >= 1 :
#     quotient, remainder = divmod(number,10)

#     number = quotient
#     sum += remainder

# print(sum)

number_str = input()
sum = 0

for apb_str in number_str : 
    sum += int(apb_str)

print(sum)


# 2019. 더블더블
number = int(input())
result = 1

for i in range(number + 1):
    print(result,end=' ')
    result *= 2


