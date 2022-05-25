# Fetch

---

[TOC]

---



## Overview

비동기 요청의 가장 대표적인 사례는 **네트워크 요청**이며, 여기서는 fetch를 이용한 네트워크 요청에 대해서 다룬다.



## 사용법

```javascript
import fetch from 'node-fetch'

let url = "<url주소>"
fetch(url)
	.then((response) => response.json())
	.then((result) => console.log(result))
	.catch((error) => throw Error(err))
```



***Copyright* © 2022 Song_Artish**
