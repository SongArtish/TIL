# Python 통합개발환경구축 (Conda+PyCharm)

2020.07.24.



[TOC]



## 1. Anaconda(Miniconda) 설치



## 2. conda 가상 환경 생성 & 모듈 설치

```
# cmd에서 실행

# 설치된 폴더로 이동
$ cd C:\Program Files\Miniconda3\condabin

# 아나콘다 버전 확인
$ conda --v
conda 4.8.3

# 아나콘다 최신버전 업그레이드
$ conda update conda

# 가상환경 구축 (python 버전: 3.7.7, 가상환경 이름: my_env)
$ conda create -n my_env anaconda python=3.7.7

# 가상환경 활성화
$ conda activate my_env

# 해당 가상환경에서 필요한 모듈 설치 (예시: tensorflow모듈 설치)
(my_env)$ conda install tensorflow

# 가상환경 종료
$ conda deactivate
```



## 3. PyCharm 설치



## 4. PyCharm 세팅

```
뭔가 오류가 생겼다. 이 과정은 잠시 보류한다. (2020.07.24.)
```

- 프로젝트 만들기 전 개발 환경에서 configure - settings 클릭
- Project Interpreter에서 나사버튼을 누르고 "Add" 선택
- Conda Environment - Existing environment에서 미리 생성해놓은 가상환경 선택하고 'Make available to all projects' 체크박스 체크 후 (위치: \Mininconda3\envs\my_envs\tools\python.exe)
- Settings - Tools - Terminal 에서 Shell path에 다음을 입력

```cmd
cmd.exe "/K" C:\Program Files\Miniconda3\condabin\conda activate my_env
    # 윈도우 cmd.exe "\K" 옵션은 명령어 실행 후 세션을 종료하지 않고 유지함
```

*Copyright* © Song_Artish