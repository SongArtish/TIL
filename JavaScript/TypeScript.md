# TypeScript

---

[TOC]

---

## Overview
> What is **TypeScript**?
- a superset of JavaScript
- makes language predictable and code more easy to read



## Setup

1. Create `package.json`

   ```bash
   npm init -y
   ```

2. Install TypeScript 📌

   ```bash
   npm i -g typescript
   ```

   - check versions

     ```bash
     tsc -v
     ```

3. Create `tsconfig.json` file

   - tell TypeScript how to compile the JS.

     ```json
     {
         "compilerOptions": {
             "module": "commonjs",
             "target": "ES2015",
             "sourceMap": true
         },
         "include": ["index.ts"],
         "exclude": ["node_modules"]
     }
     ```

4. Create `index.ts` file

   ```typescript
   // sample code
   console.log("hello");
   ```

5. Compile `index.ts` to `index.js`

   ```bash
   tsc
   ```

   - this command creates `index.js` and `index.js.map` files.

6. Add shortcut command

   - add shortcut command in `scripts` part of `package.json` file.

     ```json
       "scripts": {
         ...
         "start": "node indesx.js"
       },
     ```

     - `npm start` command will compile `index.js`
     - execute TypeScript before start

     ```json
       "scripts": {
           ...
         "prestart": "tsc"
       },
     ```

7. Start with shortcut

   ```bash
   npm start
   ```

   - this will show print `hello` on the terminal



## First Steps

> Typed language

1. Create sample codes on `index.ts`
```typescript
const name = "Songyoung",
    age = 27,
    gender = "male";

const sayHi = (name, age, gender) => {
    console.log(`Hello ${name}, you are ${age}, and you are a ${gender}.`);
}

sayHi(name, age, gender);

// make this function as a module
export {};
```

2. Run the code
```bash
npm start
// or
yarn start
```

3. Set a argument as optional
> Use `?` behind the argument.
```ts
const sayHi = name, age, gender?) => {
  ...
}
```
- it prints `gender` as `undefined`.



## Types
> VS Code에서 `TSLint`라는 확장 프로그램을 설치하면 TS 코드를 더욱 편리하게 확인할 수 있다!
- `string`
- `number`
- `void`: empty data

```ts
const sayHi = (name:string, age:number, gender?:string) => {
   ...
}
```
- `console.log` does not return anything,and in this case, you can specify by using `void` 

```ts
const sayHi = (name:string, age:number, gender?:string): void => {
    console.log(`Hello ${name}, you are ${age}, and you are a ${gender}.`);
}
```
- Below case returns the string value.

```ts
const sayHi = (name:string, age:number, gender?:string): string => {
    return `Hello ${name}, you are ${age}, and you are a ${gender}.`;
}
```


## Compile 방식 변경

1. `src`, `dist` 폴더 생성
   - src(source) 폴더에는 컴파일 대상이 되는 파일(ts)들 관리
   - dist(distribution) 폴더에는 컴파일된 파일(js)들 관리
2. Compile 옵션 변경

   - `tsconfig.json` 폴더에서 compile 옵션 변경

     ```json
       // compile everyting in src
       "include": ["src/**/*"],
     ```

     ```json
         "compilerOptions": {
           ...
           // compiled output will be saved in dist folder
           "outDir": "dist"
         },
     ```

3. `tsc-watch` 패키지 설치하기

   - `tsc-watch`를 이용하면 변경이 있을 때마다 자동으로 compile을 진행할 수 있음

     ```bash
     npm i tsc-watch
     ```

4. `package.json`에서 start 명령어 작동 방식 변경

```json
  "scripts": {
    ...
    "start": "tsc-watch --onSuccess \" node dist/index.js\" ",
  },
```


## Interface

- TS에서 Interface를 이용하면 Object를 선언하여 사용할 수 있다.
```json
// Human이라는 interface(object) 선언
interface Human {
    name: string;
    age: number;
    gender: string;
}

// person 변수 선언
const person = {
    name: "Songyoung",
    age: 27,
    gender: "male"
}

// 함수가 Human object인 임의의 person 변수를 argument로 받음
const sayHi = (person: Human): string => {
    return `Hello ${person.name}, you are ${person.age}, and you are a ${person.gender}.`;
}

// 출력
console.log(sayHi(person));
```

- ⚠️ Interface는 js로 컴파일 되지 않음! 따라서 `class`를 사용
- 단, Interface는 ts 측면에서 조금 더 안전함



## Class

```ts
class Human {
    public name: string;
    public age: number;
    public gender: string;
    // class가 시작될 때마다 호출되는 method
    constructor(name: string, age: number, gender?: string) {
        this.name = name;
        this.age = age;
        this.gender = gender;
    }
}

const lynn = new Human("Lynn", 18, "female")

const sayHi = (person: Human): string => {
    return `Hello ${person.name}, you are ${person.age}, and you are a ${person.gender}.`;
}

console.log(sayHi(lynn));

// make this function as a module
export {};
```

- class는 compile된 `js` 파일에도 표시되는 것을 확인할 수 있다.
- react, express, node 등에서는 class를 사용해야 함



***Copyright* © 2022 Song_Artish**
