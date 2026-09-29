# 130 & 131: 블랙박스 테스트 (Black Box Test)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **130 & 131: 블랙박스 테스트 (Black Box Test)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **130 & 131: 블랙박스 테스트 (Black Box Test)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **132 ~ 136: 개발 단계에 따른 애플리케이션 테스트 (V-Model Test Levels)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

블랙박스, 테스트

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **127 ~ 129: 화이트박스 테스트 (White Box Test)**에서 만든 기준을 이어받아 **130 & 131: 블랙박스 테스트 (Black Box Test)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 130 & 131: 블랙박스 테스트 (Black Box Test)

Sau khi đã đặt nền bằng **127 ~ 129: 화이트박스 테스트 (White Box Test)**, ta chuyển sang **130 & 131: 블랙박스 테스트 (Black Box Test)**. Đây là mắt xích 62/95 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **130 & 131: 블랙박스 테스트 (Black Box Test)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- 명세를 기초로 기능 테스트. 내부 구조 무시. (Dựa vào chức năng UI, không thèm nhìn code).
- **종류 (Các kỹ thuật):**
  - **동치 분할 (Equivalence Partitioning):** Chia vùng tương đương (Nhập đại 1 số đại diện).
  - **경계값 분석 (Boundary Value):** Test quanh cái mép (Max, Min, +1, -1). Lỗi hay nằm ở đây.
  - **원인-효과 그래프 (Cause-Effect):** Vẽ biểu đồ nhân quả.
  - **오류 예측 (Error Guessing):** Dựa vào kinh nghiệm (Kinh nghiệm Tester).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Black Box = UI, Chức năng. Các kỹ thuật thường chia theo vùng (Partition) và ranh giới (Boundary).

---

Ta có thể khép mục **130 & 131: 블랙박스 테스트 (Black Box Test)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **132 ~ 136: 개발 단계에 따른 애플리케이션 테스트 (V-Model Test Levels)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.