# IP 주소 및 서브네팅 (IP Address & Subnetting)

## IP 주소 및 서브네팅 (IP Address & Subnetting)

### 1. IPv4 주소 (Internet Protocol version 4)
Phần “1. IPv4 주소 (Internet Protocol version 4)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 8비트씩 4부분, 총 **32비트**로 구성됩니다.
- 네트워크 크기에 따라 A~E 클래스로 나뉩니다.
  - **A Class**: 국가/대형 망 (0~127)
  - **B Class**: 중대형 망 (128~191)
  - **C Class**: 소규모 망 (192~223)
  - **D Class**: 멀티캐스트용 (224~239)
  - **E Class**: 실험적 주소

### 2. 서브네팅 (Subnetting)
할당된 네트워크 주소를 다시 여러 개의 작은 네트워크로 나누어 사용하는 기법입니다. (서브넷 마스크 활용).

### 3. IPv6 주소 (Internet Protocol version 6)
Phần “3. IPv6 주소 (Internet Protocol version 6)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- IPv4의 주소 부족 문제를 해결하기 위해 개발되었습니다.
- 16비트씩 8부분, 총 **128비트**로 구성되며 콜론(`:`)으로 구분합니다.
- 인증성, 기밀성, 무결성을 지원하여 보안이 뛰어나고, 주소 확장성과 호환성이 좋습니다.
- **주소 체계**:
  - **유니캐스트 (Unicast)**: 1 대 1 통신
  - **멀티캐스트 (Multicast)**: 1 대 다 통신
  - **애니캐스트 (Anycast)**: 1 대 1 통신 (가장 가까운 수신자에게 전송)

💡 **Mẹo ghi nhớ (Mnemonics):**
- **IPv4**: 32-bit (4 x 8).
- **IPv6**: 128-bit (8 x 16), **U.M.A** (Unicast, Multicast, Anycast).
