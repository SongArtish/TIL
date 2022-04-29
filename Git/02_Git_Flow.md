# Git Flow

---

[TOC]

---



## 구조

```markdown
## git 공간

- working dir: 실제 작업공간
- staging area: 명령어를 입력했을 때 임시로 저장이 되는 공간
- local repository: 명령어를 입력했을 때 버전이 기록되는 공간
```

![Git Structure](img/git_structure.jfif)

`(출처: https://ndb796.tistory.com/187)`



## Git Flow

> `develop` `release` `master` 등으로 나눠서 하는 형상관리 전략

Git-flow는 총 5가지의 브랜치를 사용해서 운영을 한다.

- **master** : 제품으로 출시될 수 있는 branch
- **develop** : 다음 출시 버전을 개발하는 branch
- **feature** : 기능을 개발하는 branch
- **release** : 이번 출시 버전을 준비하는 branch
- **hotfix** : 출시 버전에서 발생한 버그를 수정하는 branch

> **master**와 **develop**가 중요한 **매인 브랜치**이고 나머지는 필요에 의해서 운영하는 브랜치라고 할 수 있다.

![git_flow](img/git_flow.png)

`(출처: https://uxgjs.tistory.com/183 [UX 공작소])`

- 참고링크: [배달의링크 Git Flow](https://woowabros.github.io/experience/2017/10/30/baemin-mobile-git-branch-strategy.html)



***Copyright* 2021 © Song_Artish**