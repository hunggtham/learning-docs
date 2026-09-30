# 081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **081-2: 셸 정렬 (Shell Sort)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

삽입, 정렬

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **028: 정렬 (Sorting / Thuật toán sắp xếp)**에서 만든 기준을 이어받아 **081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)** và nối nó với **081-2: 셸 정렬 (Shell Sort)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)

Sau khi đã đặt nền bằng **028: 정렬 (Sorting / Thuật toán sắp xếp)**, ta chuyển sang **081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)**. Đây là mắt xích 17/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **이미 순서화된 파일(앞부분)**에 새로운 레코드를 **순서에 맞게 삽입**시켜 정렬. (Lấy phần tử hiện tại chèn vào đúng vị trí trong phần mảng đã sắp xếp phía trước nó).
- **Thời gian (Time Complexity):** O(n²) cho cả Trung bình và Tệ nhất.
- **Số vòng lặp (Pass):** Mảng có n phần tử thì chạy (n-1) vòng. Bắt đầu xét từ phần tử thứ 2.

- **Ví dụ (Example):** Xếp bài tá lả. Bạn rút một lá bài mới lên, xem trên tay bài đã xếp sẵn, thấy chỗ nào vừa thì "chèn" nó vào đó.
- 💡 **Mẹo ghi nhớ (Mnemonics):** 삽입 (Chèn) = Từ khóa "Đã được sắp xếp sẵn" (Đã sắp xếp sẵn). Luôn O(n²).

Ta có thể khép mục **081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **081-2: 셸 정렬 (Shell Sort)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.