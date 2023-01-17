# import sys
# sys.stdin = open("input.txt", "r")

# 01.
number_list = map(int,input().split())
print(*number_list)


# 02.
words = input().split()
print(*words)


# 03. 
T = int(input())

for t in range(1, T + 1) : 
    # t와 관련이 없는 반복적인 함수
    N = int(input())
    for n in range(N) :
    # N을 사용한 줄 수에 따른 함수의 변화
        print(int(input()))


# 04. 
T = int(input())
for t in range(1, T + 1) :

    N = int(input())
    for n in range(N) :
        print(*map(int,input().split()))


# 05. 
T = int(input())
for t in range(1, T + 1) : 

    N = int(input())
    for n in range(N) :
        print(*input().split())
        # for word in input().split() :
        #     print(word, end=' ') 
        # print()


# 06.
T = int(input())
for t in range(1, T + 1) : 

    N = int(input())
    for n in range(N) :
        print(*map(int,input().split()))
        # for num in map(int,input().split()) : 
        #     print(num, end=' ')
        # print()


# 07.
T, N = map(int, input().split())
# print(f'T = {T}, N = {N}')

for t in range(1, T + 1) :
    # print('t =', t)

    for n in range(N) :
        # print('n =',n)
        # print('input =',int(input()))
        print(int(input()))
    

# 08.
T, N = map(int, input().split())

for t in range(1, T + 1) :

    for n in range(N) :
        print(*map(int,input().split()))
        # for num in map(int,input().split()):
        #     print(num, end=' ')
        # print()    



# 09.
T, N = map(int, input().split())

for t in range(1, T + 1) :

    for n in range(N) :
        print(*map(int,input().split()))
        # for num in map(int,input().split()):
        #     print(num, end=' ')
        # print()    
