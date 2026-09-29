# 구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **배열 심화 (Arrays - Advanced)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

구조체, 배열, 포인터

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **제어문 심화 (Control Statements - Advanced)**에서 만든 기준을 이어받아 **구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)** và nối nó với **배열 심화 (Arrays - Advanced)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)

Từ **제어문 심화 (Control Statements - Advanced)**, ta đã có điểm tựa để bước vào **구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 18/78 trước khi đi vào chi tiết.

Để đọc **구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **C언어의 구조체 (Struct in C / Cấu trúc trong C)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### C언어의 구조체 (Struct in C / Cấu trúc trong C)

Các ý ngay dưới **C언어의 구조체 (Struct in C / Cấu trúc trong C)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 자료의 종류가 다른 변수의 모임이다. (Tập hợp các biến có kiểu dữ liệu khác nhau).
- 예약어 `struct`를 이용해 정의한다. (Định nghĩa bằng từ khóa `struct`).
  - *Example / Ví dụ*: `struct Person { char name[20]; int age; };`
  - 💡 *Mẹo ghi nhớ*: Mảng (Array) lưu các giá trị cùng kiểu, Cấu trúc (Struct) lưu các giá trị khác kiểu.

Các ý về **C언어의 구조체 (Struct in C / Cấu trúc trong C)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **C언어의 구조체 (Struct in C / Cấu trúc trong C)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **177. 1차원 배열 (1D Array / Mảng 1 chiều)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **177. 1차원 배열 (1D Array / Mảng 1 chiều)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 177. 1차원 배열 (1D Array / Mảng 1 chiều)

Bây giờ ta đi vào nội dung của **177. 1차원 배열 (1D Array / Mảng 1 chiều)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 변수들을 일직선상의 개념으로 조합한 배열이다. (Tập hợp các biến trên một đường thẳng).
  - *Example / Ví dụ*: `char a[3] = {'A', 'B', 'C'};`
  - 💡 *Mẹo ghi nhớ*: Chỉ số mảng luôn bắt đầu từ 0.

Với **177. 1차원 배열 (1D Array / Mảng 1 chiều)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **177. 1차원 배열 (1D Array / Mảng 1 chiều)**, đừng bắt đầu lại từ số không. **178. 2차원 배열 (2D Array / Mảng 2 chiều)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **178. 2차원 배열 (2D Array / Mảng 2 chiều)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 178. 2차원 배열 (2D Array / Mảng 2 chiều)

Phần nguồn của **178. 2차원 배열 (2D Array / Mảng 2 chiều)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 변수들을 평면, 즉 행과 열로 조합한 배열이다. (Tập hợp các biến theo dạng bảng gồm hàng và cột).
  - *Example / Ví dụ*: `int b[2][3] = {{11, 22, 33}, {44, 55, 66}};`
  - 💡 *Mẹo ghi nhớ*: `[hàng][cột]` (Row x Column).

Với **178. 2차원 배열 (2D Array / Mảng 2 chiều)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

**178. 2차원 배열 (2D Array / Mảng 2 chiều)** vừa cho ta cách đặt câu hỏi. Bây giờ **179. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **179. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 179. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng)

Các ý ngay dưới **179. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- C언어에서는 큰따옴표("")로 묶인 글자는 문자열로 처리된다. (Trong C, chữ nằm trong ngoặc kép được xem là chuỗi).
- 배열에 문자열을 저장하면 널 문자('\0')가 문자열 끝에 자동으로 삽입된다. (Khi lưu chuỗi vào mảng, ký tự null `\0` tự động được thêm vào cuối).
  - *Example / Ví dụ*: `char a[5] = "love";` (Bao gồm l, o, v, e, \0).
  - 💡 *Mẹo ghi nhớ*: Độ dài mảng phải lớn hơn số ký tự của chuỗi ít nhất 1 (để chứa `\0`).

Với **179. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **179. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **180. 포인터와 포인터 변수 (Pointers / Con trỏ)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **180. 포인터와 포인터 변수 (Pointers / Con trỏ)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 180. 포인터와 포인터 변수 (Pointers / Con trỏ)

Bây giờ ta đi vào nội dung của **180. 포인터와 포인터 변수 (Pointers / Con trỏ)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 포인터 변수를 선언할 때는 자료형 뒤에 `*`를 붙인다. (Khai báo biến con trỏ bằng dấu `*`).
- 변수의 주소를 알아낼 때는 `&`를 붙인다. (Lấy địa chỉ của biến bằng dấu `&`).
- 실행문에서 포인터 변수에 `*`를 붙이면 해당 변수가 가리키는 곳의 값을 의미한다. (Dùng `*` trước con trỏ để lấy giá trị tại địa chỉ đó).
  - *Example / Ví dụ*: `int a = 50; int *b = &a; printf("%d", *b);` (In ra 50).
  - 💡 *Mẹo ghi nhớ*: `&` là địa chỉ (Address), `*` là giá trị (Value).

Với **180. 포인터와 포인터 변수 (Pointers / Con trỏ)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **180. 포인터와 포인터 변수 (Pointers / Con trỏ)**, đừng bắt đầu lại từ số không. **181. 포인터와 배열 (Pointer and Array / Con trỏ và mảng)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **181. 포인터와 배열 (Pointer and Array / Con trỏ và mảng)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 181. 포인터와 배열 (Pointer and Array / Con trỏ và mảng)

Phần nguồn của **181. 포인터와 배열 (Pointer and Array / Con trỏ và mảng)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 배열을 포인터 변수에 저장한 후 포인터를 이용해 배열의 요소에 접근할 수 있다. (Có thể dùng con trỏ để truy cập các phần tử mảng).
- 배열의 대표명은 배열의 첫 번째 요소의 주소와 같다. (Tên mảng chính là địa chỉ của phần tử đầu tiên).
  - *Example / Ví dụ*: `int a[5]; int *b = a;` tương đương với `b = &a[0];`.
  - 💡 *Mẹo ghi nhớ*: `a[i]` hoàn toàn tương đương với `*(a + i)`.

Với **181. 포인터와 배열 (Pointer and Array / Con trỏ và mảng)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Như vậy, **181. 포인터와 배열 (Pointer and Array / Con trỏ và mảng)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **배열 심화 (Arrays - Advanced)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.