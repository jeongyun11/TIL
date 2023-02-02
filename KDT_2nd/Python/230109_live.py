# sw expert arcademy
# 커리어리
# 요즘 it
# 퍼블리
# 동아일보
# geek news # chat gpt 많이 보인다.
# ces # 

# ------


# # (tuple) 튜플
# 불변한 값들의 나열
# 변경 불가능(immutable), 반복 가능(interable) # 변경 가능한 list 요소의 바뀌치기 유뮤
# 변경되지 않는다는 것이 tuple특징

result = divmod(4,3)
print(result)
print(type(result))

my_dict = {'name' : '더 글로리', 'cast' : '송혜교'}
# print(my_dict.keys())
print(my_dict.items())
print(type(my_dict.items()))

for a in my_dict.items() : 
    print(a)
    print(type(a))

## (set)세트
# 중복 값 제거
# 값을 나열한 중괄호
# 빈 set은 set()을 사용
# 나열이 랜덤
# .add, .remove()
# 세트를 활용하면 다른 컨테이너에서 중복된 값을 쉽게 제거할 수 있음

my_list = ['서울', '서울', '대전', '광주', '서울', '대전', '부산', '부산']
my_list2 = []
my_dict = {}
for city in my_list : 
    my_dict[city] = True

print(my_dict)

for city in my_list : 
    if city not in my_list2 :
        my_list2.append(city)



print(len(my_dict))
# 만약 길이가 0이 되면 if나 break으로 멈출 수 있게 만든다

# 지역을 하나씩 반복
    # 만약에 결과 통에 없다면, 
        # 결과 통에 추가

# 지역별 개수를 구하세요.

# 언제 써야 하는지 생각을 하자

# split
# 
# 메서드는 뭐임
# 
# 메서드와 함수의 차이점 정의
# boolean
# 위에 네 개

result = ['1', '5', '3']

for i in result : 
    print(i, end='')

# 덧셈으로도

# join 메서드
print(''.join(result))
print(' '.join(result))

# list 리스트 메서드
# 같은 값이 여러 개라면
# count 이전

text = 'hello!'

# # set
# 누가 쓸 수 있는지
a = ['a', 'b', 'c']
# a.upper()

# 인풋으로 아웃풋을 낸다.
# set은 유일한 값들의 모임

# set 연산자는 집합개념

# # dictionary(딕셔너리)
# 키 값의 쌍으로 이루어진 모음
# .get(k)
drama = {'name' : '더 글로리', 'writer' : '김은숙'}
print(drama['name'])
# print(drama['director'])
# key값의 아이템즈를 반환한다. # keyError
print(drama.get('director')) # None 

students = {'홍엽' : 89, '민지' : 20, '소담' : 47}
print(students['홍엽'])
print(students.get('길동',0))

# .update([other])

# 문서 읽어보기 자료구조, 

# 중요한 메서드 정리

# 숫자형 boolean, None

# 시퀀스 문자열 리스트 튜플 range

# 컬렉션 set dictionary

# 숫자형 boolean, None
# 변환과 반복


# 시퀀스: 문자열 리스트 튜플 range
# string  : 변환 불가능하며, 반복 가능한  문자의 나열
# list    : 변환 가능하며, 반복 가능한    변경 가능한 값의 나열
# tuple   : 변환 불가능하며, 반복 가능한  변경 불가능한 값의 나열
# range   : 숫자의 나열 변경가능

# 컬렉션 
# set         : 유일한 값들의 모음, 변환과 반복이 가능하다. 중복이 없다. 중복없는 값들의 모음
# dictionary  : 키-값의 모음

# 4번은 list로 해보자

