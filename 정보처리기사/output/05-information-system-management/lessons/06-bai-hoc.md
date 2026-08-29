# 3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

다중화, 전송, 제어

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)

### 3.1 다중화기 (Multiplexer)
- 여러 단말기가 하나의 통신 회선을 공유.
- **FDM (주파수 분할 다중화):** 주파수를 분할. 보호 대역(Guard Band) 필요(대역폭 낭비). 아날로그, 비동기식.
- **TDM (시분할 다중화):** 시간을 분할(Time Slot). 동기식/디지털.
  - **STDM (동기식):** 데이터 유무 상관없이 고정 시간 폭 할당 (효율 낮음).
  - **ATDM (비동기식/통계적):** 데이터가 있는 단말에만 시간 할당 (효율 높음).
- **역 다중화기 (Inverse MUX):** 하나의 고속 채널을 2개의 저속 채널로 분할.
- **집중화기 (Concentrator):** 회선이 부족할 때 동적으로 할당(버퍼 필요). (입력 > 출력 회선).
- **Tiếng Việt:** 
  - FDM: Chia tần số (cần khoảng vệ bảo vệ Guard Band). 
  - TDM: Chia thời gian. (STDM: Cố định, ATDM: Động/Thống kê). 
  - Concentrator: Gom kênh, cần bộ đệm, số đầu vào > đầu ra.

### 3.2 통신 속도 (Speed Metrics)
- **변조 속도 (Baud):** 1초 동안 신호 변화 횟수. (Baud = Bps / 상태 변화 수).
- **신호 속도 (Bps):** 1초 동안 전송 비트 수.
- **상태 변화 수:** Mono(1), Di(2), Tri(3), Quad(4) bit.
- **Tiếng Việt:** Baud: Số lần đổi trạng thái/s. Bps: Số bit/s.

### 3.3 전송 제어 (Transmission Control)
- **5단계 절차:** 회선 접속 → 링크 설정 → 메시지 전송 → 링크 해제 → 회선 절단.
- **전송 제어 문자:**
  - `SYN`: 동기화
  - `SOH`/`STX`/`ETX`/`ETB`/`EOT`: 헤더, 텍스트(본문), 블록, 전송 종료
  - `ENQ`: 링크 설정 요구
  - `DLE`: 데이터 링크 이스케이프 (투과성 확보)
  - `ACK`/`NAK`: 긍정/부정 응답
- **Tiếng Việt:** Các ký tự điều khiển: SYN (Đồng bộ), STX (Bắt đầu văn bản), ETX (Kết thúc văn bản), ACK (Xác nhận), NAK (Từ chối).

### 3.4 HDLC 프로토콜 (High-level Data Link Control)
- **비트(Bit) 위주**의 프로토콜. 전이중/반이중 지원, 동기식 전송.
- **비트 투과성 (Bit Stuffing):** 연속된 '1'이 5개면 강제로 '0' 추가 (플래그 `01111110`과 구분).
- **프레임 종류:**
  - **I (정보):** 데이터 전달 (0으로 시작).
  - **S (감독):** 오류/흐름 제어 (10).
  - **U (비번호):** 링크 모드 설정 (11).
- **전송 모드:** NRM (정규), ARM (비동기), ABM (비동기 균형 - 전이중 P2P).
- **Tiếng Việt:** HDLC là giao thức truyền theo bit. Dùng "Bit Stuffing" để chèn bit '0' sau 5 bit '1' liên tiếp. 3 loại Frame: I (Thông tin), S (Giám sát), U (Không số).
