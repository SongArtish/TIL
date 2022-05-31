# Vue Lifecycle

---

[TOC]

---



## Overview

Vue Life Cycle Hook에는 `created` - `mounted` - `updated` - `destroyed`, 이 4가지가 있다. 숙련된 Vue 개발자가 되기 위해서는 Vue 인스턴스의 생애주기를 파악하고, 원하는 시점에 원하는 연산을 수행할 수 있도록 개발해야 한다.

- 공식 사이트: https://kr.vuejs.org/v2/guide/instance.html

![Vue Life Cycle](img/lifecycle.png)

```vue
export default {
    name: "HelloWorld",
    created: function () {
        console.log('created!')
    },
    mounted: function () {
        console.log('mounted!')
    },
    updated: function () {
        console.log('updated!')
    }
}
```



## Lifecycle

### Created

- **beforeCreate**: Vue 인스턴스가 생성되었지만, `data`의 변화와 이벤트에 대한 감시가 설정되기 전에 호출됨
- **created**: Vue 인스턴스가 생성되었고, `data` 관찰, `computed`, `methods`, `watch`가 설정이 완료되면 호출 됨

### Mounted

- **beforeMount**: DOM에서 마운트(결합, 부착)될 대상(`el` or `.@mount(대상)`)과 마운트되기 전에 호출됨
- **mounted**: DOM에서 마운트 될 대상과 마운트된 이후에 호출됨

### Updated

- **beforeUpdate**: `data`가 변경되고 난 이후, 실제 DOM이 다시 렌더링 되기 전에 호출됨
- **updated**: `data` 변경 이후, DOM이 다시 렌더링 되고 호출됨

### Destroyed

- **beforeDestroy**: Vue 인스턴스가 제거되지 전에 호출됨
- **destroyed**: Vue 인스턴스가 제거된 이후 호출됨



## <실습> API 가져오기

`created`를 통해 어플리케이션의 초기 데이터를 API 요청을 통해 불러올 수 있다.

```javascript
export default {
    data: function () {
        return {
            imgSrc: '',
        }
    },
    methods: {
        getImg: function () {
            axios.get(API_URL).then(response => {
                this.imgSrc = response.data.src
            })
        },
    },
    created: function () {	// Vue 인스턴스가 생성되면
        this.getImg()		// 이미지 데이터를 불러온다.
    },
}
```

```html
<template>
	<div id="app">
        <img v-if="imgSrc" :src="imgSrc"/>
        <p v-else>Image Loading..</p>
    </div>
</template>
```

예시 : 랜덤한 고양이 사진을 불러오는 코드를 작성한다.

```html
<div id="app">
    <h1>Cat Image</h1>
    <!-- <img v-if="imgUrl" :src="imgUrl" />
<p v-else>Image Loading..</p> -->
    <button @click="getImg">Get Cat</button>
    <hr>
    <img v-for="image in images" :src="image">
</div>

<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script>
    const app = new Vue ({
        el: "#app",
        data: {
            // imgUrl: ''
            images: [],
        },
        methods: {
            getImg: function () {
                // console.log(this)
                axios.get("https://api.thecatapi.com/v1/images/search")
                // 중첩되어 있는 function에서는 되도록이면 arrow function(=>)을 사용한다!!
                    .then(response => {
                    // console.log(this)
                    // this.imgUrl = response.data[0].url  // 데이터의 위치는 꼭 확인해주도록 한다!
                    this.images.push(response.data[0].url)
                })
            },
        },
        created: function () {	// Vue 인스턴스가 생성되면
            this.getImg()		// 이미지 데이터를 불러온다.
        },
    })

    // function (respose) {}를 하면 위 & 아래의 this가 다르다!!
    // 따라서 response => 를 사용한다.
</script>
```



***Copyright* © 2020 Song_Artish**

