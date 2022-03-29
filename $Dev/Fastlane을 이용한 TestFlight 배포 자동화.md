# Fastlane을 이용한 TestFlight 배포 자동화

> 정경진님의 문서 참고함

2022.03.25

---

[TOC]

---

## Fastlane이란?
> Ruby 기반 클라이언트 자동 빌드 오픈소스 라이브러리
- iOS 및 Android 앱의 베타 배포 및 릴리즈 자동화를 지원

## Fastlane 설치 ⚙️ (macOS)
```markdown
**사전에 설치가 필요한 프로그램**
- Xcode
- CocoaPods
```

### 1. Homebrew로 설치
> Homebrew가 설치되어 있는지 확인 후 진행
```bash
brew install fastlane
```

### 2. bundler 설치
fastlane을 업데이트할 때 필요한 bundler를 설치한다.
```bash
sudo gem install bundler
```

## Fastlane 설정
### 1. 프로젝트에 init
```bash
/ios

fastlane init
```
1. init 옵션 선택
: `fastlane init` 명령어를 실행하면 오셥 선택창이 나타난다. (옵션은 init 후에 언제든지 변경할 수 있다.)
: TestFlight 배포를 위해 **옵션 2번**을 선택한다.
2. Apple ID 입력
: Apple ID를 입력한 뒤 설정이 끝날 때까지 Enter를 눌러준다.
3. 생성된 파일들
: 아래와 같은 파일들이 생성된 것을 확인할 수 있다.
```
/ios

ios
  ㄴ Gemfile
  ㄴ Gemfile.lock
  ㄴ fastlane
    ㄴ Appfile
    ㄴ Fastfile
```

### 2. `.env` 작성

Apple ID나 앱 암호 및 Slack URL을 관리하기 위한 환경변수 파일을 생성한다.
1. Apple 앱 암호 설정
: Apple 매뉴얼 [앱 암호 사용하기](https://support.apple.com/ko-kr/HT204397) > 앱 암호를 생성하는 방법을 참고하여 앱 암호를 생성
2. `.env` 작성
: ios/fastlane 디렉토리에 `.env` 파일을 생성한다.
: `SLACK_URL_PROJECT_DDC`는 Slack 워크 스페이스의 `project-ddc` 채널의 Incoming WebHooks 주소이다.
```
/ios/fastlane/.env

APPLE_ID="${배포 권한이 있는 Apple ID를 여기 적어주세요}"
FASTLANE_APPLE_APPLICATION_SPECIFIC_PASSWORD="${생성한 웹 암호를 여기 적어주세요}"
SLACK_URL_PROJECT_DDC="${Slack Webhoook 주소}"
```

### 3. Appfile 수정
아래 코드 2번째 라인의 `apple_id`를 환경변수로 사용하도록 변경해준다.
```
/ios/fastlane/Appfile

app_identifier("com.crscube.cubeDDC") # The bundle identifier of your app
apple_id(ENV["APPLE_ID"]) # Your Apple email address
 
itc_team_id("117487995") # App Store Connect Team ID
team_id("9FRJXJNGZK") # Developer Portal Team ID
 
# For more information about the Appfile, see:
#     https://docs.fastlane.tools/advanced/#appfile
```

### 4. Fastfile 수정
fastlane을 사용하여 실행할 파이프라인을 작성해준다.
```markdown
**예시**

1. 배포 시작 시 Slack 메시지 전송
2. App Build
3. TestFlight 배포
4. 배포 완료 시 slack 메시지 전송
```
파이프라인 실행 도중 에러가 바생하면 에러의 내용을 Slack으로 전송한다.
```
/ios/fastlane/Fastfile

default_platform(:ios)
 
platform :ios do
  desc "Push a new beta build to TestFlight"
  lane :beta do
    slack(
          message: "TestFlight #{get_version_number} (#{latest_testflight_build_number + 1}) 배포를 시작합니다.",
          slack_url: ENV["SLACK_URL_PROJECT_DDC"]
    )
    increment_build_number({
        build_number: latest_testflight_build_number + 1
    })
    build_app
    upload_to_testflight
    slack(
        message: "TestFlight #{get_version_number} (#{latest_testflight_build_number}) 배포가 완료되었습니다.",
        success: true,
        slack_url: ENV["SLACK_URL_PROJECT_DDC"]
    )
  end
  error do |lane, exception, options|
    slack(
        message: "에러 발생 : #{exception}",
        success: false,
        slack_url: ENV["SLACK_URL_PROJECT_DDC"]
    )
    end
end
```

## Fastlane 실행
파이프라인 작성 시 지정한 이름으로 fastlane을 실행한다.
```bash
/ios

fastlane beta
```

## <참고> Fastlane 업데이트
```bash
/ios

bundle update
```

***Copyright* © 2022 Song_Artish**