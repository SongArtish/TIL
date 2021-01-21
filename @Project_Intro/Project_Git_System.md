# 프로젝트 Git 시스템

2021.01.13

---

[TOC]

---



## 들어가며

개발 프로젝트를 효과적으로 완료하기 위해 다양한 개발 시스템, 도구를 활용한다.

- `Git` : 코드 관리 시스템
- `Jira`: 이슈 관리 시스템
- `Jenkins`: 빌드 자동화 도구
- `sonarQube`: 정적 분석 도구



## Git

> 버전 관리 시스템(VCS)

[Git 공식문서](https://git-scm.com/docs)



## JIRA

> 이슈 관리 소프트웨어

- `이슈`, `스프린트`, `스크럼보드` 제공 등 이슈로 정의할 수 있는 개발 항목(기능, 작업 단위, 버그 등)을 관리할 수 있다.



## Jenkins

> 빌드 문제에 대응할 수 있도록 지속적인 통합(CI, Continuous Integration)을 제공하는 도구

**배경**

```markdown
여러 명의 개발자가 하나의 프로젝트를 진행하는 경우 소스 코드 변경/병합 등의 과정에서 버전 충돌이 발생하여 문제가 없던 소스 코드가 일정 시간이 흐른 후 빌드가 되지 않는 경우가 발생하는데, 이 때 이전의 어느 시점에서 빌드 문제가 발생했는지 찾으며 이러한 문제에 대응할 수 있도록 지속적인 통합(CI, Continuous Integration)을 제공한다.
```

- 빌드를 자동화함으로써 각자 작업한 내용을 서로 공유하고 있는 Git 저장소에 업로드할 때마다 빌드를 수행하여 뒤늦게 발견될 수 있는 문제를 조기에 파악하고 어떤 변경 사항이 어떤 영향을 미쳤는지 확인할 수 있다.
- 즉, Git 저장소와 Jenkins의 연동을 통해 빌드/배포 단계에서 자동으로 진행될 수 있다.



## Git 시스템 구축 과정

### 1. 프로젝트 준비

- **프로젝트 팀 정보를 확인**하거나 프로젝트 기본 정보를 설정한다.
- `Jira`와 `GitLab/GitHub` 프로젝트를 생성한다.
- `GitLab Deploy Token`을 등록한다.
  - `Deploy Token`: 사용자의 계정 정보 없이도 해당 프로젝트에 접근할 수 있도록 하는 인증 정보
- `Jenkins`를 등록한다.
- `DB`를 생성한다.
  - 인터넷 환경에 웹을 구동하기 위해 

### 2. 기능 정의서 작성

- 기능 정의서에서는 `Depth1`, `Depth2`, `내용` 등으로 개발할 기능을 명확하게 작성한다.

![기능정의서](img/specification.jfif)

### 3. 이슈 관리

> `Jira`를 통해서 이슈 관리를 한다.
> 자세한건 [Jira](../@Program_Intro/Jira.md)를 참조한다.

- 이슈를 등록한다.
- 이슈 목록을 확인한다.

### 4. 소스 코드 관리

> `GitLab` 혹은 `Github`에서 소스 코드를 관리한다.

- `develop` 브랜치를 생성한다.
- `README.md` 파일을 작성한다.

### 5. 빌드 관리

> `Jenkins`를 이용하여 빌드 관리를 한다.

- 빌드를 설정한다.
  - `Jenkins`와 소스 코드를 연결한다.
- 빌드를 실행한다.
  - 빌드 버튼을 클릭하고 빌드 결과를 확인한다.
  - :white_check_mark: 빌드 결과는 프로젝트 환경에 따라 다를 수 있으므로 몇 번 변경한 후에도 계속 실패된다면 다음 과제로 넘어가도 무방하다.

### 6. 실행 기능

- 실행 이미지를 생성한다.
- 프로젝트를 실행한다.

### 7. 마무리

- `MR(Merge Request)`를 생성한다.
  - `develop` 브랜치를 `master`로 병합하는 등 `Merge Request`를 생성한다.
  - `Assignee`는 자기 자신을 지정한다.
- 브랜치를 병합한다.
- 병합 결과를 `Git Repository`에서 확인한다.
- 이슈를 완료한다.



## <참고> GitLab , Jira, MM 연동

> 여기서 Mattermost를 MM으로 약칭한다.

### 1. MM에서 Jira 구독

**1.1 push 채널 생성**

외부 push 메시지 수신을 위한 채널 생성

**1.2 Webhook 생성**

GitLab 연동을 위한 Webhook URL 생성

- MM `프로필 > 햄버거 메뉴 > 통합`을 클릭한다.
- `Incoming Webhook > 추가` 버튼을 클릭한다.
- 제목, 설명 등을 적절히 입력하고, 채널을 선택하고 `이 채널로 고정`을 체크한다.
- 생성된 URL을 복사한다. :point_left:

**1.3 Jira 구독**

생성한 push 채널에서 지라를 연결(connect)하고 이슈 구독(subscribe)을 설정

- MM 아무 채팅 창에서 아래의 슬래시 명령어 실행

  ```
  /jira connect
  ```

- Jira 로그인을 위한 Git 로그인 창에서 로그인을 진행한다.

- MM에서 Jira로 연결을 허용한다.

- 완료되면 창을 종료한다.

- 지라를 구독할 push 채널에서 아래의 슬래시 명령어 실행

  ```
  /jira subscribe
  ```

- `Create subscription` 버튼 클릭 후 구독 정보를 설정한다.

- 설정한 `변경사항(Events)`이 발생할 때 push 채널에 업데이트 된다.

- :white_check_mark: `/jira help` 슬래시 명령어로 할 수 있는 추가기능도 확인할 수 있다.



### 2. GitLab에서 Jira/MM 연동

> GitLab과 Jira가 연동이 완료되면 GitLab의 commit 정보가 Jira 이슈에 연결 되고 MR이 닫힐 때 이슈도 같이 완료된다.

**2.1 GitLab에서 Jira 연동**

- `GitLab Repository > 설정 > Integrations > Project services > Jira > Active`를 체크한다.
- 상세정보를 설정한다.
  - Web URL에 JIRA 사이트 url을 입력한다.
    - :white_check_mark: Web URL을 입력할 때 url 끝에 `/(슬래시)`를 입력하지 않도록 주의한다.
  - username/password에 로그인 정보를 설정한다.
  - `Transition ID`를 입력한다. (예시: 11,21,31)
    - Transition ID는 JIRA에 사전 정의된 이슈 상태 변경 코드로 사용된다.
  - 저장하고 테스트 `Success` 메시지를 확인한다.

**2.2 GitLab에서 MM 연동**

- 위와 같이 MM의 Integration 설정에서도 Active를 체크한다.
- Webhook URL에 MM에서 생성한 주소를 복사하여 입력한다. :point_left:
- 저장하고 Success 메시지를 확인한다.



***Copyright* © 2021 Song_Artish**

