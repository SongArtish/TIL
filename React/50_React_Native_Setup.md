# React Native 설치

2022.01.15

---

[TOC]

---



## Node 설치

https://nodejs.org/ko/



## 1. Expo CLI를 이용하는 방법

### CLI 설치

Node 10+ should be installed

```bash
$ npm install -g expo-cli
```

### Project 실행

> `cmd`에서 실행되어야한다.

```bash
expo init expoTest

cd expoTest
npm start
```

>`git-bash`에서는 아래와 같은 구문으로 명령어를 입력해야 한다.

```bash
expo init <project-name> --template <one-of-the-predefined-templates> --name <AppName>
```

- 참고: https://stackoverflow.com/questions/52501394/cant-create-react-native-app-input-is-required-but-expo-is-in-non-interactive
- 단, VS Code의 `git-bash` Terminal에서는 구동된다.



## 2. React Native CLI를 이용하는 방법



***Copyright* © 2022 Song_Artish**