# 리스트로 가져오거나


# ---
# '컨셉' => 구현된 방식('구현체')은 다르다.

# 'OOP' => 

# 정보 속성 동작 메서드

# 클래스 변수 : 내부에 존재하는 변수

# static method : 어떠한 인자가 전달되지 않는다.

# 함수 안에서 클래스 내부에 method 

# 스태틱은 인스턴스 사용싫음, 인스턴스는 전달된것을 조작, 클래

# 찾는 순서 인스턴스 다음에 클래스

# 클래스는 기능 덩어리 반복을 원해

# 모든사람은 이름과 나이를 가진다.

# 상속을 통한 메서드 재사용
# 오버라이딩

# 타입에러도 상속관계

# # 파이썬 응용/심화

# syntax sugar

# 조건표현식으로 값을 할당
# members = ['홍엽', '세정']
# print(enumerate(members))
# print(list(enumerate(members)))

# enumerate, .items, i-range

# List Comprehension
# list안에 for문을 사용 가능하다.

# 람다함수
numbers = ['1', '2', '3']
numbers = [int(numbers[i]) for i in range(3)]
numbers = list(map(int,numbers))
print(numbers)
numbers = [[2, 1], [1, 3]]

new_numbers = list(map(sorted, numbers))

print(new_numbers)

numbers = map()

# 리스트컴프리헨션
#  
print(list(map(lambda n: n//2, numbers)))

# sorted의 방식을 생각하자
# 괄호열고 들어가서 리턴값이 결과값
# sort(key = lamda ....)

# 개발하는 개발자들이 있고 그들이 생각하는 관점에서 바라봐라
# 개발자의 입장