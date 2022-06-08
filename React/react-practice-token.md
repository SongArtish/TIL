# <실습> React에서 Token 사용하기

여기서는 대표적인 Token인 JWT를 사용한다.

---

[TOC]

---



## Express.js 서버 구현하기

### 기본 설정

- `.env` 파일을 생성하고 DB명 등을 관리한다.
- HTTPS 사용을 위해 로컬 인증서 파일을 사용한다.

### index.js

index.js에서는 express 서버를 구성한다. 

```javascript
require("dotenv").config();
const fs = require("fs");
const https = require("https");
const cors = require("cors");
const cookieParser = require("cookie-parser");

const express = require("express");
const app = express();

const controllers = require("./controllers");

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(
  cors({
    origin: ["https://localhost:3000"],
    credentials: true,
    methods: ["GET", "POST", "OPTIONS"],
  })
);
app.use(cookieParser());

// router 역할
app.post("/login", controllers.login);
app.get("/accesstokenrequest", controllers.accessTokenRequest);
app.get("/refreshtokenrequest", controllers.refreshTokenRequest);

const HTTPS_PORT = process.env.HTTPS_PORT || 4000;

// 인증서 파일들이 존재하는 경우에만 https 프로토콜을 사용하는 서버를 실행합니다. 
// 만약 인증서 파일이 존재하지 않는경우, http 프로토콜을 사용하는 서버를 실행합니다.
// 파일 존재여부를 확인하는 폴더는 서버 폴더의 package.json이 위치한 곳입니다.
let server;
if(fs.existsSync("./key.pem") && fs.existsSync("./cert.pem")){

  const privateKey = fs.readFileSync(__dirname + "/key.pem", "utf8");
  const certificate = fs.readFileSync(__dirname + "/cert.pem", "utf8");
  const credentials = { key: privateKey, cert: certificate };

  server = https.createServer(credentials, app);
  server.listen(HTTPS_PORT, () => console.log("server runnning"));

} else {
  server = app.listen(HTTPS_PORT)
}
module.exports = server;
```

### controller/inex.js

```javascript
module.exports = {
  login: require('./users/login'),
  accessTokenRequest: require('./users/accessTokenRequest'),
  refreshTokenRequest: require('./users/refreshTokenRequest'),
};
```

### controller/users/login.js

```javascript
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

### controller/users/accessToken.js

```javascript
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

### controller/users/refreshTokenjs

```javascript
const { Users } = require('../../models');
const jwt = require('jsonwebtoken')

module.exports = async (req, res) => {
  // TODO: urclass의 가이드를 참고하여 GET /refreshtokenrequest 구현에 필요한 로직을 작성하세요.
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

### models/index.js

```javascript
'use strict';

const fs = require('fs');
const path = require('path');
const Sequelize = require('sequelize');
const basename = path.basename(__filename);
const env = process.env.NODE_ENV || 'development';
const config = require(__dirname + '/../config/config.js')[env];
const db = {};

let sequelize;
// 데이터베이스와 연결을 진행합니다.
if (config.use_env_variable) {
  sequelize = new Sequelize(process.env[config.use_env_variable], config);
} else {
  sequelize = new Sequelize(
    config.database,
    config.username,
    config.password,
    config
  );
}
//models 폴더 내부에 존재하는 파일들을 읽어와 findOne, findAll과 같은 함수를 실행할수 있게끔 모델 인스턴스를 생성합니다.
fs.readdirSync(__dirname)
  .filter((file) => {
    return (
      file.indexOf('.') !== 0 && file !== basename && file.slice(-3) === '.js'
    );
  })
  .forEach((file) => {
    const model = require(path.join(__dirname, file))(
      sequelize,
      Sequelize.DataTypes
    );
    //db.users와 같이 db 객체 내부에 모델 인스턴스를 저장합니다.
    db[model.name] = model;
  });
//associate 부분에 내용이 존재한다면 자동으로 관계를 형성합니다.
Object.keys(db).forEach((modelName) => {
  if (db[modelName].associate) {
    db[modelName].associate(db);
  }
});

db.sequelize = sequelize;
db.Sequelize = Sequelize;
//여러 모델 인스턴스가 담긴 객체를 내보냅니다.
module.exports = db;
```

### models/user.js

```javascript
'use strict';
const { Model } = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class Users extends Model {
    /**
   * 해당 파일은 시퀄라이즈 ORM이 데이터베이스 쿼리를 진행하기 위해
   * 해당되는 테이블의 이름 및 어트리뷰트의 특성을 지정하는 파일입니다.
   * 또한 아래 associate 부분을 통해서 다른 테이블과의 관계를 작성할수 있습니다.
   * 
   * 이 파일을 바탕으로 시퀄라이즈는 서버가 실행되면  findOne, findAll과 같은 함수를
   * 사용할수 있게 준비를 하게 합니다.
   */
    static associate(models) {

    }
  }
  Users.init(
    {
      id: {
        type: DataTypes.NUMBER,
        primaryKey: true,
      },
      userId: DataTypes.STRING,
      password: DataTypes.STRING,
      email: DataTypes.STRING,
    },
    {
      sequelize,
      modelName: 'Users',
    }
  );
  return Users;
};
```

### config/config.js

```javascript
const dotenv = require("dotenv");
dotenv.config();

module.exports = {
  development: {
    username: "root",
    password: process.env.DATABASE_PASSWORD,
    database: "authentication",
    host: "127.0.0.1",
    dialect: "mysql",
  },
  test: {
    username: "root",
    password: process.env.DATABASE_PASSWORD,
    database: "authentication",
    host: "127.0.0.1",
    dialect: "mysql",
  },
  production: {
    username: "root",
    password: process.env.DATABASE_PASSWORD,
    database: "authentication",
    host: "127.0.0.1",
    dialect: "mysql",
  },
};
```



## React 클라이언트 구현하기

### App.js

```react
import React, { Component } from "react";

import Login from "./components/Login";
import Mypage from "./components/Mypage";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isLogin: false,
      accessToken: "",
    };

    this.loginHandler = this.loginHandler.bind(this);
    this.issueAccessToken = this.issueAccessToken.bind(this);
  }

  
  loginHandler(data) {
    this.setState({
      isLogin: true
    })
  }

  issueAccessToken(token) {
    this.setState({
      accessToken: token
    })
  }

  render() {
    const { isLogin } = this.state;
    return (
      <div className='App'>
        {/* 
        TODO: isLogin 상태에 따라 Mypage 혹은 Login 컴포넌트를 렌더해야합니다.
        알맞은 컴포넌트를 렌더링하는것은 물론, 올바른 props전달하도록 작성하세요.
        */
          isLogin ? 
          <Mypage
            accessToken={this.state.accessToken}
            issueAccessToken={this.issueAccessToken}
          />
          : <Login 
            loginHandler={this.loginHandler}
            issueAccessToken={this.issueAccessToken}
          />
        }
      </div>
    );
  }
}

export default App;
```

### components/Login.js

```react
import axios from "axios";
import React, { Component } from "react";

class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      userId: "",
      password: "",
    };
    this.inputHandler = this.inputHandler.bind(this);
    this.loginRequestHandler = this.loginRequestHandler.bind(this);
  }

  inputHandler(e) {
    this.setState({ [e.target.name]: e.target.value });
  }

  loginRequestHandler() {
    /*
    TODO: Login 컴포넌트가 가지고 있는 state를 이용해 로그인을 구현합니다.
    로그인을 담당하는 api endpoint에 요청을 보내고, 받은 데이터로 상위 컴포넌트 App의 state를 변경하세요.
    초기 App:
    state = { isLogin: false, accessToken: "" }
    로그인 요청 후 App:
    state = { isLogin: true, accessToken: 서버에_요청하여_받은_access_token }
    */
   axios.post('https://localhost:4000/login', {
     userId: this.state.userId,
     password: this.state.password
   })
    .then((res) => {
      this.props.loginHandler(res.data.data.accessToken)
      this.props.issueAccessToken(res.data.data.accessToken)
    })
  }

  render() {
    return (
      <div className='loginContainer'>
        <div className='inputField'>
          <div>Username</div>
          <input
            name='userId'
            onChange={(e) => this.inputHandler(e)}
            value={this.state.userId}
            type='text'
          />
        </div>
        <div className='inputField'>
          <div>Password</div>
          <input
            name='password'
            onChange={(e) => this.inputHandler(e)}
            value={this.state.password}
            type='password'
          />
        </div>
        <div className='loginBtnContainer'>
          <button onClick={this.loginRequestHandler} className='loginBtn'>
            JWT Login
          </button>
        </div>
      </div>
    );
  }
}

export default Login;
```

### Components/Mypage.js

```react
import axios from "axios";
import React, { Component } from "react";

class Mypage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      userId: "",
      email: "",
      createdAt: "",
    };
    this.accessTokenRequest = this.accessTokenRequest.bind(this);
    this.refreshTokenRequest = this.refreshTokenRequest.bind(this);
  }

  accessTokenRequest() {
    /* 
    TODO: 상위 컴포넌트인 App에서 받은 props를 이용해 accessTokenRequest 메소드를 구현합니다.
    access token을 처리할 수 있는 api endpoint에 요청을 보내고, 받은 데이터로 Mypage 컴포넌트의 state (userId, email, createdAt)를 변경하세요
    초기 Mypage:
    state = { userId: "", email: "", createdAt: "" }
    accessTokenRequest 후 Mypage:
    state = { userId: "특정유저id", email: "특정유저email", created: "특정유저createdAt" }
    
    ** 주의사항 **
    App 컴포넌트에서 내려받은 accessToken props를 authorization header에 담아 요청을 보내야 합니다. 
    */
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

  refreshTokenRequest() {
    /*
    TODO: 쿠키에 담겨져 있는 refreshToken을 이용하여 refreshTokenRequest 메소드를 구현합니다.
    refresh token을 처리할 수 있는 api endpoint에 요청을 보내고, 받은 데이터로 2가지를 구현합니다.
    1. Mypage 컴포넌트의 state(userId, email, createdAt)를 변경
    2. 상위 컴포넌트 App의 state에 accessToken을 받은 새 토큰으로 교환
    */
    axios.get('https://localhost:4000/refreshtokenrequest')
      .then((res) => {
        this.setState({
          ...res.data.data.userInfo
        })
        this.props.issueAccessToken(res.data.data.accessToken)
      })
  }

  render() {
    const { userId, email, createdAt } = this.state;
    return (
      <div className='mypageContainer'>
        <div className='title'>Mypage</div>
        <hr />
        <br />
        <br />
        <div>
          안녕하세요. <span className='name'>{userId ? userId : "Guest"}</span>님! jwt 로그인이
          완료되었습니다.
        </div>
        <br />
        <br />
        <div className='item'>
          <span className='item'>나의 이메일: </span> {email}
        </div>
        <div className='item'>
          <span className='item'>나의 아이디 생성일: </span> {createdAt}
        </div>
        <br />
        <br />
        <div className='btnContainer'>
          <button className='tokenBtn red' onClick={this.accessTokenRequest}>
            access token request
          </button>
          <button className='tokenBtn navy' onClick={this.refreshTokenRequest}>
            refresh token request
          </button>
        </div>
      </div>
    );
  }
}

export default Mypage;
```



***Copyright* © 2022 Song_Artish**