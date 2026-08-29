# 1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

데이터, 통신, 개요

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)

### 1.1 데이터 통신 및 주요 발전
- **데이터 통신:** 컴퓨터와 통신기기 사이에서 디지털(0과 1) 정보를 송수신. (데이터 통신 = 데이터 전송 기술 + 데이터 처리 기술).
- **정보 통신:** 전기 통신 + 컴퓨터 (정보 처리). 통신의 3요소: 정보원, 수신원, 전송 매체.
- **주요 시스템:** 
  - `SAGE`: 최초의 데이터 통신 시스템.
  - `SABRE`: 최초 상업용. 
  - `ARPANET`: 인터넷의 효시. 
  - `ALOHA`: 최초 무선 패킷 교환.
- **Tiếng Việt:** Truyền thông dữ liệu truyền thông tin số (0, 1). 3 yếu tố: Nguồn, Đích, Môi trường truyền. ARPANET là tiền thân của Internet.

### 1.2 통신 회선 및 매체 (Transmission Media)
- **꼬임선 (Twisted Pair):** 저렴하고 설치 간편, 간섭에 취약.
- **동축 케이블 (Coaxial Cable):** 대역폭이 넓고 누화 적음, 중계기 필요.
- **광섬유 케이블 (Optical Fiber):** 빛의 반사 원리. 가장 빠르고 대역폭 큼. 도청 어려워 보안성 우수. 무유도, 무누화.
- **마이크로파/위성 통신:** 장거리 대용량 통신. 다중 접속 방식: FDMA(주파수), TDMA(시간), CDMA(코드).
- **Tiếng Việt:** 
  - Twisted Pair: Rẻ, dễ nhiễu.
  - Coaxial: Băng thông rộng, ít nhiễu.
  - Optical Fiber: Cáp quang (phản xạ ánh sáng), siêu tốc, siêu bảo mật.
  - Vệ tinh: Phân chia theo Tần số (FDMA), Thời gian (TDMA), Mã (CDMA).

### 1.3 통신 제어장치 (CCU) & 전처리기 (FEP)
- **CCU:** 데이터 신호의 직·병렬 변환 등 전반적인 제어.
- **FEP (Front-End Processor):** 호스트와 단말기 사이에 위치해 통신 제어를 전담하여 메인 컴퓨터의 부하를 줄임.
- **Tiếng Việt:** CCU điều khiển truyền tải. FEP xử lý tiền kỳ để giảm tải cho máy chủ (Host).
