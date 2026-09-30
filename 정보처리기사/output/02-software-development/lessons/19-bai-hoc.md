# 082: 선택 정렬 (Selection Sort)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **082: 선택 정렬 (Selection Sort)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **082: 선택 정렬 (Selection Sort)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **083: 버블 정렬 (Bubble Sort)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

선택, 정렬

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **081-2: 셸 정렬 (Shell Sort)**에서 만든 기준을 이어받아 **082: 선택 정렬 (Selection Sort)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **082: 선택 정렬 (Selection Sort)** và nối nó với **083: 버블 정렬 (Bubble Sort)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 082: 선택 정렬 (Selection Sort)

Ở bước 19/101, **082: 선택 정렬 (Selection Sort)** xuất hiện như phần tiếp nối của **081-2: 셸 정렬 (Shell Sort)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **082: 선택 정렬 (Selection Sort)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “082: 선택 정렬 (Selection Sort)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **최소값(Minimum)**을 찾아 첫 번째 위치에 놓고, 남은 것 중 또 최소값을 찾아 두 번째 위치에 놓는 방식. (Tìm phần tử nhỏ nhất đổi chỗ lên đầu, tiếp tục tìm số nhỏ nhì đổi chỗ lên thứ hai...).
- **시간 복잡도:** O(n²) (Luôn luôn).
- **Từ khóa:** "최소값을 찾아..." (Tìm giá trị nhỏ nhất...).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Selection = Đi "chọn" thằng nhỏ nhất mang lên đầu.

---

Như vậy, **082: 선택 정렬 (Selection Sort)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **083: 버블 정렬 (Bubble Sort)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.