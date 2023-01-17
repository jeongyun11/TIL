# 1.
a = int(input())

# print(abs(a))

if a >= 0 : 
    print(a)
else :
    print(a * -1)


# 2. 
number_list = list(map(int,input().split()))

# print(len(number_list))

cnt = 0
for i in number_list :
    cnt += 1

print(cnt)


# 3. 
number_list = list(map(int, input().split()))

# print(sum(number_list))

sum = 0
for i in number_list :
    sum += i

print(sum)


# 4. 
number_list = list(map(int, input().split()))

# print(sum(number_list) / len(number_list))

sum = 0; len = 0
for i in number_list:
    sum += i
    len += 1

print(sum/len)


# 5.
number_list = list(map(int,input().split()))

result = 1
for i in number_list :
    result *= i

print(result)


# 6. 
number_list = list(map(int, input().split()))

# print(max(number_list))

max = number_list[0]
for i in number_list[1::] :
    if max < i :
        max = i

print(max)

# for i, number in enumerate(number_list) : # enumerate 에서 count 해주는 수는 list와 독자적으로 0에서 시작한다.
#     if i == 0 :
#         max = i
#     elif max < number :
#         max = number

# print(max)


# 7. 
number_list = list(map(int, input().split()))

# print(min(number_list))

min = number_list[0]
for i in number_list[1::] :
    if min > i :
        min = i

print(min)
