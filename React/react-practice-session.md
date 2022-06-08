# <실습> React에서 Session 사용하기

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
const express = require('express');
const cors = require('cors');
const session = require('express-session');
const logger = require('morgan');
const fs = require('fs');
const https = require('https');
const usersRouter = require('./routes/user');

const app = express();
const PORT = process.env.PORT || 4000;

// TODO: express-session 라이브러리를 이용해 쿠키 설정을 해줄 수 있습니다.
app.use(
  session({
    secret: '@codestates',
    resave: false,
    saveUninitialized: true,
    cookie: {
      domain: "localhost",
      path: "/",
      maxAge: 24 * 6 * 60 * 10000,
      sameSite: "none",
      httpOnly: true,
      secure: true,
    },
  })
);
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// TODO: CORS 설정이 필요합니다. 클라이언트가 어떤 origin인지에 따라 달리 설정할 수 있습니다.
// 메서드는 GET, POST, OPTIONS를 허용합니다.
app.use(cors({
  origin: 'https://localhost:3000',
  methods: ['GET', 'POST', 'OPTIONS'],
  credentials: true,
}));
/**
 * /users 요청에 대해서 라우터를 이용하기 때문에,
 * 반드시 아래와 같은 주소와 메서드로 요청을 보내야 합니다.
 *
 * POST https://localhost:4000/users/login,
 * POST https://localhost:4000/users/logout,
 * GET https://localhost:4000/users/userinfo
 */
app.use('/users', usersRouter);

let server;

// 인증서 파일들이 존재하는 경우에만 https 프로토콜을 사용하는 서버를 실행합니다.
// 만약 인증서 파일이 존재하지 않는경우, http 프로토콜을 사용하는 서버를 실행합니다.
// 파일 존재여부를 확인하는 폴더는 서버 폴더의 package.json이 위치한 곳입니다.
if (fs.existsSync("./key.pem") && fs.existsSync("./cert.pem")) {
  server = https
    .createServer(
      {
        key: fs.readFileSync(__dirname + `/` + 'key.pem', 'utf-8'),
        cert: fs.readFileSync(__dirname + `/` + 'cert.pem', 'utf-8'),
      },
      app
    )
    .listen(PORT);
} else {
  server = app.listen(PORT)
}
module.exports = server;
```

### routes/user.js

```javascript
var express = require('express');
var router = express.Router();

const { usersController } = require('../controller');

// * POST /users/login
router.post('/login', usersController.login.post);

// * POST /users/logout
router.post('/logout', usersController.logout.post);

// * get /users/userinfo
router.get('/userinfo', usersController.userinfo.get);

module.exports = router;
```

### controller/inex.js

```javascript
module.exports = {
  usersController: require('./users'),
};
```

### controller/users/index.js

```javascript
module.exports = {
  login: require('./login'),
  logout: require('./logout'),
  userinfo: require('./userinfo'),
};
```

### controller/users/login.js

```javascript
// 해당 모델의 인스턴스를 models/index.js에서 가져옵니다.
const { Users } = require('../../models');

module.exports = {
  post: async (req, res) => {
    // userInfo는 유저정보가 데이터베이스에 존재하고, 완벽히 일치하는 경우에만 데이터가 존재합니다.
    // 만약 userInfo가 NULL 혹은 빈 객체라면 전달받은 유저정보가 데이터베이스에 존재하는지 확인해 보세요
    const userInfo = await Users.findOne({
      where: { userId: req.body.userId, password: req.body.password },
    });
    // TODO: userInfo 결과 존재 여부에 따라 응답을 구현하세요.
    // 결과가 존재하는 경우 세션 객체에 userId가 저장되어야 합니다.
    let result = userInfo
    if (!result) {
      // your code here
      res.status(404).send({message: "not authorized"})
    } else {
      // your code here
      // HINT: req.session을 사용하세요.
      req.session.save(() => {
        req.session.userId = userInfo.userId
        res.json({data: userInfo, message: "ok"})
      })
    }
  }
}
```

### controller/users/logout.js

```javascript
module.exports = {
  post: (req, res) => {

    // TODO: 세션 아이디를 통해 고유한 세션 객체에 접근할 수 있습니다.
    // 앞서 로그인시 세션 객체에 저장했던 값이 존재할 경우, 이미 로그인한 상태로 판단할 수 있습니다.
    // 세션 객체에 담긴 값의 존재 여부에 따라 응답을 구현하세요.

    if (!req.session.userId) {
      // your code here
      res.status(400).send({message: "not authorized"})
    } else {
      // your code here
      // TODO: 로그아웃 요청은 세션을 삭제하는 과정을 포함해야 합니다.
      res.status(200).send()
      req.session.user = null
    }
  },
};
```

### controller/users/userinfor.js

```javascript
const { Users } = require('../../models');

module.exports = {
  get: async (req, res) => {

    // TODO: 세션 객체에 담긴 값의 존재 여부에 따라 응답을 구현하세요.
    // HINT: 세션 객체에 담긴 정보가 궁금하다면 req.session을 콘솔로 출력해보세요

    if (!req.session.userId) {
      // your code here
      res.status(400).send({message: "not authorized"})
    } else {
      // your code here
      // TODO: 데이터베이스에서 로그인한 사용자의 정보를 조회한 후 응답합니다.
      const userInfo = await Users.findOne({
        where: { userId: req.session.userId }
      })
      res.status(200).json({data: userInfo, message: "ok"})
    }
  },
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
  /**
   * 해당 파일은 시퀄라이즈 ORM이 데이터베이스 쿼리를 진행하기 위해
   * 해당되는 테이블의 이름 및 어트리뷰트의 특성을 지정하는 파일입니다.
   * 또한 아래 associate 부분을 통해서 다른 테이블과의 관계를 작성할수 있습니다.
   * 
   * 이 파일은 서버가 실행되면 시퀄라이즈가 해당 내용을 바탕으로 findOne, findAll과 같은 함수를
   * 사용할수 있게끔 준비를 합니다.
   */
  class Users extends Model {

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
const dotenv = require('dotenv');
dotenv.config();

module.exports = {
  development: {
    username: 'root',
    password: process.env.DATABASE_PASSWORD,
    database: 'authentication',
    host: '127.0.0.1',
    dialect: 'mysql',
    logging: false
  },
  test: {
    username: 'root',
    password: process.env.DATABASE_PASSWORD,
    database: 'authentication',
    host: '127.0.0.1',
    dialect: 'mysql',
  },
  production: {
    username: 'root',
    password: process.env.DATABASE_PASSWORD,
    database: 'authentication',
    host: '127.0.0.1',
    dialect: 'mysql',
  },
};
```



## React 클라이언트 구현하기

### App.js

```react
import React, { Component } from 'react';

import Login from './components/Login';
import Mypage from './components/Mypage';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isLogin: false,
      userData: null,
    };
    this.loginHandler = this.loginHandler.bind(this);
    this.logoutHandler = this.logoutHandler.bind(this);
    this.setUserInfo = this.setUserInfo.bind(this);
  }

  loginHandler() {
    this.setState({
      isLogin: true,
    });
  }

  setUserInfo(object) {
    this.setState({ userData: object });
  }

  logoutHandler() {
    this.setState({
      isLogin: false,
    });
  }

  render() {
    const { isLogin } = this.state;
    return (
      <div className='App'>
        {isLogin ? (
          <Mypage
            logoutHandler={this.logoutHandler}
            userData={this.state.userData}
          />
        ) : (
            <Login
              loginHandler={this.loginHandler}
              setUserInfo={this.setUserInfo}
            />
          )}
      </div>
    );
  }
}

export default App;
```

### components/Login.js

```react
import React, { Component } from 'react';
import axios from "axios";

class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      password: '',
    };
    this.inputHandler = this.inputHandler.bind(this);
    this.loginRequestHandler = this.loginRequestHandler.bind(this);
  }

  inputHandler(e) {
    this.setState({ [e.target.name]: e.target.value });
  }

  loginRequestHandler() {
    // TODO: 로그인 요청을 보내세요.
    //
    // 로그인에 성공하면
    // - props로 전달받은 함수를 호출해, 로그인 상태를 변경하세요.
    // - GET /users/userinfo 를 통해 사용자 정보를 요청하세요
    //
    // 사용자 정보를 받아온 후
    // - props로 전달받은 함수를 호출해, 사용자 정보를 변경하세요.
    let params = JSON.stringify({
      userId: this.state.username,
      password: this.state.password
    })
    axios({
      url: "https://localhost:4000/users/login", // 통신할 웹문서
      method: "post", // 통신할 방식
      data: params
    })
      .then(() => {
        this.props.loginHandler()
        axios.get('https://localhost:4000/users/userinfo')
          .then((res) => {
            this.props.setUserInfo(res.data.data)
          })
      })
  }

  render() {
    return (
      <div className='loginContainer'>
        <div className='inputField'>
          <div>Username</div>
          <input
            name='username'
            onChange={(e) => this.inputHandler(e)}
            value={this.state.username}
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
        <div className='passwordField'>
          <button onClick={this.loginRequestHandler} className='loginBtn'>
            Login
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
import React from 'react';
import axios from "axios";

function Mypage(props) {
  const handleLogout = () => {
    // TODO: 서버에 로그아웃 요청을 보낸다음 요청이 성공하면 props.logoutHandler를 호출하여 로그인 상태를 업데이트 해야 합니다.
    axios
    .post("https://localhost:4000/users/logout", {
      withCredentials: true,
    })
      .then(() => {
        props.logoutHandler()
      })
  };
  return props.userData == null ? (
    <div>Loading...</div>
  ) : (
      <div>
        <div className='mypageContainer'>
          <div>
            <span className='title'>Mypage</span>
            <button className='logoutBtn' onClick={handleLogout}>
              logout
            </button>
          </div>
          <hr />

          <div>
            안녕하세요. <span className='name'>{props.userData.userId}</span>님! 로그인이 완료되었습니다.
          </div>
          <br />
          <div className='item'>
            나의 유저 네임: {props.userData.userId}
          </div>
          <div className='item'>
            나의 이메일 주소: {props.userData.email}
          </div>
        </div>
      </div>
    );
}

export default Mypage;
```



***Copyright* © 2022 Song_Artish**