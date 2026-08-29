# 309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

OSI, 계층과, 네트워크, 프로토콜

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)
- **응용 계층 (Application, 7계층)**: HTTP(웹), FTP(파일), SMTP(메일), DNS(도메인->IP 변환), SNMP(네트워크 관리).
- **전송 계층 (Transport, 4계층)**: 
  - **TCP**: 연결형, 신뢰성 보장, 양방향. 흐름 제어.
  - **UDP**: 비연결형, 신뢰성 낮음. 속도가 빨라 스트리밍에 유리.
- **인터넷/네트워크 계층 (Network, 3계층)**: 라우터 사용.
  - **IP**: 경로 설정.
  - **ICMP**: 오류 보고 및 제어.
  - **ARP**: IP 주소 -> MAC 주소 변환. (**RARP**는 반대).
- **데이터 링크/네트워크 액세스 계층 (Data Link, 2계층)**: Ethernet(CSMA/CD 방식), HDLC.

**Giải thích (Vietnamese):**
- **ARP**: Khi biết địa chỉ IP, dùng ARP để hỏi xem "Máy nào có IP này, cho xin địa chỉ MAC của card mạng (phần cứng)".
- **ICMP**: Lệnh `ping` hay dùng trên máy tính chính là chạy giao thức ICMP để kiểm tra mạng có thông không.

---
