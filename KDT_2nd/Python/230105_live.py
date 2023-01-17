# 01_len.py


#문제접근방식의 알고리즘
# - 변수, 반복, 조건
# 변수 : 어떤 type의 변수를 초기화 시킬 것인가
# 반복 : 요소 인덱스 조건 반복 때마다 뭐해
# 조건 :  조건 해당하면 뭐를 해

# 컬렉션
# 새로운 유형의 자료구조
# 다른 데이터 타입과 비교할 수 있다.

# 딕셔너리(Dictionary)
# 키, 값의 쌍으로 이뤄진 모음(collection)
# key와 value 쌍으로 이루어짐

phone_book = {
    '피자헛'    : '1588-5588',
    '전화번호'  : '114',
    '김탁희'    : '010-1233-1233',
    '대리운전'  : '1577-1577'
}

# print(phone_book['피자헛'])

# append
phone_book['추가요'] = "ㅎㅎ"
phone_book['숫자도 추가요'] = 41720389


for name in phone_book :
    print(name)
    print(phone_book[name])

# name  : 변수이름

# 패키지는 담기회에?

# 모듈
# 합 평균 표준편차 같이
# 다양한 파일을 하나의 폴더로 (모듈), 
# 하나의 묶음으로 (라이브러리)
# 이 것을 관리하는 관리자 (pip)

# 명령어 한 줄로 pip install설치 가능

# 기능의 코드들이 (function) 이 모운 게 모듈 그런 모듈을 모은 게 패키지
# git lib를 다시 듣기

# 1. 모듈을 가져오는 것
import random
# sequence? 리스트
menu = ['햄버거, 국밥, 초밥']
print(random.choice(menu))

# population
# random.sample(population, k)
# return a k length list 6개 숫자
# the population sequence. 1~45개 숫자 중

lucky_numbers = random.sample(range(1,46),6) # 리스트가 됐네

for i in range(5) : 
    print(sorted(random.sample(range(1,46),6)))

# .sort() : 메서드
# return : None
numbers = [10, 2, 5]
result = numbers.sort()
print(result)
print(numbers)

numbers = [10, 2, 5]
numbers.sort()
print(result)

# sorted() : 함수
# return : 정렬된 리스트
numbers = [10, 2, 5]
result = sorted(numbers)
print(result)

students = ['민욱', '홍엽', '현석', '정은']
print(students)
random.shuffle(students)
print(students)
random.shuffle(students)
print(students)

import datetime

print(datetime.datetime.now())
print(datetime.date(2023, 1, 5))

today = datetime.datetime.today()
print(today)
print(type(today))
print(today.year)
print(today.day)

end = datetime.datetime(2023,6,14)
print(f'우리가 개발자가 되는시간... {end - today}')

import os

print(os.listdir())

# 패키지 설치
# 넘겨넘겨
# 에러파트

# 에러와 예외
# 제어가 되는 시점
# 조건 / 반복, 함수
# '값이 변경되는 시점'
# 여러분에게 에러메시지란?
# a에러 고치고 b에러 좋다 -> 지금의 문제는 해결했다.
# 로직 에러 ?
# 러버덕 디버깅 ? 설명하다가 해결
# branches 모든 조건이 원하는대로 동작하는지
# for loops 반복문에 진입하고 횟수
# while loops + 종료조건까지 한번더 혹은 이상이하로 동작하는지
# function 함수 호출시, 함수 파라미터, 함수 결과

# 디버깅 습관화

# 문법 에러

# eol eof

# 네임에러는 변수의 오타를 봐라

# round 반올림

# 파이썬 내장 예외

# 예외 처리

# 에러제외 다른 걸 할 수 있다.

# assert 
# raise 쓰는 사람에게 개발자가 에러를 준다.\

# 질문을 할 때 내가 한 것 에러 뜬 것, 위치 그리고 다시 시도 한 거 근데 안 됨

# code up 이라는 사이트 문제집 파이썬 기초 100제

# dict_~.item() ?


