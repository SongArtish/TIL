# Anaconda

> Python과 R 기반의 오픈소스 개발 플랫폼

2021.03.05

---

[TOC]

---



## 기본 명령어

- 아나콘다 버전 확인

```
conda --version
```

- 아나콘다 업데이트

```
conda update conda
```

- 아나콘다 가상환경 생성

```
conda create --name [가상환경 이름] [설치할 패키지]
```

```
ex) $ conda create --name env numpy
```

- 생성한 가상환경 리스트 확인

```
conda info --envs
```

- 가상환경 활성화

```
activate [가상환경 이름]
```

- 가상환경 비활성화

```
deactivate
```

- 패키지 설치

```
conda install [패키지 이름]
```

-  패키지 리스트 확인

```
conda list
```

- 패키지 삭제

```
conda remove --name [가상환경 이름] --all
```

- 아나콘다 캐시 삭제

```
conda clean --all
```



## <참고> cmd에서 conda 명령어 실행하기

cmd에서 conda 명령어를 실행하기 위해서 **환경변수**에 들어가서 `시스템 변수`와 `사용자 변수`의 **PATH**에 아래의 3가지 경로를 추가해준다.

```
C:\ProgramData\Anaconda3
C:\ProgramData\Anaconda3\Library\bin
C:\ProgramData\Anaconda3\Scripts
```

- :white_check_mark: 앞 부분의 경로는 Anaconda 설치 경로에 따라서 상이할 수 있다.



***Copyright* 2021 © Song_Artish**