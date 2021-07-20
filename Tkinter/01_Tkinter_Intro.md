# Tkinter 시작하기

> Python tkinter을 활용하여 **GUI를 생성**한다.

2021.07.20

---

[TOC]

---



## tkinter란

- `tkinter`는 `GUI`에 대한 `표준 Python 인터페이스`이며 **`Window 창`을 생성**할 수 있다.



## 시작하기

### 1. 패키지 가져오기

```python
import tkinter
```

- 패키지를 import하여 사용하며, tkinter 함수는 `tkinter.*`의 방식으로 사용할 수 있다.

```python
import tkinter

# 생성: 가장 상위 레벨의 윈도우 창 생성
window = tkinter.Tk()

# 반복: window(윈도우 이름)의 윈도우 창을 윈도우가 종료될 떄까지 실행
window.mainloop()
```

- 위의 `생성`과 `반복` 구문 사이에 `widget`을 생성하고 적용한다.

### 2. Window 창 설정

```python
window = tkinter.Tk()

# 윈도우 창 제목 설정
window.title("tkinter demo")
# 창 크기 및 위치 설정 ("너비x높이+x좌표+y좌표")
window.geometry("640x400+100+100")
# 창 크기 조절 가능 여부 (가로, 세로)
window.resizable(False, False)

window.mainloop()
```

- :small_red_triangle: 여기서 geometry 함수의 `너비x높이`의 **곱셈 연산자**는 반드시 `*`가 아닌 **`x (알파벳)`를 사용**하여야 한다!

### 3. Widget 배치

```python
window = tkinter.Tk()

window.title("tkinter demo")
window.geometry("640x400+100+100")
window.resizable(False, False)

# Label(윈도우이름, text="내용")
label = tkinter.Label(window, text = "환영합니다")
# 위젯을 배치
label.pack()

window.mainloop()
```

- :ballot_box_with_check: 속성이 설정되어 있지 않기 때문에 가장 최상단에 라벨이 배치된다.



***Copyright* © 2021 Song_Artish**

