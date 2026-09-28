# 네트워크 프로토콜 및 장비 심화 (Network Protocols & Devices - Advanced)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **네트워크 프로토콜 및 장비 심화 (Network Protocols & Devices - Advanced)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

네트워크, 프로토콜, 장비, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **네트워크 통신 (Network Communication)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **088. 인터넷 구성과 네트워크 - OSI 7계층 (OSI 7 Layer)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **네트워크 프로토콜 및 장비 심화 (Network Protocols & Devices - Advanced)** và nối nó với **088. 인터넷 구성과 네트워크 - OSI 7계층 (OSI 7 Layer)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 네트워크 프로토콜 및 장비 심화 (Network Protocols & Devices - Advanced)
### 서브네팅 및 IP 클래스 (Subnetting & IP Classes)
- **A lớp (class / 클래스)**: 0~127. 대형 통신망 (Mạng rất lớn).
- **B lớp (class / 클래스)**: 128~191. 중대형 통신망 (Mạng trung-lớn).
- **C lớp (class / 클래스)**: 192~223. 소규모 통신망 (Mạng nhỏ).
- **D lớp (class / 클래스)**: 224~239. 멀티캐스트 (Multicast).
- **서브네팅 (Subnetting)**: 서브넷 마스크를 이용해 네트워크 주소를 분할. (Dùng Subnet Mask để chia nhỏ mạng).

### 계층별 주요 프로토콜 (Major Protocols by Layer / Giao thức theo tầng)
- **응용 계층 (Application)**: FTP (파일 전송), SMTP (메일), TELNET (원격 접속), SNMP (네트워크 관리), DNS (도메인-IP 변환), HTTP (웹 문서).
- **전송 계층 (Transport)**: TCP (신뢰성), UDP (빠른 속도), RTCP (실시간 제어).
- **네트워크/인터넷 계층 (Network/Internet)**: IP (주소 지정, 비연결형), ICMP (오류 제어 메시지), IGMP (멀티캐스트 그룹 관리), ARP (IP -> MAC), RARP (MAC -> IP).
- **데이터 링크 계층 (Data Link)**: Ethernet, HDLC, X.25.
  - 💡 *Mẹo ghi nhớ*: ARP = "A"ddress Resolution (Tìm MAC từ IP). RARP = "R"everse (Ngược lại).

### 네트워크 장비 (Network Devices - Bổ sung)
- **게이트웨이 (Gateway)**: 다른 네트워크로부터 데이터를 주고받는 출입구 역할, 프로토콜 구조가 다른 네트워크 연결. (Cổng ra vào giữa các mạng có giao thức hoàn toàn khác nhau).
- **NIC (Network Interface Card)**: 랜카드, 컴퓨터를 네트워크에 연결. (Card mạng).
