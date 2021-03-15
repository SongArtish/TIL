# Text to Speech

> **추출된 캡션을 스피치로 합성**

---

[TOC]

---



## 1. 딥러닝 파트

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



## 2. 웹서버 파트

> 본 프로젝트에서는 `Bootstrap`, `jQuery` 라이브러리를 기반으로 구성

- 인덱스 페이지를 통해 이미지 업로드
- 업로드 된 이미지를 입력으로 하는 Image Captioning 모듈에 전달 및 실행하여 캡션 텍스트 목록 생성
- 텍스트 목록을 전달받아 화면에 출력
- 텍스트 목록 중 하나를 사용하자 선택
- 해당 텍스트를 TTS의 입력으로 전달 및 실행하여 음성 생성
- 음성이 저장된 wav파일을 전달 받아 브라우저 화면에서 재생



***Copyright* © 2021 Song_Artish**