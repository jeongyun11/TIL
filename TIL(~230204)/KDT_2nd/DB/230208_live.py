#
# # 데이터 data
# 저장이나 처리에 효율적인 형태로 변환된 정보 (information), 저장하고 조작

# 데이터를 저장하자

# 데이터베이스 : 체계적인 데이터 모음
# # 역할 : 저장하고 조작
# create read update delete

# 기초적인 부분에 집중하기 : 데이터를 조작, crud 하기 + 권한, 자동화 



# the relation
# 관계를통한 구조적인 저장 
# 관계형 데이터베이스

# 관계 : 여러 테이블 간의 (논리적) 연결

# 고유한 식별 값 -> 기본 키, Primary Key, pk 
# pk값을 참조하는 컬럼을 외래키 컬럼 foreign key fk

# table(aka relation) :
# field column, attribute
# record row tuple
# database schema

# 우리는 관계형데이터베이스를 공부할 예정이다

# 1. table (relation)
#     데이터를 기록하는 곳
# 2. field (column, attribute(속성))
#     각 필드에는 고유한 데이터 형식(타입)이 지정됨
# 3. record(row, tuple)
#     각 레코드에는 구체적인 데이터 값이 저장됨
# 4. database (schema)스키마
#     테이블의 집합 set of tables
# 5. primary key 기본키 pk
#     각 레코드의 고유한 값
#     관계형 데이터베이스에서 레코드의 식별자로 활용
# 6. Foreign Key 외래키
#     테이블의 필드중 다른 테이블의 레코드를 식별할 수 있는 키
#     각 레코드에서 서로 다른 테이블 간의 관계를 만드는 데 사용

#     관계!!!!

#  (rdbms)relations database management system
# (관계형) 데이터베이스를 관리하는 소프트웨어 프로그램
# 저장과 관리를 용이하게 하는 시스템, db와 사용자 사이에 인터페이스 역할
# 
# MySQL 가장 널리 사용되는 오픈 소스 rdbms
    # 다양한 운영체제에서 실행가능
    # 여러 프로그래밍 언어를 위한 다양한 api를 제공
    # mySQL Workbench Tool을 통해 gui를 제공

# mysql가 database server 형태로 database들을 저장 및 조작

# sql은 db에서 사용하는 언어
# db 자체가 sql만 알아듣는 언어

# 관계형 데이터베이스 -> 테이블로 구조화 돼있다.  관계는 외래키로 
# 아이디 찾는 시간복잡도

# 파일명 0208_til.md