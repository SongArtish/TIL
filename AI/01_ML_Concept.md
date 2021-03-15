# ML Concept

> Machine Learning

[TOC]

---

![AI/머신러닝/딥러닝의 관계](img/ai_boundary.png)

`(출처: http://tobetong.com/?p=9393)`



## 구성요소

- 경험 사례
- 모델
- 평가 기준



## 과정

1. **계산/추론**: 함수를 주고 output이 나오도록 계산
2. **최적화**: 한 세트의 (input, output)을 주고, 관계를 가장 잘 설명하는 함수를 찾는 것
3. **일반화**: 본적이 없는 input 데이터로도 일관성 있는 output이 계산 가능
   - 기계학습에는 **일반화** 과정까지 포함하여야 한다.



## 유형

### 1. 지도학습

> Supervised Learning

- 명확한 목표 task와 그에 따른 입출력 데이터 쌍이 주어진 상황에서의 모델을 학습

### 2. 비지도학습

> Unsupervised Learning

- 명확한 정답 라벨 데이터가 주어지지 않고, 입력 데이터만 주어진 상황에서 데이터 안의 숨겨진 패턴을 찾아내는 형태의 학습법

### 3. 강화학습

> Reinforcement Learning

- 환경 내에 정의된 에이전트가 현재의 상태를 인식하여, 선택 가능한 행동들 중 최대한 이익이 될 것으로 판단되는 행동 혹은 행동 순서를 수행하는 방법

|                |                   지도 학습                   |                   비지도 학습                   |
| :------------: | :-------------------------------------------: | :---------------------------------------------: |
|   학습 방법    |             매핑 함수를 통한 학습             |          데이터 내 숨겨진 구조를 학습           |
| 정답 존재 여부 |                       O                       |                        X                        |
|   활용 Task    | 이미지 분류<br />이미지 캡셔닝<br />객체 인식 | 데이터 클러스터링<br />특성 학습<br />밀도 추정 |

![머신러닝 구조](img/machine_learning_structure.png)

`(출처: https://www.wordstream.com/blog/ws/2017/07/28/machine-learning-applications)`



## NN & MLP

> **Neural Networks** & **Multi_Layer Perceptron**

**Perceptron (Singel Layer Neural Network)**

- 가장 기본적인 신경망 구조
- 입력 벡터 x에 대해 (**Wx+b**) 형태
  - W는 입력에 곱해지는 가중치 파라미터 행렬
  - b는 역치를 조정하는 offset parameter
  - Affine 변환식으로 볼 수도 있음
- **Fully Connected (FC) layer**
  - 모든 노드가 서로 연결되어있기 때문에 계산량이 너무 많아짐
  - 입력 데이터가 1차원(배열) 형태로 한정됨!!
- 단, 표현력에 한계가 있음

**Multi-Layer Perceptron(MLP)**

- perceptron을 다중으로 쌓아서 활용

**메커니즘**

- NN의 최종 출력이 타겟의 차원과 일치하도록 설계
- 입력과 원하는 출력(라벨)을 이용하여 parameter 학습
- NN에 입력 값을 넣었을 때 마지막 층에서 나온 출력과 라벨과의 차이(error)를 네트워크를 학습하는데 사용
  - **뉴럴넷에서의 학습**: Gradient descent 최적화 방법 중 특수 케이스인 Back-propagation이라는 알고리즘을 통해 위의 에러를 줄이는 방향으로 parameter를 update



## CNN

Convolutional Neural Network

> FC layer와는 달리 모든 입력을 다음 층(layer)와 연결하지 않고, 국부적인 영역에 대한 filter 연산만으로 locally connected된 부분에 대해서만 출력을 계산하는 layer이다.
>
> - 이때 하나의 filter가 영상의 위치에 상관 없이 재활용되는 합성곱(convolution)연산을 활용하며, 이 때문에 Convolutional layer라고 불린다.

- CNN은 **공간적인 구조 정보를 보존**하면서 연산 및 학습이 가능하다.
- CNN의 출력은 FC layer와 달리 **채널, 세로, 가로의 3차원**으로 구성된다.
  - 입력 이미지 데이터 역시 3채널의 RGB 칼라, 가로, 세로 축을 갖는다.
- :white_check_mark: Convolutional layer에 추가적으로 pooling layer, 비선형 활성화 함수 (non-linear activation function) 등을 여러 번 깊게 적층한 구조를 **Deep CNN 구조**라고 한다.

**참고자료**

- [CNN 연산의 이해](https://wikidocs.net/64066): 합성곱 연산 및 3차원 텐서를 이용한 설명
- [CNN 모델 구현](https://nittaku.tistory.com/264): 설명 및 Keras를 이용한 구현 예시



***Copyright* © 2021 Song_Artish**