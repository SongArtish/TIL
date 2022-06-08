

# Sequelize

---


[TOC]

---



## Overview

Sequelize is a promise-based, modern TypeScript and Node.js ORM for Postgres, MySQL, MariaDB, SQLite and SQL Server, and more.

- 공식 문서: https://sequelize.org/



## 사용법

### Install Dependencies

```bash
npm install sequelize sqlite3
# or
yarn add sequelize sqlite3
```

### Define Models

```javascript
import { Sequelize, Model, DataTypes } from 'sequelize';

const sequelize = new Sequelize('sqlite::memory:');
const User = sequelize.define('User', {
  username: DataTypes.STRING,
  birthday: DataTypes.DATE,
});
```

### Persist and Query

```javascript
const jane = await User.create({
  username: 'janedoe',
  birthday: new Date(1980, 6, 20),
});

const users = await User.findAll();
```

### Running Migrations

`migrations` 폴더 하위의 모든 모델 파일을 마이그레이션한다.

```shell
npx sequelize-cli db:migrate
```

모델 파일은 다음과 같이 작성된다.

```javascript
'use strict';
module.exports = {
  // Function up or down should return a Promise
  up: async (queryInterface, Sequelize) => {
    await queryInterface.createTable('Users', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER,
      },userId: {
        type: Sequelize.STRING,
        allowNull: false,
      },
      email: {
        type: Sequelize.STRING,
        allowNull: false,
      },
      password: {
        type: Sequelize.STRING,
        allowNull: false,
      },
      createdAt: {
        allowNull: false,
        type: Sequelize.DATE,
      },
      updatedAt: {
        allowNull: false,
        type: Sequelize.DATE,
      },
    });
  },
  down: async (queryInterface, Sequelize) => {
    await queryInterface.dropTable('Users');
  },
};
```

### Running Seeds

- [관련 문서](https://sequelize.org/docs/v6/other-topics/migrations/)

`seeders` 하위 폴더의 데이터를 추가한다.

```bash
npx sequelize-cli db:seed:all
```

시드 데이터는 다음과 같이 작성된다.

```javascript
'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    /**
     * 시쿼라이즈가 실행할 시드 명령어를 작성합니다..
     *
     * 예시:
     * await queryInterface.bulkInsert('People', [{
     *   name: 'John Doe',
     *   isBetaMember: false
     * }], {});
     */
    return queryInterface.bulkInsert('Users', [
      {
        id: '0',
        userId: 'kimcoding',
        password: '1234',
        email: 'kimcoding@authstates.com',
        createdAt: new Date(),
        updatedAt: new Date(),
      },
    ]);
  },

  down: async (queryInterface, Sequelize) => {
    /**
     * 시드를 취소하기 위한 명령어를 작성합니다.
     *
     * 예시:
     * await queryInterface.bulkDelete('People', null, {});
     */
    return queryInterface.bulkDelete('Users', null, {});
  },
};
```



## 예시 코드

```javascript
var Sequelize = require('sequelize')
var db = new Sequelize('chatter', 'root', '') // 연결을 만듬
// new Sequelize(DB명, 아이디, 비밀번호)

// db.define을 통해 schema를 작성
var User = db.define('User', {
    // id(pk), created_at, updated_at 등은 자동으로 생성됨
    username: Sequelize.STRING
})

var Message = db.define('Message', {
    userid: Sequelize.INTEGER,
    text: Sequelize.STRING,
    roomname: Sequelize.STRING
})

User.sync()
	.then(() => {
    // CREATE
    return User.create({username: 'Jean Valjean'})
	})
	.then(() => {
    // READ
    return User.findAll({ where: {username: 'Jean Valjean'} })
	})
	.then((users) => {
    users.forEach((user) => {
        console.log(user.username + ' exists')
    	})
    	db.close()
	})
	.catch((err) => {
    console.error(err)
    db.close()
	})
```



## Association

> [공식문서](https://sequelize.org/docs/v6/core-concepts/assocs/)

Sequelize supports the standard associations: [One-To-One](https://en.wikipedia.org/wiki/One-to-one_(data_model)), [One-To-Many](https://en.wikipedia.org/wiki/One-to-many_(data_model)) and [Many-To-Many](https://en.wikipedia.org/wiki/Many-to-many_(data_model)). To do this, Sequelize provides **four** types of associations that should be combined to create them:

- the `HasOne` association
- the `BelongsTo` association
- the `HasMany` association
- the `BelongsToMany` association

```javascript
// 예시
const A = sequelize.define('A', /* ... */);
const B = sequelize.define('B', /* ... */);

A.hasOne(B); // A HasOne B
A.belongsTo(B); // A BelongsTo B
A.hasMany(B); // A HasMany B
A.belongsToMany(B, { through: 'C' }); // A BelongsToMany B through the junction table C
```



## Transaction

> [공식문서](https://sequelize.org/docs/v6/other-topics/transactions/)

Sequelize does not use [transactions](https://en.wikipedia.org/wiki/Database_transaction) by default. However, for production-ready usage of Sequelize, you should definitely configure Sequelize to use transactions. Sequelize supports two ways of using transactions.

### Unmanaged Transactions

Committing and rolling back the transaction should be done manually by the user (by calling the appropriate Sequelize methods).

```javascript
// First, we start a transaction and save it into a variable
const t = await sequelize.transaction();

try {
  // Then, we do some calls passing this transaction as an option:
  const user = await User.create({
    firstName: 'Bart',
    lastName: 'Simpson'
  }, { transaction: t });

  await user.addSibling({
    firstName: 'Lisa',
    lastName: 'Simpson'
  }, { transaction: t });

  // If the execution reaches this line, no errors were thrown.
  // We commit the transaction.
  await t.commit();

} catch (error) {

  // If the execution reaches this line, an error was thrown.
  // We rollback the transaction.
  await t.rollback();

}
```

### Managed transactions

Sequelize will automatically rollback the transaction if any error is thrown, or commit the transaction otherwise. Also, if CLS (Continuation Local Storage) is enabled, all queries within the transaction callback will automatically receive the transaction object.

```javascript
try {

  const result = await sequelize.transaction(async (t) => {

    const user = await User.create({
      firstName: 'Abraham',
      lastName: 'Lincoln'
    }, { transaction: t });

    await user.setShooter({
      firstName: 'John',
      lastName: 'Boothe'
    }, { transaction: t });

    return user;

  });

  // If the execution reaches this line, the transaction has been committed successfully
  // `result` is whatever was returned from the transaction callback (the `user`, in this case)

} catch (error) {

  // If the execution reaches this line, an error occurred.
  // The transaction has already been rolled back automatically by Sequelize!

}
```



***Copyright* © 2022 Song_Artish**