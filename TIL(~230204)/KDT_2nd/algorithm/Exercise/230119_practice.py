# 2576
numbers = [int(input()) for i in range(7)]
nums_odd = []

for i in range(len(numbers)) :
    if numbers[i] % 2 == 1 :
        nums_odd.append(numbers[i])
# print('nums_odd =', nums_odd) # test 


if nums_odd :
    # sum = 0
    # min = 100
    # for num_odd in nums_odd :
    #     sum += num_odd
    #     if num_odd < min :
    #         min = num_odd
    # print(sum)
    # print(min)
    print(sum(nums_odd))
    print(min(nums_odd))
else :
    print(-1)


# 10822
numbers = map(int, input().split(',')) # map 안 쓰고?

print(sum(numbers))


# # 2754
score = input()
score_num = 0.0

for i in range(4) :
    if  ord(score[0]) == (65 + i) :
        score_num = 4.0 - i

        if score[1] == '+' :
            score_num += 0.3
        elif score[1] == '-' :
            score_num -= 0.3

        break

print(score_num)
        
            
# 5622
# list_apb = []
# word = input()
# len_apb = 3
# fn_bef = 65
# result = 0
# for apb in word : 
#     for i in range(2,9 + 1) : 

#         if (i == 7) or (i == 9) :
#             len_apb = 4
#         if (i == 8) :
#             len_apb = 3

#         for j in range(fn_bef, fn_bef + len_apb) :
#             if ord(apb) == j :
#                 result += i

#         fn_bef += len_apb

#     fn_bef = 65
#     len_apb = 3
# print(result + len(word))

list_alphabet = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
word = input()
result = 0
for chr_word in word.lower() :
    for i_list in range(len(list_alphabet)) :
        if chr_word in list_alphabet[i_list] :
            result += i_list + 3
            break
print(result)


# 2577
numbers = []
for i in range(3) :
    numbers.append(int(input()))

num_mul = 1
dict_count = {}

for number in numbers :
    num_mul *= number

# just int
# while num_mul >= 1 :
#     dict_count[num_mul % 10] = dict_count.get(num_mul % 10, 0) + 1
#     num_mul = num_mul // 10

# use str
for one_num in str(num_mul) :
    dict_count[int(one_num)] = dict_count.get(int(one_num),0) + 1

for i in range(10) :
    print(dict_count.get(i,0))

# A = int(input())
# B = int(input()) 
# C = int(input())

# number = list(str(A * B * C))
# count_num = 0

# for i in range(0,10):
#     count_num = number.count(str(i))
#     print(count_num)


import sys
N = int(input())
dict_state = {}
for n in range(N) :
    name, state = sys.stdin.readline().split()

    dict_state[name] = True if state == 'enter' else False

list_state = []
for key, value in dict_state.items() :
    if value == True : 
        list_state.append(key) 
print(*sorted(list_state,reverse=True), sep='\n')
# for i in range(5) :
#     apb_list = []
#     for key in dict_state.keys() :
#         apb_list.append(key[i])
#     apb_list = sorted(apb_list)
#     if apb_list.count(apb_list[0]) == 1 :
#         print(dict_state.keys()[1])
    
    
# for i in range(5) :
#     for key in dict_state : 
# # 처음이 다르면 순서대로 하고 출력