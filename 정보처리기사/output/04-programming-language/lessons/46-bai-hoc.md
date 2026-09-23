# 088. 인터넷 구성과 네트워크 - OSI 7계층 (OSI 7 Layer)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **088. 인터넷 구성과 네트워크 - OSI 7계층 (OSI 7 Layer)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

인터넷, 구성과, 네트워크, OSI, 계층

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 088. 인터넷 구성과 네트워크 - OSI 7계층 (OSI 7 Layer)
- **IEEE 802 표준**: 802.3 (Ethernet, 유선랜), 802.11 (무선랜, Wi-Fi).
- **OSI 7계층 (상위 계층부터)**:
  7. **응용 계층 (Application)**: 사용자 인터페이스. (HTTP, FTP, DNS) - 데이터 단위: Data.
  6. **표현 계층 (Presentation)**: 암호화, 압축, 포맷 변환. - 데이터 단위: Data.
  5. **세션 계층 (Session)**: 응용 프로그램 간 논리적 연결 생성/유지. - 데이터 단위: Data.
  4. **전송 계층 (Transport)**: 종단 간(End-to-End) 신뢰성 있는 전송. 포트 번호 사용. (TCP, UDP). 장비: L4 스위치. - 데이터 단위: Segment.
  3. **네트워크 계층 (Network)**: 경로 설정(Routing). IP 주소 사용. (IP, ICMP, ARP). 장비: 라우터, L3 스위치. - 데이터 단위: Packet.
  2. **데이터 링크 계층 (Data Link)**: 인접 노드 간 전송 제어, 오류/흐름 제어. MAC 주소 사용. (HDLC, PPP). 장비: 브리지, L2 스위치. - 데이터 단위: Frame.
  1. **물리 계층 (Physical)**: 전기적 신호 전송. 장비: 허브, 리피터. - 데이터 단위: Bit.

**Giải thích (Vietnamese):**
Mô hình OSI 7 lớp chia nhỏ quá trình gửi dữ liệu qua mạng.
Tầng 1 (Cáp mạng, dây điện), Tầng 2 (Truyền giữa 2 máy tính kề nhau qua địa chỉ MAC), Tầng 3 (Tìm đường đi trên mạng Internet qua IP), Tầng 4 (Đảm bảo gói tin không bị rớt qua TCP/UDP), Tầng 5-7 (Phần mềm xử lý hiển thị lên màn hình).

**💡 Mẹo ghi nhớ (Mnemonics):**
Tên 7 tầng từ dưới lên (1->7): **물데네 전세표응** (Vật - Dữ - Mạng - Truyền - Phiên - Biểu - Ứng).
Đơn vị dữ liệu (1->4): **비프패세** (Bit, Frame, Packet, Segment).

---
