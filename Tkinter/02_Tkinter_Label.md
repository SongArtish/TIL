# Tkinter Label

> [윤대희님 github 블로그](https://076923.github.io/posts/Python-tkinter-2/)를 참고하였다.

2021.07.20

---

[TOC]

---



## Label

> `Label`을 이용하여 삽입한 삽입한 이미지나 도표, 그림 등에 사용되는 `주석문`을 생성할 수 있다.



## 사용하기

```python
import tkinter

window = tkinter.Tk()
window.title("tkinter demo")
window.geometry("1280x640+150+80")
window.resizable(True, True)

# 라벨 속성 설정
# tkinter.Label(window, param1, param2, param3, ...)
label = tkinter.Label(window, text="python", width=10, height=5, fg="red", relief="solid")
label.pack()

window.mainloop()
```



## Parameter

### 문자열

|       이름       |                   의미                    | 기본값 |                 속성                 |
| :--------------: | :---------------------------------------: | :----: | :----------------------------------: |
|     **text**     |           라벨에 표시할 문자열            |   -    |                  -                   |
| **textvariable** |    라벨에 표시할 문자열을 가져올 변수     |   -    |                  -                   |
|    **anchor**    |    라벨안의 문자열 또는 이미지의 위치     | center | `n, ne, e, se, s, sw, w, nw, center` |
|   **justify**    | 라벨의 문자열이 여러 줄 일 경우 정렬 방법 | center |        `center, left, right`         |
|  **wraplength**  |           자동 줄내림 설정 너비           |   0    |                 상수                 |

### 형태

|        이름        |               의미               |      기본값      |                     속성                     |
| :----------------: | :------------------------------: | :--------------: | :------------------------------------------: |
|     **width**      |           라벨의 너비            |        0         |                     상수                     |
|     **height**     |           라벨의 높이            |        0         |                     상수                     |
|     **relief**     |        라벨의 테두리 모양        |       flat       | `flat, groove, raised, ridge, solid, sunken` |
| **borderwidth=bd** |        라벨의 테두리 두께        |        2         |                     상수                     |
| **background=bg**  |         라벨의 배경 색상         | SystemButtonFace |                    color                     |
| **foreground=fg**  |        라벨의 문자열 색상        | SystemButtonFace |                    color                     |
|      **padx**      | 라벨의 테두리와 내용의 가로 여백 |        1         |                     상수                     |
|      **pady**      | 라벨의 테두리와 내용의 세로 여백 |        1         |                     상수                     |

### 형식

|     이름     |                          의미                           |    기본값     |                             속성                             |
| :----------: | :-----------------------------------------------------: | :-----------: | :----------------------------------------------------------: |
|  **bitmap**  |                라벨에 포함할 기본 이미지                |       -       | `info, warning, error, question, questhead, hourglass, gray12, gray25, gray50, gray75` |
|  **image**   |                라벨에 포함할 임의 이미지                |       -       |                              -                               |
| **compound** | 라벨에 문자열과 이미지를 동시에 표시할 때 이미지의 위치 |     none      |           `bottom, center, left, none, right, top`           |
|   **font**   |                 라벨의 문자열 글꼴 설정                 | TkDefaultFont |                             font                             |
|  **cursor**  |                 라벨의 마우스 커서 모양                 |       -       |                          커서 속성                           |

### 상태

|          이름          |                 의미                  |       기본값       |            속성            |
| :--------------------: | :-----------------------------------: | :----------------: | :------------------------: |
|       **state**        |               상태 설정               |       normal       | `normal, active, disabled` |
|  **activebackground**  |   active 상태일 때 라벨의 배경 색상   |  SystemButtonFace  |           color            |
|  **activeforeground**  |  active 상태일 때 라벨의 문자열 색상  |  SystemButtonText  |           color            |
| **disabledforeground** | disabeld 상태일 때 라벨의 문자열 색상 | SystemDisabledText |           color            |

### 하이라이트

|          이름           |              의미              |      기본값       | 속성  |
| :---------------------: | :----------------------------: | :---------------: | :---: |
|   **highlightcolor**    |   라벨이 선택되었을 때 색상    | SystemWindowFrame | color |
| **highlightbackground** | 라벨이 선택되지 않았을 때 색상 | SystemButtonFace  | color |
| **highlightthickness**  |   라벨이 선택되었을 때 두께    |         0         | 상수  |



***Copyright* © 2021 Song_Artish**

