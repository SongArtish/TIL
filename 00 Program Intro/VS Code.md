# VS Code

2020.08.05.

*****

[TOC]

*****



## 준비하기

**기본 shell을 Git Bash로 변경하기**

​	(1) `Ctrl+Shift+P`를 입력하면 `>`로 시작하는 입력창이 나타난다.

​	(2) 검색창에서 `Select Default Shell`을 검색하여 클릭한다.

​	(3) 선택옵션 창에서 `Git Bash`를 클릭한다.

​	(4) `Ctrl + J` 혹은 `Ctrl+backtick`을 누르고 terminal에서 기본값이 `bash`로 바뀐 것을 확인한다.



## 1. Basic Key

### 문자 일괄 선택

> 문자 선택 후 해당 문자와 동일 한 문자 일관 선택 (하나씩)

`Ctrl`+`D` 

### 한줄 복사

> 커서가 위치한 행이 그대로 복사된다.

`Shift` + `Alt` + `↑`/`↓`

### 한줄 이동

> 선택한 행을 위/아래로 이동한다.

코드 선택 + `Alt` + `↑`/`↓`

### 한줄 삭제

> 커서가 위치한 해당 행 전체가 삭제된다.

`Ctrl`+`Shift` + `K`

### 여러 줄 들여쓰기

> 여러 줄을 지정하여 한 번에 들여쓰기를 한다.

`줄 지정`+`Tab`

### 여러 줄 내어쓰기

> 여러 줄을 지정하여 한 번에 내여쓰기를 한다.

`줄 지정`+`Shift`+`Tab`



## 2. Terminal (Bash)

- `↑` : 위에서 사용한 명령어 불러오기
- `Ctrl`+`C` : run 도중 interrupt(중지)
- `code test.py`: test.py 창을 연다.
- `code test.html`: test.html 창을 연다.

---

**cd** : 현재 bash창의 작업 위치 변경

```bash
$ cd <폴더명>
```

```bash
# 예시: 홈 디렉토리로 이동
$ cd
# 예시: 상위폴더로 이동
$ cd ..
```

---

**mkdir** : 폴더 생성

```bash
$ mkdir <폴더명>
```

---

**리스트**

```bash
$ ls		# 위치 내 폴더 및 파일 표시
$ ls -a		# 숨김 파일까지 표시
$ ls -al
```

---

- `pwd` : 현재 위치 확인     *# print working directory*
- `ctrl+L` 혹은 `clear :  현재 화면 창 clear

```bash
$ touch <파일명.확장자>
```

```bash
$ rm <파일명.확장자>
```

```bash
$ rm -rf <폴더명>/
```

---

현재 작업 위치를 VS Code로 열기

```bash
$ code .
```

---





## 3. HTML

### html 문서 기본세팅

- `!`+`Enter`

```html
<!-- 예시 -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```

### 태그 복수 선택

> 태그를 클릭 후 다른 태그를 복수 선택해서 일괄적으로 수정할 수 있다. (예시, 클래스 입력하기)

`Alt`++`클릭`



*Copyright* © Song_Artish