# <실습> Mnemonic Wallet

---

[TOC]

---



## Overview

> [LightWallet](https://github.com/ConsenSys/eth-lightwallet#readme): A minimal ethereum javascript wallet

`eth-lightwallet` 모듈을 이용하여 Express.js 서버에서 간단한 Mnemonic Wallet을 개발한다. API 테스트는 Postman을 사용해서 한다.

- eth-lightwallet 모듈에 내장되어 있는 함수를 사용하여 개발
  - 랜덤한 니모닉 코드 생성
  - 니모닉을 시드로 키스토어 생성
- Postman을 사용하여 결과 확인
- fs 모듈을 사용하여 키스토어 로컬 저장



## Express.js 서버

```
폴더구조

...
routes
ㄴ wallet.js
app.js
...
```

Express 서버는 다음과 같이 구성되어 있다.

```javascript
// app.js
const express = require('express');
const cookieParser = require('cookie-parser');
const logger = require('morgan');
const cors = require('cors');

const walletRouter = require('./routes/wallet');

const app = express();
const port = 3000;

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(
  cors({
    origin: ['http://localhost:3000'],
    methods: ['GET', 'POST'],
    credentials: true
  })
);

app.get('/', function(req, res, next) {
  res.status(200).send({"message": "Mnemonic server is running..."});
});
app.use('/wallet', walletRouter);

// catch 404 and forward to error handler
app.use((req, res, next) => {
  const err = new Error('Not Found');
  err['status'] = 404;
  next(err);
});

// error handler
app.use((err, req, res, next) => {
  res.status(err.status || 500);
  res.json({
      errors: {
          message: err.message,
      },
  });
});

app.listen(port, () => {
  console.log(`
  ################################################
  🛡️  Server listening on port: ${port} 🛡️
  http://localhost:${port}
  ################################################
  `);
});

module.exports = app;

```

```javascript
// routes/wallet.js

const express = require('express');
const router = express.Router();
const lightwallet = require("eth-lightwallet");
const fs = require('fs');
...
```



## Mnemonic 코드 생성하기

`lightwallet` 모듈의 `keystore.generateRandomSeed()` 함수를 사용하여 니모닉 코드를 생성한다. 성공했을 경우, mnemonic 변수를 응답으로, 에러 발생 시 에러를 응답한다.

```javascript
// routes/wallet.js

router.post('/newMnemonic', async(req,res) => {
    let mnemonic
    try {
        mnemonic = lightwallet.keystore.generateRandomSeed()
        console.log(mnemonic)
        res.json({mnemonic})
    }
    catch (err) {
        console.log(err)
    }
});
```

API 요청을 해보면 다음과 같이 12개의 니모닉 코드가 응답으로 오는 것을 확인할 수 있다.

```json
{
    "mnemonic": "fun crystal alarm there car casual auction pizza rigid symbol habit between"
}
```



## 키스토어 생성하기

> **키스토어(Key Store)**: 암호화폐 지갑을 사용하기 위한 프라이빗 키(private key)를 비밀번호로 암호화한 텍스트 또는 파일

키스토어를 생성하는 API는 `password`와 `mnemonic`을 parameter로 받는다.

```json
// 예시 parameter
{
    "password": "test1234",
    "mnemonic": "fun crystal alarm there car casual auction pizza rigid symbol habit between"
}
```

`lightwallet` 모듈의 `keystore.createVault` 함수를 사용하여 키스토어를 생성한다.

- 첫 번째 인자(options)에는 password, seedPhrase, hdPathString을 담는다.
- 두 번째 인자(callback)에는 키스토어를 인자로 사용하는 함수를 만든다.

```javascript
// routes/wallet.js
router.post('/newWallet', async(req, res) => {
    let password = req.body.password
    let mnemonic = req.body.mnemonic

    try {
        lightwallet.keystore.createVault(
            {
                password: password,
                seedPhrase: mnemonic,
                hdPathString: "m/0'/0'/0'"
            },
            // ks: key store
            function (err, ks) {
                ks.keyFromPassword(password, function (err, pwDerivedKey) {
                    ks.generateNewAddress(pwDerivedKey, 1)

                    let address = (ks.getAddresses().toString())
                    let keystore = ks.serialize()

                    res.json({ keystore: keystore, address: address })
                })
            }
        )
    }
    catch (exception) {
        console.log("NewWallet ==>>>>" + exception)
    }
});

module.exports = router;
```

생성된 `keystore`를 json 파일로 로컬에 저장할 수도 있다.

```javascript
// routes/wallet.js
					...
                    // res.json({ keystore: keystore, address: address })
                    fs.writeFile('wallet.json', keystore, function(err, data) {
                        if (err) res.json({code: 999, message: "fail"})
                        else res.json({code: 1, message: "success"})
                    })
					...
```

저장된 파일의 내용은 다음과 같다.

```json
// wallet.json
{"encSeed":{"encStr":"lcksyXsBqyWDMZs1LXCTFrOuhJjUovUyN2E/W/WXALh+ziqkvMo2Su45CYRN914ORPVgFy7yRuwP98O2zz5xayiLWFTWaxWPDJqhcH+yLsYzBAoOC7b2WjBCu+qAslTQwHrQPn3p441IfPQc9Azfkqd19X7JzzzLof4mGrzCMgPalBexJDJfqw==","nonce":"FneYH6Ndc7XFNrSQoS5v25cjYoKqbeMP"},"encHdRootPriv":{"encStr":"QAk08kM7tf8n0apWWQwt8KIqGWAPqUOwlReylrNmDCy9OCb+5K+2FWAPvY39+0eAfKiZ8l8XAGNAQa8jHm9b34XeCKDGa+CdQP9c7efE2NyTKBIxsJW5c+vjTN1NWI00OjbF87+MNUSQ5PA38ZfZKU/PDeDRn0wWLh6OHVyngA==","nonce":"kl4CcATcf45TH/M0PULWW9nD1geaIdKV"},"addresses":["b554735356986df17d4fc452195d9af82fe04441"],"encPrivKeys":{"b554735356986df17d4fc452195d9af82fe04441":{"key":"0kPtGwUQmOMwMJcWYtTKAtlo5YWgvED/FjGCdxQhk79vq+teVow/qpKIL5YWTdWE","nonce":"YpZ6KGKspXiuJjL9L3TIP8+xfhgMo+xw"}},"hdPathString":"m/0'/0'/0'","salt":"seSTfL5n6NAxapsib9VhryZK/kMVr+Nd+CauVmLP0oY=","hdIndex":1,"version":3}
```



***Copyright* © 2022 Song_Artish**