# 배열 심화 (Arrays - Advanced)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **배열 심화 (Arrays - Advanced)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **배열 심화 (Arrays - Advanced)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **배열과 포인터 심화 (Arrays & Pointers - Advanced)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

배열, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)**에서 만든 기준을 이어받아 **배열 심화 (Arrays - Advanced)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 배열 심화 (Arrays - Advanced)

Sau khi đã đặt nền bằng **구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)**, ta chuyển sang **배열 심화 (Arrays - Advanced)**. Đây là mắt xích 20/77 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **배열 심화 (Arrays - Advanced)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **258. 배열과 1차원 배열 (Array & 1D Array / Mảng 1 chiều - Bổ sung)**. Hãy xác định **258. 배열과 1차원 배열 (Array & 1D Array / Mảng 1 chiều - Bổ sung)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 258. 배열과 1차원 배열 (Array & 1D Array / Mảng 1 chiều - Bổ sung)

Phần nguồn của **258. 배열과 1차원 배열 (Array & 1D Array / Mảng 1 chiều - Bổ sung)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 배열은 행 우선으로 데이터가 할당된다. (Mảng được cấp phát theo thứ tự ưu tiên hàng).
- 첨자 없이 배열 이름을 사용하면 첫 번째 요소의 주소를 지정하는 것과 같다. (Tên mảng không có chỉ số chính là địa chỉ phần tử đầu tiên).
  - *Example / Ví dụ*: Khởi tạo mảng bằng `for` loop: `for(i=0; i<5; i++) a[i] = i+10;`
  - 💡 *Mẹo ghi nhớ*: Mảng trong C/Java đếm từ 0.

Với **258. 배열과 1차원 배열 (Array & 1D Array / Mảng 1 chiều - Bổ sung)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **258. 배열과 1차원 배열 (Array & 1D Array / Mảng 1 chiều - Bổ sung)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **259. 2차원 배열 (2D Array / Mảng 2 chiều - Bổ sung)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **259. 2차원 배열 (2D Array / Mảng 2 chiều - Bổ sung)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 259. 2차원 배열 (2D Array / Mảng 2 chiều - Bổ sung)

Các ý ngay dưới **259. 2차원 배열 (2D Array / Mảng 2 chiều - Bổ sung)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 변수들을 평면, 즉 행과 열로 조합한 배열. (Mảng kết hợp hàng và cột).
- 형식: `자료형 변수명[행개수][열개수]`
  - *Example / Ví dụ*: `int b[3][3];` (Mảng 3 hàng, 3 cột. Chỉ số hàng 0-2, cột 0-2).
  - Sử dụng vòng lặp lồng nhau (Nested loops) để gán giá trị: `for(i=0; i<3; i++) { for(j=0; j<4; j++) { a[i][j] = ++k; } }`
  - 💡 *Mẹo ghi nhớ*: Array 2D giống như ma trận Toán học. `i` là hàng (bên ngoài), `j` là cột (bên trong).

Với **259. 2차원 배열 (2D Array / Mảng 2 chiều - Bổ sung)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **259. 2차원 배열 (2D Array / Mảng 2 chiều - Bổ sung)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **배열 심화 (Arrays - Advanced)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **배열과 포인터 심화 (Arrays & Pointers - Advanced)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.