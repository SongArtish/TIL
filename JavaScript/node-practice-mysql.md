# <실습> Node.js에서 MySQL 사용하기

---

[TOC]

---



## Overview

Node.js 서버에서 MySQL을 데이터베이스로 연결하여 사용해본다. 서버는 `Express.js`를 사용하였으며, 클라이언트는 react 프로젝트로 진행하였다. 이와 관련된 개념적인 내용은 [Node_MySQL TIL](./56_Node_MySQL.md)을 참고한다.

MySQL 데이터베이스를 Node.js 서버에 연결할 경우, 작동 원리는 대략적으로 다음과 같다.

1. URL을 통해 요청을 한다.
2. Router를 통해서 해당 URL에 해당하는 controller로 연결한다.
3. Controller에서 DB 요청이 필요한 경우 model로 연결한다.
4. 모델에서 DB 서버에 연결(`db > index.js` 파일을 통해)하여 특정 query문을 수행한다.
5. DB 서버의 작업이 완료되면, 모델에서 Controller로부터 받은 callback함수를 실행한다.
6. Controller에서는 callback 함수가 실행되며, 이 때 응답에 대한 status 및 결과를 보내준다.



## 시작하기

본격적으로 시작하기 앞서 필요한 패키지가 모두 설치가 되어 있는지 확인한다. 대표적인 패키지는 다음과 같다.

- cors
- dotenv
- express
- mysql
- nodemon



## 서버 폴더구조

서버의 폴더 구조는 다음과 같다. 관심사 분리 원칙을 적용하여 각각의 구별된 부분을 폴더로 구분한다.

```javascript
// server의 폴더 구조
ㄴ config
	ㄴ config.js	// DB 접속 정보에 대해 정의
ㄴ controllers
	ㄴ index.js	// url을 통해 요청된 데이터를 처리
ㄴ db
	ㄴ index.js	// mysql DB 접속에 대한 내용 정의
ㄴ models
	ㄴ index.js	// 모델에 대한 정의: url을 통해 요청하면 적합한 query문을 DB에 던져줌
ㄴ node_modules
	ㄴ ...
ㄴ routes
	ㄴ index.js	// url endpoint에 따라 적절한 router로 연결해줌
	ㄴ items.js	// 세부 router (item router)
	ㄴ users.js	// 세부 router (user router)
.env	// 환경 변수
app.js
package-lock.json
package.json
schema.sql	// 데이터베이스 스키마를 정의한 파일
seed.sql	// 데이터베이스 내에 넣어줄 데이터
```



## DB 생성하기

MySQL로 접속하여 DB를 생성해준다. MySQL은 CLI로 접속한다.

```bash
$ mysql -u root -p
# 명령어 입력 후 패스워드 입력
```

mysql 서버에 접속하면 `cmarket`이라는 DB를 생성해준다.

```sql
CREATE DATABASE cmarket;
SHOW DATABASES;
```

### 스키마 파일을 사용하여 테이블 생성하기

`.sql` 파일에서 정의된 스키마를 사용하여 테이블을 생성한다. `schema.sql` 파일에는 다음과 같이 테이블 생성문이 정의되어 있다.

```sql
# schema.sql
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username varchar(255),
  PRIMARY KEY (id)
);

CREATE TABLE orders (
  id INT AUTO_INCREMENT,
  user_id INT,
  total_price INT,
  created_at datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

CREATE TABLE order_items (
  id INT AUTO_INCREMENT,
  order_id INT,
  item_id INT,
  order_quantity INT,
  PRIMARY KEY (id)
);

ALTER TABLE orders ADD FOREIGN KEY (user_id) REFERENCES users (id);

ALTER TABLE order_items ADD FOREIGN KEY (order_id) REFERENCES orders (id);

ALTER TABLE order_items ADD FOREIGN KEY (item_id) REFERENCES items (id);

/*  Execute this file from the command line by typing:
 *    mysql -u root < server/schema.sql -p -Dcmarket
 *  to create the database and the tables.*/
```

아래 명령어를 사용하여 테이블을 생성한다.

```bash
mysql -u root < server/schema.sql -p -Dcmarket
# server 하위 폴더의 schema.sql 파일을 지정한다.
# -D[데이터베이스명] 형식이다.
```

### DB에 시드 데이터 추가하기

`seed.sql` 파일에 정의된 시드 데이터는 다음과 같이 SQL 문으로 작성되어 있다.

```sql
# seed.sql
INSERT INTO items (name, price, image) VALUES ("노른자 분리기", 9900, "../images/egg.png"), ("2020년 달력", 12000, "../images/2020.jpg"), ("개구리 안대", 2900, "../images/frog.jpg"), ("뜯어온 보도블럭", 4900, "../images/block.jpg"), ("칼라 립스틱", 2900, "../images/lip.jpg"), ("잉어 슈즈", 3900, "../images/fish.jpg"), ("웰컴 매트", 6900, "../images/welcome.jpg"), ("강시 모자", 9900, "../images/hat.jpg");
INSERT INTO users (username) VALUES ("김코딩")

/*  Execute this file from the command line by typing:
 *    mysql -u root < server/seed.sql -p -Dcmarket
 *  to create the database and the tables.*/
```

아래 명령어를 사용하여 테이블에 데이터를 추가한다.

```bash
mysql -u root < server/seed.sql -p -Dcmarket
# server 하위 폴더의 seed.sql 파일을 지정한다.
# -D[데이터베이스명] 형식이다.
```



## 서버 구축하기

DB 서버를 구축한다.

### 서버 정보 만들기

`config.js` 파일에서 DB 서버에 대한 정보를 정의한다. `dotenv` 패키지를 사용하여 필요한 환경 변수를 가져온다.

```javascript
// config/config.js
const dotenv = require('dotenv');
dotenv.config();

// 여기서는 테스트로 사용할 config를 구분하기 위해, development와 test 2가지로 정의하였다.
const config = {
  development: {
    host: 'localhost',
    user: 'root',
    password: process.env.DATABASE_SPRINT_PASSWORD,
    database: 'cmarket'
  },
  test: {
    host: 'localhost',
    user: 'root',
    password: process.env.DATABASE_SPRINT_PASSWORD,
    database: 'cmarket_test'
  }
};

module.exports = config;
```

### 환경 변수 만들기

환경 변수 파일 `.env`를 생성해 비밀번호 등 필요한 환경 변수를 선언한다.

```
// .env
DATABASE_SPRINT_PASSWORD=MySQL비밀번호
```

### DB 서버 연결하기

`db > index.js` 파일에서 mysql 모듈을 불러와 DB 서버에 연결한다.

```javascript
// db/index.js
const mysql = require('mysql2');
// 원래는 mysql이지만, 특정 오류를 해결하기 위해 여기서는 mysql2를 사용하였다.
const dotenv = require('dotenv');
const config = require('../config/config');
dotenv.config();

const con = mysql.createConnection(
  config[process.env.NODE_ENV || 'development']
);

con.connect((err) => {
  if (err) throw err;
});

module.exports = con;
```



## Router 만들기

서버는 `Express.js`를 사용하였다. url을 통해서 받은 요청을 처리할 router를 만들어 준다. 

```java
// routes/index.js

const express = require('express');
const router = express.Router();
const itemsRouter = require('./items');
const usersRouter = require('./users');

// endpoint에 따라 적절히 router를 연결하였다.
router.use('/items', itemsRouter);
router.use('/users', usersRouter);

module.exports = router;
```

각 endpoint에 따라 세부 router로 정의한다.

```javascript
// routes/items.js
const router = require('express').Router();
const controller = require('./../controllers');

// GET /items Router와 Controller를 연결합니다.
router.get('/', controller.items.get);

module.exports = router;
```

```javascript
// routes/users.js
const router = require('express').Router();
const controller = require('../controllers');

// GET /items Router와 Controller를 연결합니다.
router.get('/:userId/orders', controller.orders.get);
router.post('/:userId/orders', controller.orders.post);

module.exports = router;
```



## DB 요청 모델 생성하기

마지막으로 url을 통해서 요청된 내용이 DB에 전달될 수 있도록 모델을 만들어준다. 여기서 DB에 요청될 때까지의 과정은 다음과 같다.

1. URL을 통해 요청을 한다.
2. Router를 통해서 해당 URL에 해당하는 controller로 연결한다.
3. Controller에서 DB 요청이 필요한 경우 model로 연결한다.
4. 모델에서 DB 서버에 연결(`db > index.js` 파일을 통해)하여 특정 query문을 수행한다.
5. DB 서버의 작업이 완료되면, 모델에서 Controller로부터 받은 callback함수를 실행한다.
6. Controller에서는 callback 함수가 실행되며, 이 때 응답에 대한 status 및 결과를 보내준다.

```javascript
// models/index.js
const db = require('../db');	// db 파일에 정의된 서버와 통신하기 위해

module.exports = {
  items: {
    get: (callback) => {
      // TODO: Cmarket의 모든 상품을 가져오는 함수를 작성하세요
      const queryString = `SELECT * FROM items`;

      db.query(queryString, (error, result) => {
        callback(error, result);
      });
    },
  },
  orders: {
    get: (userId, callback) => {
      // TODO: 해당 유저가 작성한 모든 주문을 가져오는 함수를 작성하세요
      // const queryString = `SELECT * FROM orders WHERE orders.user_id = ${userId}`
      const queryString = `SELECT orders.id, name, image, price, total_price, order_quantity, created_at
      FROM orders
      LEFT JOIN users
      ON users.id = orders.user_id
      LEFT JOIN order_items
      ON orders.id = order_items.order_id
      LEFT JOIN items
      ON items.id = order_items.item_id
      WHERE users.id = ${userId}`;
      
      db.query(queryString, (err, result) => {
        callback(err, result);
      });
      // callback(/* err, result */);
    },
    post: (userId, orders, totalPrice, callback) => {
      // TODO: 해당 유저의 주문 요청을 데이터베이스에 생성하는 함수를 작성하세요
      const queryString = `INSERT INTO orders (user_id, total_price) VALUES ?`
      console.log(queryString);
      const params = [[userId, totalPrice]];
      
      db.query(queryString, [params], (err, result) => {
        if(result){
          const queryString2 = `INSERT INTO order_items (order_id, item_id, order_quantity) VALUES ?`;
          const params2 = orders.map(el => {
            return [result.insertId, el.itemId, el.quantity];
          });
          db.query(queryString2, [params2], (err, result)=>{
            callback(err, result);
          })
        }
        else{        
          callback(err, result)
        }
      });
      // callback(/* err, result */);
    }
  },
};
```



## 클라이언트에서 호출하기

클라이언트에서는 `fetch`를 사용하여 url로 DB에 요청할 수 있다.

```javascript
// client/src/pages/OrderList.js

import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchData, setOrders } from '../actions';	// actions.js에서 fetch를 활용해 정의한 사용자정의 함수

export default function OrderList () {
  const userId = 1;
  const state = useSelector((state) => state.itemReducer);
  const dispatch = useDispatch();
  const { orders } = state;

  useEffect(() => {
    dispatch(
        // url을 통해 요청을 보낸다.
      fetchData(`http://localhost:4000/users/${userId}/orders`, setOrders)
    );
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
```



***Copyright* © 2022 Song_Artish**