# 1. 
number = int(input("정수를 입력하세요 > "))
if number > 0 : 
    print(True)
else :
    print(False)


# 2. 
first_number = int(input("첫 번째 정수를 입력하세요 > "))
second_number = int(input("두 번째 정수를 입력하세요 > "))

if first_number > second_number : 
    print(first_number)
elif first_number < second_number : 
    print(second_number)
else : 
    print(False)


# 3. 
number = int(input("정수를 입력하세요 > "))
if (number > 0) and (number % 2 == 0) : 
    print(True)
else : 
    print(False)

# number = int(input("정수를 입력하세요 > "))
# if (number > 0) :
#     if(number % 2) == 0 :
#         print(True)
#     else :
#         print(False)
# else : 
#     print(False)


# # 4. 
# number = int(input("정수를 입력하세요 > "))
# if number > 100 :
#     print("에러")
# elif number >= 60 :
#     print("합격")
# elif number >= 0 :
#     print("불합격")
# else :
#     print("에러")

number = int(input("정수를 입력하세요 > "))
if number > 100 or number < 0:
    print("에러")
elif number >= 60 :
    print("합격")
else :
    print("불합격")

# number = int(input("정수를 입력하세요 > "))
# if number < 0 :
#     print("에러")
# elif number < 60 :
#     print("불합격")
# elif number <= 100 :
#     print("합격")
# else :
#     print("에러")

# number = int(input("정수를 입력하세요 > "))
# if number < 0 or number > 100:
#     print("에러")
# elif number < 60 :
#     print("불합격")
# else :
#     print("합격")


# 5. enumerate()?
text = input("문자열을 입력하세요 > ")
text_len = len(text)
text_chindex =  range(text_len-1,-1,-1)
for i in text_chindex :
    print(text[i])

# 그 외에 더 생각해보기


# 6. 
# first_number = int(input("첫 번째 정수를 입력하세요 > "))
# second_number = int(input("두 번째 정수를 입력하세요 > "))

# decision = True

# if first_number > second_number : 
#     start_number = second_number
#     end_number = first_number
# elif first_number < second_number : 
#     start_number = first_number
#     end_number = second_number
# else : 
#     decision = False
#     print(decision)

# if decision == True :
#     range_number = range(start_number + 1, end_number)
#     for number in range_number : 
#         print(number)

first_number = int(input("첫 번째 정수를 입력하세요 > "))
second_number = int(input("두 번째 정수를 입력하세요 > "))

if first_number > second_number : 
    range_number = range(second_number + 1, first_number)
    for number in range_number : 
        print(number)
elif first_number < second_number : 
    range_number = range(first_number + 1, second_number)
    for number in range_number : 
        print(number)
else : 
    print(False)

# 다른 거 생각해보기


# 7. 
# first_number = int(input("첫 번째 정수를 입력하세요 > "))
# second_number = int(input("두 번째 정수를 입력하세요 > "))

# decision = True

# if first_number < second_number : 
#     start_number = second_number
#     end_number = first_number
# elif first_number > second_number : 
#     start_number = first_number
#     end_number = second_number
# else : 
#     decision = False
#     print(decision,end=" ")

# if decision == True :
#     range_number = range(start_number -1, end_number, -1)
#     for number in range_number : 
#         print(number,end=" ")

first_number = int(input("첫 번째 정수를 입력하세요 > "))
second_number = int(input("두 번째 정수를 입력하세요 > "))

if first_number < second_number : 
    range_number = range(second_number - 1, first_number, -1)
    for number in range_number : 
        print(number,end=" ")
elif first_number > second_number : 
    range_number = range(first_number - 1, second_number, -1)
    for number in range_number : 
        print(number,end=" ")
else : 
    print(False)


# 8. 
number = int(input("정수를 입력하세요 > "))
if number == 1 : 
    print(1)
elif number < 1 :
    print(False)
else :
    for i in range(1, number, 2) : 
        print(i)






# 9. 
# "{} X {}"
A = list(range(2,10))
B = list(range(2,10))

for i in A : 
    for j in B :
        print(f"{i} X {j}")

# # 9. 가로
# # "{} X {}"
# A = list(range(2,10))
# B = list(range(2,10))

# for j in B : 
#     for i in A :
#         print(f"{i} X {j}", end="   ")
#     print("")
    
# 반복문에서는 루프가 돌면 항상 배열이나 list에서 +1이 된다.
