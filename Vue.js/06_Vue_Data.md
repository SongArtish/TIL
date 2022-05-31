# Vue Data

---

[TOC]

---



## Overview

데이터 단방향 흐름

- 상위 컴포넌트에서 하위 컴포넌트로 흐른다. (Pass Props)
- 하위 컴포넌트는 이벤트로 상위 컴포넌트에게 데이터를 전달할 수 있다. (Emit Events)

![Pass Props & Emit Events](img/pass_props&emit_events.png)



## Props

**1. 넘겨준다**

상위 컴포넌트에서는 가져온 태그에서 데이터를 바인딩하여 넘겨준다.

```vue
<<하위 컴포넌트 이름> :<넘겨줄 데이터 이름>="<데이터 이름>">
```

예시

```vue
<Child :appData="appData"/>
```

**2. 받아준다**

props로 상위 컴포넌트의 데이터를 받을 때는, 데이터 형을 지정해준다.

```javascript
props: {
    <넘겨받은 데이터 이름>: <데이터 형태>
}
```

예시

```vue
props: {
    appData: String,
	app: {
	type: Object
	}
  },
```



## Emit

```vue
this.$emit('<이벤트>', <데이터>)
```

1. 올려준다

input 태그에 `v-on`으로 이벤트를 달아준다.

```vue
<<이벤트 대상 태그> @<이벤트>="<이벤트 함수>">
```

```vue
<input type="text" v-model="childData" @input="onInput">
```

- 이벤트가 발생하면 `emit`하도록 함수를 작성한다.

```javascript
methods: {
    onInput: function () {
      this.$emit('child-input', event.target.value)
      // this.$emit('<올려줄 이벤트 이름>', <올려줄 데이터>)
    }
```

2. 받아준다

`v-on`으로 넘겨받은 이벤트에 새로운 이벤트를 연결한다.

```vue
<<하위 컴포넌트 태그> @<올려받은 이벤트 이름>="<정의할 이벤트 함수>">
```

```vue
<Child :appData="appData" :parentData="parentData" @child-input="onChildInput" />
```

해당 이벤트 함수를 작성한다. 해당 내용을 `text`라는 변수로 받아온다.

```javascript
methods: {
    onChildInput: function (text) {
        this.childData = text
        this.$emit('child-input', text) // text = this.childData
    }
}
```



***Copyright* © 2020 Song_Artish**

