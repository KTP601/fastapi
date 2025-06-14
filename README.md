# YOLO + FastAPI

YOLO 모델(`best.pt`)을 활용하여 이미지에 삼다수가 있는지 판단하는 간단한 FastAPI

## 디렉터리 구조

```
├── main.py # FastAPI 서버 코드
├── client.py # 이미지 업로드용 클라이언트 코드
├── best.pt # 학습된 YOLO 모델
├── requirements.txt
├── test.jpg # 테스트 이미지
````


## 실행 방법

### 1. Conda 환경 생성 (Python 3.10 권장)

```bash
conda create -n fastapi python=3.10
conda activate fastapi
pip install -r requirements.txt
```

### 3. 서버 실행
터미널에서 아래 명령어로 API 서버 실행:

```
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 4. 클라이언트로 이미지 전송
다른 터미널에서 client.py 실행:
```
python client.py
```
test.png 이미지가 같은 경로에 있어야 함
### 응답 예시
```json
{"result": "Detected Samdasoo"}
```
또는

```json
{"result": "Samdasoo Not Detected"}
```
