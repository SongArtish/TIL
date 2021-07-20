# Tkinter Button

> [윤대희님 github 블로그](https://076923.github.io/posts/Python-tkinter-3/)를 참고하였다.

2021.07.20

---

[TOC]

---



## Button

> `Button`을 이용하여 `메소드` 또는 `함수` 등을 실행시키기 위한 `단추`를 생성할 수 있다.



## 사용하기

```python
import tkinter

window = tkinter.Tk()
window.title("tkinter demo")
window.geometry("1280x640+150+80")
window.resizable(True, True)

count = 0

def countUp():
    global count
    count += 1
    # label text를 바꿔준다.
    label.config(text=str(count))

label = tkinter.Label(window, text="0")
label.pack()

button = tkinter.Button(
    window,
    overrelief="sunken",    # 버튼에 마우스를 올렸을 때 버튼의 테두리 모양
    width=15,
    command=countUp,	# 사용자정의 함수 실행
    repeatdelay=1000,   # 누르고 있기 시작한 1초 후에 command가 실행됨
    repeatinterval=100  # 0.1초마다 버튼을 뗄 때까지 command가 계속 실행됨
    )
'''
repeatdelay와 repeatinterval을 실제로 테스트 해보니 변화가 없다.
'''
button.pack()

window.mainloop()
```



## Method

------

|     이름     |   의미    |
| :----------: | :-------: |
| **invoke**() | 버튼 실행 |
| **flash**()  |  깜빡임   |

- Tip : `invoke()` : 버튼을 클릭했을 때와 동일한 실행
- Tip : `flash()` : `normal` 상태 배경 색상과 `active` 상태 배경 색상 사이에서 깜빡임



## Parameter

------

### 문자열

|     이름     |                   의미                    | 기본값 |                 속성                 |
| :----------: | :---------------------------------------: | :----: | :----------------------------------: |
|     text     |           버튼에 표시할 문자열            |   -    |                  -                   |
| textvariable |    버튼에 표시할 문자열을 가져올 변수     |   -    |                  -                   |
|    anchor    |    버튼안의 문자열 또는 이미지의 위치     | center | `n, ne, e, se, s, sw, w, nw, center` |
|   justify    | 버튼의 문자열이 여러 줄 일 경우 정렬 방법 | center |         center, left, right          |
|  wraplength  |           자동 줄내림 설정 너비           |   0    |                 상수                 |





### 형태

|      이름      |                     의미                     |      기본값      |                     속성                     |
| :------------: | :------------------------------------------: | :--------------: | :------------------------------------------: |
|     width      |                 버튼의 너비                  |        0         |                     상수                     |
|     height     |                 버튼의 높이                  |        0         |                     상수                     |
|     relief     |              버튼의 테두리 모양              |       flat       | `flat, groove, raised, ridge, solid, sunken` |
|   overrelief   | 버튼에 마우스를 올렸을 때 버튼의 테두리 모양 |      raised      | `flat, groove, raised, ridge, solid, sunken` |
| borderwidth=bd |              버튼의 테두리 두께              |        2         |                     상수                     |
| background=bg  |               버튼의 배경 색상               | SystemButtonFace |                    color                     |
| foreground=fg  |              버튼의 문자열 색상              | SystemButtonFace |                    color                     |
|      padx      |       버튼의 테두리와 내용의 가로 여백       |        1         |                     상수                     |
|      pady      |       버튼의 테두리와 내용의 세로 여백       |        1         |                     상수                     |



### 형식

|   이름   |                          의미                           |    기본값     |                             속성                             |
| :------: | :-----------------------------------------------------: | :-----------: | :----------------------------------------------------------: |
|  bitmap  |                버튼에 포함할 기본 이미지                |       -       | `info, warning, error, question, questhead, hourglass, gray12, gray25, gray50, gray75` |
|  image   |                버튼에 포함할 임의 이미지                |       -       |                              -                               |
| compound | 버튼에 문자열과 이미지를 동시에 표시할 때 이미지의 위치 |     none      |            bottom, center, left, none, right, top            |
|   font   |                 버튼의 문자열 글꼴 설정                 | TkDefaultFont |                             font                             |
|  cursor  |                 버튼의 마우스 커서 모양                 |       -       | [커서 속성](https://076923.github.io/posts/Python-tkinter-3/#reference-1) |



### 상태

|        이름        |                 의미                  |       기본값       |            속성            |
| :----------------: | :-----------------------------------: | :----------------: | :------------------------: |
|       state        |               상태 설정               |       normal       | `normal, active, disabled` |
|  activebackground  |   active 상태일 때 버튼의 배경 색상   |  SystemButtonFace  |           color            |
|  activeforeground  |  active 상태일 때 버튼의 문자열 색상  |  SystemButtonText  |           color            |
| disabledforeground | disabeld 상태일 때 버튼의 문자열 색상 | SystemDisabledText |           color            |



### 하이라이트

|        이름         |              의미              |      기본값       | 속성  |
| :-----------------: | :----------------------------: | :---------------: | :---: |
|   highlightcolor    |   버튼이 선택되었을 때 색상    | SystemWindowFrame | color |
| highlightbackground | 버튼이 선택되지 않았을 때 색상 | SystemButtonFace  | color |
| highlightthickness  |   버튼이 선택되었을 때 두께    |         0         | 상수  |



### 동작

|      이름      |                        의미                         | 기본값 |     속성     |
| :------------: | :-------------------------------------------------: | :----: | :----------: |
|   takefocus    |        Tab 키를 이용하여 위젯 이동 허용 여부        |  True  |   Boolean    |
|    command     |    버튼이 active 상태일 때 실행하는 메소드(함수)    |   -    | 메소드, 함수 |
|  repeatdelay   | 버튼이 눌러진 상태에서 command 실행까지의 대기 시간 |   0    |   상수(ms)   |
| repeatinterval |   버튼이 눌러진 상태에서 command 실행의 반복 시간   |   0    |   상수(ms)   |



***Copyright* © 2021 Song_Artish**

