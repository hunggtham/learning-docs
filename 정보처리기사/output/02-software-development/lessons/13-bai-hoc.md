# 080: 수식의 표기법 (Expression Notation)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **080: 수식의 표기법 (Expression Notation)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối expression notation với infix, prefix, postfix và stack, để cú pháp được chuyển thành thứ tự thực thi.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **080: 수식의 표기법 (Expression Notation)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **080: 수식의 표기법 (Expression Notation)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **6. 정렬 알고리즘 (Sorting Algorithms)** khi chuyển sang phần tiếp theo.

Mục tiêu vừa đặt expression notation vào mối quan hệ giữa cú pháp và thứ tự thực thi. Phần **핵심 키워드 (Từ khóa)** sau đây giữ lại các thuật ngữ để phân biệt infix, prefix và postfix trước khi nối chúng với cây và stack.

## 핵심 키워드 (Từ khóa)

수식의, 표기법

Các từ khóa cho thấy ba cách viết chỉ khác vị trí toán tử nhưng dẫn đến cách duyệt và cách tính khác nhau. Phần **선행·연결 개념 (Kiến thức liên kết)** sẽ nối quy tắc đó với phép chuyển đổi ở bài trước.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **5. 수식의 표기법 변환 (Expression Notation Conversion)**에서 만든 기준을 이어받아 **080: 수식의 표기법 (Expression Notation)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

Sau khi nối các dạng biểu thức với quy tắc chuyển đổi, **읽는 방법 (Cách đọc)** sẽ hướng dẫn theo dõi ưu tiên, ngoặc và vị trí toán tử để thấy vì sao postfix phù hợp với stack.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

Với trình tự đọc vừa xác lập, phần **080: 수식의 표기법 (Expression Notation)** áp dụng các quy tắc vào chuyển infix sang postfix và giải thích vai trò của stack. Hãy giữ quan hệ giữa biểu thức và cấu trúc dữ liệu khi chuyển sang sorting.

## 080: 수식의 표기법 (Expression Notation)

Ở bước 13/101, **080: 수식의 표기법 (Expression Notation)** xuất hiện như phần tiếp nối của **5. 수식의 표기법 변환 (Expression Notation Conversion)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **080: 수식의 표기법 (Expression Notation)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Chuyển đổi biểu thức toán học tương ứng với duyệt cây.
- **Infix (Trung tố):** `A + B` (Giống Inorder).
- **Prefix (Tiền tố):** `+ A B` (Giống Preorder).
- **Postfix (Hậu tố):** `A B +` (Giống Postorder - Máy tính rất thích kiểu này vì dùng Stack tính cực dễ).

Trước hết, ta đặt **Cách chuyển đổi Infix sang Postfix** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **Cách chuyển đổi Infix sang Postfix** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### Cách chuyển đổi Infix sang Postfix

Bây giờ ta đi vào nội dung của **Cách chuyển đổi Infix sang Postfix**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

1. Đóng ngoặc toàn bộ theo thứ tự ưu tiên: `A / B * (C + D)` -> `((A / B) * (C + D))`
2. Kéo Dấu toán tử ra phía **SAU** dấu ngoặc của nó: `((A B /) (C D +) *)`
3. Xóa ngoặc: `A B / C D + *`

- **Vietnamese Explanation:** Máy tính không hiểu `A+B*C` vì nó không biết cái nào ưu tiên trước. Nó dùng Postfix `A B C * +` ném vào Stack để tính một lèo không cần ngoặc.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Postfix = Dấu nằm ở cuối cụm. Prefix = Dấu nằm ở đầu cụm.

---

Với **Cách chuyển đổi Infix sang Postfix**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **Cách chuyển đổi Infix sang Postfix**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức, với đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Như vậy, **080: 수식의 표기법 (Expression Notation)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **6. 정렬 알고리즘 (Sorting Algorithms)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **080: 수식의 표기법 (Expression Notation)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
