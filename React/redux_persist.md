# redux-persist

---

[TOC]

---



## Overview

redux store의 데이터는 새로고침하면 사라진다. 이를 해결하기 위해 `redux-persist`를 사용할 수 있다.

## 사용하기

1. `redux-persist`를 설치한다.
  ```bash
  npm install redux-persist
  ```
2. `index.js`를 수정한다.
  ```javascript
  ...
  import persistedReducer from './_reducers';	// 추가
  import { persistStore } from 'redux-persist';	// 추가
  import { PersistGate } from 'redux-persist/integration/react';	// 추가

  import store from './redux/store';  // redux

  const persistor = persistStore(store)	// 추가

  root.render(
    <Provider store={store}>
      <PersistGate persistor={persistor}>	// 추가
        <BrowserRouter>
          <App />
        </BrowserRouter>
      </PersistGate>
    </Provider>,
  );
  ```
3. redux 폴더에 정의된 `store.js`를 수정한다.
  ```javascript
  // redux/store.js
  ...
  import persistedReducer from '.';   // redux-persist

  ...
  const store = createStore(persistedReducer, composeEnhancers(applyMiddleware(thunk)));  // rootReducer를 persistedReducer로 변경
  ...
  ```
4. redux 폴더에서 rootReducer가 정의된 `index.js`를 수정한다.
  ```javascript
  // redux/index.js
  ...
  import { persistReducer } from 'redux-persist';	// redux-persist
  import storage from 'redux-persist/lib/storage';	// redux-persist

  const persistConfig = {
    key: 'root',
    storage,
  }	// redux-persist

  const rootReducer = combineReducers({
    accountReducer
  });

  const persistedReducer = persistReducer(persistConfig, rootReducer);	// redux-persist

  export default persistedReducer;  // redux-persist
  ```

  여기서, 저장하고 싶은 위치에 따라 다르게 import 해주어야 한다.
  ```javascript
  import storage from 'redux-persist/lib/storage' // localstorage에 저장하고 싶은 경우
  import storageSession from 'redux-persist/lib/storage/session // sessionstorage에 저장하고 싶은 경우
  ```



***Copyright* © 2022 Song_Artish**