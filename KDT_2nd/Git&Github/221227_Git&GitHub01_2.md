# `마크다운` 문법 정리

## 문법 종류

<br />

### 1. heading (제목과 소제목)

  - #으로 정리한다.

  - #개수의 증가에 따라 소제목으로 변환 (최대 6개까지)  

    ```
    # Heading1
    ## Heading2
    ...
    ###### Heading6
    ```

<br />

### 2. 텍스트 강조

  1. 굵게(bold)

  2. 기울임(italic)

  - \* or _ 을 사용한다.

  - 한가지 사용시 italic 두가지사용시 bold 
    
    \*\*bold\*\*, \_\_bold\_\_ -> **bold**

    \*italic\*, \_italic\_ -> *italic*

<br />

### 3. blockquotes (인용문)

- \>를 사용해서 줄을 강조한다.

  > 중꺽마 : 중요한 것은 꺽이지 않는 마음

<br />

### 4. list

  1. ordered list

  - 순서대로 정렬할 때 사용

  - 숫자에 .을 붙여서 사용

    1. 순
    2. 서
    3. 대
    4. 로

  2. unordered list

  - 순서와 상관없이 나열할 때 사용

  - -을 사용

    - 상
    - 관
    - 없
    - 이

<br />

### 5. code (= inline code block?)

  - 같은 줄 안에 코드를 강조

  - \` \` 사이에 작성

    중요한 것은 \`꺾이지 않는 마음\`이다.

    ->
    중요한 것은 `꺾이지 않는 마음`이다.

<br />

### 6. horizontal Rule (수평선)

  - \-\-\-을 사용해서 수평선을 만든다
  ---

<br />

### 7. link

- \[제목\]\(링크\) 형식으로 사용

  \[네이버\]\(https://www.naver.com\)

  ->[네이버](https://www.naver.com)



<br />

### 8. image

  - !\[제목\]\(링크\) 형식으로 사용

    !\[꺼무위키에서 가져온 국룰 바탕화면\]\(https://w.namu.la/s/0b37ca973c31f23cf3e58137ce18c0668ba08220a176f480e7c66fa628a5724a4c90385043fe463af2acbcadedc3f58382a56164be6a1403b25572e6b50fda63370eda6e7ee744cbd7cc700508af19d8f8544f3a58ce1b5b08316edeec452904\) ->

    ![꺼무위키에서 가져온 국룰 바탕화면](https://w.namu.la/s/0b37ca973c31f23cf3e58137ce18c0668ba08220a176f480e7c66fa628a5724a4c90385043fe463af2acbcadedc3f58382a56164be6a1403b25572e6b50fda63370eda6e7ee744cbd7cc700508af19d8f8544f3a58ce1b5b08316edeec452904)


<br />

### 9. table

- 형태가 복잡하므로 [여기](https://www.markdownguide.org/extended-syntax/#tables)를 참조

  | 중요한 | 것은 |
  | ----- | ----- |
  | 꺾이지 | 않는 |
  | 마 | 움 |

<br />

### 10. Fenced Code Block (코드블록)

\`\`\` \`\`\`사이에 생성
특정 언어를 명시하면 Syntax Highlighting 적용 가능

```
` = backtick

* = asterisk

- = hyphen

_ = underscore or underbar
```

``` python
{
print('내 이름은 정윤원')
}
```

<br />

### 11. Underline

- \~\~ \~\~ 사이에 글을 넣는다 

  \~\~Underline\~\~

  ->~~Underline~~

<br />

### 12. Strikethrough (밑줄)

- \<U\>\</U\> 사이에 글을 넣는다.

  \<U\>Strikethrough\</U\>

  -> <U>Strikethrough</U>

