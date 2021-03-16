# Text to Speech

> **추출된 캡션을 스피치로 합성**

---

[TOC]

---



## 딥러닝 파트

1. **데이터셋 준비**

   - 데이터 셋은 `LJ Speech Dataset`을 사용

     > LJ Speech Dataset은 단일 여성 화자의 131,000개의 짧은 영어 음성 클립으로 **{(음성, 텍스트)}**의 데이터 쌍을 가지고 있다.

   - 데이터셋을 학습에 이용하기 위해 train, validate, test 데이터로 나눠준다.

2. **데이터 전처리**

   > `{(음성, 텍스트)}`의 데이터 쌍을 모델이 처리 가능한 형태로 변환

   - 텍스트 데이터 전처리

     - 텍스트를 문자 단위로 분리
     - 이를 특징 추출 및 수치화를 위한 **캐릭터 임베딩 벡터화(Character Embedding Vector)**

   - 음성 데이터 전처리

     > 음성 데이터는 시간 영역의 1차원 데이터이다. 

   - 1차원의 긴 음성 데이터는 기존 CNN, RNN 구조에 바로 사용하기에 비효율적
   - 따라서, **Short Time Fourier Transform (STFT, 단시간 푸리에 변환)**을 통해 **spectrogram**이라는 데이터 형태로 변환
   - 사람의 청력 시스템을 모사한 **Mel filter bank**라는 필터를 통과시켜 최종적으로 **mel_spectrograms()** 함수를 통하여 구현

3. **모델 학습**

   > 대표적인 TTS 모델인 **Tacotron2**를 구현한다.

   1) **인코더**: text를 문자 단위로 chracter embedding vector화한 값을 입력으로 하며, CNN과 LSTM을 거쳐 특정 벡터 (feature vector)를 출력

   2) **디코더**: Attention mechanism을 사용하여 앞서 출력한 feature vector를 입력으로 하고 ,LSTM을 거쳐 mel-spectrogram을 생성하여 출력

   3) **보코더**: 시간-주파수 영역의 신호인 mel-spectrogram은 바로 재생 가능한 데이터 형태가 아니므로, 시간 영역에서 재생 가능한 waveform으로 변환해주는 모듈. Mel-spectrogram을 입력으로 하여 waveform을 출력 

   - 여기서는 보코더로 변환 성능이 좋은 **WaveNet(2016)** 대신, 추론 시간이 짧은 **WaveGlow(2018)**을 사용한다.

4. **중간평가 및 로그기록**

   > 학습이 잘 진행되고 있는지 지속적으로 확인한다.

   - 학습 진행 중 일정 주기마다, **validate 데이터셋**으로 모델 평가 가능
   - 평가 후 loss 값 등의 학습 중간 정보들을 로그(log)로 기록, 학습된 모델의 parameter 정보 저장

5. **테스트하기**

   - 학습이 완료된 후, 가장 좋은 성능을 보인 모델을 선정
   - 사전 학습된 WaveGlow 모델을 연결하여 TTS 시스템 완성



## 웹서버 파트

> 본 프로젝트에서는 `Bootstrap`, `jQuery` 라이브러리를 기반으로 구성

- 인덱스 페이지를 통해 이미지 업로드
- 업로드 된 이미지를 입력으로 하는 Image Captioning 모듈에 전달 및 실행하여 캡션 텍스트 목록 생성
- 텍스트 목록을 전달받아 화면에 출력
- 텍스트 목록 중 하나를 사용하자 선택
- 해당 텍스트를 TTS의 입력으로 전달 및 실행하여 음성 생성
- 음성이 저장된 wav파일을 전달 받아 브라우저 화면에서 재생



## 1. 데이터 전처리 및 파라미터 구성

### 1.1 음성 데이터 전처리

> waveform에서 Mel spectrogram으로 변환한다.

#### 음성 파일 다운로드

- 먼저 구글 드라이브에서 음성 파일을 다운로드한다.
- :ballot_box_with_check: With **gdown** library, we can download a large file from Google Drive.

```python
import gdown
url = "https://drive.google.com/uc?id=1W_5ECH8QcJYF2Fkt-HWyIAZCKmyizv7S"
output = 'sample.wav' # sample.wav 파일 다운로드
gdown.download(url,output,quiet=False)
```

- 다음으로 필요한 라이브러리를 import하고 waveform을 나타낼 도형의 크기도 지정해준다.
  - :ballot_box_with_check: **librosa** is a python package for music and audio analysis.

```python
import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt

FIG_SIZE = (15,10)  # Figure Size
```

- 다음으로 [librosa.load](https://librosa.org/doc/main/generated/librosa.load.html#librosa-load)를 통해 음성 파일을 load한다.
  - Load an audio file as a floating point time series.
  - `librosa.load(path, sr=22050, mono=True, offset=0.0, duration=None, dtype=<class 'numpy.float32'>, res_type='kaiser_best')`
    - :white_check_mark: 여기서 `sr` refers to the target sampling rate.

```python
# 음성 파일 load
sig, sr = librosa.load("sample.wav", sr=22050)	# signal, sampling rate
```

- return 값은 아래와 같다.
  - **y**: audio time series
  - **sr**: sampling rate of `y
- 그리고 아래와 같이 waveplot을 그려준다.

```python
plt.figure(figsize=FIG_SIZE)
librosa.display.waveplot(sig, sr, alpha=0.5)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Waveform")
```

- 아래의 코드로 오디오를 display할 수도 있다.

```python
from IPython.display import Audio
Audio(data=sig, rate=sr)
```

#### 퓨리에 변환으로 스펙트럼 구하기

> **푸리에 변환(Fourier Transform, FT)**은 시간이나 공간에 대한 함수를 시간 또는 공간 주파수 성분으로 분해하는 변환을 말한다. 즉, 아날로그에서 디지털 신호로 변경하며, 반대로 디지털에서 아날로그 신호로 변경하는 것은 `푸리에 역 변환`이라고 한다.
> 여기서는 연산을 줄이기 위해서 **고속 푸리에 변환(FFT)**을 사용한다.

```python
# 단순 퓨리에 변환으로 스펙트럼 구하기
fft = np.fft.fft(sig)	# FFT

# 복소공간 값 절댓갑 취해서, magnitude 구하기
magnitude = np.abs(fft)

# Frequency 값 만들기
f = np.linspace(0,sr,len(magnitude))

# 푸리에 변환을 통과한 specturm은 대칭구조로 나와서 high frequency 부분 절반을 날려고 앞쪽 절반만 사용한다.
left_spectrum = magnitude[:int(len(magnitude)/2)]
left_f = f[:int(len(magnitude)/2)]

plt.figure(figsize=FIG_SIZE)
plt.plot(left_f, left_spectrum)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.title("Power spectrum")
```

- :white_check_mark: `numpy.linspace` returns evenly spaced numbers over a specified interval.	
  - `numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)`

#### STFT를 사용하여 Spectrogram 생성하기

> STFT(Short-time Fourier Transform, 단시간 푸리에 변환)는 푸리에 변환 관계가 시간에 따라 변화하는 신호로서, 로컬 섹션의 정현파 주파수와 위상 콘텐츠를 결정하기 위해 사용된다. (출처: 위키백과)

```python
hop_length = 512  # 전체 frame 수
n_fft = 2048  # frame 하나당 sample 수

# calculate duration hop length and window in seconds
hop_length_duration = float(hop_length)/sr
n_fft_duration = float(n_fft)/sr

# STFT
stft = librosa.stft(sig, n_fft=n_fft, hop_length=hop_length)

# 복소공간 값 절댓값 취하기
magnitude = np.abs(stft)

# magnitude > Decibels 
log_spectrogram = librosa.amplitude_to_db(magnitude)

# display spectrogram
plt.figure(figsize=FIG_SIZE)
librosa.display.specshow(log_spectrogram, sr=sr, hop_length=hop_length)
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.colorbar(format="%+2.0f dB")
plt.title("Spectrogram (dB)")
```



***Copyright* © 2021 Song_Artish**