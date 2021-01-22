# Kakao 지도 API

2021.01.22

> Web용 Javascript API를 가져온다. 연습에서는 Vue 프레임워크를 사용하였다.  [카카오 지도 API 사이트](https://apis.map.kakao.com/web/guide/)

---

[TOC]

---



## 준비하기

### API 키 발급

1. [카카오 개발자 사이트](https://developers.kakao.com) 접속
2. 개발자 등록 및 앱 생성
3. 웹 플랫폼 추가
   - `앱 선택 > 플랫폼 > Web 플랫폼 등록 > 사이트 도메인 등록`
4. 사이트 도메인 등록
   - `웹` 플랫폼 선택하고, `사이트 도메인` 등록 (예: http://localhost:8080)
5. 페이지 상단 `JavaScript 키`를 지도 API의 앱 키로 사용
   - :ballot_box_with_check: API 앱 키를 `.env.local` 파일에서 환경변수로 관리하여 사용하였다.
6. 앱 실행



## 시작하기

> Vue에서는 API를 호출할 때, 사이트에서 소개하는 것과는 다른 방법으로 가져와야 한다!
>
> [이 사이트](https://velog.io/@sdsdsrd/Vue.js%EC%97%90%EC%84%9C-%EC%B9%B4%EC%B9%B4%EC%98%A4%EB%A7%B5API-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)를 참고한다.

### 패키지 추가

:heavy_exclamation_mark: 이걸 추가해도 되고 Vue 컴포넌트에서 처리해도 된다!!

- Vue에서 `package.json`에 아래의 코드를 추가해준다.
- :ballot_box_with_check: 기존에 `eslintConfig`가 존재한다면, 그 안에 아이템만 넣어준다!

```json
"eslintConfig": {
  "globals": {
    "kakao": false
  }
}
```



### 지도 영역 만들기

- 지도를 담을 영역을 `<div>` 태그로 선언한다.

```html
<div id="map" style="width:500px;height:400px;"></div>
```

- `500x400` 의 크기로 선언했다.

- `<div` 태그의 id값은 `map`으로 정의하였다.

- 아래와 같이 입력할 수도 있다.

  ```vue
  <style>
  #map {
    width: 500px;
    height: 400px;
  }
  </style>
  ```

  

### API 호출하기

> 아래와 같이 `API를 로딩하는 스크립트 태그`를 입력한다.
>
> - :white_check_mark: `head`, `body` 등 넣는 위치는 상관 없으나, 반드시 **실행 코드보다 먼저 선언되어야 한다** !!
>
> ```javascript
> <script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=발급받은 APP KEY를 넣으시면 됩니다."></script>
> ```
>
> - :ballot_box_with_check: `//(상대 프로토콜)`을 사용하면, 사용자의 `http`, `https` 환경에 따라 자동으로 해당 프로토콜을 따라가게 된다.

Vue에서는 아래와 같이 코드를 입력한다.

```javascript
// Location.vue (지도를 입력할 component)
  mounted() {
    if (window.kakao && window.kakao.maps) {
      this.initMap()
    } else {
      const script = document.createElement('script'); /* global kakao */
      script.onload = () => kakao.maps.load(this.initMap()); 
      script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${MAP_API_KEY}`;
      document.head.appendChild(script)
    }
  },
```

- `MAP_API_KEY`는 `.env.local`에서 환경변수로 관리하기 때문에 가져와 준다.

  ```javascript
  const MAP_API_KEY = process.env.MAP_API_KEY
  ```



### 지도 표시하기

- :ballot_box_with_check: `options > center` 속성은 지도를 생성하는데 반드시 필요하다!!
  - `center`에 할당할 값은 `LatLng` 클래스를 사용하여 생성하는데, 위/경도 좌표라고 부르는 `WGS84` 좌표계의 좌표값을 넣어서 만든다. - 위도(Lat), 경도(Lng) 순으로 넣어준다.

```javascript
  methods: {
    initMap() {
       var container = document.getElementById('map')
       var options = { center: new kakao.maps.LatLng(33.450701, 126.570667), level: 3 }
       var map = new kakao.maps.Map(container, options) 
       //마커추가하려면 객체를 아래와 같이 하나 만든다. 
       var marker = new kakao.maps.Marker({ position: map.getCenter() })
       marker.setMap(map); 
       }, 
  }
```



***Copyright* © 2021 Song_Artish**