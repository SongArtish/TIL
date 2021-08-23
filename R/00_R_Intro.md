# R Intro

2021.08.23

---

[TOC]

---



## 알아보기

> R 프로그램은 S언어 기반 통계패키지이다.

**역사**

- 미국 벨 연구소의 John Chamber가 개발한 S언어를 기반
- 뉴질랜드 오클랜드대학교 로스이하카와 로버트 젠트맨에 의해 개발
- 2000년 최초 1 version 시작



## 특징

- open source
- 데이터 핸들링이 우수
  - txt, csv, xlsx, SAS, SPSS, Stata, DB 등 다양한 데이터를 읽어오는 기능이 있다.
- interpreter
- 우수한 그래픽 기능
  - 2D, 3D, 동적 그래프 지원
- 다양한 형태(벡터, 행렬, 배열, 데이터 프레임, 리스트)의 데이터 구조를 지원하므로 분석 대응력이 좋다.
- 데이터 메모리(RAM)에서 작동하기 때문에 속도가 빠르다.



## 설치하기

### R 설치

- R 프로그램 설치를 시작하기 전, 이후 작업시 오류 발생을 방지하기 위해서 아래의 3가지 사항을 체크한다.

  ```markdown
  1. 컴퓨터의 이름을 영어로 지정
  2. 사용자 이름도 영어로 지정
  3. 폴더 이름도 영어로 지정 (특수문자나 공백 사용X)
  ```

- [R 홈페이지](https://www.r-project.org/)에 접속하여 CRAN > Korea로 이동 후 컴퓨터 OS 환경에 맞는 **base** 파일을 다운로드 한다.
- :pushpin: 설치 파일 경로를 default인 `Program Files`에 할 경우 경로에 공백이 있어 나중에 사용 중 오류가 발생할 수 있기 때문에, 다른 경로를 선택해줄 수 있도록 한다!

### R Studio 설치

- [공식 홈페이지](https://www.rstudio.com/)에서 OS 환경에 맞는 R Studio를 설치한다.

### VS Code 환경 구축

> R Studio 대신 VS Code에서 R을 사용할 수 있는 환경을 구축할 수도 있다.

- VS Code > Extensions에서 `R`을 검색하고 해당 플러그인을 설치해준다.

- `Ctrl + Shift + P > User Settings > Extensions > R > (스크롤 제법 아래) Rterm: Windows`에서 R 설치경로의 실행파일을 설정해준다.

  - 예시

    ```markdown
    C:\R\R-4.1.1\bin\R.exe
    ```
    
    - :pushpin: Rpath에도 위의 실행파일 경로를 설정해준다!

- 이렇게 하면 설치가 완료된다.

> - `*.R` 형태의 파일을 생성하여 R 프로젝트를 생성할 수 있다.
> - 코드를 입력하고 블럭 처리 한 다음 Ctrl + Enter 로 코드를 실행시킬 수 있다.



***Copyright* © 2021 Song_Artish**