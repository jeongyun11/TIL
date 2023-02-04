# 1. 
number1 = 1
number2 = number1 + 1
print(number1, number2) # 1 2
# 주석 만들기 : ctrl(컨트롤) + /(슬래시)


# 2. 
number1 = 10
number2 = 5
number3 = str(number1) + str(number2)
number4 = number1 + number2

print(number1, number2, number3, number4) # 10 5 105 15


# 3. 
string1 = "Hello"
string2 = string1
string3 = "World" + "!"

print(string2, "2", string3) # Hello 2 World!


# 4.
string = "Hello?"
n = 5

print(string * n) # Hello?Hello?Hello?Hello?Hello?


# 5. 오답
string = "abc hello def"
sub_string1 = string[3:10]
sub_string2 = string[1:4]
sub_string3 = string[-1]


print(sub_string1) # c hello ->  hello 
print(sub_string2) # bc 
print(sub_string3) # f
# [3:10]은 세 번째가 아닌 네 번째에서 시작하므로 c가 아닌 띄어쓰기에서 시작된다.


# 6. 오답
number1 = 5
number2 = 10.0 + number1
number1 - 5
number3 = number1 * (number2 + 10)

print(number1, number2, number3) # 5 15.0 0 -> 5 15.0 125.0
# number1의 값을 할당해 준 것이 아니므로 5로 유지된다.


# 7. 
list_variable = [1, 2, 3, [1, 2, 3]]
sub_list = list_variable[3][-1]

print(sub_list) # 3


# 8. 오답
list_variable = []
list_variable.append(1)
list_variable.append("a")
list_variable[0] = 0

print(list_variable) # [0, a] -> [0, 'a']
# 문자열이 list에 들어오면 ''로 표시가 된다.


# 9. 오답
name = input("너의 이름은?") # 너의 이름은? 입력값 -> 너의 이름은?입력값
print(name) # 입력값
# 띄여쓰기 없이 바로 입력값이 나온다


# 10. 오답
age = int(input("너의 나이는?")) # 너의 나이는?입력값

print("올해 나이 : ", age) # 올해 나이 : 입력값 -> 올해 나이 :  입력값
print("내년 나이 : ", age + 1) # 내년 나일 : 입력값 + 1 -> 내년 나일 :  입력값 + 1 
# 이전에 문자열이 있으면 프로그램 자체에서 띄어쓰기를 한 번 해준다. 그러므로 : 이후에 띄어쓰기를 한번 더 해준다.
