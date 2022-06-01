# Yarn Berry

---

[TOC]

---



## Overview

Node.js를 위한 새로운 패키지 관리 시스템이다.  node_modules를 생성하지 않고 기본 캐시 폴더에 zip 파일로 저장해서 경로를 `.pnp.js`에 명시한다. Plug n Play라는 개념을 사용하여, 기존 npm의 node_modules`의 비효율성을 개선한다. pnp는 버전, 위치, 의존성 등을 담고 있다.



## 시작하기

NPM에서 최신 버전을 내려받고, 버전을 Berry로 설저하면 Yarn Berry를 사용할 수 있다. (Plug'n'Play를 켠다.)

```bash
$ yarn set version berry
```

해당 레포지토리에 `.yarnrc.yml`, `.yarn/releases` 폴더 아래에 `yarn-berry.js` 또는 `yarn-3.0.2.cjs` 파일과 `.pnp.cjs`가 생성된다. node_modules와 package.lock.json은 필요없으므로 지워준다.

```bash
rm -rf node_modules
rm -rf package-lock.json
```

만약 `.yarnrc.yml` 파일에 아래와 같이 nodeLinker가 node_modules를 가리키고 있다면, 속성을 지워준다.

```yaml
nodeLinker: node-modules	# 삭제

yarnPath: .yarn/releases/yarn-3.2.1.cjs
```





## Plug'n'Play 동작 방법

Plug'n'Play 설치 모드에서 `yarn install`로 의존성을 설치하면, 기존과 다른 모습으로 `.yarn` 폴더에 파일이 생성되는 것을 확인할 수 있다. Yarn Berry는 node_modules를 생성하지 않는다. 대신, `.yarn/cache` 폴더에 의존성의 정보가 저장되고, `.pnp.cjs` 파일에 의존성을 찾을 수 있는 정보가 기롤된다. `.pnp.cjs`를 이용하면 디스크 I/O 없이 어떤 패키지가 어떤 라이브러리에 의존하는지, 각 라이브러리는 어디에 위치하는지 바로 알 수 있다.

```
# 예시: react 패키지의 .pnp.cjs 파일
/* react 패키지 중에서 */
["react", [
  /* npm:17.0.1 버전은 */
  ["npm:17.0.1", {
    /* 이 위치에 있고 */
    "packageLocation": "./.yarn/cache/react-npm-17.0.1-98658812fc-a76d86ec97.zip/node_modules/react/",
    /* 이 의존성들을 참조한다. */
    "packageDependencies": [
      ["loose-envify", "npm:1.4.0"],
      ["object-assign", "npm:4.1.1"]
    ],
  }]
]],
```

Yarn은 Node.js가 제공하는 `require()`문의 동작을 덮어씀으로써 효율적인 패키지를 찾을 수 있도록 한다. 이 때문에 PnP API를 이용하여 의존성 관리를 하고 있을 때에는 `node` 명령어 대신에 `yarn node` 명령어를 사용한다.

```bash
$ yarn node
```



## ZipFS

> Zip Filesystem

Yarn PnP 시스템에서 각 의존성은 Zip 아카이브로 관리된다. zip으로 묶임 라이브러리는 `.yarn/cache` 폴더에 저장된다.



## 장점

1. 새로 저장소를 복제하거나 브랜치를 바꾸었다고 해서 yarn install을 실행하지 않아도 된다. (**Zero-Install**)
2. CI에서 의존성 설치하는 시간을 크게 절약할 수 있다.



***Copyright* © 2022 Song_Artish**
