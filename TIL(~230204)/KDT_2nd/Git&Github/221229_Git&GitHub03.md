# Branch

Git의 구조

WD (working directory)

-add->

Staging Area (INDEX)

-commit->

Local Repository

<-push, pull->

Remote Git Repository (GitHub)

branch : 독립적인 작업흐름을 만들고 관리

- 합동 작업의 유형
1. clone 담아서 작업하는 데, 아무도 안하고 나 혼자하고 했을 때 (fastforward)
2. 각자 다른 파일로 분업했을 때 (just merge)
3. 같은 파일을 분업했을 때 (merge conflict)

- 브랜치 생성

merge : branch를 통합하는 명령어 (conflict를 조심!)

fastforward : 한 branch가 commit을 생성할 때 다른 branch가 변경이 없으면 작동
    merge를 하면 두 branch에 같이 적용된다. (git log 참조!)

# Git Flow

Git을 활용하여 협업하는 흐름으로 branch를 활용하는 전략을 의미한다.
develop이란 branch에서 개발을 완료하고 master에 적용한다.

(그림으로 뜯어가며 분석할 예정)

고정된 답이 있는 것이 아니라 상황에 알맞게 바뀐다.

master branch는 배포 가능한 상태여야 한다.
feature branch는 각 기능의 의도를 알 수 있도록 작성한다.
Commit message는 매우 중요하며, 명확하게 작성한다.
Pull Request를 통해 협업한다.
master branch에 병합하여 배포한다.

## GitHub Flow Models

Git Flow 원칙 아래 GitHub이 제시하는 2가지 방법
Shared Repository Model : 동일한 저장소를 공유 (master + feature) repository owner (project manager) + collaborator 
병합 완료 후 branch삭제 후 master branch를 업데이트하고 반복


Fork & Pull Model : 협업이 아닌 상태의 모델
반드시 fork후 clone 

내가 원격 저장소에 직접적인 push 권한이 있는지 여부

# git restore, git commit --amend

git restore             : 마지막 commit으로 되돌린다. wd에 있는 수정 정보를 없앤다
git restore --staged    : add에 있는 자료를 wd로 되돌린다.
git commit --amend      : commit 메세지를 바꿀 수 있다. 하지만 해쉬값이 바뀐다.(commit history가 바뀐다.)






---

부가적인 내용

## GitHub Profile README


---

서술 : git config(-l), branch, git구조, merge, merge명령어5개, master 짱개발자, head, pr, feature

오늘의 목적

branch의 목적을 알교 활용할 수 있다.
branch 병합 과정의 상황을 이해하고 충돌을 해결할 수 있다.

할 것 : 리팩토링, 깃헙꾸미기, font(d2 coding?), 올려준 정보 참고, .gitignore, addwith에서 cs50, commit메세지 쓰는 법, commit history 차이로 pull 안되는 개념 다시 생각하기

자세 : **세이브를 하자**
3번 이상 파고들기
commit은 완성상태만 할 것
README.md를 적극 활용
.gitignore를 활용
생각하고 검색하고 -> 핑프 컷
commit message 일관성