# 11. 보충 및 심화 내용 (Bổ sung & Nâng cao)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **11. 보충 및 심화 내용 (Bổ sung & Nâng cao)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

보충, 심화, 내용

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 11. 보충 및 심화 내용 (Bổ sung & Nâng cao)

### 11.1 소프트웨어 프레임워크 및 개발 심화
- **프레임워크의 특성 (Framework Characteristics):**
  - **모듈화 (Modularity):** 캡슐화를 통해 변경의 영향을 최소화하고 품질 향상.
  - **재사용성 (Reusability):** 재사용 가능한 모듈 제공 (생산성 향상).
  - **확장성 (Extensibility):** 다형성을 통한 인터페이스 확장.
  - **제어의 역흐름 (Inversion of Control):** 객체 제어 권한을 프레임워크에 넘김.
- **프레임워크 종류 (Framework Types):**
  - **스프링 (Spring):** 자바 플랫폼을 위한 경량형 오픈소스 프레임워크.
  - **전자정부 (e-Government):** 공공부문 정보화 사업을 지원하는 프레임워크.
  - **닷넷 (.NET):** 마이크로소프트의 Windows 개발 및 실행 환경.
- **Tiếng Việt:** Đặc điểm của Framework: Mô-đun hóa, Tái sử dụng, Khả năng mở rộng, và Đảo ngược quyền điều khiển (IoC - Inversion of Control). Các loại: Spring (Java), e-Government (Hàn Quốc), .NET (Microsoft).

### 11.2 네트워크 구조 및 표준 심화
- **네트워크 토폴로지 (Network Topology):**
  - **성형 (Star):** 중앙 컴퓨터를 중심으로 연결 (포인트 투 포인트).
  - **링형 (Ring):** 이웃하는 단말끼리 원형으로 연결. 
  - **버스형 (Bus):** 하나의 통신 회선에 여러 단말 연결 (신뢰성 높음).
  - **망형 (Mesh):** 모든 지점을 서로 연결. 회선 수 = `n(n-1)/2`.
- **IEEE 802 표준 규격:**
  - `802.3`: CSMA/CD (유선 LAN)
  - `802.11`: 무선 LAN (WLAN)
    - `802.11a/g`: 54Mbps
    - `802.11i`: 보안 표준 (WPA/WPA2)
    - `802.11n`: 2.4GHz/5GHz 듀얼 대역, 최고 600Mbps
- **경로 제어 프로토콜 (Routing Protocols):**
  - **IGP (내부):** AS 내부 라우팅 (RIP, OSPF)
  - **EGP (외부):** AS 간의 라우팅
  - **BGP (Border Gateway Protocol):** EGP 단점 보완. 변화된 정보만 교환.
- **흐름 제어 (Flow Control):**
  - **정지-대기 (Stop-and-Wait):** ACK를 받은 후 다음 패킷 전송.
  - **슬라이딩 윈도우 (Sliding Window):** ACK 없이도 미리 정해진 윈도우 크기(Window Size)만큼 연속 전송.
- **Tiếng Việt:** 
  - Topology mạng: Star, Ring, Bus, Mesh (Số đường truyền = n(n-1)/2).
  - IEEE 802.11: Tiêu chuẩn mạng không dây (Wi-Fi).
  - Flow Control: Sliding Window truyền liên tục dựa vào kích thước cửa sổ mà không cần chờ ACK cho từng gói.

### 11.3 데이터베이스 동시성 및 교착상태 심화
- **교착상태 해결 방법 (Deadlock Handling):**
  - **예방 (Prevention):** 발생 4조건(상호배제, 점유대기, 비선점, 환형대기) 중 하나를 부정 (자원 낭비 심함).
  - **회피 (Avoidance):** 가능성을 피함 (**은행원 알고리즘**).
  - **발견 (Detection):** 교착상태가 발생했는지 점검.
  - **회복 (Recovery):** 프로세스 종료 또는 자원 선점.
- **회복 기법 (Recovery):**
  - **연기 갱신 기법 (Deferred Update):** 트랜잭션 부분 완료 전까지 실제 DB 반영을 연기하고 Log에 기록 (Redo만 가능).
  - **즉각 갱신 기법 (Immediate Update):** 즉시 반영. 장애 시 Undo, Redo 모두 사용 가능.
  - **그림자 페이지 대체 기법 (Shadow Paging):** 그림자 페이지 보관 (Log, Undo, Redo 불필요).
  - **검사점 기법 (Check Point):** 검사점부터 회복하여 시간 절약.
- **Tiếng Việt:** Xử lý Deadlock: Phòng ngừa (Prevention) -> Tránh (Avoidance - Thuật toán Banker) -> Phát hiện (Detection) -> Phục hồi (Recovery). Phục hồi DB bằng Log, Shadow Paging, Check Point.

### 11.4 암호화 및 해시 알고리즘 심화
- **암호화 키 개수 (Key Count):**
  - **개인키(대칭키):** `n(n-1)/2` 개
  - **공개키(비대칭키):** `2n` 개
- **블록 암호화 알고리즘 (Block Ciphers):**
  - **SEED:** 한국인터넷진흥원(KISA) 개발 (128/256bit).
  - **ARIA:** 국가정보원 및 산학연 협회 개발 (128/192/256bit).
  - **DES:** 미국 NBS 발표, 64bit 블록 / 56bit 키 (3DES로 강화됨).
  - **AES:** DES 한계 극복, NIST 발표 (128/192/256bit).
- **해시 함수 종류 (Hash Functions):**
  - **SHA 시리즈:** 미국 NSA 설계, NIST 발표.
  - **MD5:** R. Rivest 고안 (128bit 키).
  - **N-NASH, SNEFRU.**
- **Tiếng Việt:** Thuật toán mã hóa Hàn Quốc: SEED, ARIA. Thuật toán quốc tế: DES, AES, RSA. Số lượng khóa đối xứng = n(n-1)/2. Số lượng khóa bất đối xứng = 2n.

### 11.5 기타 보안 및 공격 기법 심화
- **Secure SDLC 방법론:**
  - **CLASP:** 활동 중심, 역할 기반 (초기 단계 보안 강화).
  - **MS SDL:** 마이크로소프트의 나선형 모델 기반 방법론.
  - **Seven Touchpoints:** 모범사례를 SDLC에 통합 (위험 분석 및 테스트).
- **추가 웹 보안 약점 (Additional Web Vulnerabilities):**
  - **운영체제 명령어 삽입:** 외부 입력으로 시스템 명령어 실행 유도.
  - **위험한 파일 업로드:** 스크립트 파일 업로드로 시스템 제어.
  - **신뢰되지 않는 URL 주소로 자동접속 연결 (Open Redirect):** 피싱 사이트로 유도.
- **분산 서비스 공격용 툴 (DDoS Tools):**
  - **Trin00:** UDP Flooding 주도.
  - **TFN / TFN2K:** UDP/TCP SYN, 스머핑 동시 수행.
  - **Stacheldraht:** 암호화된 통신 수행 및 자동 업데이트.
- **새로운 공격 기법 (New Attack Vectors):**
  - **제로 데이 공격 (Zero Day Attack):** 보안 취약점이 공표되기도 전에 이루어지는 신속한 공격.
  - **스미싱 (Smishing):** SMS를 이용한 개인정보 탈취.
  - **Evil Twin Attack:** 실제와 동일한 이름의 가짜 Wi-Fi(AP)를 송출해 정보 탈취.
- **Tiếng Việt:** 
  - Zero Day Attack: Tấn công khai thác lỗ hổng trước khi có bản vá.
  - Smishing: Phishing qua tin nhắn SMS.
  - Evil Twin: Tấn công bằng trạm Wi-Fi giả mạo tên (SSID) giống hệt trạm thật.
  - DDoS Tools: Trin00, TFN, Stacheldraht (ẩn danh và mã hóa liên lạc).

EOF
# 데이터 통신 및 통신 프로토콜 (Truyền thông Dữ liệu & Giao thức)
