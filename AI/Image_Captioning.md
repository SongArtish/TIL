# Image Captioning

> pytorch를 이용하여 분류기(classifier) 모델을 설계하고, CIFAR10 데이터셋에 대하여 학습 및 테스트 코드를 작성한다. 
> [참고사이트](https://tutorials.pytorch.kr/beginner/blitz/cifar10_tutorial.html)

2021.03.03

---

[TOC]

---



---

아래의 순서로 진행한다.

1. **데이터셋 준비 및 전처리**: `torchvision`을 사용하여 CIFAR10 training, test 데이터셋을 load하고 normalize
2. **분류기 모델 설계**: CNN을 사용하여 분류기 모델 설계
3. **Loss function 정의**: 학습 시 사용되는 loss function 정의하기
4. **모델 학습하기**: <1번>의 training 데이터셋으로 설정한 epoch만큼 모델을 학습
5. **테스트하기**: 학습이 오나료된 모델을 <1번>의 test 데이터셋으로 테스트하기

---



## 용어

### Dataset

데이터셋을 다루기 위해서는 아래의 과정을 수행해야한다.

- `numpy array`로 특정 데이터 load
- 이후 pytorch로 연산가능한 `torch.*Tensor`로 변환

또한, 아래의 패키지를 사용한다.

- 이미지: Pillow, OpenCV 패키지
- 오디오(스피치): scipy, librosa 패키지
- 컴퓨터 비전 데이터: `torchvision`
  - 여러 데이터셋들을 다운받을 수 있다.
  - 모든 데이터셋을 `torchvision`으로 다운 받을 수 있는 것은 아니지만, CIFAR10은 `torchvision`으로 손쉽게 다운받을 수 있습니다.

### CIFAR10

여기서는 CIFAR10을 데이터셋으로 사용한다.

> CIFAR10은 3x32x32 크기의 이미지로 총 10개의 클래스(‘airplane’, ‘automobile’, ‘bird’, ‘cat’, ‘deer’, ‘dog’, ‘frog’, ‘horse’, ‘ship’, ‘truck’) 로 구성된 6000장의 데이터셋이다.

### torchvision

> Computer vision에서 사용하는 각종 테크닉들을 torch와 연동하여 구현한 라이브러리



## 1. 데이터셋 준비 및 전처리

### 1.1 데이터 load 및 normalize

- `torchvision`을 사용하여 CIFAR10을 load할 수 있다.

  > The [`torchvision`](https://pytorch.org/vision/stable/index.html#module-torchvision) package consists of popular datasets, model architectures, and common image transformations for computer vision.

- `torchvision.transform`을 사용하여 데이터를 normalize할 수 있다.

  > Transforms are common image transformations. They can be chained together using [`Compose`](https://pytorch.org/vision/stable/transforms.html?highlight=transform#torchvision.transforms.Compose). Additionally, there is the [`torchvision.transforms.functional`](https://pytorch.org/vision/stable/transforms.html?highlight=transform#module-torchvision.transforms.functional) module.

**references**

- `dataloader(pytorch doc)` :arrow_right: [link](https://pytorch.org/docs/stable/data.html)
- `dataloader parameter(blog)` :arrow_right: [link](https://subinium.github.io/pytorch-dataloader/)

```python
import torch
import torchvision
import torchvision.transforms as transforms
```

```python
# [0,1] 범위의 데이터셋을 [-1, 1] 범위의 값으로 normalize하도록 transform 정의
transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

# torchvision으로 CIFAR10 trainset load, trainset dataloader 정의
trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,shuffle=True, num_workers=2)

# torchvision으로 CIFAR10 testset load, trainset dataloader 정의
testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=4, shuffle=False, num_workers=2)
# CIFAR10의 10개의 class 정의
classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
```

- :white_check_mark: batch_size를 변경하여 출력되는 이미지 개수를 조정할 수 있다.



### 1.2 데이터 시각화

- `matplotlib`는 python visualization library
- `matplotlib`의 `imshow` 함수를 활용해 데이터들을 시각화 할 수 있다.

**references**

- `matplotlib doc` :arrow_right: [link](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html)

```python
import matplotlib.pyplot as plt
import numpy as np
```

```python
# 이미지를 보여주기 위한 함수
def visualize(img):
    # [-1, 1] 범위로 normalize된 데이터를 [0,1] 범위로 unnormalize
    img = img / 2 + 0.5     # unnormalize
    # img를 numpy값으로 변환
    npimg = img.numpy()
    # plt.imshow함수로 시각화
    plt.imshow(np.transpose(npimg, (1, 2, 0)))	# np.transpose -> 전치행렬 반환
    plt.show()

# 학습용 이미지를 무작위로 가져오기
dataiter = iter(trainloader)
images, labels = dataiter.next() ## image

# show images
visualize(torchvision.utils.make_grid(images))

# print labels
print(' '.join('%5s' % classes[labels[j]] for j in range(4)))
```

- :white_check_mark: `numpy.transpose()`는 전치행렬을 반환하는 함수이다.



## 2. 분류기 모델 설계



***Copyright* © 2021 Song_Artish**