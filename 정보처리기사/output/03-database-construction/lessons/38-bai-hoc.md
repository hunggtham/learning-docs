# 201-203. 스토리지 시스템 (Storage Systems)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **201-203. 스토리지 시스템 (Storage Systems)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **201-203. 스토리지 시스템 (Storage Systems)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **198. 암호화 심화 (Encryption Deep Dive)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

스토리지, 시스템

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)**에서 만든 기준을 이어받아 **201-203. 스토리지 시스템 (Storage Systems)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 201-203. 스토리지 시스템 (Storage Systems)

Sau khi đã đặt nền bằng **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)**, ta chuyển sang **201-203. 스토리지 시스템 (Storage Systems)**. Đây là mắt xích 38/55 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **201-203. 스토리지 시스템 (Storage Systems)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **DAS (Direct Attached Storage):** 서버와 저장장치를 전용 케이블로 직접 연결. (외장하드 방식). 확장성 떨어짐.
- **NAS (Network Attached Storage):** 네트워크를 통해 연결. 파일 공유 가능, 확장성 우수.
- **SAN (Storage Area Network):** 서버와 저장장치를 연결하는 전용 네트워크 구성. (광 채널 스위치). DAS의 속도 + NAS의 공유 장점.
- **VI (Vietnamese) (Tiếng Việt):** Hệ thống lưu trữ.
  - DAS: Kết nối trực tiếp (cáp).
  - NAS: Kết nối qua mạng LAN (chia sẻ file).
  - SAN: Mạng lưu trữ chuyên dụng (tốc độ cao + chia sẻ).

Ta có thể khép mục **201-203. 스토리지 시스템 (Storage Systems)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **198. 암호화 심화 (Encryption Deep Dive)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.