# 6. 통신 프로토콜 (Giao thức Truyền thông)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **6. 통신 프로토콜 (Giao thức Truyền thông)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

통신, 프로토콜

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 6. 통신 프로토콜 (Giao thức Truyền thông)

### 6.1 통신 프로토콜 3요소 (Protocol 3 Elements)
- **구문 (Syntax):** 데이터 형식, 코딩.
- **의미 (Semantics):** 제어 정보 및 오류 관리.
- **시간 (Timing):** 속도 조절, 동기화.
- **Tiếng Việt:** 3 yếu tố của giao thức: Cú pháp (Syntax), Ngữ nghĩa (Semantics), Thời gian (Timing).

### 6.2 OSI 7계층 (OSI 7 Layers)
1. **물리 계층 (Physical):** 기계/전기적 특성 (RS-232C, 리피터).
2. **데이터 링크 계층 (Data Link):** 인접 시스템 간 신뢰성 보장, 오류/흐름 제어 (HDLC, LLC).
3. **네트워크 계층 (Network):** 경로 설정(Routing), 데이터 교환 (IP, X.25, 라우터).
4. **전송 계층 (Transport):** 종단 간(End-to-End) 투명한 데이터 전송 (TCP, UDP).
5. **세션 계층 (Session):** 대화 제어 및 동기점(체크점) 관리.
6. **표현 계층 (Presentation):** 데이터 포맷 변환, 암호화, 압축.
7. **응용 계층 (Application):** 사용자에게 네트워크 서비스 제공.
- **Tiếng Việt:** Mô hình OSI 7 lớp: Vật lý -> Liên kết dữ liệu -> Mạng -> Giao vận -> Phiên -> Trình diễn -> Ứng dụng.
- 💡 **Mẹo ghi nhớ:** Vật Liên Mạng Giao Phiên Trình Ứng (Vật lý -> Liên kết dữ liệu -> Mạng -> Giao vận -> Phiên -> Trình diễn -> Ứng dụng).

### 6.3 주요 네트워크 프로토콜
- **X.25:** 패킷 교환망 프로토콜 (물리 - 프레임 - 패킷 계층). LAPB 사용.
- **TCP/IP:**
  - **응용 계층:** FTP, SMTP, HTTP, DNS 등.
  - **전송 계층:** 
    - **TCP:** 연결형, 신뢰성 보장, 순서/흐름 제어, 스트림 전송.
    - **UDP:** 비연결형, 빠른 전송.
  - **인터넷 계층:** 
    - **IP:** 비연결형(데이터그램), 경로 선택(Routing).
    - **ICMP:** IP 오류 처리 및 제어 메시지.
    - **ARP:** IP → MAC / **RARP:** MAC → IP.
  - **네트워크 액세스 계층:** 이더넷, X.25, RS-232C.
- **Tiếng Việt:** 
  - TCP: Tin cậy, hướng kết nối. UDP: Nhanh, không kết nối.
  - IP: Định tuyến. ICMP: Báo lỗi mạng. ARP: Đổi IP sang MAC.

# 정보처리기사 (Information Processing Engineer) - Part 2
