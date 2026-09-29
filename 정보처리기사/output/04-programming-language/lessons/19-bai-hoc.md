# 배열 심화 (Arrays - Advanced)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **배열 심화 (Arrays - Advanced)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **배열 심화 (Arrays - Advanced)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **배열과 포인터 심화 (Arrays & Pointers - Advanced)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

배열, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)**에서 만든 기준을 이어받아 **배열 심화 (Arrays - Advanced)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **배열 심화 (Arrays - Advanced)** và nối nó với **배열과 포인터 심화 (Arrays & Pointers - Advanced)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 배열 심화 (Arrays - Advanced)

Ở bước 19/78, **배열 심화 (Arrays - Advanced)** xuất hiện như phần tiếp nối của **구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **배열 심화 (Arrays - Advanced)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **258. 배열과 1차원 배열 (Array & 1D Array / Mảng 1 chiều - Bổ sung)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **258. 배열과 1차원 배열 (Array & 1D Array / Mảng 1 chiều - Bổ sung)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 258. 배열과 1차원 배열 (Array & 1D Array / Mảng 1 chiều - Bổ sung)

Bây giờ ta đi vào nội dung của **258. 배열과 1차원 배열 (Array & 1D Array / Mảng 1 chiều - Bổ sung)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 배열은 행 우선으로 데이터가 할당된다. (Mảng được cấp phát theo thứ tự ưu tiên hàng).
- 첨자 없이 배열 이름을 사용하면 첫 번째 요소의 주소를 지정하는 것과 같다. (Tên mảng không có chỉ số chính là địa chỉ phần tử đầu tiên).
  - *Example / Ví dụ*: Khởi tạo mảng bằng `for` loop: `for(i=0; i<5; i++) a[i] = i+10;`
  - 💡 *Mẹo ghi nhớ*: Mảng trong C/Java đếm từ 0.

Với **258. 배열과 1차원 배열 (Array & 1D Array / Mảng 1 chiều - Bổ sung)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **258. 배열과 1차원 배열 (Array & 1D Array / Mảng 1 chiều - Bổ sung)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **259. 2차원 배열 (2D Array / Mảng 2 chiều - Bổ sung)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **259. 2차원 배열 (2D Array / Mảng 2 chiều - Bổ sung)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 259. 2차원 배열 (2D Array / Mảng 2 chiều - Bổ sung)

Phần nguồn của **259. 2차원 배열 (2D Array / Mảng 2 chiều - Bổ sung)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 변수들을 평면, 즉 행과 열로 조합한 배열. (Mảng kết hợp hàng và cột).
- 형식: `자료형 변수명[행개수][열개수]`
  - *Example / Ví dụ*: `int b[3][3];` (Mảng 3 hàng, 3 cột. Chỉ số hàng 0-2, cột 0-2).
  - Sử dụng vòng lặp lồng nhau (Nested loops) để gán giá trị: `for(i=0; i<3; i++) { for(j=0; j<4; j++) { a[i][j] = ++k; } }`
  - 💡 *Mẹo ghi nhớ*: Array 2D giống như ma trận Toán học. `i` là hàng (bên ngoài), `j` là cột (bên trong).

Với **259. 2차원 배열 (2D Array / Mảng 2 chiều - Bổ sung)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **259. 2차원 배열 (2D Array / Mảng 2 chiều - Bổ sung)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **배열 심화 (Arrays - Advanced)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **배열과 포인터 심화 (Arrays & Pointers - Advanced)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.