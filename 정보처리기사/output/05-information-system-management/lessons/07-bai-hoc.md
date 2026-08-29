# 4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

오류, 제어, 교환, 방식

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)

### 4.1 오류 발생 원인 및 제어 (Error Causes & Control)
- **원인:** 감쇠, 지연 왜곡, 상호 변조, 누화 잡음, 충격성 잡음(디지털 통신 주요인).
- **FEC (순방향 오류 수정):** 수신 측에서 스스로 수정 (해밍 코드 등). 오버헤드 큼, 역채널 불필요.
- **BEC (역방향 오류 수정):** 오류 시 재전송(ARQ) 요구 (패리티, CRC 등).
- **Tiếng Việt:** 
  - FEC: Tự sửa lỗi (vd: Hamming Code). 
  - BEC: Yêu cầu gửi lại (vd: CRC, Parity).

### 4.2 ARQ (자동 반복 요청) 및 오류 검출 방식
- **ARQ 종류:**
  - **Stop-and-Wait:** 한 블록 보내고 기다림.
  - **Go-Back-N:** 오류 발생 지점부터 *모두* 재전송.
  - **Selective Repeat:** 오류 발생 블록*만* 재전송 (버퍼 필요, 복잡).
  - **Adaptive:** 채널 상태에 따라 동적 변경.
- **오류 검출 및 수정:**
  - **패리티 (Parity):** 1비트 검출, 짝수오류 검출 불가.
  - **CRC:** 다항식 기반, 집단 오류 검출 특화 (HDLC 사용).
  - **해밍 코드 (Hamming Code):** 1비트 *수정* 가능. `2^n` 번째 자리에 비트 삽입.
- **Tiếng Việt:** 
  - Go-Back-N: Gửi lại từ lỗi. Selective Repeat: Chỉ gửi lại gói lỗi. 
  - CRC: Kiểm tra đa thức (phổ biến nhất). Hamming Code: Sửa được lỗi 1 bit.

### 4.3 교환 방식 (Switching Methods)
- **회선 교환 (Circuit Switching):** 물리적 전용선 할당. 고정 대역, 연속적 데이터 전송. (접속 지연 O, 전송 지연 X). 전화망.
- **축적 교환 (Store-and-Forward):** 데이터를 저장했다가 경로를 찾아 전송.
  - **메시지 교환 (Message Switching):** 전체 메시지 전송. 지연 매우 긺.
  - **패킷 교환 (Packet Switching):** 패킷 단위로 잘라서 전송 (다음 파트에서 상세 서술).
- **Tiếng Việt:** 
  - Circuit Switching (Chuyển mạch kênh): Tạo đường truyền vật lý (Điện thoại).
  - Message Switching (Chuyển mạch thông điệp): Lưu rồi chuyển toàn bộ.

EOF
### 4.4 패킷 교환 방식 및 네트워크 기능 (Packet Switching & Network Functions)
- **가상 회선 (Virtual Circuit):** 패킷 교환 전에 논리적인 가상 회선을 설정. 전송 순서가 보장되며 신뢰성이 높음. (호 설정 → 데이터 전송 → 호 해제).
- **데이터그램 (Datagram):** 연결 경로 설정 없이 각 패킷이 독립적으로 운반됨. 패킷마다 경로가 다르고 순서가 다를 수 있음. 짧은 데이터 전송에 적합.
- **패킷 교환망의 기능:** 패킷 다중화, 논리 채널 설정, 경로 제어, 순서 제어, 트래픽 제어, 오류 제어.
- **Tiếng Việt:** 
  - Virtual Circuit: Tạo đường dẫn ảo trước khi truyền (thứ tự được đảm bảo). 
  - Datagram: Truyền độc lập không cần tạo đường dẫn (thứ tự có thể thay đổi).

### 4.5 트래픽 제어 및 라우팅 심화 (Traffic Control & Routing)
- **경로 설정 방식 (Routing Strategies):**
  - **고정 경로 (Static):** 미리 정해진 경로 사용.
  - **적응 경로 (Adaptive):** 트래픽 상황에 따라 동적 변경.
  - **범람 (Flooding):** 모든 경로로 패킷 복사 전송 (네트워크 정보 불필요).
  - **임의 경로 (Random):** 인접 교환기 중 임의 선택.
- **폭주(혼잡) 제어 (Congestion Control):** 오버플로를 방지하기 위해 네트워크 내 패킷 수 조절.
- **Tiếng Việt:** Routing có Static (Tĩnh), Adaptive (Động), Flooding (Tràn ngập). Congestion Control giúp chống quá tải mạng.
