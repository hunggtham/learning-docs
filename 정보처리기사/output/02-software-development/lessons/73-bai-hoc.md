# 18. 최악의 시간 복잡도 (Worst-case Time Complexity)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **18. 최악의 시간 복잡도 (Worst-case Time Complexity)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **18. 최악의 시간 복잡도 (Worst-case Time Complexity)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **19. 클린 코드 작성 원칙 (Clean Code Principles)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

최악의, 시간, 복잡도

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **14. 파레토 법칙 (Pareto Principle)**에서 만든 기준을 이어받아 **18. 최악의 시간 복잡도 (Worst-case Time Complexity)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **18. 최악의 시간 복잡도 (Worst-case Time Complexity)** và nối nó với **19. 클린 코드 작성 원칙 (Clean Code Principles)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 18. 최악의 시간 복잡도 (Worst-case Time Complexity)

Ở bước 73/95, **18. 최악의 시간 복잡도 (Worst-case Time Complexity)** xuất hiện như phần tiếp nối của **14. 파레토 법칙 (Pareto Principle)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **18. 최악의 시간 복잡도 (Worst-case Time Complexity)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **O(1)**, **O(n log n)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **O(1)**: 입력값 크기에 관계 없이 일정. (스택 삽입/삭제).
* **O(n log n)**: n log n번 수행. (힙 정렬, 병합 정렬).
* **VI (Vietnamese) (Tiếng Việt):** Độ phức tạp thời gian. O(1) là hằng số, O(n log n) cho Heap/Merge sort.
* **Example**: 데이터가 아무리 많아도 스택의 최상단에 값을 넣는 것은 1번의 연산만 필요하므로 O(1)입니다.

Như vậy, **18. 최악의 시간 복잡도 (Worst-case Time Complexity)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **19. 클린 코드 작성 원칙 (Clean Code Principles)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.