# 6. 정렬 알고리즘 (Sorting Algorithms)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **6. 정렬 알고리즘 (Sorting Algorithms)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **6. 정렬 알고리즘 (Sorting Algorithms)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **31. 추가 정렬 알고리즘 (Additional Sorting Algorithms)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

정렬, 알고리즘

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **5. 수식의 표기법 변환 (Expression Notation Conversion)**에서 만든 기준을 이어받아 **6. 정렬 알고리즘 (Sorting Algorithms)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 6. 정렬 알고리즘 (Sorting Algorithms)

Ở bước 10/95, **6. 정렬 알고리즘 (Sorting Algorithms)** xuất hiện như phần tiếp nối của **5. 수식의 표기법 변환 (Expression Notation Conversion)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **6. 정렬 알고리즘 (Sorting Algorithms)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **삽입 정렬 (Insertion Sort)**, **선택 정렬 (Selection Sort)**, **버블 정렬 (Bubble Sort)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **삽입 정렬 (Insertion Sort)**: 두 번째 값부터 시작해 앞의 값들과 비교하여 알맞은 위치에 삽입.
* **선택 정렬 (Selection Sort)**: 가장 작은 값을 선택해 첫 번째와 교환, 그 다음 작은 값을 두 번째와 교환하는 방식.
* **버블 정렬 (Bubble Sort)**: 인접한 두 값을 비교하여 큰 값을 뒤로 보내는 과정을 반복.
* **VI (Vietnamese) (Tiếng Việt):**
  * Insertion: Chèn phần tử vào đúng vị trí của dãy đã sắp xếp.
  * Selection: Chọn phần tử nhỏ nhất đưa lên đầu.
  * Bubble: Nổi bọt, so sánh 2 phần tử kề nhau, lớn hơn thì đổi chỗ.
* **Example**: `8, 5, 6` 버블 정렬 1회전: 5, 8, 6 -> 5, 6, 8. (Bubble sort đổi chỗ 8 và 5, rồi 8 và 6).
* 💡 **Mẹo ghi nhớ**: Insertion: bốc bài và chèn. Selection: tìm người lùn nhất xếp hàng. Bubble: bong bóng lớn nổi lên cuối cùng.

Như vậy, **6. 정렬 알고리즘 (Sorting Algorithms)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **31. 추가 정렬 알고리즘 (Additional Sorting Algorithms)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.