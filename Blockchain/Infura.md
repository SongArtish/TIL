# Infura

---

[TOC]

---



## Overview

Infura는 원격 이더리움 노드를 통해 이더리움 네트워크에 접근할 수 있게 해주는 서비스이다. Infura에서는 RPC URL과 API Key를 제공하기 때문에, 직접 이더리움 네트워크에 접근하여 블록을 동기화하지 않아도 네트워크에 접근할 수 있다.

> 이더리움 클라이언트 소프트웨어인 Geth 또는 Parity는 사용하려면 블록체인의 블록을 동기화해야 하기 때문에 많은 데이터를 단운로드 받아야 한다는 불편함 점이 있다.



## API Key 받기

> 시작하기에 앞서, infura.io에 접속하여 회원가입을 진행한다.

1. 대시보드에서 `Create New Project` 버튼을 눌러서 새로운 이더리움 프로젝트를 생성한다.
2. 프로젝트를 생성하면 프로젝트 디테일 페이지로 이동한다.
    - Project ID: API Key이다.
    - Project Secret: 프로젝트의 비밀 키이다.
    - Endpoints: 원격 이더리움 노드를 통해 이더리움 네트워크에 접속할 수 있는 URL이다.
        보통 `https://{network_name}.infura.io/v3/{API_KEY}` 형태이다.
3. 주어진 API Key를 사용해 원격 이더리움 노드에 접근할 수 있다.



## 사용해보기

Infura에서는 HTTP 요청을 보내 이더리움 네트워크와 상호작용할 수 있다. 간단하게 터미널 창에서 curl로 HTTP 요청을 보내본다.

```bash
curl https://ropsten.infura.io/v3/자신의_API_KEY \
    -X POST \
    -H "Content-type: application/json" \
    -d '{"jsonrpc": "2.0", "method": "eth_getBalance", "params": ["메타마스크_계정_주소", "latest"], "id": 1}'
```

위 명령어는 원격 이더리움 노드를 통해 특정 계정 주소의 잔액을 확인하는 요청이다. 요청에 성공하면 다음과 같은 결과가 표시된다
~~~~
```bash
jsonrpc":"2.0","id":1,"result":"0x14b26fcaebcb36790"}
```

`result`로는 16진수의 값이 출력되는데, 이는 계정의 잔액을 wei 단위로 표시한 것이다.



***Copyright* © 2022 Song_Artish**