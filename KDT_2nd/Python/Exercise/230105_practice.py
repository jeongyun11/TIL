# # 1. 
# a = input('문자열을 입력하세요 > ')

# cnt = 0
# for i in a :
#     if i == 'e' :
#         cnt += 1

# print(cnt)


# # 2.
# a = input('문자열을 입력하세요 > ')
# cnt = 0

# for i in a :
#     if      i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' :
#         cnt +=1
#     elif    i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' :
#         cnt +=1

# # 김민기님 코드 참조
# print(cnt)  
# cnt = 0
# b = ['a','e','i','o','u','A','E','I','O','U']

# for i in a :
#     for j in b :
#         if i == j :
#             cnt += 1
# print(cnt)


# # 3. 
# dict_variable = {
#     '이름' : '정우영',
#     '생년' : '2000',
#     '회사' : '하이퍼그로스',
# }

# if '나이' not in dict_variable :
#     dict_variable['나이'] = '24세'

# print(f"나이 : {dict_variable['나이']}") #dict_variable['나이']


# # 4. 
# dict_a = {}
# dict_a['이름'] = input('이름을 입력하세요 > ')
# dict_a['전화번호'] = input('전화번호를 입력하세요 > ')
# dict_a['거주지'] = input('거주지를 입력하세요 > ')
# print(dict_a)
# print(f"이름 : {dict_a['이름']}")
# print(f"전화번호 : {dict_a['전화번호']}")
# print(f"거주지 : {dict_a['거주지']}")


# # 5.
# dict_name = {}
# dict_info = {}
# name = input('이름을 입력하세요 > ')
# dict_info['전화번호'] = input('전화번호를 입력하세요 > ')
# dict_info['이메일'] = input('이메일를 입력하세요 > ')
# dict_info['거주지'] = input('거주지를 입력하세요 > ')
# dict_name[name] = dict_info

# print(dict_name)


# # 6.
# a = input('문자열을 입력하세요 > ')
# dict_a = {}

# for i in a :
#     if i in dict_a : 
#         dict_a[i] += 1
#     else :
#         dict_a[i] = 1

# for i,j in dict_a.items() :
#     print(f"{i} {j}")

