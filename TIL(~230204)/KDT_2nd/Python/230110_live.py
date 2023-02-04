

# # # 사용자 정의 함수
# # 컴퓨터는 계싼하고 저장한다
# # 필요한 것은 명령적 지식
# # 논리가 필요

# # 한 쪽에는 알파벳 한쪽은 숫자
# # 한쪽이 D이면 반대쪽은 3이다.
# # 주장이 사실인지 확인하고 싶음
# # 제가 가지고 있는 카드는 ....

# # 명제와 대우
# # 함수에서 제일 중요한 것 입력과 출력과 타입

# # 힘수 기본 구조
# # 인풋 과정 아웃풋을 정의
# # 함수를 정의한다.def
# # 정의된 함수 호출해서 쓴다.            


# def add(a, b): # 정의
#     return a + b


# print(add)
# print(add(-10,-20)) # 호출
# print(add(10,20))

# # 숫자 n을 입력 받아서 세제곱을 반환하는
# # 함수 cube를 작성

# def cube(n) : 
#     return n**3

# print(cube(2))
# print(cube(100))

# # 함수의 결과값(Output)
# # 무조건 return (None이라도)
# # return 실행되고 종료
# # 여러개도 하나의 튜플일 뿐이다.
# # return 안 넣어줘도 알아서 None으로 리턴

# # return 
# # 명시적인 return문이 없는 경우 : None
# # 여러 값을 return 하는 경우 : tuple

# a = divmod(4, 2)
# print(a)

# # # 함수의 입력
# # Parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자
# # Argument : 함수를 호출 할 때, 넣어주는 값
# # 핵심적으로 이름 붙이기

# # 개발자로 평생 먹고 사는 법

# # argument

# # 필수 / 선택 파라미터 print / end sep

# # keyword arguments : 키워드

# # 기본 값으로 지정하고 선택해서 바꾼다.

# # *은 패킹 언패킹 연산자

# def add(*numbers) :
#     print(type(numbers)) # 튜플
#     result = 0
#     for n in numbers : 
#         result += n
#     return result

# print(add(1,2,3))

# def movie(**kwargs) : 
#     print(type(kwargs))

# print(movie(name = '더 글로리', writer = '김은숙'))

# # 함수를 읽는 법
# # open(file, mode = 'r', buffering = -1)
# # open('README.md', 'r', encoding='UTF8') 
# # open('README.md', mode='r', encoding='UTF8') 
# # open('README.md', 'r', 'UTF8') # 다르게 동작! 왜? buffering이 세번째!

# # global scope
# a = 10
# # 함수는 코드 내부에 local scope를 생성하며, 
# def foo() : 
#     b = 10

# foo()
# # print(b)

# python tutor
# ---------
# legb
print(sum([1,2,3]))

# sum : Global scope
sum = 1 + 2

print(type(sum), sum)
print(sum([1,2,3]))

a = 5
def foo() : 
    print(a)

foo()

def boo() : 
    global a
    a = 3
    print(a)

boo()

# LEGB
# 찾고 없으면 밖에 있는 걸 쓴다.

# 원칙
# return 할당 

# 함수가  global변수 값을 바꾸는 용도로도 사용되나요?
# 반복 조건문은 어디 영역인가요

# 글로벌 테스트
# 알고리즘 문제 풀이서 임시적으로 활용을 할 수 있다.
# 하나의 input - 기본은 위치로 인자를 받는다. 키워드로 호출( 아무것도 없으면 기본 값), 키워드로 호출 encoding을 생각해라
# 하나의 output으로 리턴
# *<>은 튜플로 받는다 **<>은 딕셔너리로 받는다.
# 프로그래머스랑 해외사이트는 함수로 시작되는 경우가 많다. 하지만 스웨어랑 백준은 문자열을 알아서 쪼개서 쓰면 되는 거라서 함수는 잘 없다.