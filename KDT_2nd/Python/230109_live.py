
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

locations = ['서울', '서울', '대전', '광주', '서울', '대전', '부산', '부산']
result = []

# 지역을 하나씩 반복
# for location in locations :
    #만


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