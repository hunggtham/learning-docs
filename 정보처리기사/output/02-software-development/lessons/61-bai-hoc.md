# 127 ~ 129: 화이트박스 테스트 (White Box Test)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **127 ~ 129: 화이트박스 테스트 (White Box Test)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **127 ~ 129: 화이트박스 테스트 (White Box Test)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **130 & 131: 블랙박스 테스트 (Black Box Test)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

화이트박스, 테스트

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)**에서 만든 기준을 이어받아 **127 ~ 129: 화이트박스 테스트 (White Box Test)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 127 ~ 129: 화이트박스 테스트 (White Box Test)

Ở bước 61/95, **127 ~ 129: 화이트박스 테스트 (White Box Test)** xuất hiện như phần tiếp nối của **120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **127 ~ 129: 화이트박스 테스트 (White Box Test)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- 내부 로직과 제어 구조를 직접 관찰. (Test dựa trên mã nguồn (Source Code). Nhìn thấu bên trong).
- **종류 (Các kỹ thuật):** 기초 경로 (Đường dẫn cơ bản), 조건 (Điều kiện), 루프 (Vòng lặp), 데이터 흐름 (Luồng dữ liệu).
- **검증 기준 (Coverage - Mức độ bao phủ):**
  - **문장 검증 (Statement):** Mọi dòng code phải chạy qua 1 lần.
  - **분기/결정 검증 (Branch/Decision):** Mọi nhánh lệnh (If True / False) phải chạy qua 1 lần.
  - **조건 검증 (Condition):** Mọi biểu thức điều kiện con bên trong If phải kiểm tra T/F.

- 💡 **Mẹo ghi nhớ (Mnemonics):** White Box = Code (Câu lệnh, Rẽ nhánh, Vòng lặp). Do Dev tự làm.

---

Như vậy, **127 ~ 129: 화이트박스 테스트 (White Box Test)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **130 & 131: 블랙박스 테스트 (Black Box Test)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.