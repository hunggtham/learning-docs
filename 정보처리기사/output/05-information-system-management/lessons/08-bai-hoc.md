# 5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

네트워크, 인프라, 기술

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)

### 5.1 신기술 동향 (New Technologies)
- **SDN (Software Defined Networking):** 네트워크를 가상화하여 소프트웨어로 제어/관리.
- **SDS (Software-Defined Storage):** 물리적 스토리지를 가상화하여 하나처럼 관리.
- **SDDC (Software Defined Data Center):** 데이터 센터의 모든 자원을 가상화하여 소프트웨어 조작만으로 자동 제어.
- **클라우드 기반 HSM:** 클라우드 기반 암호화 키 생성/처리 하드웨어 보안기기.
- **파스-타 (PaaS-TA):** 개발 환경을 제공하는 개방형 클라우드 플랫폼.
- **징 (Zing):** 10cm 이내에서 3.5Gbps 속도의 초고속 근접무선통신.
- **스마트 그리드 (Smart Grid):** 전력선을 기반으로 효율적 에너지 관리 통합 시스템.
- **SSO (Single Sign On):** 한 번 로그인으로 여러 사이트 이용.
- **메시 네트워크 (Mesh Network):** 여러 디바이스를 그물망처럼 유기적으로 연결.
- **피코넷 (PICONET):** 블루투스/UWB 기술로 형성하는 독립적 무선망.
- **Tiếng Việt:** 
  - SDN/SDS/SDDC: Ảo hóa và điều khiển mạng/lưu trữ/trung tâm dữ liệu bằng phần mềm.
  - PaaS-TA: Nền tảng cloud mở của Hàn Quốc.
  - SSO: Đăng nhập một lần.
  - Zing: Giao tiếp không dây tầm cực gần, tốc độ cao.

### 5.2 LAN 표준 및 위상 (LAN Standards & Topology)
- **CSMA/CD:** IEEE 802.3 유선 LAN 매체 접속 제어 방식 (충돌 감지).
- **CSMA/CA:** 무선 랜(WLAN) 데이터 전송 시 충돌을 피하기 위해 일정 시간 기다림 (충돌 회피).
- **WPA (Wi-Fi Protected Access):** 무선 랜 인증/암호화 표준.
- **802.11e:** QoS 기능 지원을 위해 MAC 계층 수정.
- **버스형 (Bus Topology):** 한 통신 회선에 여러 단말장치 연결.
- **VLAN (Virtual LAN):** 물리적 배치와 무관하게 논리적으로 네트워크 분리.
- **WDM (Wavelength Division Multiplexing):** 파장이 다른 광선을 이용해 동시 통신 (광다중화).
- **Tiếng Việt:** 
  - CSMA/CD: Phát hiện xung đột (Mạng có dây).
  - CSMA/CA: Tránh xung đột (Mạng không dây).
  - VLAN: Mạng LAN ảo, phân chia logic không phụ thuộc vật lý.

### 5.3 라우팅 프로토콜 및 흐름 제어 (Routing Protocols & Flow Control)
- **ARP (Address Resolution Protocol):** IP 주소를 MAC 주소로 변환.
- **RIP (Routing Information Protocol):** 거리 벡터 라우팅 (최대 홉 15 제한).
- **OSPF (Open Shortest Path First):** 링크 상태 기반 최단 경로 라우팅 (대규모 망).
- **흐름 제어 - 정지-대기 (Stop-and-Wait):** 수신 측의 ACK(확인 신호)를 받은 후 다음 패킷 전송.
- **Tiếng Việt:** 
  - ARP: IP -> MAC.
  - RIP: Dựa trên số Hop (tối đa 15).
  - OSPF: Dựa trên trạng thái Link, tìm đường ngắn nhất.
  - Stop-and-Wait: Chờ phản hồi (ACK) rồi mới gửi tiếp.
