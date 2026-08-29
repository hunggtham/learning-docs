# 2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

데이터, 전송, 방식, 변조

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)

### 2.1 통신 방식 및 전송 동기 (Transmission Modes & Sync)
- **방향에 따른 분류:** 단방향 (Simplex), 반이중 (Half-Duplex, 무전기), 전이중 (Full-Duplex, 전화).
- **비동기식 (Asynchronous):** 문자마다 Start Bit / Stop Bit를 붙여 전송. 저속 단거리, 오버헤드 큼.
- **동기식 (Synchronous):** 프레임(블록) 단위로 일시에 전송. 속도 빠르고 효율 좋음. 비트/블록 동기 방식.
- **Tiếng Việt:** 
  - Đơn công (Simplex), Bán song công (Half-Duplex), Song công toàn phần (Full-Duplex).
  - Bất đồng bộ: Dùng Start/Stop bit (overhead cao). Đồng bộ: Truyền theo block (nhanh, hiệu quả).

### 2.2 신호 변환 장치 (MODEM & DSU)
- **모뎀 (MODEM):** 디지털 ↔ 아날로그 변환.
- **DSU (Digital Service Unit):** 디지털 ↔ 디지털 (단극성 ↔ 양극성 변환). 디지털 전용선에 사용.
- **Tiếng Việt:** MODEM (Chuyển đổi Số <-> Tương tự). DSU (Chuyển đổi Số <-> Số).
- 💡 **Mẹo ghi nhớ:** MO-Dem = MOdulation - DEModulation. D-SU = Digital - Digital.

### 2.3 디지털 변조 (Digital Modulation - Keying)
- **ASK (진폭 편이):** 진폭 변화.
- **FSK (주파수 편이):** 주파수 변화 (1,200bps 이하).
- **PSK (위상 편이):** 위상 변화 (중/고속 모뎀).
- **QAM (직교 진폭 변조):** 진폭과 위상 동시 변화 (고속, 9,600bps 표준).
- **Tiếng Việt:** Điều chế tín hiệu số sang tương tự: ASK (Biên độ), FSK (Tần số), PSK (Pha), QAM (Biên độ + Pha kết hợp cho tốc độ cao).

### 2.4 PCM (Pulse Code Modulation)
- 아날로그 데이터를 디지털 신호로 변환. CODEC 이용.
- **과정:** 표본화(Sampling) → 양자화(Quantizing) → 부호화(Encoding) → 복호화(Decoding) → 여파화(Filtering).
- **표본화 (Sampling):** 횟수 = 2 × 최고 주파수.
- **Tiếng Việt:** Biến đổi Tương tự -> Số (dùng CODEC). Quá trình: Lấy mẫu -> Lượng tử hóa -> Mã hóa.
- 💡 **Mẹo ghi nhớ:** Mẫu Lượng Mã Giải Lọc (Lấy mẫu -> Lượng tử hóa -> Mã hóa -> Giải mã -> Lọc).
