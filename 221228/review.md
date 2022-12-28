# 오늘 내용 정리

- 분산버전관리시스템 : 중앙(서버?)뿐만 아니라 로컬에서 버전을 관리하는 시스템 

- 관리(crud) : create, read, update, delete

- 버전관리 : 작업을 (add) commit 하는 것

git은 버전을 관리한다.

## **github은 버전을 관리한다.**

- github에서 삭제한다X, 삭제한 최신 버전을 받아온다 O

**.git을 포함한 폴더의 하위 폴더에 또 .git을 만들지 말자**

**clone을 하면 그 폴더로 들어가면 링크가 그 clone한 사람의 url로 연결.**

- push
  - 로컬 저장소의 버전을 원격저장소로 보낸다.

- pull
  - 원격저장소의 버전을 로컬 저장소로 가져온다.

- 로컬 시작은 git init
- 원격 시작은 git clone

- git remote add origin url 실패 시
  git remote rm <원격저장소>


# push conflict
- github과 local의 commit이 통일이 안되면 pull로 통일시켜준다.
- 같은 파일에서 갈리면 merge conflict가 발생한다. (재밌겠다.)

---

**remote된 url이 폴더마다 다르다.**

---

브랜치란 무엇인가

