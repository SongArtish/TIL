# Testflight

2021.10.19

---

[TOC]

---



## 개요

> iOS 앱 베타 테스트 tool

- App Store에 앱을 release하기 전에 TestFlight에서 사용자를 간편하게 초대하여 앱 및 앱 클립을 테스트하고 의미 있는 피드백을 얻을 수 있다.



## 등록 과정

> flutter 프레임워크로 작성한 DDC 프로젝트를 기준으로 작성됨(현욱님이 작성한 문서 참고)

### 1. Flutter 프로젝트 정리

- 최신 버전 코드를 git repository에서 Pull/Download 받은 후에 진행한다.

- `Terminal`에서 프로젝트 폴더로 이동한다.

- 빌드 폴더를 정리한다.

  ```c++
  // 빌드 폴더 정리
  flutter clean
  ```

  - :no_entry: 참고 사항

    - 빌드 폴더를 정리할 때 Pub 라이브러리 또한 정리되면서 에러가 발생한다.

    - Pub 라이브러리 다운로드와 업그레이드를 하면 에러가 사라진다.

      ```c++
      // Pub 라이브러리 다운로드
      flutter pub get
      // Pub 라이브러리 업그레이드
      flutter pub upgrade
      ```

    ```c++
    // ios 폴더 들어가기
    cd ios
    // Pod 라이브러리 제거
    rm Pods & Podfile.lock & Runners.xcworkspace
    // Pod 라이브러리 다운로드
    pod install
    // ios 폴더 나오기
    cd ../
    ```

    - `Finder` 를 통해 ios 폴더에 들어가서 직접 제거해도 된다.

### 2. 프로젝트 build 및 열기

```c++
// iOS 프로젝트 빌드
flutter build ios
// xcworkspace 프로젝트 열기
open ./ios/Runner.xcworkspace
```

- Runner.xcworkspace 프로젝트를 열어야 한다.

### 3. Xcode에서 app distribute

- **Xcode**에서 진행한다.
- Runner > TARGETS (Runner) > General에 들어간다.
- Build version number를 변경한다.
- 상단 메뉴 > Product > Clean Build Folder를 클릭한다. (COMMAND + SHIFT + K)
- Build Target을 `Any iOS Device (arm64)`로 변경한다.
- 상단 메뉴 > Product > Archive를 클릭한다.
- 그리고 상단 메뉴 > Window > Organizer를 클릭한다. (COMMAND + OPTION + SHIFT + O)
- Build Version을 체크한다.
- 그리고 `Validate App` 버튼을 누르고 `Disribute App`을 누른다.

### 4. App Store Connect 확인

- 위의 모든 작업이 완료되면 [App Store Connect](https://appstoreconnect.apple.com)에 접속하여 업로드를 확인한다.



***Copyright* © 2021 Song_Artish**