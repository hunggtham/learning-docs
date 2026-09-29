# 51. 빅오 표기법 (Big-O Notation) 심화

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **51. 빅오 표기법 (Big-O Notation) 심화**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **51. 빅오 표기법 (Big-O Notation) 심화** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **52. 소스 코드 최적화와 순환 복잡도 (Source Code Optimization & Cyclomatic Complexity)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

빅오, 표기법

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **38. 릴리즈 노트 (Release Note)**에서 만든 기준을 이어받아 **51. 빅오 표기법 (Big-O Notation) 심화**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 51. 빅오 표기법 (Big-O Notation) 심화

Ở bước 82/95, **51. 빅오 표기법 (Big-O Notation) 심화** xuất hiện như phần tiếp nối của **38. 릴리즈 노트 (Release Note)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **51. 빅오 표기법 (Big-O Notation) 심화** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **O(1)**, **O(log_2 n)**, **O(n)**, **O(n log_2 n)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **O(1)**: 스택 삽입/삭제.
* **O(log_2 n)**: 이진 트리, 이진 검색 (단계가 절반씩 줄어듦).
* **O(n)**: 1중 for문.
* **O(n log_2 n)**: 힙 정렬, 2-Way 합병 정렬.
* **O(n^2)**: 삽입, 선택, 버블, 퀵 정렬(최악). 2중 for문.
* **O(2^n)**: 피보나치 수열.
* **VI (Vietnamese) (Tiếng Việt):** Độ phức tạp thuật toán Big-O. O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n).

Như vậy, **51. 빅오 표기법 (Big-O Notation) 심화** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **52. 소스 코드 최적화와 순환 복잡도 (Source Code Optimization & Cyclomatic Complexity)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.