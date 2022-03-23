# 원티드 프리온보딩 텍스트 유사도(한글) API server


## 폴더 구조
```
.
├── README.md
├── app
│   ├── basemodels.py
│   ├── neuralnet.py
│   ├── router
│   │   └── predict.py
│   ├── torch_models
│   │   ├── torch_model.pt
│   │   └── vocab_snu_subchar12367.txt
│   └── utils.py
├── download_model.py
├── main.py
├── pyproject.toml
└── requirements.txt
```

<br>
<br>

## 실행방법

### local enviroment

1. 다운로드 프로젝트
```console
$ git clone https://github.com/preonboarding-team4/STS_APIserver.git
$ cd STS_APIserver
```

2. 필요한 패키지 설치
```console
$ pip install -r requirements.txt
```

3. 모델 가중치 파일 다운로드
```console
$ python download_model.py
```

4. API서버 실행
```console
$ python main.py
```

<br>
<br>

### Docker

