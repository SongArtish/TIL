# Go 이론

2022.04.18

---

[TOC]

---



## 1. Main Package

- Go 프로젝트에서 `main.go` 명칭의 파일은 컴파일을 위해 사용된다.
- Go는 main 패키지의 main function을 가장 먼저 찾아서 실행시킨다.

```go
// main.go
package main

import (
	"fmt"
)

func main() {
    // Formatting.PrintLine
	fmt.Println("Hello, World!")
}
```





## 2. Packages and Imports

- :pushpin: function을 export하는 경우, 해당 function을 첫 글자를 대문자로 작성한다.

```go
// test.go
package test

import "fmt"

func sayBye(){
  fmt.Println("Bye")
}

func SayHello(){
  fmt.Println("Hello")
}
```

```go
// main.go
package main

import (
	"main/test"
)

func main() {
  test.SayHello()
}

```

- `main.go`에서 `SayHello` 함수는 import되지만, `sayBye` 함수는 import되지 않는다.



## 3. Variables and Constants

- constant 선언 시, 데이터 타입이 무엇인지 함께 선언해주어야 한다.
  - constant는 다른 데이터를 재할당할 수 없다.

```go
const name string = "song"
```

- variable은 다른 데이터를 재할당할 수 있다.

```go
var name string = "song"
name = "ju"
fmt.Println(name)

> ju
```

- :ballot_box_with_check: 아래와 같이 데이터 타입을 입력하지 않고 선언할 수도 있다.
  - 이런 경우, Go에서 자동으로 데이터 타입을 찾아준다.
  - 단, function 밖에서는 작동하지 않는다.

```go
func main() {
  name := "song"
  fmt.Println(name)
}
```





***Copyright* © 2022 Song_Artish**