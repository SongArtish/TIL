# Image Captioning

> **이미지를 설명하는 캡션 추출**. pytorch를 이용하여 분류기(classifier) 모델을 설계하고, CIFAR10 데이터셋에 대하여 학습 및 테스트 코드를 작성한다.  [참고사이트](https://tutorials.pytorch.kr/beginner/blitz/cifar10_tutorial.html)

2021.03.03

---

[TOC]

---



## 개념

> **이미지 캡셔닝**이란 이미지를 입력으로 받아 이에 대한 적절한 설명을 텍스트로 출력하는 기술이다.

- 1번: 이미지 입력이 들어오면 이미지에서 의미 있는 물체들의 후보를 나열하는 기술
- 2번: 앞서 뽑은 물체 후보들을 RNN(Recurrent Neural Network)을 통해 문장으로 변환하는 기술



---

아래의 순서로 진행한다.

1. **데이터셋 준비 및 전처리**: `torchvision`을 사용하여 CIFAR10 데이터셋(training, test)을 load하고 normalize
2. **분류기 모델 설계**: CNN을 사용하여 분류기 모델 설계
3. **Loss function 정의**: 학습 시 사용되는 loss function 정의하기
4. **모델 학습하기**: <1번>의 training 데이터셋으로 설정한 epoch만큼 모델을 학습
5. **테스트하기**: 학습이 완료된 모델을 <1번>의 test 데이터셋으로 테스트하기

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

**`torchvision`**

> CIFAR10을 load할 수 있다.

**`torchvision.transform`**

> 데이터를 normalize할 수 있다.

references

- dataloader([pytorch doc](https://pytorch.org/docs/stable/data.html))
- dataloader parameter([blog](https://subinium.github.io/pytorch-dataloader/))

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

## for train
# torchvision으로 CIFAR10 trainset load, trainset dataloader 정의
trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,shuffle=True, num_workers=2)

## for test
# torchvision으로 CIFAR10 testset load, trainset dataloader 정의
testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=4, shuffle=False, num_workers=2)

# CIFAR10의 10개의 class 정의
classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
```

- :white_check_mark: batch_size를 변경하여 출력되는 이미지 개수를 조정할 수 있다.



### 1.2 데이터 시각화

**`matplotlib`**

> python visualization library
>
> - **`imshow` 함수** - 데이터들을 시각화 할 수 있다.

references

- matplotlib [doc](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html)

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

- **CNN**(Convolutional Neural Network)을 사용하여 모델을 설계한다.
- 이미지는 3-channel을 입력으로 받고, 최종적으로 10개의 class에 대한 확률을 구한다.
- 아래 모델은 예시이므로, layer을 직접 추가해보며 연습해본다.

**Classifier 클래스**

- `nn.Module:` 뉴럴넷 구현을 위한 base class. forward, parameter 등 모델을 만들고 사용할 때 필요한 부분들이 내부적으로 구현되어 있음
- `torch.nn`: 모델을 정의할 때 사용하는 Class들을 포함
- `init`: python class의 constructor. 필요한 멤버변수들을 초기화하고, `nn.Sequential` or `nn.ModuleList`를 이용하여 모델의 구성을 정의
- `forward`: 모델의 input을 받고 output을 return하는 함수

**Pytorch functions**

- `nn.Conv2d` : torch.nn.Conv2d(in_channels: int, out_channels: int, kernel_size, stride = 1, padding = 0)
- `nn.Maxpool2d` : torch.nn.MaxPool2d(kernel_size, stride = None, padding = 0)
- `nn.Linear` : torch.nn.Linear(in_features: int, out_features: int, bias: bool = True)

```python
import torch.nn as nn
import torch.nn.functional as F

# 분류기 모델 설계
class Classifier(nn.Module):
    def __init__(self):
        super(Classifier, self).__init__()
        
        # 이미지 3-channel 입력
        self.conv1 = nn.Conv2d(3, 16, 5)
        self.pool = nn.MaxPool2d(2, 2)

        # 최종 10개의 class에 대한 확률
        self.fc1 = nn.Linear(16*14*14, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
       
        x = self.pool(F.relu(self.conv1(x)))
        x = x.view(-1, 16*14*14)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        
        return x

classifier = Classifier()
```



## 3. Loss function 정의

- 분류기를 위해서 **cross-entropy loss**를 사용한다.
- optimzer로 SGD를 사용하고, learning rate, momentum등을 설정해준다.

**Pytorch functions**

- `nn.CrossEntropyLoss` : torch.nn.CrossEntropyLoss(weight: Optional[torch.Tensor] = None, size_average=None)
- `optim.SGD` :torch.optim.SGD(params, lr=, momentum=0)

```python
# Loss function 및 optimizer정의

import torch.optim as optim

# loss function
criterion = nn.CrossEntropyLoss()

# optimizer
optimizer = optim.SGD(classifier.parameters(), lr=0.001, momentum=0.9)
```



## 4. 모델 학습시키기

모델을 학습시키는 과정은 다음과 같다.

```markdown
1. 첫 번째 for문으로 epochs 만큼 반복
2. 두 번째 for문으로 trainset이 저장되어 있는 trainloader에서 배치 사이즈 만큼씩 샘플링하여 data load
3. load한 data에서 input 값과 label로 분리하여 저장
4. 각각의 값을 device에 올린다 (GPU or CPU)
5. optimizer에서 gradient 값 0으로 초기화
6. model에 input값을 입력하여 forward propagation
7. loss function으로 예측값과 label 비교
8. loss 값 backpropagation 하여 gradient 계산
9. 계산된 gradient를 모두 parameter에 적용
10. loss 값을 합하여 일정 주기(ex.2000 batch) 마다 평균 loss 값 출력 후 초기화
11. <2번>으로 돌아가 반복 한뒤 2)가 모두 마치면 1)로 돌아가 반복
12. 학습이 마친 이후 모델 저장
```

**Pytorch functions**

- `nn.CrossEntropyLoss` : torch.nn.CrossEntropyLoss(weight: Optional[torch.Tensor] = None, size_average=None)
- `optim.SGD` :torch.optim.SGD(params, lr=, momentum=0)

:ballot_box_with_check: Google Colab에서는 GPU를 사용할 수 있다.

- GPU가 있다면 GPU를 통해 학습을 가속화하고, 없으면 CPU로 학습하기 위해 device를 정해줍니다.

```python
# model을 device에 올린다 (GPU or CPU) 
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# 구현 완료 상태
classifier = classifier.to(device)
```

```python
# 모델 학습

epochs = 100  #define epochs

# 1) for문으로 epochs 만큼 반복
for epoch in range(epochs):  # epochs 횟수만큼 반복

    # loss값 누적 
    running_loss = 0.0
    
    # 2) for문으로 trainset이 저장되어 있는 trainloader에서 배치 사이즈 만큼씩 샘플링하여 data load
    for i, data in enumerate(trainloader, 0):
       
          # 3) load한 data에서 input 값과 label로 분리하여 저장
          inputs, labels = data   # data = [inputs, labels]
       
          # 4) 각각의 값을 device에 올린다 (GPU or CPU)
          inputs = inputs.to(device)
          labels = labels.to(device)

          # 5) optimizer에서 gradient 값 0으로 초기화
          optimizer.zero_grad() # 변화도(Gradient) 매개변수를 0으로 만들고

          # 6) model에 input값을 입력하여 forward propagation
          outputs = classifier(inputs)   # 순전파 + 역전파 + 최적화를 한 후

          # 7)  loss function으로 예측값과 label 비교
          loss = criterion(outputs, labels)
        
          # 8) loss 값 backpropagation 하여 gradient 계산
          loss.backward()
        
          # 9) 계산된 gradient를 모두 parameter에 적용
          optimizer.step()

          # 10) loss 값을 합하여 일정 주기(ex.2000 batch) 마다 평균 loss 값 출력 후 초기화
          running_loss += loss.item()
          if i % 2000 == 1999:    # print every 2000 mini-batches
                  print('[%d, %5d] loss: %.3f' % (epoch + 1, i + 1, running_loss / 2000))
                  running_loss = 0.0

# 12) torch.save로 학습이 마친 이후 모델 저장        

print('Finished Training')
```



## 5. 테스트하기

>학습 완료된 모델을 testset이 저장되어 있는 **testloader**에 대하여 성능 평가를 진행한다.
>
>- 모델을 evaluation 모드로 변경
>- gradient는 계산 할 필요가 없고, backpropagation도 진행하지 않는다.

테스트를 진행하는 방식은 아래와 같다.

- :white_check_mark: 만약 저장한 모델을 load해야 한다면, 모델의 인스턴스를 생성하고, 모델의 weight이 저장되어 있는 .ckpt(`checkpoint`) 파일을 모델에 load

```markdown
1. 모델을 evaluation 모드로 전환
2. with torch.no_grad로 gradient 계산을 제외
3. for문으로 testset에 저장되어 있는 testloader에서 배치 사이즈 만큼씩 샘플링하여 data load
4. load한 data에서 input 값과 label로 분리하여 저장
5. 각각의 값을 device에 올린다 (GPU or CPU)
6. model에 input값을 입력하여 forward propagation
7. 예측한 값들 중 가장 높은 확률의 class 선택
8. label과 예측한 class 비교하여 정답 확인
9. 정답률 출력
```

**Pytorch functions**

- `torch.no_grad` : gradient를 계산하기 위해 추적하는 수고를 하지 않음

```python
# 모델 테스트

# 만약 저장한 모델을 load해야 한다면, 모델의 인스턴스를 생성하고, 모델의 weight이 저장되어 있는 .ckpt 파일을 모델에 load
# new_classifier = Net()
# new_classifier.load_state_dict(torch.load('model_weight.ckpt'))
# new_classifier.to(device)

# 1) 모델을 evaluation 모드로 전환
correct = 0
total = 0

# 2) with torch.no_grad로 gradient 계산을 제외
with torch.no_grad():

    # 3) for문으로 testset에 저장되어 있는 testloader에서 배치 사이즈 만큼씩 샘플링하여 data load
    for data in testloader:

        # 4) load한 data에서 input 값과 label로 분리하여 저장
        inputs, labels = data

        # 5) 각각의 값을 device에 올린다 (GPU or CPU)
        images = inputs.to(device)
        labels = labels.to(device)

        # 6) model에 input값을 입력하여 forward propagation
        outputs = classifier(images)

        # 7) 예측한 값들 중 가장 높은 확률의 class 선택
        _, predicted = torch.max(outputs.data, 1)

        # 8) label과 예측한 class 비교하여 정답 확인
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
    

# 9) 정답률 출력
print('Accuracy of the network on the 10000 test images: %d %%' % (
    100 * correct / total))
```



***Copyright* © 2021 Song_Artish**