# 1.
str = input()

for i in range(len(str)) :
    if 'e' not in str : 
        print(-1)
        break
    elif str[i] == 'e' :
        print(i)
        break

# for i, apb in enumerate(str) : 
#     if 'e' not in str :
#         print(-1)
#         break
#     elif apb == 'e' :
#         print(i)
#         break
    
# index() / find()


# 2. 
list_Word = list(input().split())

dict_Word = {}

for words in list_Word :
    if words not in dict_Word :
        dict_Word[words] = 1
    else :
        dict_Word[words] += 1

for words in dict_Word : # .items
    print(words, dict_Word[words])
# count()


# 3. 
str = input()

for i in range(len(str)) : # h e l l o 
    if str[i] == 'e' :
        continue
    print(str[i], end = '')    

# 

# for i, apb in enumerate(str) : 
#     if apb == 'e' :
#         continue
#     print(apb, end = '')
    

# 4. list로도
word, apb = input().split() # unpacking
cnt = 0
# dict_apb = {} # sdflkjsdflk s key s = 2
# for apb_inword in word :
#     dict_apb[apb_inword] = dict_apb.get(apb_inword, 0) + 1

# print(dict_apb.get(apb, 0)) # a존재하면 dict_apb에 담기게, 
                            # a가 없으면 dict_apb에 안 담기게 

for i in word :
    if word == apb : 
        cnt +=1 
print(cnt)

# 5.
str = input()
list_word = str.split()

# for apb in str : 
#     if apb == ' ' :
#         # print('', end='-')
#         print('-', end='')
#     else :
#         print(apb, end='')
# 
for i, word in enumerate(list_word) : 
    if i == len(list_word) - 1 :
        print(word, end='\n')
    else :
        print(word, end='-')



# 6. 
number = int(input())
sum = 0 # result = 각 자리수의 합

if number < 0 : 
    print (-1)
else : 
    while number >= 1 :
        sum +=  number % 10 # 나머지     1  7  4  2
        number = number // 10  # 몫 2471  247 24  2  0
    print(sum)

    # sign_number = 0

# if number >= 0 : sign_number = 1
# else : sign_number = -1

# number *= sign_number

# while number >= 10 :
#     num_one =  number % 10
#     number = number // 10
#     sum += num_one

# sum += ((number % 10) * sign_number)

# print(sum)
