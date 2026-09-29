# 18. 최악의 시간 복잡도 (Worst-case Time Complexity)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **18. 최악의 시간 복잡도 (Worst-case Time Complexity)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **18. 최악의 시간 복잡도 (Worst-case Time Complexity)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **19. 클린 코드 작성 원칙 (Clean Code Principles)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

최악의, 시간, 복잡도

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **14. 파레토 법칙 (Pareto Principle)**에서 만든 기준을 이어받아 **18. 최악의 시간 복잡도 (Worst-case Time Complexity)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 18. 최악의 시간 복잡도 (Worst-case Time Complexity)

Từ **14. 파레토 법칙 (Pareto Principle)**, ta đã có điểm tựa để bước vào **18. 최악의 시간 복잡도 (Worst-case Time Complexity)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 72/95 trước khi đi vào chi tiết.

Để đọc **18. 최악의 시간 복잡도 (Worst-case Time Complexity)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **O(1)**, **O(n log n)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **O(1)**: 입력값 크기에 관계 없이 일정. (스택 삽입/삭제).
* **O(n log n)**: n log n번 수행. (힙 정렬, 병합 정렬).
* **VI (Vietnamese) (Tiếng Việt):** Độ phức tạp thời gian. O(1) là hằng số, O(n log n) cho Heap/Merge sort.
* **Example**: 데이터가 아무리 많아도 스택의 최상단에 값을 넣는 것은 1번의 연산만 필요하므로 O(1)입니다.

Điểm chốt của **18. 최악의 시간 복잡도 (Worst-case Time Complexity)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **19. 클린 코드 작성 원칙 (Clean Code Principles)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.