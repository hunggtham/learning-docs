# 입출력 심화 (Input/Output - Advanced)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **입출력 심화 (Input/Output - Advanced)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **입출력 심화 (Input/Output - Advanced)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **074. 데이터 입출력 (Data Input/Output)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

입출력, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **입출력 (Input/Output)**에서 만든 기준을 이어받아 **입출력 심화 (Input/Output - Advanced)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **입출력 심화 (Input/Output - Advanced)** và nối nó với **074. 데이터 입출력 (Data Input/Output)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 입출력 심화 (Input/Output - Advanced)

Sau khi đã đặt nền bằng **입출력 (Input/Output)**, ta chuyển sang **입출력 심화 (Input/Output - Advanced)**. Đây là mắt xích 14/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **입출력 심화 (Input/Output - Advanced)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **출력 포맷**, **문자열 연결** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **246. scanf() 함수 (scanf() Function / Hàm nhập trong C)**. Hãy xác định **246. scanf() 함수 (scanf() Function / Hàm nhập trong C)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 246. scanf() 함수 (scanf() Function / Hàm nhập trong C)

Phần nguồn của **246. scanf() 함수 (scanf() Function / Hàm nhập trong C)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “246. scanf() 함수 (scanf() Function / Hàm nhập trong C)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- C언어의 표준 입력 함수로, 키보드로 입력받아 변수에 저장한다. (Hàm nhập chuẩn của C, lấy dữ liệu từ bàn phím lưu vào biến).
- 형식: `scanf(서식 문자열, &변수)` (Định dạng, &Tên_biến).
- 변수에 주소연산자 `&`를 붙여야 한다. (Bắt buộc phải có toán tử địa chỉ `&` trước tên biến, trừ chuỗi).
  - *Example / Ví dụ*: `scanf("%3d", &a);` (Nhập số nguyên tối đa 3 chữ số vào địa chỉ biến a).
  - 💡 *Mẹo ghi nhớ*: "Scan" là quét (đọc vào), luôn nhớ phải có dấu `&` để chỉ đường cho dữ liệu đi vào bộ nhớ.

Các ý về **246. scanf() 함수 (scanf() Function / Hàm nhập trong C)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **246. scanf() 함수 (scanf() Function / Hàm nhập trong C)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **247. 서식 문자열 (Format String / Chuỗi định dạng - Bổ sung)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **247. 서식 문자열 (Format String / Chuỗi định dạng - Bổ sung)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 247. 서식 문자열 (Format String / Chuỗi định dạng - Bổ sung)

Các ý ngay dưới **247. 서식 문자열 (Format String / Chuỗi định dạng - Bổ sung)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “247. 서식 문자열 (Format String / Chuỗi định dạng - Bổ sung)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `%u`: 부호없는 정수 10진수 (Số nguyên hệ 10 không dấu).
- `%o`: 정수 8진수 (Hệ bát phân - Octal).
- `%x`: 정수 16진수 (Hệ thập lục phân - Hexadecimal).
- `%e`: 지수형 실수 (Số thực dạng số mũ - Exponential).
- `%p`: 주소를 16진수로 (Địa chỉ con trỏ hệ 16).
  - 💡 *Mẹo ghi nhớ*: o = octal, x = hex, u = unsigned, p = pointer.

Với **247. 서식 문자열 (Format String / Chuỗi định dạng - Bổ sung)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **247. 서식 문자열 (Format String / Chuỗi định dạng - Bổ sung)**, đừng bắt đầu lại từ số không. **249. 주요 제어문자 (Major Control Characters / Ký tự điều khiển)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **249. 주요 제어문자 (Major Control Characters / Ký tự điều khiển)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 249. 주요 제어문자 (Major Control Characters / Ký tự điều khiển)

Bây giờ ta đi vào nội dung của **249. 주요 제어문자 (Major Control Characters / Ký tự điều khiển)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “249. 주요 제어문자 (Major Control Characters / Ký tự điều khiển)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `\n`: new line (Xuống dòng).
- `\b`: backspace (Lùi lại 1 ký tự).
- `\t`: tab (Lùi khoảng cách tab).
- `\r`: carriage return (Về đầu dòng hiện tại).
- `\0`: null (Ký tự rỗng).
- `\'`: in dấu nháy đơn.
- `\"`: in dấu nháy kép.
- `\\`: in dấu xuyệt ngược.

Các bullet của **249. 주요 제어문자 (Major Control Characters / Ký tự điều khiển)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**249. 주요 제어문자 (Major Control Characters / Ký tự điều khiển)** vừa cho ta cách đặt câu hỏi. Bây giờ **250. JAVA에서의 표준 출력 (JAVA Standard Output / Đầu ra chuẩn trong JAVA)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **250. JAVA에서의 표준 출력 (JAVA Standard Output / Đầu ra chuẩn trong JAVA)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 250. JAVA에서의 표준 출력 (JAVA Standard Output / Đầu ra chuẩn trong JAVA)

Phần nguồn của **250. JAVA에서의 표준 출력 (JAVA Standard Output / Đầu ra chuẩn trong JAVA)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “250. JAVA에서의 표준 출력 (JAVA Standard Output / Đầu ra chuẩn trong JAVA)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **출력 포맷**: `System.out.printf("%-8.2f", 200.2);`
  - `-`: Căn trái (왼쪽 정렬).
  - `8`: Tổng 8 ký tự (8자리).
  - `.2`: 2 chữ số thập phân (소수점 이하 2자리).
  - Kết quả: `200.20   ` (Thêm khoảng trắng phía sau).
- **문자열 연결**: `System.out.print("abc" + "def");` (Dùng dấu `+` để nối chuỗi).

Các bullet của **250. JAVA에서의 표준 출력 (JAVA Standard Output / Đầu ra chuẩn trong JAVA)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **250. JAVA에서의 표준 출력 (JAVA Standard Output / Đầu ra chuẩn trong JAVA)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **251. 단순 if문 (Simple if statement / Câu lệnh if đơn giản - Nhắc lại)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **251. 단순 if문 (Simple if statement / Câu lệnh if đơn giản - Nhắc lại)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 251. 단순 if문 (Simple if statement / Câu lệnh if đơn giản - Nhắc lại)

Các ý ngay dưới **251. 단순 if문 (Simple if statement / Câu lệnh if đơn giản - Nhắc lại)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “251. 단순 if문 (Simple if statement / Câu lệnh if đơn giản - Nhắc lại)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- Nếu có nhiều hơn 1 câu lệnh thực thi, phải bọc trong `{ }` (Ngoặc nhọn).
  - *Example / Ví dụ*: `if(a > 10) { b = a - 10; printf("%d", b); }`

Với **251. 단순 if문 (Simple if statement / Câu lệnh if đơn giản - Nhắc lại)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **251. 단순 if문 (Simple if statement / Câu lệnh if đơn giản - Nhắc lại)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **입출력 심화 (Input/Output - Advanced)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **074. 데이터 입출력 (Data Input/Output)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.