

# 

# -------------------복습------------------------------
# 박스가 있고 값을 할당하다 이름을 설정한 변수에 타입이 정해진 값을 할당하다
# bool, intfloot, sequence - string, list, range, collection - dictionary
# 타입 별 연산자나 메서드
# dict는 keu value 쌍, range 숫자의 나열, list 변경 가능한 값들의 시퀀스, string : 문자들의 나열

# 조건과 반복 for 객체순회 요소 인덱스, while 조건
# 함수 - input(파라미터) output(return), 특정한 객체가 들어가서 특정한 객체가 나온다.

# 조작을 못하면 에러 예외
# dict와 조건반복보다 어려운 게 아니라 다른 거다 dict는 약통의 키와 알약인 value

# range 빈칸 확인

# ------------------ 교제 -------------------
# # 파일 입출력
# 파일을 읽고 쓸 수 있다.

# 인자로 무엇을 넣어야 하는지 r w a
f = open('hello.txt', 'r', encoding = 'utf-8')
print(f.readline())
print(f.read())
f.close
# 반복문 가능

# type확인 습관화

with open('hello.txt', 'r', encoding = 'utf-8') as f :
    print(type(f))
    text = f.readline()
    print(text)
    print(text)
    print(text)
    print(f.read())

# 두 개의 문법을 반드시 기억

# json은 하나의 표기 방식
import json
from pprint import pprint
with open('data/movie.json', 'r', encoding = 'utf-8') as f :
    movie = json.load(f)
    print(movie)
    print(type(movie))
    print(movie['title'])

# movie라는 dictionary가 movies라는 list에 담겼다.