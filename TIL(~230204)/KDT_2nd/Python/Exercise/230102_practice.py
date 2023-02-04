# 1. 
number = int(input("숫자를 입력해주세요 > "))
print(number + 10)
print(number * 2)


# 2. 
food = input("좋아하는 음식을 입력해주세요 > ")
print("좋아하는 음식 :", food)


# 3.
name = input("이름을 입력해주세요 > ")
age = 2023 - int(input("태어난 년도를 입력해주세요 > ")) + 1
print("저의 이름은 ",name,"이고 올해 나이는 ",age,"세 입니다.")


# 4.
first =  input("첫 번째 문장을 입력해주세요 > ")
second = input("두 번째 문장을 입력해주세요 > ")
add = first + second
print(add)


# 5. 
number = int(input("숫자를 입력해주세요 > "))
number = number * -1
print(number)


# 6. 
first = int(input("첫 번째 숫자를 입력해주세요 > "))
second = int(input("두 번째 숫자를 입력해주세요 > "))
print("더하기 연산 :", first + second,"\n빼기 연산 :", first - second)
print("곱하기 연산 :", first * second,"\n몫 연산 :", first // second,"\n나머지 연산 :", first % second)
# // int(/)


# 7.
first_number = int(input("첫 번째 숫자를 입력해주세요 > "))
second_number = int(input("두 번째 숫자를 입력해주세요 > "))
third_number = int(input("세 번째 숫자를 입력해주세요 > "))
number = int((first_number + second_number + third_number) / 3)
print(number)


# 8.
first_number = int(input("첫 번째 숫자를 입력해주세요 > "))
second_number = int(input("두 번째 숫자를 입력해주세요 > "))
third_number = int(input("세 번째 숫자를 입력해주세요 > "))
fourth_number = int(input("네 번째 숫자를 입력해주세요 > "))
fifth_number = int(input("다섯 번째 숫자를 입력해주세요 > "))
list_number = [first_number, second_number, third_number, fourth_number, fifth_number]
print(list_number)
# 추가로 숫자마다 글 바뀌는


# 9.
array_input = input("문자열을 입력해주세요 > ")
array_number = int(input("숫자를 입력해주세요 > "))
print(array_input * 3)


# 10.
first_number = int(input("첫 번째 숫자를 입력해주세요 > "))
number = first_number
print(number)
second_number = int(input("두 번째 숫자를 입력해주세요 > "))
number = number + second_number
print(number)
third_number = int(input("세 번째 숫자를 입력해주세요 > "))
number = number + third_number
print(number)
fourth_number = int(input("네 번째 숫자를 입력해주세요 > "))
number = number + fourth_number
print(number)
fifth_number = int(input("다섯 번째 숫자를 입력해주세요 > "))
number = number + fifth_number
print(number)