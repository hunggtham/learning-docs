# 5. 네트워크 통신망 및 주소 체계 (Mạng lưới & Hệ thống Địa chỉ)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **5. 네트워크 통신망 및 주소 체계 (Mạng lưới & Hệ thống Địa chỉ)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

네트워크, 통신망, 주소, 체계

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 5. 네트워크 통신망 및 주소 체계 (Mạng lưới & Hệ thống Địa chỉ)

### 5.1 LAN 및 매체 접근 제어 (LAN & MAC)
- **LAN (Local Area Network):** 단일 기관 소유, 고속 전송, 오류율 낮음.
- **IEEE 802 주요 규격:**
  - `802.1` (전체 구성), `802.2` (LLC), `802.3` (CSMA/CD), `802.4` (토큰 버스), `802.5` (토큰 링), `802.11` (무선 LAN).
- **CSMA/CD (Carrier Sense Multiple Access/Collision Detection):** 채널 사용권 경쟁. 충돌 감지. 
  - 규격 명칭 (예: `10 BASE T` - 10Mbps, 베이스밴드, 꼬임선).
  - **이더넷 (Ethernet):** CSMA/CD 방식을 사용하는 LAN.
- **Tiếng Việt:** Mạng LAN cục bộ. IEEE 802.3 là tiêu chuẩn CSMA/CD (Ethernet - phát hiện xung đột). 

### 5.2 기타 통신망 (VAN, ISDN)
- **VAN (부가 가치 통신망):** 공중 통신망을 임대해 정보 가공/변환 등 부가 가치를 첨가해 서비스 제공.
- **ISDN (종합 정보 통신망):** 음성/문자/영상을 디지털 방식으로 종합 제공.
- **Tiếng Việt:** 
  - VAN: Mạng giá trị gia tăng (thuê đường truyền, thêm dịch vụ). 
  - ISDN: Mạng số đa dịch vụ tích hợp.

### 5.3 인터넷 주소 체계 (IP Addresses)
- **IPv4:** 32비트 (8비트 × 4부분). 클래스 A~E (A: 대형 ~ C: 소규모망, D: 멀티캐스트).
- **IPv6:** 128비트 (16비트 × 8부분, 16진수, 콜론 `:` 구분). 주소 부족 문제 해결.
- **IPv4 → IPv6 전환 전략:** 듀얼 스택(Dual Stack), 터널링(Tunneling), 헤더/전송/응용 게이트웨이 변환(Translation).
- **DNS (Domain Name System):** 문자 도메인 네임을 IP 주소로 변환.
- **Tiếng Việt:** IPv4 (32 bit, Class A-E). IPv6 (128 bit, giải quyết cạn kiệt IP). DNS dịch tên miền sang IP.
- 💡 **Mẹo ghi nhớ:** Chuyển đổi IPv4/IPv6: "Dual - Tunnel - Translate".

### 5.4 네트워크 관련 장비 (Network Devices)
- **허브 (Hub):** 물리 계층, 포트 통합 관리 및 리피터 역할.
- **리피터 (Repeater):** 물리 계층, 신호 재생 및 증폭.
- **브리지 (Bridge):** 데이터 링크 계층, LAN-LAN 연결.
- **라우터 (Router):** 네트워크 계층, 경로 선택(Routing) 및 서로 다른 망 연결.
- **게이트웨이 (Gateway):** 전 계층(주로 상위), 프로토콜이 전혀 다른 네트워크 연결.
- **Tiếng Việt:** 
  - L1: Hub, Repeater (Khuếch đại tín hiệu).
  - L2: Bridge (Nối LAN).
  - L3: Router (Định tuyến).
  - L4-L7: Gateway (Nối mạng khác giao thức).
