

number = int(input())

a = 0
sum = 0
while number > a : # a가 ~일때
    a += 1 # a + 1을
    sum += a # 더한다.
print(sum)
#===

a = 1
sum = 0
while number >= a : 
    sum += a
    a += 1
print(sum)

# 머리로 계속 생각 주입시키자 눈 감고도 할 수 있을 만큼

# 가우스수열로도 해결해보자

# 조건 : target_nubmer >= n
# 반복 때마다 n += 1

# for의 기본!
# 반복 가능한 객체...
# 숫자통

sum = 0
for i in range(1,number + 1) :
    sum += (i)
print(sum)

sum = 0
for i in range(number) :
    sum += (i + 1)  
print(sum)

# 처음에는 특정 수를 넣고 나중에 input (?)

# for문과 while문


########## 함수

# print(sum(range(1, int(input()))))
#abstraction 복잡한 내용을 숨기곡 기능에 집중할 수 있음
#추상 : 특정한 측면

# 변수와 객체 : 하드웨어 속에서 

# decomposition : 분해해서 가독성 업!

# 함수 : input을 받아서 output을 내준다.

# 내장 함수

print('hi')
print('hi', 'hello') # *object : *이 붙어있다 = 여러 값을 무한다게 받을 수 있다.

# print(sep = ' ', end = '\n')
# sep=' ' : sep라는 키워드는 기본 값이 space
# end='\n' : end라는 키워드는 기본 값이 개행
print('hi', 'hello', sep='!')
print('hi', end='')
print('hello')

# 함수의 반환 값(return)

print('hi')
# print함수는 반환 값이 없습니다. -> 보여주는 과정이고 리턴은 없다.
# sum 함수는 합을 반환합니다.

# a = print(a)

# 각 함수는 그래도 짤 줄 알아야지

# count +1, 외에 있나

# 사용하는 함수마다 분석하자 iterable 리스트 문자열같이 반복 가능한 모든 객체

# abs 절대값 divmod 몫과 나머지 리턴 pow 거듭제곱** round 반올림 
# all(iterable) 모든 요소 참이거나 비면 true,

print(ord('a'))
print(chr(97))
print(int('1'))
# map
print(len)
print(type(len))

# Input을 넣어서 함수를 실행시켰다.
#len도 하나의 타입이다.

# map 함수
# 첫번째 인자(Input)으로 함수를 받아서
# 두번째 인자(Input)인 반복 가능한 객체의 모든 요소에 적용!
numbers = ['1', '2', '3']
result = 0
for number in numbers :
    result += int(number)
print(result)

new_numbers = []
for number in numbers : 
    new_numbers.append(int(number))
print(new_numbers)

# 첫번째 인자(Input)으로 함수를 받아서
# 두번째 인자(Input)인 반복 가능한 객체의 모든 요소에 적용!
new_new_numbers = map(int, numbers)
print(new_new_numbers)
print(list(new_new_numbers))

print(range(1,6))

a = input()
print(a)

# .split을 하면 쪼개서 list에 담는다.
# 각 요소를 숫자로 변환

d, e = map(int, a.split()) # map으로 list에서 쪼개진다.
numbers = list(map(int, a.split()))