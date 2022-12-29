## 마크다운 기반 문서 작성

### **마크다운언어**
 
  존 그루버가 만든 텍스트 기반의 마크업 언어

- 최소한의 문법으로 구성되며 순수 텍스트로 작성이 가능하다
 
  이런 단순한 텍스트 문법으로 다양한 환경에서 변환하여 보여준다.

- text를 html로 변환하는 언어

  쉽게 읽고 쓸 수 있는 기본 text format

- 워드프로세서는 다양한 기능과 달리 다른 프로그램에 호환이 제약되지만 마크다운언어는 순수텍스트로 다양한 환경에서 변환돼서 보여진다

  README.md, 정적사이트생성기(Static site generator) 기반 블로그, 마크다운 기반 SW (Jupyter notebook, markdown + @ = Notion)

- 마크업언어
 
  문서가 화면에 표시되는 형식을 나타내거나 데이터의 논리적인 구조를 명시하기 위한 규칙들을 정의한 언어의 일종이다

  명령과 연산을 시키는 **프로그래밍 언어**와 달리 데이터를 단순히 기술하는 언어여서 기록하기 위한 매체에 더 가깝다

  그 외에

  문서나 데이터의 구조를 명기하는 언어의 한 가지
  
  데이터를 화면에 표시하기 위해서 사용하는 언어

마크다운의 문법은 [markdown.md](markdown.md)를 참조

디스코드에서도 일부 사용 가능

## 개발자에게 문서 작성이란?
교제에서 나오는 링크와 같이 상당히 중요한 것을 알 수 있다. [참조교제](https://syllaverse.com/courses/17/s/15/curriculum)(30page)

---------------------------

## CLI

- command line interface or 명령어 인터페이스

- 가상 터미널 또는 텍스트 터미널로 사용자와 컴퓨터가 상호 작용하는 방식

- 이런 인터페이스를 제공하는 프로그램을 명령 줄 해석기 또는 셸(shell)이라고 한다.

- 여기서 사용되는 인터페이스(interface)란 사물과 인간 사이의 경계에서, 상호 간의 소통을 위해 만들어진 매개체나 프로토콜

    쉽게 무언갈 조작하는 하나의 접면

**gui**(graphic user interface)는 그래픽 기반의 인터페이스로 **cli**라는 명령 기반의 인터페이스보다 유저친화적이다.


## **<U>명령을 하고 그 결과를 읽어서 정보를 습득한다.</U>**
## **<U>불편한 게 아니라 다른 것이다.</U>**
## **CLI와 친해지자**

- 기초 파일시스템 명령어

  pwd   : 현재 디렉토리 출력   (print working directory)

  cd    : 디렉토리 이동        (change directory)

  ls    : 목록                (list)

  mkdir : 디렉토리 생성        (make directory)

  touch : 파일 생성

  rm    : 파일 삭제하기

  rm -r : 폴더 삭제하기

## 버전 관리의 의미

git은 분산버전관리시스템중 하나다. (협업할 때, 기록할 때, 깃헙할 때 쓰는 거요?)

버전은 컴퓨터 소프트웨어의 특정 상태

이상적인 버전관리는 <U>**효율적인 버전관리**</U>다.

분산버전관리시스템은 중앙집중식버전관리시스템과 다르게 개인 컴퓨터에도 버전이 있다.

### git init

- ls -al 하면 .git을 발견 가능

git init으로 시작!

- git 버전 관리 기초 흐름

  작업한 파일 상태       - Working directory

  -(add)->

  커밋할 파일 목록 상태  - INDEX(staging area)

  -(commit)->

  버전                  - HEAD(Repository)

### git add <file>

커밋 이전의 대기

### git commit -m '<커밋메시지>'

버전 기록

**상황에 맞는 commit이 중요하다.**

- git status로 working directory와 staging area의 상태 확인

  tracked : unmodified(not place in git), modified(changes **not staged** for commit)(working directory), staged(changes to be committed)(staging area)

- git log로 기록된 commit을 조회

add는 장전이다 commit은 버전을 방출 (다시 장전해야함)

모르면 검색하고 읽어라 연장선으로 인생을 디버깅해라

---

주말 단어 서술


