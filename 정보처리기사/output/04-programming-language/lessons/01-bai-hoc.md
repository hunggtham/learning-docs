# 프로그래밍 언어 기초 (Programming Language Basics)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **프로그래밍 언어 기초 (Programming Language Basics)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **프로그래밍 언어 기초 (Programming Language Basics)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **프로그래밍 언어 기초 (Mở rộng) (Programming Language Basics - Extended)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

프로그래밍, 언어, 기초

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **프로그래밍 언어 기초 (Programming Language Basics)**을(를) 독립된 암기 항목으로 두지 않고, 이 과목에서 다룰 문제의 출발점으로 삼는다. 먼저 무엇을 설명하는지와 어디까지 적용되는지를 확인한 뒤 세부 규칙으로 들어간다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **프로그래밍 언어 기초 (Programming Language Basics)** và nối nó với **프로그래밍 언어 기초 (Mở rộng) (Programming Language Basics - Extended)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 프로그래밍 언어 기초 (Programming Language Basics)

Chúng ta bắt đầu mạch học bằng **프로그래밍 언어 기초 (Programming Language Basics)**. Trước khi đi vào từng thuật ngữ, hãy giữ câu hỏi trung tâm: phần kiến thức này giải quyết vấn đề gì và vì sao các khái niệm sau phải được đọc trong cùng một bối cảnh? Mục đích của mục 1/91 là tạo điểm tựa để những phần tiếp theo được hiểu theo quan hệ, không chỉ được ghi nhớ như danh sách.

Để đọc **프로그래밍 언어 기초 (Programming Language Basics)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **159. C/JAVA의 자료형 (Data Types / Kiểu dữ liệu)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **159. C/JAVA의 자료형 (Data Types / Kiểu dữ liệu)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 159. C/JAVA의 자료형 (Data Types / Kiểu dữ liệu)

Bây giờ ta đi vào nội dung của **159. C/JAVA의 자료형 (Data Types / Kiểu dữ liệu)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “159. C/JAVA의 자료형 (Data Types / Kiểu dữ liệu)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **C (exam assumption / giả định đề thi phổ biến):** `char` 1 byte, `int` 4 bytes; `long` phụ thuộc ABI/compiler và không nên ghi là 8 bytes tuyệt đối.
- **Java:** `byte` 1 byte, `short` 2 bytes, `int` 4 bytes, `long` 8 bytes, `char` 2 bytes (Unicode), `float` 4 bytes, `double` 8 bytes. `boolean` là kiểu logic; Java không quy định một kích thước lưu trữ cố định.
  - *Example / Ví dụ*: `int age = 25; boolean isStudent = true;`
  - 💡 *Mẹo ghi nhớ*: Java `char` = 2 bytes; C `char` = 1 byte; không suy ra kích thước storage của `boolean` từ ví dụ JVM.

Với **159. C/JAVA의 자료형 (Data Types / Kiểu dữ liệu)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **159. C/JAVA의 자료형 (Data Types / Kiểu dữ liệu)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **162. 변수명 작성 규칙 (Variable Naming Rules / Quy tắc đặt tên biến)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **162. 변수명 작성 규칙 (Variable Naming Rules / Quy tắc đặt tên biến)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 162. 변수명 작성 규칙 (Variable Naming Rules / Quy tắc đặt tên biến)

Phần nguồn của **162. 변수명 작성 규칙 (Variable Naming Rules / Quy tắc đặt tên biến)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “162. 변수명 작성 규칙 (Variable Naming Rules / Quy tắc đặt tên biến)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 영문자, 숫자, _(under bar)를 사용할 수 있다. (Có thể sử dụng chữ cái tiếng Anh, số và dấu gạch dưới).
- 첫 글자는 숫자는 올 수 없다. (Chữ cái đầu tiên không được là số).
- 공백이나 *, +, -, / 등의 특수문자를 사용할 수 없다. (Không được sử dụng khoảng trắng hoặc ký tự đặc biệt).
- 대소문자를 구분한다. (Phân biệt chữ hoa và chữ thường).
- 예약어를 변수명으로 사용할 수 없다. (Không được sử dụng từ khóa dự phòng làm tên biến).
  - *Example / Ví dụ*: Hợp lệ: `my_var_1`, Không hợp lệ: `1_my_var` (bắt đầu bằng số), `my var` (có khoảng trắng).
  - 💡 *Mẹo ghi nhớ*: Chỉ dùng `A-Z, a-z, 0-9, _`. Số không đi đầu. Không dùng từ khóa.

Các ý về **162. 변수명 작성 규칙 (Variable Naming Rules / Quy tắc đặt tên biến)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Sau khi đọc **162. 변수명 작성 규칙 (Variable Naming Rules / Quy tắc đặt tên biến)**, đừng bắt đầu lại từ số không. **163. 가비지 콜렉터 (Garbage Collector / Trình thu gom rác)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **163. 가비지 콜렉터 (Garbage Collector / Trình thu gom rác)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 163. 가비지 콜렉터 (Garbage Collector / Trình thu gom rác)

Các ý ngay dưới **163. 가비지 콜렉터 (Garbage Collector / Trình thu gom rác)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “163. 가비지 콜렉터 (Garbage Collector / Trình thu gom rác)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 선언만 하고 사용하지 않는 변수들이 점유한 메모리 공간을 강제로 해제하여 다른 프로그램들이 사용할 수 있도록 하는 것이다. (Tự động giải phóng không gian bộ nhớ do các biến được khai báo nhưng không sử dụng để các chương trình khác có thể sử dụng).
  - *Example / Ví dụ*: Trong Java, Garbage Collector (GC) tự động dọn dẹp các đối tượng không còn được tham chiếu.
  - 💡 *Mẹo ghi nhớ*: "Garbage" (rác) -> Dọn dẹp bộ nhớ không dùng đến.

Các ý về **163. 가비지 콜렉터 (Garbage Collector / Trình thu gom rác)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Như vậy, **163. 가비지 콜렉터 (Garbage Collector / Trình thu gom rác)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **프로그래밍 언어 기초 (Programming Language Basics)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **프로그래밍 언어 기초 (Mở rộng) (Programming Language Basics - Extended)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.