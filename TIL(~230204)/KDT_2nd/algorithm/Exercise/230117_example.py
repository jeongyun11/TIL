# 10818
N = input()
numbers = list(map(int,input().split()))
# max_num = numbers[0]
# min_num = numbers[0]

# for i in range(1,len(numbers)) : 
#     if max_num < numbers[i] :
#         max_num = numbers[i]
#     if min_num > numbers[i] :
#         min_num = numbers[i]




# for i in range(1,len(numbers)) : 
#     if max_num < numbers[i] :
#         max_num = numbers[i]
#     elif min_num > numbers[i] :
#         min_num = numbers[i]
        
print(min(numbers), max(numbers))
# print(min_num, max_num)


# 11720
N = input()

# number = int(input())
number_str = input()
sum = 0

# while number >= 1 :
#     sum += (number % 10)
#     number //= 10
for one_number in number_str :
    sum += int(one_number)
print(sum)


# 2750
N = int(input())
numbers = [int(input()) for i in range(N)]
numbers.sort()
# print(numbers)
# numbers = []
# for i in range(N) : 
#     number = int(input())
#     numbers.append(number)

print(*numbers, sep='\n')


# 2562
for i in range(9) : 
    number = int(input())
    if i == 0 :
        max_num = number
        index = 0
    elif max_num < number :
        max_num = number
        index = i
        
print(max_num)
print(index + 1)

