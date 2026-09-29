# 핵심 041: 테스트 케이스 / 시나리오 / 오라클 (Test Case/Scenario/Oracle)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **핵심 041: 테스트 케이스 / 시나리오 / 오라클 (Test Case/Scenario/Oracle)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **핵심 041: 테스트 케이스 / 시나리오 / 오라클 (Test Case/Scenario/Oracle)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **핵심 042: 블랙박스 테스트 / 화이트박스 테스트 (Black-Box vs White-Box)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

핵심, 테스트, 케이스, 시나리오, 오라클

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **핵심 040: 애플리케이션 테스트 원리 및 종류 (Test Principles & Types)**에서 만든 기준을 이어받아 **핵심 041: 테스트 케이스 / 시나리오 / 오라클 (Test Case/Scenario/Oracle)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 핵심 041: 테스트 케이스 / 시나리오 / 오라클 (Test Case/Scenario/Oracle)

Từ **핵심 040: 애플리케이션 테스트 원리 및 종류 (Test Principles & Types)**, ta đã có điểm tựa để bước vào **핵심 041: 테스트 케이스 / 시나리오 / 오라클 (Test Case/Scenario/Oracle)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 54/95 trước khi đi vào chi tiết.

Để đọc **핵심 041: 테스트 케이스 / 시나리오 / 오라클 (Test Case/Scenario/Oracle)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **테스트 케이스 (Test Case):** Một bộ gồm: Dữ liệu đầu vào, Điều kiện chạy, Kết quả mong đợi.
- **테스트 시나리오 (Test Scenario):** Kịch bản gồm nhiều Test Case nối tiếp nhau.
- **테스트 오라클 (Test Oracle):** Tiêu chuẩn/Cơ chế để tự động đánh giá kết quả test là Đúng hay Sai (True/False).
  - **참 (True):** Kiểm tra 100% mọi trường hợp (Dùng cho máy bay, y tế).
  - **샘플링 (Sampling):** Lấy mẫu ngẫu nhiên vài test case.
  - **추정 (Heuristic):** Lấy mẫu vài cái chắc chắn, còn lại thì dùng logic ước lượng (Heuristic).
  - **일관성 검사 (Consistent):** Kiểm tra xem code cũ và mới có cho kết quả giống nhau không khi bị thay đổi (Hồi quy).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Oracle (Nhà tiên tri) = Cái để phán xét đúng/sai. True = 100%. Heuristic = Đoán.

---

Điểm chốt của **핵심 041: 테스트 케이스 / 시나리오 / 오라클 (Test Case/Scenario/Oracle)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **핵심 042: 블랙박스 테스트 / 화이트박스 테스트 (Black-Box vs White-Box)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.