# Tkinter Entry

> [윤대희님 github 블로그](https://076923.github.io/posts/Python-tkinter-4/)를 참고하였다.

2021.07.20

---

[TOC]

---



## Entry

> `Entry`(기입창)을 이용하여 텍스트를 `입력`받거나 `출력`하기 위한 `기입창`을 생성할 수 있다.



## 사용하기

- 아래의 코드를 활용하면 계산기를 만들 수 있다.

```python
import tkinter
from math import *

window = tkinter.Tk()
window.title("tkinter demo")
window.geometry("1280x640+150+80")
window.resizable(True, True)

def calc(event):
    # python evel 함수: 매개변수로 받은 expression(식)을 문자열로 받아서, 실행하는 함수 -> 계산을 해준다.
    label.config(text="결과="+str(eval(entry.get())))   # get함수: 기입창의 텍스트를 문자열로 반환

entry = tkinter.Entry(window)
# key나 mouse 등의 event를 처리하여 메소드/함수를 실행
entry.bind("<Return>", calc)    # 여기서 "<Return>"이 없으면 실행이 되지 않는다.
entry.pack()

label = tkinter.Label(window)
label.pack()


window.mainloop()
```



## Method

------

|                 이름                 |                             의미                             |
| :----------------------------------: | :----------------------------------------------------------: |
|       insert(index, “문자열”)        |                 `index` 위치에 `문자열` 추가                 |
|    delete(start_index, end_index)    |       `start_index`부터 `end_index`까지의 문자열 삭제        |
|                get()                 |               기입창의 텍스트를 문자열로 반환                |
|             index(index)             |                 `index`에 대응하는 위치 획득                 |
|            icursor(index)            |                `index` 앞에 키보드 커서 설정                 |
|         select_adjust(index)         |             `index` 위치까지의 문자열을 블록처리             |
| select_range(start_index, end_index) |          `start_index`부터 `end_index`까지 블록처리          |
|           select_to(index)           |             키보드 커서부터 `index`까지 블록처리             |
|          select_from(index)          | 키보드 커서의 색인 위치를 `index` 위치에 문자로 설정하고 선택 |
|           select_present()           |       블록처리 되어있는 경우 `True`, 아닐 경우 `False`       |
|            select_clear()            |                        블록처리 해제                         |
|               xview()                |                       가로스크롤 연결                        |
|        xview_scroll(num, str)        |                    가로스크롤의 속성 설정                    |

- xview_scroll

  - ```plaintext
    num
    ```

    - num > 0 : 왼쪽에서 오른쪽으로 스크롤
    - num < 0 : 오른쪽에서 왼쪽으로 스크롤

  - ```plaintext
    str
    ```

    - `units` : 문자 너비로 스크롤
    - `pages` : 위젯 너비로 스크롤





## Parameter

------

### 문자열

|     이름     |                    의미                     | 기본값 |         속성          |
| :----------: | :-----------------------------------------: | :----: | :-------------------: |
|     show     |           기입창에 표시되는 문자            |   -    |         문자          |
| textvariable |    기입창에 표시할 문자열을 가져올 변수     |   -    |           -           |
|   justify    | 기입창의 문자열이 여러 줄 일 경우 정렬 방법 | center | `center, left, right` |





### 형태

|       이름        |                 의미                 |      기본값      |                     속성                     |
| :---------------: | :----------------------------------: | :--------------: | :------------------------------------------: |
|       width       |            기입창의 너비             |        0         |                     상수                     |
|      relief       |         기입창의 테두리 모양         |       flat       | `flat, groove, raised, ridge, solid, sunken` |
|  borderwidth=bd   |         기입창의 테두리 두께         |        2         |                     상수                     |
|   background=bg   |          기입창의 배경 색상          | SystemButtonFace |                    color                     |
|   foreground=fg   |         기입창의 문자열 색상         | SystemButtonFace |                    color                     |
|    insertwidth    |      기입창의 키보드 커서 너비       |        2         |                     상수                     |
| insertborderwidth |   기입창의 키보드 커서 테두리 두께   |        0         |                     상수                     |
| insertbackground  |      기입창의 키보드 커서 색상       | SystemWindowText |                    color                     |
| selectborderwidth | 기입창의 문자열 블록처리 테두리 두께 |        0         |                     상수                     |
| selectbackground  |  기입창의 문자열 블록처리 배경 색상  | SystemHighlight  |                    color                     |
| selectforeground  | 기입창의 문자열 블록처리 문자열 색상 | SystemHighlight  |                    color                     |





### 형식

|      이름      |             의미              |    기본값     |       속성        |
| :------------: | :---------------------------: | :-----------: | :---------------: |
|      font      |   기입창의 문자열 글꼴 설정   | TkDefaultFont |       font        |
|     cursor     |   기입창의 마우스 커서 모양   |       -       |     커서 속성     |
| xscrollcommand | 기입창의 가로스크롤 위젯 적용 |       -       | Scrollbar위젯.set |





### 상태

|        이름        |                  의미                   |       기본값       |            속성            |
| :----------------: | :-------------------------------------: | :----------------: | :------------------------: |
|       state        |                상태 설정                |       normal       | normal, readonly, disabled |
| readonlybackground |  readonly 상태일 때 기입창의 배경 색상  |  SystemButtonFace  |           color            |
| disabledbackground |  disabeld 상태일 때 기입창의 배경 색상  |  SystemButtonFace  |           color            |
| disabledforeground | disabeld 상태일 때 기입창의 문자열 색상 | SystemDisabledText |           color            |





### 하이라이트

|        이름         |               의미               |      기본값       | 속성  |
| :-----------------: | :------------------------------: | :---------------: | :---: |
|   highlightcolor    |   기입창이 선택되었을 때 색상    | SystemWindowFrame | color |
| highlightbackground | 기입창이 선택되지 않았을 때 색상 | SystemButtonFace  | color |
| highlightthickness  |   기입창이 선택되었을 때 두께    |         0         | 상수  |





### 동작

|     이름      |                      의미                      | 기본값 |   속성   |
| :-----------: | :--------------------------------------------: | :----: | :------: |
|   takefocus   |     Tab 키를 이용하여 위젯 이동 허용 여부      |  True  | Boolean  |
| insertontime  |   기입창의 키보드 커서 깜빡임이 보이는 시간    |  600   | 상수(ms) |
| insertofftime | 기입창의 키보드 커서 깜빡임이 보이지 않는 시간 |  300   | 상수(ms) |



***Copyright* © 2021 Song_Artish**

