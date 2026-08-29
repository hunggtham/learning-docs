# 089. IP와 서브네팅, IPv4 vs IPv6 (IP & Subnetting)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **089. IP와 서브네팅, IPv4 vs IPv6 (IP & Subnetting)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

서브네팅, IPv4, IPv6

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 089. IP와 서브네팅, IPv4 vs IPv6 (IP & Subnetting)
- **IPv4 헤더 필드**: Version, Header Length, TOS, Total Length, TTL (수명), Source/Destination Address 등.
- **IPv4 클래스**:
  - Class A: `0.~` (거대 망)
  - Class B: `128.~` (중형 망)
  - Class C: `192.~` (소형 망)
- **IPv4 vs IPv6**:
  - 주소 길이: IPv4(32비트) -> **IPv6(128비트)** 확장.
  - IPv6 특징: 호스트 주소 자동 설정, 패킷 크기 제한 없음, 헤더 단순화, **보안(인증/무결성) 강화**, 플로 레이블링(QoS), 이동성 지원.
- **데이터 전송 방법**:
  - **유니캐스트 (Unicast)**: 1:1 통신.
  - **멀티캐스트 (Multicast)**: 1:N (특정 그룹).
  - **브로드캐스트 (Broadcast)**: 1:전체 (IPv4에서만 사용, 과부하 원인).
  - **애니캐스트 (Anycast)**: 1:가장 가까운 1개 노드 (IPv6에서 도입).

**Giải thích (Vietnamese):**
IPv4 sắp hết số (vì chỉ có 32 bit = khoảng 4 tỷ địa chỉ). Nên người ta sinh ra IPv6 (128 bit = số lượng vô hạn). IPv6 bảo mật tốt hơn, không cần cấu hình DHCP phức tạp (tự gán địa chỉ) và loại bỏ Broadcast để tránh nghẽn mạng.

**💡 Mẹo ghi nhớ (Mnemonics):**
Các kiểu truyền:
- Unicast = Nói chuyện riêng.
- Multicast = Nhắn tin vào group chat Zalo.
- Broadcast = Cầm loa hét cho cả trường nghe (Chỉ IPv4).
- Anycast = Gọi tổng đài, ai rảnh thì nhấc máy nghe trước (Chỉ IPv6).

---
