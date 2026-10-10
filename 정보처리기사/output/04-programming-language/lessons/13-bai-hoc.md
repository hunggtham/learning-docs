# 입출력 (Input/Output)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **입출력 (Input/Output)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối input/output với stream, encoding, buffer và error handling, để giao tiếp dữ liệu không bị tách khỏi môi trường.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **입출력 (Input/Output)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **입출력 (Input/Output)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **입출력 심화 (Input/Output - Advanced)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **입출력 (Input/Output)**, **핵심 키워드 (Từ khóa)** chuyển mục tiêu học thành các điểm giao tiếp dữ liệu cần theo dõi; **선행·연결 개념 (Kiến thức liên kết)** xác định nền tảng và giới hạn của chúng.

## 핵심 키워드 (Từ khóa)

입출력

> **Nối mạch:** Sau từ khóa, **선행·연결 개념 (Kiến thức liên kết)** chỉ ra bài này kế thừa điều gì từ thứ tự toán tử; **읽는 방법 (Cách đọc)** chuyển nền tảng đó thành cách theo dõi dữ liệu vào và ra.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **245. 연산자 우선순위 (Operator Precedence)**에서 만든 기준을 이어받아 **입출력 (Input/Output)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** **선행·연결 개념 (Kiến thức liên kết)** nối từ thứ tự đánh giá biểu thức sang cách dữ liệu được định dạng và xuất ra; **읽는 방법 (Cách đọc)** sẽ theo dõi stream, format và newline trong từng ngôn ngữ.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Sau khi xác định cách đọc, phần chính đối chiếu format string, `printf()` và các hàm xuất của Java bằng khung **dữ liệu → định dạng → đầu ra**, rồi bàn giao sang phần input/output nâng cao.

## 입출력 (Input/Output)

Ở bước 13/91, **입출력 (Input/Output)** xuất hiện như phần tiếp nối của **245. 연산자 우선순위 (Operator Precedence)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **입출력 (Input/Output)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **169. 주요 서식 문자열 (Format String / Chuỗi định dạng)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **169. 주요 서식 문자열 (Format String / Chuỗi định dạng)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 169. 주요 서식 문자열 (Format String / Chuỗi định dạng)

Bây giờ ta đi vào nội dung của **169. 주요 서식 문자열 (Format String / Chuỗi định dạng)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “169. 주요 서식 문자열 (Format String / Chuỗi định dạng)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `%d`: 정수형 10진수 (Số nguyên hệ thập phân).
- `%c`: 문자 (Ký tự).
- `%s`: 문자열 (Chuỗi ký tự).
  - *Example / Ví dụ*: `printf("Tuổi: %d", 20);`
  - 💡 *Mẹo ghi nhớ*: d = decimal (số thập phân), c = character (ký tự), s = string (chuỗi).

Với **169. 주요 서식 문자열 (Format String / Chuỗi định dạng)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **169. 주요 서식 문자열 (Format String / Chuỗi định dạng)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **170. printf() 함수 (printf() Function / Hàm in C)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **170. printf() 함수 (printf() Function / Hàm in C)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 170. printf() 함수 (printf() Function / Hàm in C)

Phần nguồn của **170. printf() 함수 (printf() Function / Hàm in C)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “170. printf() 함수 (printf() Function / Hàm in C)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 인수로 주어진 값을 화면에 출력하는 함수이다. (Hàm in giá trị ra màn hình theo định dạng).
  - *Example / Ví dụ*: `printf("%d, %c", a, b);`
  - 💡 *Mẹo ghi nhớ*: 'f' trong printf là 'format' (định dạng).

Các ý về **170. printf() 함수 (printf() Function / Hàm in C)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Sau khi đọc **170. printf() 함수 (printf() Function / Hàm in C)**, đừng bắt đầu lại từ số không. **171. JAVA의 출력 함수 (Output Functions in JAVA / Hàm in Java)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **171. JAVA의 출력 함수 (Output Functions in JAVA / Hàm in Java)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 171. JAVA의 출력 함수 (Output Functions in JAVA / Hàm in Java)

Các ý ngay dưới **171. JAVA의 출력 함수 (Output Functions in JAVA / Hàm in Java)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “171. JAVA의 출력 함수 (Output Functions in JAVA / Hàm in Java)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `printf()`: Định dạng đầu ra. `System.out.printf("%d", r);`
- `print()`: In không xuống dòng. `System.out.print(r + s);`
- `println()`: In và xuống dòng. `System.out.println(r + "은 소수");`
  - 💡 *Mẹo ghi nhớ*: 'ln' trong println là 'line new' (xuống dòng mới).

Các bullet của **171. JAVA의 출력 함수 (Output Functions in JAVA / Hàm in Java)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **171. JAVA의 출력 함수 (Output Functions in JAVA / Hàm in Java)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **입출력 (Input/Output)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **입출력 심화 (Input/Output - Advanced)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **입출력 (Input/Output)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
