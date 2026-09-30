# 연산자 (Operators)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **연산자 (Operators)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **연산자 (Operators)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **연산자 심화 (Operators - Advanced)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

연산자

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **237. 변수명 작성 규칙 (Variable Naming Rules)**에서 만든 기준을 이어받아 **연산자 (Operators)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **연산자 (Operators)** và nối nó với **연산자 심화 (Operators - Advanced)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 연산자 (Operators)

Sau khi đã đặt nền bằng **237. 변수명 작성 규칙 (Variable Naming Rules)**, ta chuyển sang **연산자 (Operators)**. Đây là mắt xích 8/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **연산자 (Operators)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **164. 산술 연산자 (Arithmetic Operators / Toán tử số học)**. Hãy xác định **164. 산술 연산자 (Arithmetic Operators / Toán tử số học)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 164. 산술 연산자 (Arithmetic Operators / Toán tử số học)

Phần nguồn của **164. 산술 연산자 (Arithmetic Operators / Toán tử số học)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “164. 산술 연산자 (Arithmetic Operators / Toán tử số học)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `%`: 나머지 (Phần dư). 정수만 연산 가능 (Chỉ dùng cho số nguyên).
- `++`: 증가 (Tăng 1).
  - 전치 (Prefix): `++a` (Tăng rồi mới dùng).
  - 후치 (Postfix): `a++` (Dùng rồi mới tăng).
- `--`: 감소 (Giảm 1). `--a` hoặc `a--`.
  - *Example / Ví dụ*: `int a = 5; b = ++a;` -> a=6, b=6.
  - 💡 *Mẹo ghi nhớ*: Prefix (++a) = Làm trước. Postfix (a++) = Làm sau.

Với **164. 산술 연산자 (Arithmetic Operators / Toán tử số học)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **164. 산술 연산자 (Arithmetic Operators / Toán tử số học)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **165. 비트 연산자 (Bitwise Operators / Toán tử bit)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **165. 비트 연산자 (Bitwise Operators / Toán tử bit)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 165. 비트 연산자 (Bitwise Operators / Toán tử bit)

Các ý ngay dưới **165. 비트 연산자 (Bitwise Operators / Toán tử bit)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “165. 비트 연산자 (Bitwise Operators / Toán tử bit)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `&` (and): 모든 비트가 1일 때만 1. (Chỉ bằng 1 khi tất cả các bit đều là 1).
- `^` (xor): 다르면 1, 같으면 0. (Khác nhau là 1, giống nhau là 0).
- `|` (or): 한 비트라도 1이면 1. (Chỉ cần một bit là 1 thì bằng 1).
- `~` (not): 각 비트의 부정. (Phủ định từng bit).
- `<<` / `>>`: 왼쪽/오른쪽 시프트. (Dịch trái/phải bit).
  - *Example / Ví dụ*: `5 & 3` (0101 & 0011) = `1` (0001).
  - 💡 *Mẹo ghi nhớ*: AND (&) khắt khe (đều phải 1). OR (|) dễ dãi (1 cái là đủ). XOR (^) thích sự khác biệt.

Với **165. 비트 연산자 (Bitwise Operators / Toán tử bit)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **165. 비트 연산자 (Bitwise Operators / Toán tử bit)**, đừng bắt đầu lại từ số không. **166. 논리 연산자 (Logical Operators / Toán tử logic)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **166. 논리 연산자 (Logical Operators / Toán tử logic)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 166. 논리 연산자 (Logical Operators / Toán tử logic)

Bây giờ ta đi vào nội dung của **166. 논리 연산자 (Logical Operators / Toán tử logic)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “166. 논리 연산자 (Logical Operators / Toán tử logic)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `!` (not): 부정 (Phủ định).
- `&&` (and): 모두 참이면 참 (Cả hai đúng thì đúng).
- `||` (or): 하나라도 참이면 참 (Một trong hai đúng thì đúng).
  - *Example / Ví dụ*: `(a > 0) && (b > 0)`
  - 💡 *Mẹo ghi nhớ*: Tương tự như toán tử bit nhưng áp dụng cho giá trị đúng/sai (true/false).

Các ý về **166. 논리 연산자 (Logical Operators / Toán tử logic)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

**166. 논리 연산자 (Logical Operators / Toán tử logic)** vừa cho ta cách đặt câu hỏi. Bây giờ **167. 조건 연산자 (Conditional Operator / Toán tử điều kiện)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **167. 조건 연산자 (Conditional Operator / Toán tử điều kiện)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 167. 조건 연산자 (Conditional Operator / Toán tử điều kiện)

Phần nguồn của **167. 조건 연산자 (Conditional Operator / Toán tử điều kiện)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “167. 조건 연산자 (Conditional Operator / Toán tử điều kiện)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 조건에 따라 서로 다른 수식을 수행한다. (Thực hiện các biểu thức khác nhau tùy thuộc vào điều kiện).
- `조건 ? 참일 때 : 거짓일 때`
  - *Example / Ví dụ*: `mx = a < b ? b : a;` (Nếu a < b thì mx = b, ngược lại mx = a).
  - 💡 *Mẹo ghi nhớ*: Dấu `?` là hỏi xem điều kiện đúng không, nếu đúng lấy cái trước `:`, sai lấy cái sau `:`.

Với **167. 조건 연산자 (Conditional Operator / Toán tử điều kiện)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **167. 조건 연산자 (Conditional Operator / Toán tử điều kiện)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **168. 연산자 우선순위 (Operator Precedence / Thứ tự ưu tiên toán tử)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **168. 연산자 우선순위 (Operator Precedence / Thứ tự ưu tiên toán tử)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 168. 연산자 우선순위 (Operator Precedence / Thứ tự ưu tiên toán tử)

Các ý ngay dưới **168. 연산자 우선순위 (Operator Precedence / Thứ tự ưu tiên toán tử)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “168. 연산자 우선순위 (Operator Precedence / Thứ tự ưu tiên toán tử)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 단항 (Unary) > 산술 (Arithmetic) > 시프트 (Shift) > 관계 (Relational) > 비트 (Bitwise) > 논리 (Logical) > 조건 (Conditional) > 대입 (Assignment) > 순서 (Comma).
- 산술 연산자 중에서는 `*, /, %` ưu tiên cao hơn `+, -`.
  - *Example / Ví dụ*: `a + b * c` thì phép nhân `*` được thực hiện trước `+`.
  - 💡 *Mẹo ghi nhớ*: Dấu ngoặc () luôn cao nhất. Đơn, Số, Dịch, Quan, Bit, Logic, Điều, Gán.

Các ý về **168. 연산자 우선순위 (Operator Precedence / Thứ tự ưu tiên toán tử)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Điểm chốt của **168. 연산자 우선순위 (Operator Precedence / Thứ tự ưu tiên toán tử)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **연산자 (Operators)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **연산자 심화 (Operators - Advanced)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.