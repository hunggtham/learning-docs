# 기본 프로토콜 (Basic Protocols)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **기본 프로토콜 (Basic Protocols)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

기본, 프로토콜

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 기본 프로토콜 (Basic Protocols)
* **ARP**: 호스트의 IP 주소(논리 주소)를 호스트와 연결된 네트워크 접속장치의 물리적 주소(MAC Address)로 변환함.
  * *Tiếng Việt*: Chuyển đổi địa chỉ IP (địa chỉ logic) của máy chủ thành địa chỉ vật lý (MAC Address) của thiết bị kết nối mạng.
  * *Ví dụ (Example)*: 컴퓨터가 IP 192.168.1.5의 MAC 주소를 찾을 때 ARP를 사용합니다. (Máy tính sử dụng ARP để tìm địa chỉ MAC của IP 192.168.1.5)
  * 💡 *Mnemonic*: **A**ddress **R**esolution (IP -> MAC)
* **RARP**: 물리적 주소를 IP 주소(논리 주소)로 변환함.
  * *Tiếng Việt*: Chuyển đổi địa chỉ vật lý thành địa chỉ IP (địa chỉ logic).
  * 💡 *Mnemonic*: **R**everse ARP (MAC -> IP)
* **RTCP**: 실시간 전송 프로토콜(RTP)이 안정되게 기능을 유지하도록 데이터 전송을 모니터링하고 최소한의 제어와 인증 기능을 제공함.
  * *Tiếng Việt*: Giám sát truyền dữ liệu và cung cấp chức năng điều khiển, xác thực tối thiểu để duy trì ổn định RTP.
* **WAP**: 이동 단말이나 PDA 등 소형 무선 단말기에서 인터넷을 이용할 수 있도록 해주는 프로토콜.
  * *Tiếng Việt*: Giao thức cho phép sử dụng internet trên các thiết bị không dây nhỏ như điện thoại di động, PDA.
* **PPP**: 주로 두 개의 라우터를 접속할 때 사용되며, 오류 검출 기능만 제공됨.
  * *Tiếng Việt*: Chủ yếu dùng để kết nối 2 router, chỉ cung cấp chức năng phát hiện lỗi (không phục hồi/điều khiển luồng).
* **UDP (User Datagram Protocol)**: 데이터 전송 전에는 연결을 설정하지 않는 비연결형 서비스. 오버헤드가 적고 실시간 전송에 유리.
  * *Tiếng Việt*: Dịch vụ không kết nối (không thiết lập kết nối trước khi truyền). Ít overhead, thuận lợi cho truyền thời gian thực (tốc độ quan trọng hơn độ tin cậy).
  * *Ví dụ*: 실시간 스트리밍(Video streaming)에 주로 사용됩니다. (Thường dùng cho phát video trực tiếp).

---
