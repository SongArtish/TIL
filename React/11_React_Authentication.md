# React 인증

---

[TOC]

---



## Session

### Login

서버에서는 다음과 같이 로직을 처리한다.

- 요청이 들어오면 해당 유저에 대한 정보를 DB에서 확인한다.

- 유저 정보가 DB에 있는 경우, 세션에 사용자 id 등을 저장해준다.

  ```javascript
  request.session.save(() => {
      req.session.<저장할 정보 key> = <저장할 정보>
      res.json({data: <사용자 정보>, message: "ok"})
  })
  ```

```javascript
// login.js
const { Users } = require('../../models'); // 해당 모델의 인스턴스를 models/index.js에서 가져옵니다.

module.exports = {
  post: async (req, res) => {
    // userInfo는 유저정보가 데이터베이스에 존재하고, 완벽히 일치하는 경우에만 데이터가 존재합니다.
    const userInfo = await Users.findOne({
      where: { userId: req.body.userId, password: req.body.password },
    });
    // 결과가 존재하는 경우 세션 객체에 userId가 저장되어야 합니다.
    let result = userInfo
    if (!result) {
      // your code here
      res.status(404).send({message: "not authorized"})
    } else {
      req.session.save(() => {
        req.session.userId = userInfo.userId
        res.json({data: userInfo, message: "ok"})
      })
    }
  }
}
```

react에서는 다음과 같이 요청을 할 수 있다.

```javascript
// Login.js
loginRequestHandler() {
    let params = JSON.stringify({
        userId: this.state.username,
        password: this.state.password
    })
    axios({
        url: "https://localhost:4000/users/login", // 통신할 웹문서
        method: "post", // 통신할 방식
        data: params
    })
    // 로그인에 성공하면
    // - props로 전달받은 함수를 호출해, 로그인 상태를 변경하세요.
        .then(() => {
        this.props.loginHandler()
        // - GET /users/userinfo 를 통해 사용자 정보를 요청하세요
        axios.get('https://localhost:4000/users/userinfo')
            .then((res) => {
            // - props로 전달받은 함수를 호출해, 사용자 정보를 변경하세요.
            this.props.setUserInfo(res.data.data)
        })
    })
}
```

### Logout

서버에서는 다음과 같이 로직을 처리한다.

- session에 로그인 시 저장했던 값이 존재하는지 판별한다.

- session에 값이 존재하면, 세션을 삭제해준다.

  ```javascript
  req.session.user = null
  ```

```javascript
// logout.js
module.exports = {
  post: (req, res) => {
    // 앞서 로그인시 세션 객체에 저장했던 값이 존재할 경우, 이미 로그인한 상태로 판단할 수 있습니다.
    if (!req.session.userId) {
      res.status(400).send({message: "not authorized"})
    } else {
      // 로그아웃 요청은 세션을 삭제하는 과정을 포함해야 합니다.
      res.status(200).send()
      req.session.user = null
    }
  },
};
```

react에서는 다음과 같이 요청할 수 있다.

```javascript
// Logout 관련
  const handleLogout = () => {
    axios
    .post("https://localhost:4000/users/logout", {
      withCredentials: true,
    })
      .then(() => {
        props.logoutHandler()
      })
  };
```

### 사용자 정보 요청

서버는 다음과 같이 로직을 구현한다.

- session에서 user 정보를 확인한다.
- session에 들어있는 user 정보를 바탕으로 DB에서 사용자 정보를 조회한다.

```javascript
// userinfo.js
const { Users } = require('../../models');

module.exports = {
  get: async (req, res) => {
    if (!req.session.userId) {
      res.status(400).send({message: "not authorized"})
    } else {
      // 데이터베이스에서 로그인한 사용자의 정보를 조회한 후 응답합니다.
      const userInfo = await Users.findOne({
        where: { userId: req.session.userId }
      })
      res.status(200).json({data: userInfo, message: "ok"})
    }
  },
};
```

react에서는 요청을 다음과 같이 보낼 수 있다.

```javascript
// - GET /users/userinfo 를 통해 사용자 정보를 요청
axios.get('https://localhost:4000/users/userinfo')
    .then((res) => {
    // - props로 전달받은 함수를 호출해, 사용자 정보를 변경
    this.props.setUserInfo(res.data.data)
})
```



## Token

### Login

서버에서는 다음과 같이 로직을 처리해준다.

- 요청한 아이디/비밀번호가 DB에 존재하는지 확인한다.

- 일치하는 유저가 있으면, `access token`과 `refresh token`을 생성해준다.

  ```javascript
  const accessToken = jwt.sign(payload, process.env.ACCESS_SECRET, { expiresIn: '1d' })
  const refreshToken = jwt.sign(payload, process.env.REFRESH_SECRET, { expiresIn: '2d'})
  // 일반적으로 refresh token이 더 유효기간이 길다.
  ```

- `refresh token`은 쿠키에 저장해준다.

  ```javascript
  res.cookie('refreshToken', refreshToken)
  ```

```javascript
// login.js
const { request } = require('express');
const { Users } = require('../../models');
const jwt = require('jsonwebtoken')

module.exports = async (req, res) => {
  // TODO: urclass의 가이드를 참고하여 POST /login 구현에 필요한 로직을 작성하세요.
  console.log(req.body.userId)
  // 여기서 await를 해주지 않으면 데이터를 가져오기 전에 아래 작업이 시작됨
  let userInfo = await Users.findOne({
    where: { userId: req.body.userId, password: req.body.password}
  })
  if (!userInfo) {
    res.status(404).send({ data: null, message: "not authorized" })
  }
  // 일치하는 유저가 있는 경우
  else {
    let payload = {
      id: userInfo.id,
      userId: userInfo.userId,
      email: userInfo.email,
      createdAt: userInfo.createdAt,
      updatedAt: userInfo.updatedAt
    }
    console.log(payload)
    // userInfo를 담아 JWT 생성
    // 1) access token 2) refresh token
    const accessToken = jwt.sign(payload, process.env.ACCESS_SECRET, { expiresIn: '1d' })
    const refreshToken = jwt.sign(payload, process.env.REFRESH_SECRET, { expiresIn: '2d'})

    res.cookie('refreshToken', refreshToken)
    // res.cookie('refreshToken', refreshToken, {maxAge: 10000})
    res.status(200).send({data: {accessToken: accessToken}, message: "ok"})
  }
};
```

React에서는 axios를 활용하여 로그인을 해준다.

```react
loginRequestHandler() {
    axios.post('https://localhost:4000/login', {
        userId: this.state.userId,
        password: this.state.password
    })
        .then((res) => {
        this.props.loginHandler(res.data.data.accessToken)
        // access token을 state로 저장하여 관리한다.
        this.props.issueAccessToken(res.data.data.accessToken)
    })
}
```

### Access Token 가져오기

서버에서는 다음과 같이 처리한다.

- request의 headers에 authorization이 있는지 확인한다.

- authorization이 있으면 `.env`에 저장해놨던 access token 키로 복호화한다.

  ```javascript
  const data= jwt.verify(token, process.env.ACCESS_SECRET)
  // data에 담긴 정보
  // {
  //   id: 1,
  //   userId: 'kimcoding',
  //   email: 'kimcoding@codestates.com',
  //   createAt: '2020-11-18T10:00:00.000Z',
  //   updatedAt: '2020-11-18T10:00:00.000Z',
  //   iat: 1654653961,
  //   exp: 1654740361
  // }
  ```

```javascript
// accessToken.js
const { Users } = require('../../models');
const jwt = require('jsonwebtoken')

module.exports = async (req, res) => {
  // TODO: urclass의 가이드를 참고하여 GET /accesstokenrequest 구현에 필요한 로직을 작성하세요.
  const authorization = req.headers['authorization']
  // authorization 데이터가 'Bearer jwt_code' 이런 식으로 들어온다!
  if (!authorization) res.status(404).send({data: null, message: "invalid access token"})
  else {
    const token = authorization.split(' ')[1]
    const data= jwt.verify(token, process.env.ACCESS_SECRET)
    if (!data) res.status(404).end({data: null, message: "access token has been tempered"})
    else {
      let params = {
        userInfo: {
          id: data.id,
          userId: data.userId,
          email: data.email,
          createdAt: data.createdAt,
          updatedAt: data.updatedAt,
        }
      }
      res.status(200).send({data: params, message: "ok"})
    }
  }
};
```

React에서는 다음과 같이 처리한다.

```javascript
accessTokenRequest() {
    axios.get('https://localhost:4000/accesstokenrequest', {
        headers: {
            authorization: `Bearer ${this.props.accessToken}`
        }
    })
        .then((res) => {
        this.setState({
            ...res.data.data.userInfo
        })
    })
}
```

### Token 갱신하기

서버에서는 다음과 같이 로직을 구현한다.

- 쿠키(request.cookies)에 refresh token이 있는지 확인한다.

- 있을 경우 `.env`에 저장되어 있는 키로 복호화를 한다.

  ```javascript
  const data= jwt.verify(token, process.env.REFRESH_SECRET)
  ```

- 복호화된 데이터로 access token을 다시 생성하여 보낸다.

  ```javascript
  let accessToken = jwt.sign(userInfo, process.env.ACCESS_SECRET, { expiresIn: '1d' })
  let payload = {
      userInfo: userInfo,
      accessToken: accessToken
  }
  res.status(200).send({data: payload, message: "ok"})
  ```

```javascript
// refreshToken.js
const { Users } = require('../../models');
const jwt = require('jsonwebtoken')

module.exports = async (req, res) => {
  const token = req.cookies.refreshToken
  if (!token) res.status(404).send({data: null, message: "refresh token not provided"})
  else if (token === 'invalidtoken') res.status(404).send({data: null, message: "invalid refresh token, please log in again"})
  else {
    const data= jwt.verify(token, process.env.REFRESH_SECRET)
    if (!data) res.status(404).send({data: null, meesage: "refresh token has been tempered"})
    else {
      let userInfo = {
        id: data.id,
        userId: data.userId,
        email: data.email,
        createdAt: data.createdAt,
        updatedAt: data.updatedAt,
      }
      let accessToken = jwt.sign(userInfo, process.env.ACCESS_SECRET, { expiresIn: '1d' })
      let payload = {
        userInfo: userInfo,
        accessToken: accessToken
      }
      res.status(200).send({data: payload, message: "ok"})
    }
  }
};
```

React에서는 다음과 같이 함수를 만들어 사용할 수 있다.

```react
refreshTokenRequest() {
    axios.get('https://localhost:4000/refreshtokenrequest')
        .then((res) => {
        this.setState({
            ...res.data.data.userInfo
        })
        this.props.issueAccessToken(res.data.data.accessToken)
    })
}
```



***Copyright* © 2022 Song_Artish**