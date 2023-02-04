# 1.
number = int(input())
print(number)


# 2.
string_list = input().split()
for word in string_list : 
    print(word, end=' ')

print()

print(*string_list,sep=' ')


# 3.
T = int(input())

for t in range(1, T + 1) :
    print(t)
    # 입력코드
    pass


# 4. 
list_num = list(map(int, input().split()))

for number in list_num :
     print(number, end = ' ')

print()

print(list_num)


# 5. 
a, b = map(int, input().split())

print(a, b)


# 6. 
list_word = list(input().split())

for word in list_word :
    print(word, end=' ')

print()


# 7. 
number = int(input())
for i in range(1, number + 1) : 
    numbers = list(map(int, input().split()))
    print(numbers)


# 8. 
number = int(input())
for i in range(1, number + 1) : 
    numbers = list(map(int, input().split()))
    print(numbers)