# # 1. 
# dict_variable = {}
# dict_variable["이름"] = "정우영"
# dict_variable["생년월일"] = "19000101"
# dict_variable["회사"] = "하이퍼그로스"

# print(dict_variable["이름"]) # 정우영
# print(dict_variable["생년월일"]) # 19000101 # 문자열
# print(dict_variable["회사"]) # 하이퍼그로스


# # 2. 
# dict_variable = {"a" : "A", "B" : "b"}
# dict_variable["c"] = "C"
# dict_variable["D"] = "d"
# dict_variable["e"] = "E"

# print(dict_variable["a"]) # A
# print(dict_variable["D"]) # d
# print(dict_variable["b"]) # KeyError: 'b'


# # 3. 
# dict_variable = {}
# dict_variable["apple"] = 5000
# dict_variable["banana"] = 3000
# dict_variable["apple"] = 2000
# dict_variable["banana"] = dict_variable["banana"] + 1000 # banana == 4000

# print(dict_variable["apple"] + dict_variable["banana"]) # 6000


# # 4. 
# dict_variable = {
#     "이름" : "정우영",
#     "생년월일" : "19000101",
#     "회사" : "하이퍼그로스"
# }

# for key in dict_variable : 
#     print(key, dict_variable[key])

# '''
# 이름 정우영
# 생년월일 19000101
# 회사 하이퍼그로스
# '''


# # 5. 
# for key, value in dict_variable.items():
#     print(key, value)
#  # print (dict_variable.items())
# '''
# 이름 정우영
# 생년월일 19000101
# 회사 하이퍼그로스
# '''


# # 6. 
# print("나이" in dict_variable) # 에러인데 에러가 어떤 에러일까 index error? false
# print("이름" in dict_variable) # 존재하는지를 bool형태로 나타낸다.


# # 7.
# if "거주지" not in dict_variable : # True
#     dict_variable["거주지"] = "서울특별시"
#     # "거주지"라는 key가 없으면 value가 "서울특별시"인 key를 추가한다.

# print(dict_variable) # {"이름" : "정우영", "생년월일" : "19000101", "회사" : "하이퍼그로스", "거주지" : "서울특별시"}


# # 8. 
# list_variable = []

# try: 
#     list_variable.append(0)
#     list_variable.append(1)
#     list_variable.append(2)
#     print(list_variable[3])
# except:
#     print("에러가 발생했습니다")
#     print("에러의 원인은 무엇인가요?")

# '''
# 에러가 발생했습니다
# 에러의 원인은 무엇인가요?

# try에서 append로 list_variable[2]까지만 담기고 [3]은 없어서 에러가 발생한다.
# try에서 에러가 발생하면 except가 실행되므로 print가 출력된다.
# '''


# # 9. 
# try:
#     number = 1
#     if number == 1
#         print(number)

# except:
#     print("에러가 발생했습니다")
#     print("에러의 원인은 무엇인가요?")

# '''
# if number == 1 -> if number == 1:
# ':'를 붙여준다. 
# 가 아니라
# 실행이 안 돼야 except로 넘어간다.
# 하지만 문법이 틀린 것은 except로 넘어가지 않는다

# '''


# # 10. 
# n = 10
# total = 0

# for number in range(0, n + 1) : 
#     if number % 2 == 0 :  #0, 넘버가 짝수일 때
#         total += number * 2 #넘버를 2 곱한다.
#     elif number % 2 == 1 : # 홀수일 때
#         total += number + 1 * 3 # number + 3

# print(total) # 짝수일 때 60 + 3 * 5 + 25 = 100
