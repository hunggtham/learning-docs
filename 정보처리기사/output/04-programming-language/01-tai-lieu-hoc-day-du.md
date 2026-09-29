# Môn 4 — 프로그래밍 언어 활용 (Programming Language Application) (Ứng dụng ngôn ngữ lập trình)

## 학습 목표 (Mục tiêu học tập)

Phần này đặt mục tiêu của bài, để người mới biết mình cần giải thích được điều gì trước khi đi vào thuật ngữ và ví dụ.

- 시험에서 사용하는 한국어 용어를 영어와 베트남어 뜻까지 함께 인식한다.
- 각 개념을 정의 → 구성요소/절차 → 비교 포인트 → 예시 순서로 설명할 수 있다.
- 앞에서 배운 개념과 뒤의 심화 개념을 연결하여 문제의 조건을 빠르게 해석한다.

> **Câu hỏi trung tâm:** Khi học môn này, người học không chỉ cần nhận ra thuật ngữ Hàn mà còn phải giải thích khái niệm đang giải quyết vấn đề nào, dựa trên điều kiện nào và được dùng để nối sang phần kiến thức nào tiếp theo.

## 권장 학습 순서 (Lộ trình đề xuất)

Phần này là đường đi của bài giảng: đọc theo thứ tự để mỗi mục sau dùng lại hoặc mở rộng tiêu chí của mục trước.

1. 먼저 이 문서의 각 `##` 단원을 순서대로 읽는다.
2. 단원마다 **핵심 키워드**를 소리 내어 읽고, 한국어 원문과 베트남어 설명을 함께 확인한다.
3. 마지막에 `복습 체크리스트`를 점검한 뒤, 세부 lesson 파일에서 헷갈리는 부분을 다시 본다.

> **Nguồn:** tổng hợp từ các Markdown đã generate trong `raw_md/final`, được đối chiếu với các nguồn `raw` và `raw_md` cùng môn. Nội dung gốc được giữ lại; chỉ chuẩn hoá cấu trúc bài học.

> **Quy ước ngôn ngữ:** phần giải thích ưu tiên tiếng Việt; ở mọi lần xuất hiện, thuật ngữ đề thi dùng dạng `nghĩa Việt (English / 한국어)` để không phải quay lại tìm nghĩa.

> **Cách học:** học theo thứ tự các mục; với mỗi mục, xác định khái niệm → cơ chế/quy tắc → ví dụ → mẹo nhớ. Các mục lặp lại ở phần “심화” (nâng cao) dùng để nối kiến thức trước đó với dạng câu hỏi sâu hơn.

> **Mạch giảng:** mỗi mục mở bằng vị trí và mục đích học, đi qua phần giải thích của nguồn, rồi chốt bằng một câu bàn giao sang mục kế tiếp. Hãy đọc các câu nối như một phần của bài giảng: chúng cho biết vì sao kiến thức hiện tại cần thiết trước khi chuyển sang kiến thức sau.

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

---

## 프로그래밍 언어 기초 (Mở rộng) (Programming Language Basics - Extended)

Sau khi đã đặt nền bằng **프로그래밍 언어 기초 (Programming Language Basics)**, ta chuyển sang **프로그래밍 언어 기초 (Mở rộng) (Programming Language Basics - Extended)**. Đây là mắt xích 2/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **프로그래밍 언어 기초 (Mở rộng) (Programming Language Basics - Extended)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **리스트 (List)**, **튜플 (Tuple)**, **range**, **문자 (Char)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **236. Python의 시퀀스 자료형 (Python Sequence Type / Kiểu chuỗi trong Python - Nhắc lại)**. Hãy xác định **236. Python의 시퀀스 자료형 (Python Sequence Type / Kiểu chuỗi trong Python - Nhắc lại)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 236. Python의 시퀀스 자료형 (Python Sequence Type / Kiểu chuỗi trong Python - Nhắc lại)

Phần nguồn của **236. Python의 시퀀스 자료형 (Python Sequence Type / Kiểu chuỗi trong Python - Nhắc lại)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “236. Python의 시퀀스 자료형 (Python Sequence Type / Kiểu chuỗi trong Python - Nhắc lại)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **리스트 (List)**: Khác kiểu dữ liệu, thêm xóa được.
- **튜플 (Tuple)**: Không thể thay đổi (immutable).
- **range**: Sinh dãy số liên tiếp.

Các bullet của **236. Python의 시퀀스 자료형 (Python Sequence Type / Kiểu chuỗi trong Python - Nhắc lại)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **236. Python의 시퀀스 자료형 (Python Sequence Type / Kiểu chuỗi trong Python - Nhắc lại)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **구조체 정의 예 (Struct Definition Example / Ví dụ định nghĩa Struct)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **구조체 정의 예 (Struct Definition Example / Ví dụ định nghĩa Struct)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 구조체 정의 예 (Struct Definition Example / Ví dụ định nghĩa Struct)

Các ý ngay dưới **구조체 정의 예 (Struct Definition Example / Ví dụ định nghĩa Struct)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “구조체 정의 예 (Struct Definition Example / Ví dụ định nghĩa Struct)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- C언어: `struct sawon { char name[10]; int pay; };`

Các ý về **구조체 정의 예 (Struct Definition Example / Ví dụ định nghĩa Struct)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Sau khi đọc **구조체 정의 예 (Struct Definition Example / Ví dụ định nghĩa Struct)**, đừng bắt đầu lại từ số không. **235. JAVA의 데이터 타입 크기 (JAVA Data Type Sizes / Kích thước kiểu dữ liệu JAVA)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **235. JAVA의 데이터 타입 크기 (JAVA Data Type Sizes / Kích thước kiểu dữ liệu JAVA)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 235. JAVA의 데이터 타입 크기 (JAVA Data Type Sizes / Kích thước kiểu dữ liệu JAVA)

Bây giờ ta đi vào nội dung của **235. JAVA의 데이터 타입 크기 (JAVA Data Type Sizes / Kích thước kiểu dữ liệu JAVA)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “235. JAVA의 데이터 타입 크기 (JAVA Data Type Sizes / Kích thước kiểu dữ liệu JAVA)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **문자 (Char)**: `char` (2Byte - Khác với C là 1Byte).
- **정수 (Integer)**: `byte` (1Byte), `short` (2Byte), `int` (4Byte), `long` (8Byte).
- **실수 (Float)**: `float` (4Byte), `double` (8Byte).
- **논리 (Boolean)**: `boolean` (1Byte).
  - 💡 *Mẹo ghi nhớ*: Java dùng Unicode nên `char` là 2 Bytes. Có thêm kiểu `byte` (1 Byte).

Các bullet của **235. JAVA의 데이터 타입 크기 (JAVA Data Type Sizes / Kích thước kiểu dữ liệu JAVA)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**235. JAVA의 데이터 타입 크기 (JAVA Data Type Sizes / Kích thước kiểu dữ liệu JAVA)** vừa cho ta cách đặt câu hỏi. Bây giờ **237. 변수의 개요 및 헝가리안 표기법 (Variables & Hungarian Notation / Biến và Ký pháp Hungary)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **237. 변수의 개요 및 헝가리안 표기법 (Variables & Hungarian Notation / Biến và Ký pháp Hungary)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 237. 변수의 개요 및 헝가리안 표기법 (Variables & Hungarian Notation / Biến và Ký pháp Hungary)

Phần nguồn của **237. 변수의 개요 및 헝가리안 표기법 (Variables & Hungarian Notation / Biến và Ký pháp Hungary)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “237. 변수의 개요 및 헝가리안 표기법 (Variables & Hungarian Notation / Biến và Ký pháp Hungary)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **헝가리안 표기법 (Hungarian Notation)**: 변수 선언 시 변수명에 데이터 타입을 명시하는 것. (Gắn tiền tố kiểu dữ liệu vào tên biến, vd: `strName`, `nAge`).
- Mọi câu lệnh khai báo biến trong C/Java đều phải kết thúc bằng dấu chấm phẩy `;`.

Các bullet của **237. 변수의 개요 및 헝가리안 표기법 (Variables & Hungarian Notation / Biến và Ký pháp Hungary)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **237. 변수의 개요 및 헝가리안 표기법 (Variables & Hungarian Notation / Biến và Ký pháp Hungary)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **238. 가비지 콜렉터 (Garbage Collector / Trình thu gom rác - Nhắc lại)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **238. 가비지 콜렉터 (Garbage Collector / Trình thu gom rác - Nhắc lại)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 238. 가비지 콜렉터 (Garbage Collector / Trình thu gom rác - Nhắc lại)

Các ý ngay dưới **238. 가비지 콜렉터 (Garbage Collector / Trình thu gom rác - Nhắc lại)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “238. 가비지 콜렉터 (Garbage Collector / Trình thu gom rác - Nhắc lại)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 메모리 공간을 강제로 해제 (Giải phóng không gian bộ nhớ không còn sử dụng).

Các bullet của **238. 가비지 콜렉터 (Garbage Collector / Trình thu gom rác - Nhắc lại)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **238. 가비지 콜렉터 (Garbage Collector / Trình thu gom rác - Nhắc lại)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **프로그래밍 언어 기초 (Mở rộng) (Programming Language Basics - Extended)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)

Từ **프로그래밍 언어 기초 (Mở rộng) (Programming Language Basics - Extended)**, ta đã có điểm tựa để bước vào **072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 3/91 trước khi đi vào chi tiết.

Để đọc **072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô. Trong khối này, **데이터 타입 (Data Types)**, **변수 작성 규칙 (Variable Naming Rules)**, **연산자 (Operators)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **데이터 타입 (Data Types)**:
  - 정수형 (Integer): `int`, `short`, `long` (Ví dụ: 1, -1).
  - 부동 소수형 (Float Point): `float`, `double` (실수, 소수점) (Ví dụ: 3.14).
  - 문자형 (Character): `char` ('A').
  - 문자열 (String): `char` 배열, `string` ("ABC").
  - 논리형 (Boolean): 참/거짓 (True/False).
- **변수 작성 규칙 (Variable Naming Rules)**:
  - 영문자, 숫자, 밑줄(`_`) 사용 가능.
  - **숫자로 시작 불가**, 중간 공백 특수문자 불가, 예약어(`if`, `for` 등) 사용 불가.
- **연산자 (Operators)**:
  - 산술 (Arithmetic): `+`, `-`, `*`, `/` (몫), `%` (나머지).
  - 증감 (Increment/Decrement): `++` (1 증가), `--` (1 감소).
    - 전치 (`++A`): 연산 전 증가.
    - 후치 (`A++`): 연산 후 증가.
  - 관계 (Relational): `>`, `<`, `==` (같다), `!=` (다르다).
  - 논리 (Logical): `&&` (AND), `||` (OR), `!` (NOT).
  - 삼항 (Ternary): `(조건) ? (참) : (거짓);`

Điểm chốt của **072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)

Ở bước 4/91, **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)** xuất hiện như phần tiếp nối của **072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `char`: 1바이트 (문자 하나)
- `short`: 2바이트 (짧은 정수)
- `int` / `long`: 4바이트 (기본 정수)
- `long long`: 8바이트 (긴 정수)
- `float`: 4바이트 (실수)
- `double`: 8바이트 (정밀도 높은 실수)

**Giải thích (Vietnamese):**
Kích thước bộ nhớ các biến trong C/C++. Chữ cái (char) chiếm 1 byte. Số nguyên (int) chiếm 4 byte. Số thực (float) 4 byte, double (gấp đôi) là 8 byte.

---

Như vậy, **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)

Sau khi đã đặt nền bằng **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)**, ta chuyển sang **235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)**. Đây là mắt xích 5/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `byte`: 1바이트 (작은 숫자)
- `boolean`: 1바이트 (참/거짓)
- **`char`: 2바이트** (유니코드 지원으로 인해 C언어와 달리 2바이트를 차지함)
- `int`: 4바이트
- `long`: 8바이트 (C언어는 보통 4바이트지만 JAVA는 8바이트)
- `float`: 4바이트 / `double`: 8바이트

**Giải thích (Vietnamese):**
Java có 2 điểm khác biệt lớn với C: `char` chiếm 2 byte (để lưu bảng mã Unicode đa ngôn ngữ), và có kiểu `boolean` (chỉ lưu True/False).

---

Ta có thể khép mục **235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)

Từ **235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)**, ta đã có điểm tựa để bước vào **087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 6/91 trước khi đi vào chi tiết.

Để đọc **087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **환경변수 명령어**, **운영체제별 주요 명령어 (Windows / Unix(Linux))** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **환경변수 명령어**:
  - `printenv`: 단일 변수 반환.
  - `env`: 환경 변수 출력/설정.
  - `set` / `setenv`: 변수 추가/업데이트.
  - `export`: 변수를 전역(Global) 변수로 변경 (export 안하면 현재 쉘에만 국한됨).
- **운영체제별 주요 명령어 (Windows / Unix(Linux))**:
  - 목록 보기: `dir` / `ls`
  - 복사: `copy` / `cp`
  - 삭제: `del` / `rm`
  - 이름 변경/이동: `ren`, `move` / `mv`
  - 폴더 생성: `md` / `mkdir`
  - 기타 Unix 명령어:
    - `chmod`: 권한 변경. / `chown`: 소유자 변경.
    - `cat`: 파일 내용 출력.
    - `grep`: 문자열(패턴) 검색 (Windows의 `find`).
    - `ps`: 프로세스 상태. / `kill`: 프로세스 종료.
    - `tar`: 파일 묶기/풀기. / `crontab`: 스케줄링.

**Giải thích (Vietnamese):**
- Lệnh `export` rất hay dùng trong Linux để set biến môi trường (Ví dụ: `export PATH=...`) để các chương trình khác cũng đọc được biến đó.
- Các lệnh Linux kinh điển: `ls` (list - liệt kê), `cp` (copy), `rm` (remove), `mv` (move), `mkdir` (make directory), `grep` (tìm text).

---

Điểm chốt của **087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **237. 변수명 작성 규칙 (Variable Naming Rules)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 237. 변수명 작성 규칙 (Variable Naming Rules)

Ở bước 7/91, **237. 변수명 작성 규칙 (Variable Naming Rules)** xuất hiện như phần tiếp nối của **087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **237. 변수명 작성 규칙 (Variable Naming Rules)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “237. 변수명 작성 규칙 (Variable Naming Rules)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 영문자, 숫자, 밑줄(`_`)의 조합만 가능.
- **첫 글자는 숫자로 시작할 수 없음** (예: `1a` 안됨).
- 공백이나 특수문자(`+`, `-`, `*`, `/`, `@` 등) 사용 금지.
- 예약어(`if`, `for`, `while` 등) 사용 금지.
- 대소문자 엄격히 구분.

**Giải thích (Vietnamese):**
Quy tắc đặt tên biến: Không được bắt đầu bằng số, không có khoảng trắng, không chứa ký tự đặc biệt (trừ dấu gạch dưới `_`), không dùng từ khoá của ngôn ngữ.

---

Như vậy, **237. 변수명 작성 규칙 (Variable Naming Rules)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **연산자 (Operators)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

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

---

## 연산자 심화 (Operators - Advanced)

Từ **연산자 (Operators)**, ta đã có điểm tựa để bước vào **연산자 심화 (Operators - Advanced)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 9/91 trước khi đi vào chi tiết.

Để đọc **연산자 심화 (Operators - Advanced)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **240. 관계 연산자 (Relational Operators / Toán tử quan hệ)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 240. 관계 연산자 (Relational Operators / Toán tử quan hệ)

Các ý ngay dưới **240. 관계 연산자 (Relational Operators / Toán tử quan hệ)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “240. 관계 연산자 (Relational Operators / Toán tử quan hệ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 두 수의 관계를 비교하여 참(1) 또는 거짓(0)을 결과로 얻는다. (So sánh hai số trả về 1 (Đúng) hoặc 0 (Sai)).
- `==` (Bằng), `!=` (Khác), `>`, `>=`, `<`, `<=`.
  - 💡 *Mẹo ghi nhớ*: Trong C, 0 là Sai, mọi số khác 0 đều được coi là Đúng (Thường dùng 1).

Các bullet của **240. 관계 연산자 (Relational Operators / Toán tử quan hệ)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **240. 관계 연산자 (Relational Operators / Toán tử quan hệ)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **243. 대입 연산자 (Assignment Operators / Toán tử gán)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **243. 대입 연산자 (Assignment Operators / Toán tử gán)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 243. 대입 연산자 (Assignment Operators / Toán tử gán)

Bây giờ ta đi vào nội dung của **243. 대입 연산자 (Assignment Operators / Toán tử gán)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “243. 대입 연산자 (Assignment Operators / Toán tử gán)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 연산 후 결과를 대입한다. (Thực hiện phép tính xong rồi gán kết quả lại cho biến).
- `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`.
  - *Example / Ví dụ*: `a += 1` tương đương `a = a + 1`.

*(Lưu ý: Các toán tử 산술 (Số học), 비트 (Bit), 논리 (Logic), 조건 (Điều kiện), ưu tiên 연산자 우선순위 đã được trình bày ở phần trước).*

Với **243. 대입 연산자 (Assignment Operators / Toán tử gán)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **243. 대입 연산자 (Assignment Operators / Toán tử gán)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **연산자 심화 (Operators - Advanced)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **239 - 243. 연산자 (Operators)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 239 - 243. 연산자 (Operators)

Ở bước 10/91, **239 - 243. 연산자 (Operators)** xuất hiện như phần tiếp nối của **연산자 심화 (Operators - Advanced)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **239 - 243. 연산자 (Operators)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận. Trong khối này, **산술 연산자**, **관계 연산자**, **비트 연산자**, **논리 연산자** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “239 - 243. 연산자 (Operators)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **산술 연산자**: 사칙연산, `%`(나머지), `++`/`--`(증감).
  - 전치(`++a`): 먼저 증가시키고 연산. 후치(`a++`): 연산 후 증가시킴.
- **관계 연산자**: `==`(같다), `!=`(다르다), `>`, `<`. C언어에서는 0 이외의 값을 참(True)으로 간주.
- **비트 연산자**: 비트 단위 연산. `&`(AND), `|`(OR), `^`(XOR: 서로 다를 때만 1), `~`(NOT). `<<`, `>>`(비트 이동).
- **논리 연산자**: `&&`(AND), `||`(OR), `!`(NOT).
- **대입 연산자**: `=`, `+=`, `-=` 등. `a += 1`은 `a = a + 1`과 동일.

---

Như vậy, **239 - 243. 연산자 (Operators)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **244. 조건(삼항) 연산자 (Ternary Operator)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 244. 조건(삼항) 연산자 (Ternary Operator)

Sau khi đã đặt nền bằng **239 - 243. 연산자 (Operators)**, ta chuyển sang **244. 조건(삼항) 연산자 (Ternary Operator)**. Đây là mắt xích 11/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **244. 조건(삼항) 연산자 (Ternary Operator)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “244. 조건(삼항) 연산자 (Ternary Operator)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 조건의 참/거짓에 따라 서로 다른 값을 반환.
- 형식: `조건 ? 참일때_값 : 거짓일때_값;`
- (예: `int max = (a > b) ? a : b;`)

**Giải thích (Vietnamese):**
Toán tử 3 ngôi giúp viết tắt câu lệnh if-else trên 1 dòng. Trả về giá trị 1 nếu điều kiện đúng, giá trị 2 nếu sai.

---

Ta có thể khép mục **244. 조건(삼항) 연산자 (Ternary Operator)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **245. 연산자 우선순위 (Operator Precedence)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 245. 연산자 우선순위 (Operator Precedence)

Từ **244. 조건(삼항) 연산자 (Ternary Operator)**, ta đã có điểm tựa để bước vào **245. 연산자 우선순위 (Operator Precedence)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 12/91 trước khi đi vào chi tiết.

Để đọc **245. 연산자 우선순위 (Operator Precedence)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “245. 연산자 우선순위 (Operator Precedence)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 하나의 수식에 여러 연산자가 있을 때 계산되는 순서.
- 순위: **단항**(`!`, `++`, `~`) > **산술**(`*`, `/` > `+`, `-`) > **관계**(`>`, `==`) > **논리**(`&&` > `||`) > **대입**(`=`, `+=`).
- 괄호 `()`가 가장 우선.

**Giải thích (Vietnamese):**
Thứ tự ưu tiên tính toán: Ngoặc () -> Đơn nguyên (phủ định, tăng giảm) -> Nhân chia cộng trừ -> So sánh -> Logic (AND trước OR sau) -> Gán.

**💡 Mẹo ghi nhớ (Mnemonics):**
**단산관논대** (Đơn - Toán - Quan - Luận - Gán): 단항 -> 산술 -> 관계 -> 논리 -> 대입.

---

Điểm chốt của **245. 연산자 우선순위 (Operator Precedence)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **입출력 (Input/Output)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

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

---

## 074. 데이터 입출력 (Data Input/Output)

Từ **입출력 심화 (Input/Output - Advanced)**, ta đã có điểm tựa để bước vào **074. 데이터 입출력 (Data Input/Output)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 15/91 trước khi đi vào chi tiết.

Để đọc **074. 데이터 입출력 (Data Input/Output)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **표준 입력 함수 (C언어)**, **표준 출력 함수 (C언어)**, **서식 문자열 유형 (Format Strings)**, **이스케이프 문자** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “074. 데이터 입출력 (Data Input/Output)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **표준 입력 함수 (C언어)**: `scanf("서식 문자열", &변수명);` (변수의 주소 `&`를 붙임).
- **표준 출력 함수 (C언어)**: `printf("서식 문자열", 변수);`
- **서식 문자열 유형 (Format Strings)**:
  - `%d`: 정수형 10진수 (Decimal)
  - `%f`: 실수형 (Float)
  - `%c`: 문자형 1개 (Character)
  - `%s`: 문자열 (String)
- **이스케이프 문자**: `\n` (줄바꿈), `\t` (탭), `\b` (백스페이스).
- **JAVA 입출력**: `System.out.println()` (출력 후 자동 개행), `System.out.print()` (개행 없음).
- **Python 입출력**: `print(문자열, end='')` (끝에 개행 대신 다른 문자 삽입).

**Giải thích (Vietnamese):**
Khi lập trình bằng C, bạn dùng `scanf` để nhận dữ liệu người dùng nhập (nhớ có dấu `&` trước tên biến) và `printf` để in ra màn hình. Dấu `%d` dùng cho số nguyên, `%f` cho số thập phân. Java dùng `System.out.println()`. Python thì ngắn gọn hơn chỉ cần `print()`.

---

Điểm chốt của **074. 데이터 입출력 (Data Input/Output)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)

Ở bước 16/91, **246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)** xuất hiện như phần tiếp nối của **074. 데이터 입출력 (Data Input/Output)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **`scanf("서식문자열", &변수)`**, **`printf("서식문자열", 변수)`**, **서식 문자열**, **제어문자 (Escape Sequence)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **`scanf("서식문자열", &변수)`**: C언어 표준 입력. 변수명 앞에 주소 연산자 **`&`**를 반드시 붙여야 함.
- **`printf("서식문자열", 변수)`**: C언어 표준 출력. `&`를 붙이지 않음.
- **서식 문자열**:
  - `%d`: 10진수 정수 / `%f`: 실수 (예: `%8.2f`는 총 8자리, 소수점 2자리) / `%c`: 문자 1개 / `%s`: 문자열.
  - `%o`: 8진수 / `%x`: 16진수.
- **제어문자 (Escape Sequence)**:
  - `\n`: 줄바꿈 (New Line) / `\t`: 탭 (Tab) / `\b`: 백스페이스 / `\0`: 널 문자(문자열의 끝 표시).

**Giải thích (Vietnamese):**
Nhớ kĩ `scanf` phải có dấu `&` (địa chỉ) để nhét dữ liệu vào đúng chỗ trong RAM. `printf` thì không cần. Dấu `\0` (Null) cực kỳ quan trọng trong C để đánh dấu kết thúc một chuỗi (string).

---

Như vậy, **246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **제어문 (Control Statements)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 제어문 (Control Statements)

Sau khi đã đặt nền bằng **246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)**, ta chuyển sang **제어문 (Control Statements)**. Đây là mắt xích 17/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **제어문 (Control Statements)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **172. 단순 if문 (Simple if statement / Câu lệnh if đơn giản)**. Hãy xác định **172. 단순 if문 (Simple if statement / Câu lệnh if đơn giản)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 172. 단순 if문 (Simple if statement / Câu lệnh if đơn giản)

Phần nguồn của **172. 단순 if문 (Simple if statement / Câu lệnh if đơn giản)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “172. 단순 if문 (Simple if statement / Câu lệnh if đơn giản)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 조건이 한 개일 때 사용하는 제어문이다. (Câu lệnh điều khiển khi chỉ có một điều kiện).
  - *Example / Ví dụ*: `if (a > b) printf("참"); else printf("거짓");`
  - 💡 *Mẹo ghi nhớ*: Nếu (if) đúng thì làm, nếu không (else) thì làm cái khác.

Các ý về **172. 단순 if문 (Simple if statement / Câu lệnh if đơn giản)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **172. 단순 if문 (Simple if statement / Câu lệnh if đơn giản)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **173. switch문 (switch statement / Câu lệnh switch)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **173. switch문 (switch statement / Câu lệnh switch)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 173. switch문 (switch statement / Câu lệnh switch)

Các ý ngay dưới **173. switch문 (switch statement / Câu lệnh switch)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “173. switch문 (switch statement / Câu lệnh switch)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 조건에 따라 분기할 곳이 여러 곳인 경우 간단하게 처리할 수 있다. (Sử dụng khi có nhiều nhánh rẽ).
- break문이 생략되면 모든 문장이 실행된다. (Nếu thiếu `break`, các câu lệnh bên dưới cũng sẽ được chạy theo hiệu ứng rơi xuyên).
  - *Example / Ví dụ*: `switch(a) { case 1: printf("A"); break; }`
  - 💡 *Mẹo ghi nhớ*: Đừng quên `break`, nếu không nó sẽ trôi xuống tận dưới cùng.

Các ý về **173. switch문 (switch statement / Câu lệnh switch)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Sau khi đọc **173. switch문 (switch statement / Câu lệnh switch)**, đừng bắt đầu lại từ số không. **174. for문 (for loop / Vòng lặp for)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **174. for문 (for loop / Vòng lặp for)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 174. for문 (for loop / Vòng lặp for)

Bây giờ ta đi vào nội dung của **174. for문 (for loop / Vòng lặp for)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “174. for문 (for loop / Vòng lặp for)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 초기값, 최종값, 증가값을 지정하여 정해진 횟수를 반복하는 제어문이다. (Vòng lặp với số lần xác định, bao gồm giá trị khởi tạo, điều kiện kết thúc và bước nhảy).
  - *Example / Ví dụ*: `for (i = 1; i <= 10 ; i++) sum = sum + i;`
  - 💡 *Mẹo ghi nhớ*: Dùng khi biết trước số lần lặp.

Với **174. for문 (for loop / Vòng lặp for)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

**174. for문 (for loop / Vòng lặp for)** vừa cho ta cách đặt câu hỏi. Bây giờ **175. while문 (while loop / Vòng lặp while)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **175. while문 (while loop / Vòng lặp while)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 175. while문 (while loop / Vòng lặp while)

Phần nguồn của **175. while문 (while loop / Vòng lặp while)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “175. while문 (while loop / Vòng lặp while)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 조건이 참인 동안 실행할 문장을 반복 수행한다. (Lặp lại chừng nào điều kiện còn đúng).
  - *Example / Ví dụ*: `while (i <= 10) { i++; }`
  - 💡 *Mẹo ghi nhớ*: Kiểm tra điều kiện trước, làm sau. Có thể không chạy lần nào nếu điều kiện sai ngay từ đầu.

Các ý về **175. while문 (while loop / Vòng lặp while)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **175. while문 (while loop / Vòng lặp while)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **176. do~while문 (do~while loop / Vòng lặp do~while)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **176. do~while문 (do~while loop / Vòng lặp do~while)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 176. do~while문 (do~while loop / Vòng lặp do~while)

Các ý ngay dưới **176. do~while문 (do~while loop / Vòng lặp do~while)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “176. do~while문 (do~while loop / Vòng lặp do~while)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 무조건 한 번 실행한 다음 조건을 판단하여 탈출 여부를 결정한다. (Thực hiện ít nhất một lần, sau đó mới kiểm tra điều kiện).
  - *Example / Ví dụ*: `do { i++; } while (i <= 10);`
  - 💡 *Mẹo ghi nhớ*: Làm (do) trước, hỏi (while) sau. Chắc chắn chạy ít nhất 1 lần.

Các ý về **176. do~while문 (do~while loop / Vòng lặp do~while)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Điểm chốt của **176. do~while문 (do~while loop / Vòng lặp do~while)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **제어문 (Control Statements)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **제어문 심화 (Control Statements - Advanced)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 제어문 심화 (Control Statements - Advanced)

Từ **제어문 (Control Statements)**, ta đã có điểm tựa để bước vào **제어문 심화 (Control Statements - Advanced)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 18/91 trước khi đi vào chi tiết.

Để đọc **제어문 심화 (Control Statements - Advanced)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **break**, **continue** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **252. 다중 if문 (Multi if statement / Câu lệnh if nhiều nhánh)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 252. 다중 if문 (Multi if statement / Câu lệnh if nhiều nhánh)

Các ý ngay dưới **252. 다중 if문 (Multi if statement / Câu lệnh if nhiều nhánh)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “252. 다중 if문 (Multi if statement / Câu lệnh if nhiều nhánh)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 조건이 여러 개일 때 사용하는 제어문이다. (Sử dụng khi có nhiều điều kiện khác nhau).
- `if (조건1) ... else if (조건2) ... else ...`
  - *Example / Ví dụ*: `if(jum >= 90) printf("A"); else if(jum >= 80) printf("B"); else printf("F");`
  - 💡 *Mẹo ghi nhớ*: Xếp hạng hoặc các điều kiện loại trừ lẫn nhau thì dùng `else if`.

Các ý về **252. 다중 if문 (Multi if statement / Câu lệnh if nhiều nhánh)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **252. 다중 if문 (Multi if statement / Câu lệnh if nhiều nhánh)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **253. switch문 (switch statement / Câu lệnh switch - Bổ sung)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **253. switch문 (switch statement / Câu lệnh switch - Bổ sung)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 253. switch문 (switch statement / Câu lệnh switch - Bổ sung)

Bây giờ ta đi vào nội dung của **253. switch문 (switch statement / Câu lệnh switch - Bổ sung)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “253. switch문 (switch statement / Câu lệnh switch - Bổ sung)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `case`문의 레이블에는 상수만 지정할 수 있으며 변수는 지정할 수 없다. (Nhãn `case` chỉ chấp nhận hằng số, không dùng biến).
- `int`, `char`, `enum`형의 상수만 가능하다. (Chỉ dùng được số nguyên, ký tự, hoặc kiểu enum).
  - *Example / Ví dụ*: `switch (jum / 10) { case 10: case 9: printf("A"); break; ... }` (Chia cho 10 để tính điểm thập phân thành số nguyên).
  - 💡 *Mẹo ghi nhớ*: `switch` thích sự chính xác tuyệt đối (giá trị cụ thể), không thích sự so sánh lớn/nhỏ.

Các ý về **253. switch문 (switch statement / Câu lệnh switch - Bổ sung)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Sau khi đọc **253. switch문 (switch statement / Câu lệnh switch - Bổ sung)**, đừng bắt đầu lại từ số không. **254. for문 (for loop / Vòng lặp for - Bổ sung)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **254. for문 (for loop / Vòng lặp for - Bổ sung)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 254. for문 (for loop / Vòng lặp for - Bổ sung)

Phần nguồn của **254. for문 (for loop / Vòng lặp for - Bổ sung)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “254. for문 (for loop / Vòng lặp for - Bổ sung)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 처음부터 조건식을 만족하지 못하면 한 번도 수행하지 않는다. (Nếu điều kiện sai ngay từ đầu, vòng lặp không chạy lần nào).
- `for(초기값; 최종값조건; 증가값) { 실행문; }`

Các bullet của **254. for문 (for loop / Vòng lặp for - Bổ sung)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**254. for문 (for loop / Vòng lặp for - Bổ sung)** vừa cho ta cách đặt câu hỏi. Bây giờ **255. while문 (while loop / Vòng lặp while - Bổ sung)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **255. while문 (while loop / Vòng lặp while - Bổ sung)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 255. while문 (while loop / Vòng lặp while - Bổ sung)

Các ý ngay dưới **255. while문 (while loop / Vòng lặp while - Bổ sung)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “255. while문 (while loop / Vòng lặp while - Bổ sung)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `while(조건) { 실행문; }`
- Điều kiện được kiểm tra trước, nếu sai từ đầu sẽ bỏ qua.
  - *Example / Ví dụ*: `while(a < 5) { a++; hap += a; }`

Các ý về **255. while문 (while loop / Vòng lặp while - Bổ sung)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **255. while문 (while loop / Vòng lặp while - Bổ sung)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **256. do~while문 (do~while loop / Vòng lặp do~while - Bổ sung)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **256. do~while문 (do~while loop / Vòng lặp do~while - Bổ sung)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 256. do~while문 (do~while loop / Vòng lặp do~while - Bổ sung)

Bây giờ ta đi vào nội dung của **256. do~while문 (do~while loop / Vòng lặp do~while - Bổ sung)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “256. do~while문 (do~while loop / Vòng lặp do~while - Bổ sung)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 실행할 문장을 무조건 한 번 실행한 다음 조건을 판단. (Thực hiện ít nhất 1 lần rồi mới kiểm tra điều kiện ở cuối).
- `do { 실행문; } while(조건);` (Nhớ có dấu chấm phẩy ở cuối `while`).

Các bullet của **256. do~while문 (do~while loop / Vòng lặp do~while - Bổ sung)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **256. do~while문 (do~while loop / Vòng lặp do~while - Bổ sung)**, đừng bắt đầu lại từ số không. **257. break, continue (Keywords / Từ khóa điều khiển vòng lặp)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **257. break, continue (Keywords / Từ khóa điều khiển vòng lặp)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 257. break, continue (Keywords / Từ khóa điều khiển vòng lặp)

Phần nguồn của **257. break, continue (Keywords / Từ khóa điều khiển vòng lặp)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “257. break, continue (Keywords / Từ khóa điều khiển vòng lặp)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **break**: switch문이나 반복문 안에서 나오면 블록을 벗어난다. (Thoát ngay lập tức khỏi vòng lặp hoặc switch).
- **continue**: 이후의 문장을 실행하지 않고 반복문의 처음으로 옮긴다. (Bỏ qua các lệnh bên dưới và quay lại đầu vòng lặp để tiếp tục vòng lặp mới).
  - *Example / Ví dụ*: `if(a % 2 == 0) continue; hap += a;` (Bỏ qua số chẵn, chỉ cộng số lẻ).
  - 💡 *Mẹo ghi nhớ*: `break` = Phá vỡ (thoát ra). `continue` = Tiếp tục (bước tiếp).

Với **257. break, continue (Keywords / Từ khóa điều khiển vòng lặp)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Như vậy, **257. break, continue (Keywords / Từ khóa điều khiển vòng lặp)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **제어문 심화 (Control Statements - Advanced)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)

Ở bước 19/91, **구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)** xuất hiện như phần tiếp nối của **제어문 심화 (Control Statements - Advanced)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **C언어의 구조체 (Struct in C / Cấu trúc trong C)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **C언어의 구조체 (Struct in C / Cấu trúc trong C)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### C언어의 구조체 (Struct in C / Cấu trúc trong C)

Bây giờ ta đi vào nội dung của **C언어의 구조체 (Struct in C / Cấu trúc trong C)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “C언어의 구조체 (Struct in C / Cấu trúc trong C)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 자료의 종류가 다른 변수의 모임이다. (Tập hợp các biến có kiểu dữ liệu khác nhau).
- 예약어 `struct`를 이용해 정의한다. (Định nghĩa bằng từ khóa `struct`).
  - *Example / Ví dụ*: `struct Person { char name[20]; int age; };`
  - 💡 *Mẹo ghi nhớ*: Mảng (Array) lưu các giá trị cùng kiểu, Cấu trúc (Struct) lưu các giá trị khác kiểu.

Các ý về **C언어의 구조체 (Struct in C / Cấu trúc trong C)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **C언어의 구조체 (Struct in C / Cấu trúc trong C)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **177. 1차원 배열 (1D Array / Mảng 1 chiều)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **177. 1차원 배열 (1D Array / Mảng 1 chiều)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 177. 1차원 배열 (1D Array / Mảng 1 chiều)

Phần nguồn của **177. 1차원 배열 (1D Array / Mảng 1 chiều)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “177. 1차원 배열 (1D Array / Mảng 1 chiều)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 변수들을 일직선상의 개념으로 조합한 배열이다. (Tập hợp các biến trên một đường thẳng).
  - *Example / Ví dụ*: `char a[3] = {'A', 'B', 'C'};`
  - 💡 *Mẹo ghi nhớ*: Chỉ số mảng luôn bắt đầu từ 0.

Với **177. 1차원 배열 (1D Array / Mảng 1 chiều)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **177. 1차원 배열 (1D Array / Mảng 1 chiều)**, đừng bắt đầu lại từ số không. **178. 2차원 배열 (2D Array / Mảng 2 chiều)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **178. 2차원 배열 (2D Array / Mảng 2 chiều)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 178. 2차원 배열 (2D Array / Mảng 2 chiều)

Các ý ngay dưới **178. 2차원 배열 (2D Array / Mảng 2 chiều)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “178. 2차원 배열 (2D Array / Mảng 2 chiều)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 변수들을 평면, 즉 행과 열로 조합한 배열이다. (Tập hợp các biến theo dạng bảng gồm hàng và cột).
  - *Example / Ví dụ*: `int b[2][3] = {{11, 22, 33}, {44, 55, 66}};`
  - 💡 *Mẹo ghi nhớ*: `[hàng][cột]` (Row x Column).

Với **178. 2차원 배열 (2D Array / Mảng 2 chiều)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

**178. 2차원 배열 (2D Array / Mảng 2 chiều)** vừa cho ta cách đặt câu hỏi. Bây giờ **179. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **179. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 179. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng)

Bây giờ ta đi vào nội dung của **179. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “179. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- C언어에서는 큰따옴표("")로 묶인 글자는 문자열로 처리된다. (Trong C, chữ nằm trong ngoặc kép được xem là chuỗi).
- 배열에 문자열을 저장하면 널 문자('\0')가 문자열 끝에 자동으로 삽입된다. (Khi lưu chuỗi vào mảng, ký tự null `\0` tự động được thêm vào cuối).
  - *Example / Ví dụ*: `char a[5] = "love";` (Bao gồm l, o, v, e, \0).
  - 💡 *Mẹo ghi nhớ*: Độ dài mảng phải lớn hơn số ký tự của chuỗi ít nhất 1 (để chứa `\0`).

Với **179. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **179. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **180. 포인터와 포인터 변수 (Pointers / Con trỏ)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **180. 포인터와 포인터 변수 (Pointers / Con trỏ)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 180. 포인터와 포인터 변수 (Pointers / Con trỏ)

Phần nguồn của **180. 포인터와 포인터 변수 (Pointers / Con trỏ)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “180. 포인터와 포인터 변수 (Pointers / Con trỏ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 포인터 변수를 선언할 때는 자료형 뒤에 `*`를 붙인다. (Khai báo biến con trỏ bằng dấu `*`).
- 변수의 주소를 알아낼 때는 `&`를 붙인다. (Lấy địa chỉ của biến bằng dấu `&`).
- 실행문에서 포인터 변수에 `*`를 붙이면 해당 변수가 가리키는 곳의 값을 의미한다. (Dùng `*` trước con trỏ để lấy giá trị tại địa chỉ đó).
  - *Example / Ví dụ*: `int a = 50; int *b = &a; printf("%d", *b);` (In ra 50).
  - 💡 *Mẹo ghi nhớ*: `&` là địa chỉ (Address), `*` là giá trị (Value).

Với **180. 포인터와 포인터 변수 (Pointers / Con trỏ)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **180. 포인터와 포인터 변수 (Pointers / Con trỏ)**, đừng bắt đầu lại từ số không. **181. 포인터와 배열 (Pointer and Array / Con trỏ và mảng)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **181. 포인터와 배열 (Pointer and Array / Con trỏ và mảng)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 181. 포인터와 배열 (Pointer and Array / Con trỏ và mảng)

Các ý ngay dưới **181. 포인터와 배열 (Pointer and Array / Con trỏ và mảng)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “181. 포인터와 배열 (Pointer and Array / Con trỏ và mảng)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 배열을 포인터 변수에 저장한 후 포인터를 이용해 배열의 요소에 접근할 수 있다. (Có thể dùng con trỏ để truy cập các phần tử mảng).
- 배열의 대표명은 배열의 첫 번째 요소의 주소와 같다. (Tên mảng chính là địa chỉ của phần tử đầu tiên).
  - *Example / Ví dụ*: `int a[5]; int *b = a;` tương đương với `b = &a[0];`.
  - 💡 *Mẹo ghi nhớ*: `a[i]` hoàn toàn tương đương với `*(a + i)`.

Với **181. 포인터와 배열 (Pointer and Array / Con trỏ và mảng)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Như vậy, **181. 포인터와 배열 (Pointer and Array / Con trỏ và mảng)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **배열 심화 (Arrays - Advanced)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 배열 심화 (Arrays - Advanced)

Sau khi đã đặt nền bằng **구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)**, ta chuyển sang **배열 심화 (Arrays - Advanced)**. Đây là mắt xích 20/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **배열 심화 (Arrays - Advanced)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **258. 배열과 1차원 배열 (Array & 1D Array / Mảng 1 chiều - Bổ sung)**. Hãy xác định **258. 배열과 1차원 배열 (Array & 1D Array / Mảng 1 chiều - Bổ sung)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 258. 배열과 1차원 배열 (Array & 1D Array / Mảng 1 chiều - Bổ sung)

Phần nguồn của **258. 배열과 1차원 배열 (Array & 1D Array / Mảng 1 chiều - Bổ sung)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “258. 배열과 1차원 배열 (Array & 1D Array / Mảng 1 chiều - Bổ sung)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 배열은 행 우선으로 데이터가 할당된다. (Mảng được cấp phát theo thứ tự ưu tiên hàng).
- 첨자 없이 배열 이름을 사용하면 첫 번째 요소의 주소를 지정하는 것과 같다. (Tên mảng không có chỉ số chính là địa chỉ phần tử đầu tiên).
  - *Example / Ví dụ*: Khởi tạo mảng bằng `for` loop: `for(i=0; i<5; i++) a[i] = i+10;`
  - 💡 *Mẹo ghi nhớ*: Mảng trong C/Java đếm từ 0.

Với **258. 배열과 1차원 배열 (Array & 1D Array / Mảng 1 chiều - Bổ sung)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **258. 배열과 1차원 배열 (Array & 1D Array / Mảng 1 chiều - Bổ sung)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **259. 2차원 배열 (2D Array / Mảng 2 chiều - Bổ sung)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **259. 2차원 배열 (2D Array / Mảng 2 chiều - Bổ sung)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 259. 2차원 배열 (2D Array / Mảng 2 chiều - Bổ sung)

Các ý ngay dưới **259. 2차원 배열 (2D Array / Mảng 2 chiều - Bổ sung)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “259. 2차원 배열 (2D Array / Mảng 2 chiều - Bổ sung)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 변수들을 평면, 즉 행과 열로 조합한 배열. (Mảng kết hợp hàng và cột).
- 형식: `자료형 변수명[행개수][열개수]`
  - *Example / Ví dụ*: `int b[3][3];` (Mảng 3 hàng, 3 cột. Chỉ số hàng 0-2, cột 0-2).
  - Sử dụng vòng lặp lồng nhau (Nested loops) để gán giá trị: `for(i=0; i<3; i++) { for(j=0; j<4; j++) { a[i][j] = ++k; } }`
  - 💡 *Mẹo ghi nhớ*: Array 2D giống như ma trận Toán học. `i` là hàng (bên ngoài), `j` là cột (bên trong).

Với **259. 2차원 배열 (2D Array / Mảng 2 chiều - Bổ sung)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **259. 2차원 배열 (2D Array / Mảng 2 chiều - Bổ sung)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **배열 심화 (Arrays - Advanced)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **배열과 포인터 심화 (Arrays & Pointers - Advanced)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 배열과 포인터 심화 (Arrays & Pointers - Advanced)

Từ **배열 심화 (Arrays - Advanced)**, ta đã có điểm tựa để bước vào **배열과 포인터 심화 (Arrays & Pointers - Advanced)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 21/91 trước khi đi vào chi tiết.

Để đọc **배열과 포인터 심화 (Arrays & Pointers - Advanced)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **260. 배열의 초기화 (Array Initialization / Khởi tạo mảng)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 260. 배열의 초기화 (Array Initialization / Khởi tạo mảng)

Các ý ngay dưới **260. 배열의 초기화 (Array Initialization / Khởi tạo mảng)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “260. 배열의 초기화 (Array Initialization / Khởi tạo mảng)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 배열 선언 시 초기값을 지정할 수 있다. (Có thể gán giá trị khởi tạo ngay khi khai báo mảng).
- 배열의 크기를 생략하려면 반드시 초기값을 지정해야 한다. (Nếu bỏ trống kích thước mảng trong ngoặc `[]`, bắt buộc phải có giá trị khởi tạo để máy tự đếm).
- 적은 수로 초기화하면 나머지 요소는 0이 입력된다. (Nếu khởi tạo ít phần tử hơn kích thước mảng, các phần tử còn lại tự động bằng 0).
  - *Example / Ví dụ*: `int a[5] = {3};` -> `[3, 0, 0, 0, 0]`.
  - 💡 *Mẹo ghi nhớ*: C/Java không tự làm sạch bộ nhớ trừ khi bạn khởi tạo ít nhất 1 phần tử.

Với **260. 배열의 초기화 (Array Initialization / Khởi tạo mảng)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **260. 배열의 초기화 (Array Initialization / Khởi tạo mảng)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **261. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng - Bổ sung)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **261. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng - Bổ sung)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 261. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng - Bổ sung)

Bây giờ ta đi vào nội dung của **261. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng - Bổ sung)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “261. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng - Bổ sung)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 배열에 문자열을 저장할 때는 초기값으로 지정해야 하며, 이미 선언된 배열에는 대입 연산자로 문자열을 통째로 저장할 수 없다. (Chỉ được gán chuỗi trực tiếp lúc khởi tạo. Không được gán chuỗi vào mảng đã khai báo bằng dấu `=`).
- `%s`를 이용해 문자열을 출력할 때는 배열 이름이나 포인터 변수만 적어주면 된다. (Khi in chuỗi bằng `%s`, chỉ cần truyền tên mảng hoặc con trỏ, không cần dấu `&`).

Các bullet của **261. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng - Bổ sung)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **261. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng - Bổ sung)**, đừng bắt đầu lại từ số không. **262. 포인터와 포인터 변수 (Pointer & Pointer Variable / Con trỏ - Bổ sung)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **262. 포인터와 포인터 변수 (Pointer & Pointer Variable / Con trỏ - Bổ sung)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 262. 포인터와 포인터 변수 (Pointer & Pointer Variable / Con trỏ - Bổ sung)

Phần nguồn của **262. 포인터와 포인터 변수 (Pointer & Pointer Variable / Con trỏ - Bổ sung)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “262. 포인터와 포인터 변수 (Pointer & Pointer Variable / Con trỏ - Bổ sung)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 포인터 변수는 동적으로 할당되는 메모리 영역인 **힙(Heap) 영역**에 접근하는 동적 변수이다. (Con trỏ là biến động truy cập vào vùng nhớ Heap được cấp phát động).
- `*` 연산자: 간접 연산자 (Lấy giá trị).
- `&` 연산자: 번지 연산자 (Lấy địa chỉ).
  - 💡 *Mẹo ghi nhớ*: Con trỏ giống như tấm bản đồ (chỉ chứa địa chỉ), dùng `*` để đi đến đích và lấy kho báu (giá trị).

Các bullet của **262. 포인터와 포인터 변수 (Pointer & Pointer Variable / Con trỏ - Bổ sung)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**262. 포인터와 포인터 변수 (Pointer & Pointer Variable / Con trỏ - Bổ sung)** vừa cho ta cách đặt câu hỏi. Bây giờ **263. 포인터와 배열 (Pointer & Array / Con trỏ và mảng - Bổ sung)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **263. 포인터와 배열 (Pointer & Array / Con trỏ và mảng - Bổ sung)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 263. 포인터와 배열 (Pointer & Array / Con trỏ và mảng - Bổ sung)

Các ý ngay dưới **263. 포인터와 배열 (Pointer & Array / Con trỏ và mảng - Bổ sung)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “263. 포인터와 배열 (Pointer & Array / Con trỏ và mảng - Bổ sung)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `p + 1`은 메모리 주소가 1 증가하는 것이 아니라 해당 자료형의 크기(int는 4Byte)만큼 증가한다. (`p + 1` không cộng thêm 1 vào địa chỉ, mà cộng thêm kích thước của kiểu dữ liệu, ví dụ int thì cộng thêm 4 Bytes).
  - *Example / Ví dụ*: `p` là `1000` -> `p + 1` là `1004` (với int).

Các ý về **263. 포인터와 배열 (Pointer & Array / Con trỏ và mảng - Bổ sung)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Với **263. 포인터와 배열 (Pointer & Array / Con trỏ và mảng - Bổ sung)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Điểm chốt của **배열과 포인터 심화 (Arrays & Pointers - Advanced)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)

Ở bước 22/91, **075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)** xuất hiện như phần tiếp nối của **배열과 포인터 심화 (Arrays & Pointers - Advanced)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **배열 (Array)**, **조건문 (if/switch)**, **반복문 (for/while)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **배열 (Array)**: `자료형 변수명[개수] = {초깃값};` (C/Java). 2차원 배열은 `변수명[행][열]`.
- **조건문 (if/switch)**:
  - C/Java: `if (조건) { ... } else if (조건) { ... } else { ... }`
  - Python: `if 조건:` -> `elif 조건:` -> `else:`
  - switch문 (C/Java): 식의 값에 따라 `case`를 찾아가며, `break;`가 없으면 아래 문장들도 계속 실행됨.
- **반복문 (for/while)**:
  - for문 (C/Java): `for (초기식; 조건식; 증감식) { ... }`
  - for문 (Python): `for 변수 in range(시작, 끝+1):`
  - while문: 조건이 참일 동안 반복.
  - do~while문 (C/Java): 조건과 상관없이 무조건 **최소 1번**은 실행하고 조건을 검사함.

**Giải thích (Vietnamese):**
- Trong Python, cấu trúc điều kiện là `if`, `elif` (viết tắt của else if) và `else`. Không cần ngoặc nhọn `{}` mà dùng thụt lề (indentation).
- `do~while` khác `while` ở chỗ: `do~while` sẽ làm việc trước rồi mới kiểm tra điều kiện sau, nên chắc chắn code bên trong được chạy ít nhất 1 lần.

---

Như vậy, **075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **258 - 261. 배열과 문자열 (Arrays & Strings)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 258 - 261. 배열과 문자열 (Arrays & Strings)

Sau khi đã đặt nền bằng **075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)**, ta chuyển sang **258 - 261. 배열과 문자열 (Arrays & Strings)**. Đây là mắt xích 23/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **258 - 261. 배열과 문자열 (Arrays & Strings)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **배열 (Array)**, **2차원 배열**, **배열 초기화**, **배열 형태의 문자열 (C언어)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “258 - 261. 배열과 문자열 (Arrays & Strings)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **배열 (Array)**: **동일한 자료형**의 변수들을 연속된 메모리에 모아둔 것. `인덱스(첨자)`는 0부터 시작. 배열 이름 자체가 **첫 번째 요소의 시작 주소**를 의미.
- **2차원 배열**: 행과 열의 평면 구조 (예: `a[3][4]`는 3행 4열로 총 12개).
- **배열 초기화**: 선언과 동시에 값을 넣는 것. 크기를 생략해도 값의 개수만큼 자동 결정됨. 초기화되지 않은 빈칸은 자동으로 `0`으로 채워짐.
- **배열 형태의 문자열 (C언어)**: C언어는 문자열 자료형이 없어 `char` 배열을 사용. 문자열 끝에는 반드시 **널 문자(`\0`)**가 포함되어야 함 (글자수 + 1바이트 크기 필요).

**Giải thích (Vietnamese):**
Trong C, chuỗi "love" sẽ chiếm 5 ô nhớ (l, o, v, e, `\0`). Ký tự `\0` (Null) báo hiệu cho máy tính biết "đây là kết thúc của chuỗi".

---

Ta có thể khép mục **258 - 261. 배열과 문자열 (Arrays & Strings)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **262 - 263. 포인터 (Pointers)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 262 - 263. 포인터 (Pointers)

Từ **258 - 261. 배열과 문자열 (Arrays & Strings)**, ta đã có điểm tựa để bước vào **262 - 263. 포인터 (Pointers)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 24/91 trước khi đi vào chi tiết.

Để đọc **262 - 263. 포인터 (Pointers)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **포인터 (Pointer)**, **포인터와 배열** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “262 - 263. 포인터 (Pointers)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **포인터 (Pointer)**: 변수의 실제 **메모리 주소값**을 저장하는 특수 변수.
- `*` (간접 참조 연산자): 포인터가 가리키는 주소의 '값'.
- `&` (주소 연산자): 변수의 '주소'.
- **포인터와 배열**: 배열 이름은 포인터와 같음 (`배열명 == &배열명[0]`). 포인터 연산(`p+i`)으로 배열 요소에 접근 가능.

**Giải thích (Vietnamese):**
Pointer (Con trỏ) không lưu giá trị (như số 5), mà lưu "địa chỉ nhà" (ví dụ: nhà số 100A).
`&a` là lấy địa chỉ nhà của a. `*p` là mở cửa vào nhà để lấy đồ (lấy giá trị).

---

Điểm chốt của **262 - 263. 포인터 (Pointers)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **Python 기초 (Python Basics)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## Python 기초 (Python Basics)

Ở bước 25/91, **Python 기초 (Python Basics)** xuất hiện như phần tiếp nối của **262 - 263. 포인터 (Pointers)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **Python 기초 (Python Basics)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **리스트 (List)**, **튜플 (Tuple)**, **range**, **range를 이용하는 방식 (Dùng range)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **161. Python의 시퀀스 자료형 (Python Sequence Types / Kiểu chuỗi trong Python)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **161. Python의 시퀀스 자료형 (Python Sequence Types / Kiểu chuỗi trong Python)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 161. Python의 시퀀스 자료형 (Python Sequence Types / Kiểu chuỗi trong Python)

Bây giờ ta đi vào nội dung của **161. Python의 시퀀스 자료형 (Python Sequence Types / Kiểu chuỗi trong Python)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “161. Python의 시퀀스 자료형 (Python Sequence Types / Kiểu chuỗi trong Python)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **리스트 (List)**: 요소의 추가, 삭제, 변경 가능 (Có thể thêm, xóa, sửa phần tử).
- **튜플 (Tuple)**: 요소의 추가, 삭제, 변경 불가능함 (Không thể thay đổi phần tử).
- **range**: 연속된 숫자를 생성함 (Tạo dãy số liên tiếp).
  - *Example / Ví dụ*: List `[1, 2]`, Tuple `(1, 2)`.
  - 💡 *Mẹo ghi nhớ*: List dùng `[]` và linh hoạt. Tuple dùng `()` và cố định (bất biến).

Các ý về **161. Python의 시퀀스 자료형 (Python Sequence Types / Kiểu chuỗi trong Python)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **161. Python의 시퀀스 자료형 (Python Sequence Types / Kiểu chuỗi trong Python)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **185. Python의 리스트 (Python List / Danh sách trong Python)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **185. Python의 리스트 (Python List / Danh sách trong Python)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 185. Python의 리스트 (Python List / Danh sách trong Python)

Phần nguồn của **185. Python의 리스트 (Python List / Danh sách trong Python)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “185. Python의 리스트 (Python List / Danh sách trong Python)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 크기를 지정하지 않는다. 하나의 리스트에 다양한 자료형을 섞어 저장할 수 저장할 수 있다. (Không cần chỉ định kích thước. Có thể chứa nhiều kiểu dữ liệu khác nhau).
- 위치는 0부터 시작한다. (Chỉ số bắt đầu từ 0).
  - *Example / Ví dụ*: `a = [10, 'mike', 23.45]`
  - 💡 *Mẹo ghi nhớ*: Python List giống như một cái túi thần kỳ, có thể bỏ bất cứ thứ gì vào.

Với **185. Python의 리스트 (Python List / Danh sách trong Python)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **185. Python의 리스트 (Python List / Danh sách trong Python)**, đừng bắt đầu lại từ số không. **186. Python의 딕셔너리 (Dictionary / Từ điển)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **186. Python의 딕셔너리 (Dictionary / Từ điển)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 186. Python의 딕셔너리 (Dictionary / Từ điển)

Các ý ngay dưới **186. Python의 딕셔너리 (Dictionary / Từ điển)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “186. Python의 딕셔너리 (Dictionary / Từ điển)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 연관된 값을 묶어서 저장하는 용도. (Dùng để lưu trữ dữ liệu theo cặp Khóa - Giá trị).
- 위치값 대신 사용자가 원하는 키를 직접 지정하여 사용한다. (Dùng Khóa tự định nghĩa thay vì chỉ số số học).
  - *Example / Ví dụ*: `d = {'name': 'John', 'age': 25}`
  - 💡 *Mẹo ghi nhớ*: Key-Value (Khóa-Giá trị). Dùng `{}` giống như một từ điển thực sự (tra từ -> ra nghĩa).

Với **186. Python의 딕셔너리 (Dictionary / Từ điển)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

**186. Python의 딕셔너리 (Dictionary / Từ điển)** vừa cho ta cách đặt câu hỏi. Bây giờ **187. Python의 Range (Python Range / Dãy số)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **187. Python의 Range (Python Range / Dãy số)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 187. Python의 Range (Python Range / Dãy số)

Bây giờ ta đi vào nội dung của **187. Python의 Range (Python Range / Dãy số)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “187. Python의 Range (Python Range / Dãy số)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 연속된 숫자를 생성하는 것. (Tạo dãy số liên tiếp).
  - `range(5)` -> 0, 1, 2, 3, 4
  - `range(4, 9)` -> 4, 5, 6, 7, 8
  - `range(1, 15, 3)` -> 1, 4, 7, 10, 13
  - 💡 *Mẹo ghi nhớ*: `range(start, stop, step)`. Bao gồm `start`, nhưng **không** bao gồm `stop`.

Các bullet của **187. Python의 Range (Python Range / Dãy số)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **187. Python의 Range (Python Range / Dãy số)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **188. Python의 슬라이스 (Python Slice / Cắt chuỗi/mảng)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **188. Python의 슬라이스 (Python Slice / Cắt chuỗi/mảng)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 188. Python의 슬라이스 (Python Slice / Cắt chuỗi/mảng)

Phần nguồn của **188. Python의 슬라이스 (Python Slice / Cắt chuỗi/mảng)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “188. Python의 슬라이스 (Python Slice / Cắt chuỗi/mảng)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 객체에서 일부를 잘라 반환하는 기능. (Trích xuất một phần của chuỗi hoặc mảng).
- `a[1:3]`: Lấy từ index 1 đến 2.
- `a[0:5:2]`: Lấy từ 0 đến 4, bước nhảy 2.
- `a[3:]`: Lấy từ index 3 đến cuối.
- `a[:3]`: Lấy từ đầu đến index 2.
- `a[::-1]`: Đảo ngược mảng.
  - 💡 *Mẹo ghi nhớ*: `[start : stop : step]`. Giống range, không bao gồm `stop`.

Các bullet của **188. Python의 슬라이스 (Python Slice / Cắt chuỗi/mảng)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **188. Python의 슬라이스 (Python Slice / Cắt chuỗi/mảng)**, đừng bắt đầu lại từ số không. **182. Python의 input() 함수 (Python input() Function / Hàm nhập)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **182. Python의 input() 함수 (Python input() Function / Hàm nhập)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 182. Python의 input() 함수 (Python input() Function / Hàm nhập)

Các ý ngay dưới **182. Python의 input() 함수 (Python input() Function / Hàm nhập)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “182. Python의 input() 함수 (Python input() Function / Hàm nhập)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 키보드로 입력받아 변수에 저장하는 함수이다. (Nhập từ bàn phím và lưu vào biến).
- 입력되는 값은 기본적으로 문자열로 취급된다. (Giá trị mặc định luôn là chuỗi).
  - *Example / Ví dụ*: `a = input('Nhập tên:')`

Với **182. Python의 input() 함수 (Python input() Function / Hàm nhập)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

**182. Python의 input() 함수 (Python input() Function / Hàm nhập)** vừa cho ta cách đặt câu hỏi. Bây giờ **183. Python의 print() 함수 (Python print() Function / Hàm in)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **183. Python의 print() 함수 (Python print() Function / Hàm in)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 183. Python의 print() 함수 (Python print() Function / Hàm in)

Bây giờ ta đi vào nội dung của **183. Python의 print() 함수 (Python print() Function / Hàm in)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “183. Python의 print() 함수 (Python print() Function / Hàm in)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 인수로 주어진 값을 출력한다. (In giá trị ra màn hình).
  - *Example / Ví dụ*: `print(82, 24, sep='-', end=',')` -> `82-24,`
  - 💡 *Mẹo ghi nhớ*: `sep` = phân cách giữa các đối số, `end` = ký tự kết thúc (mặc định là xuống dòng `\n`).

Với **183. Python의 print() 함수 (Python print() Function / Hàm in)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **183. Python의 print() 함수 (Python print() Function / Hàm in)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **184. 입력 값의 형변환 (Input Type Casting / Ép kiểu dữ liệu đầu vào)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **184. 입력 값의 형변환 (Input Type Casting / Ép kiểu dữ liệu đầu vào)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 184. 입력 값의 형변환 (Input Type Casting / Ép kiểu dữ liệu đầu vào)

Phần nguồn của **184. 입력 값의 형변환 (Input Type Casting / Ép kiểu dữ liệu đầu vào)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “184. 입력 값의 형변환 (Input Type Casting / Ép kiểu dữ liệu đầu vào)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `input()` 함수는 무조건 문자열로 저장하므로, 숫자로 사용하려면 형 변환이 필요하다. (Vì `input()` trả về chuỗi, cần ép kiểu nếu muốn dùng số).
- 변환할 데이터가 1개: `a = int(input())`
- 변환할 데이터가 2개 이상: `a, b = map(int, input().split())`
  - 💡 *Mẹo ghi nhớ*: `split()` để cắt khoảng trắng, `map()` để ép tất cả sang kiểu nguyên `int`.

Với **184. 입력 값의 형변환 (Input Type Casting / Ép kiểu dữ liệu đầu vào)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **184. 입력 값의 형변환 (Input Type Casting / Ép kiểu dữ liệu đầu vào)**, đừng bắt đầu lại từ số không. **189. Python의 for문 (Python for loop)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **189. Python의 for문 (Python for loop)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 189. Python의 for문 (Python for loop)

Các ý ngay dưới **189. Python의 for문 (Python for loop)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “189. Python의 for문 (Python for loop)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **range를 이용하는 방식 (Dùng range)**: `for i in range(1, 11): sum = sum + i`
- **리스트를 이용하는 방식 (Dùng list)**: `for i in a:` (với `a` là list).
  - 💡 *Mẹo ghi nhớ*: `for item in tập_hợp`. Lặp qua từng phần tử.

Với **189. Python의 for문 (Python for loop)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

**189. Python의 for문 (Python for loop)** vừa cho ta cách đặt câu hỏi. Bây giờ **191. Python의 클래스 및 메소드 (Python Classes & Methods / Lớp và phương thức)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **191. Python의 클래스 및 메소드 (Python Classes & Methods / Lớp và phương thức)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 191. Python의 클래스 및 메소드 (Python Classes & Methods / Lớp và phương thức)

Bây giờ ta đi vào nội dung của **191. Python의 클래스 및 메소드 (Python Classes & Methods / Lớp và phương thức)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “191. Python의 클래스 및 메소드 (Python Classes & Methods / Lớp và phương thức)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 클래스 없이 메소드만 단독으로 사용할 수 있다. (Có thể sử dụng phương thức độc lập mà không cần lớp).
- 클래스를 사용하려면 속성과 메소드를 정의한 후 객체를 선언한다. (Để dùng lớp, định nghĩa thuộc tính và phương thức, sau đó khởi tạo đối tượng).
  - *Example / Ví dụ*: `def calc(x, y): return x * y` (Hàm độc lập). `class Cls: x = 10` (Lớp).
  - 💡 *Mẹo ghi nhớ*: Python hỗ trợ cả lập trình thủ tục (như C) và hướng đối tượng (OOP). Tham số đầu tiên của hàm trong lớp luôn là `self`.

Với **191. Python의 클래스 및 메소드 (Python Classes & Methods / Lớp và phương thức)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **191. Python의 클래스 및 메소드 (Python Classes & Methods / Lớp và phương thức)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Như vậy, **Python 기초 (Python Basics)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **Python 기본 문법 (Python Basic Syntax)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## Python 기본 문법 (Python Basic Syntax)

Sau khi đã đặt nền bằng **Python 기초 (Python Basics)**, ta chuyển sang **Python 기본 문법 (Python Basic Syntax)**. Đây là mắt xích 26/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **Python 기본 문법 (Python Basic Syntax)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **자료형 선언 없음**, **세미콜론 생략**, **연속 할당**, **코드 블록** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **264. Python의 기본 문법 (Python Basic Syntax / Cú pháp cơ bản của Python)**. Hãy xác định **264. Python의 기본 문법 (Python Basic Syntax / Cú pháp cơ bản của Python)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 264. Python의 기본 문법 (Python Basic Syntax / Cú pháp cơ bản của Python)

Phần nguồn của **264. Python의 기본 문법 (Python Basic Syntax / Cú pháp cơ bản của Python)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “264. Python의 기본 문법 (Python Basic Syntax / Cú pháp cơ bản của Python)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **자료형 선언 없음**: 변수 선언 시 타입을 명시하지 않는다. (Không cần khai báo kiểu dữ liệu).
- **세미콜론 생략**: 문장 끝에 `;`이 필요 없다. (Không cần dấu chấm phẩy ở cuối câu).
- **연속 할당**: `x, y, z = 10, 20, 30` (Có thể gán liên tiếp nhiều biến).
- **코드 블록**: 콜론(`:`)과 여백(Indentation)으로 구분한다. (Dùng dấu hai chấm và thụt lề để xác định khối lệnh, thay vì dùng `{ }`).
  - 💡 *Mẹo ghi nhớ*: Python yêu cầu thụt lề (thường là 4 spaces) vô cùng khắt khe. Sai thụt lề = Lỗi (IndentationError).

Với **264. Python의 기본 문법 (Python Basic Syntax / Cú pháp cơ bản của Python)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **264. Python의 기본 문법 (Python Basic Syntax / Cú pháp cơ bản của Python)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **265 ~ 269. Python 입출력, 리스트, 딕셔너리, 슬라이스 (Python I/O, List, Dict, Slice - Ôn tập)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **265 ~ 269. Python 입출력, 리스트, 딕셔너리, 슬라이스 (Python I/O, List, Dict, Slice - Ôn tập)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 265 ~ 269. Python 입출력, 리스트, 딕셔너리, 슬라이스 (Python I/O, List, Dict, Slice - Ôn tập)

Các ý ngay dưới **265 ~ 269. Python 입출력, 리스트, 딕셔너리, 슬라이스 (Python I/O, List, Dict, Slice - Ôn tập)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “265 ~ 269. Python 입출력, 리스트, 딕셔너리, 슬라이스 (Python I/O, List, Dict, Slice - Ôn tập)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

*(Các khái niệm này đã được đề cập kỹ ở phần trước, dưới đây là tóm tắt nhanh các điểm chú ý)*:
- **`input()`**: Luôn trả về chuỗi. Dùng `int(input())` để ép kiểu. Đa trị: `map(int, input().split())`.
- **`print()`**: Có thể dùng `sep` (ký tự phân tách) và `end` (ký tự kết thúc).
- **리스트 (List)**: Khai báo bằng `[]` hoặc `list()`. Hỗ trợ chứa nhiều kiểu dữ liệu hỗn hợp.
- **딕셔너리 (Dictionary)**: Khai báo bằng `{}` hoặc `dict()`. Cấu trúc Key:Value.
- **슬라이스 (Slice)**: Cắt `[start:stop:step]`. Nếu bỏ trống `start` thì lấy từ đầu, bỏ trống `stop` thì lấy đến cuối.

Các bullet của **265 ~ 269. Python 입출력, 리스트, 딕셔너리, 슬라이스 (Python I/O, List, Dict, Slice - Ôn tập)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **265 ~ 269. Python 입출력, 리스트, 딕셔너리, 슬라이스 (Python I/O, List, Dict, Slice - Ôn tập)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **Python 기본 문법 (Python Basic Syntax)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **236. Python의 시퀀스 자료형 (Sequence Data Types in Python)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 236. Python의 시퀀스 자료형 (Sequence Data Types in Python)

Từ **Python 기본 문법 (Python Basic Syntax)**, ta đã có điểm tựa để bước vào **236. Python의 시퀀스 자료형 (Sequence Data Types in Python)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 27/91 trước khi đi vào chi tiết.

Để đọc **236. Python의 시퀀스 자료형 (Sequence Data Types in Python)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **리스트(List)**, **튜플(Tuple)**, **range** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “236. Python의 시퀀스 자료형 (Sequence Data Types in Python)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 여러 값이 연속적으로 이어진 데이터 구조.
- **리스트(List)**: `[]` 사용. 데이터의 추가/삭제/변경이 자유로움 (Mutable).
- **튜플(Tuple)**: `()` 사용. 한 번 생성하면 데이터의 변경(수정/삭제)이 **불가능함** (Immutable). 읽기 전용에 적합.
- **range**: 반복문에서 연속된 숫자를 생성할 때 사용.

**Giải thích (Vietnamese):**
List và Tuple đều dùng để lưu danh sách. Nhưng List có thể sửa được, còn Tuple thì "Bất di bất dịch" (không thể thêm/xoá/sửa sau khi tạo).

---

Điểm chốt của **236. Python의 시퀀스 자료형 (Sequence Data Types in Python)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **264 - 274. 파이썬 문법 (Python Syntax & Basics)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 264 - 274. 파이썬 문법 (Python Syntax & Basics)

Ở bước 28/91, **264 - 274. 파이썬 문법 (Python Syntax & Basics)** xuất hiện như phần tiếp nối của **236. Python의 시퀀스 자료형 (Sequence Data Types in Python)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **264 - 274. 파이썬 문법 (Python Syntax & Basics)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **기본 문법**, **입출력**, **형변환 (Casting)**, **자료형** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “264 - 274. 파이썬 문법 (Python Syntax & Basics)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **기본 문법**: 자료형 선언 생략, 세미콜론(`;`) 불필요. 코드 블록은 중괄호 `{}` 대신 **콜론(`:`)과 들여쓰기(Indentation)**로 구분.
- **입출력**: `input()` (기본적으로 모두 문자열로 입력받음), `print()`. `sep`(분리 문자), `end`(종료 문자).
- **형변환 (Casting)**: `int()`(정수), `float()`(실수). 여러 개 입력 받을 땐 `map(int, input().split())` 사용.
- **자료형**:
  - **리스트 (List, `[]`)**: 수정/추가/삭제 자유로움 (Mutable). 서로 다른 타입 혼용 가능.
  - **딕셔너리 (Dictionary, `{}`)**: `Key:Value` 쌍으로 저장 (해시 맵). Key로 빠르게 검색.
  - **슬라이스 (Slice)**: `객체[시작:끝:증가값]`. 끝 번호는 제외됨 (n-1까지). 원본은 변경하지 않음.
- **제어문**: `if`, **`elif`** (else if 아님), `else`. `for i in range(시작, 끝)` 또는 `for i in 리스트`. `while`문.
- **클래스 (Class)**: `class` 키워드. 메소드(함수) 정의 시 첫 번째 매개변수로 반드시 **`self`**를 써야 함. 파이썬은 클래스 밖에서도 `def`로 독립된 함수를 만들 수 있음.

**Giải thích (Vietnamese):**
- Python dùng "thụt lề" (indentation) để phân chia các khối code thay vì `{}`.
- `input()` luôn trả về chuỗi (String). Nếu nhập số 5, nó hiểu là chữ "5". Phải bọc lại bằng `int(input())`.
- Dictionary giống như từ điển: tra chữ "Apple" (Key) ra "Quả táo" (Value).
- Cắt lát (Slicing): `a[1:4]` lấy các phần tử ở index 1, 2, 3 (không lấy 4).

---

Như vậy, **264 - 274. 파이썬 문법 (Python Syntax & Basics)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **A+ Deep Dive: Java 비교 연산과 Python 제어 흐름**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## A+ Deep Dive: Java 비교 연산과 Python 제어 흐름

Sau khi đã đặt nền bằng **264 - 274. 파이썬 문법 (Python Syntax & Basics)**, ta chuyển sang **A+ Deep Dive: Java 비교 연산과 Python 제어 흐름**. Đây là mắt xích 29/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **A+ Deep Dive: Java 비교 연산과 Python 제어 흐름** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. Java의 `==`는 문맥을 먼저 본다**. Hãy xác định **1. Java의 `==`는 문맥을 먼저 본다** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. Java의 `==`는 문맥을 먼저 본다

Phần nguồn của **1. Java의 `==`는 문맥을 먼저 본다** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1. Java의 `==`는 문맥을 먼저 본다” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

```java
int a = 1;
double b = 1.0;
System.out.println(a == b);        // true: 수치 승격 후 비교
String x = new String("A");
String y = new String("A");
System.out.println(x == y);        // false: 서로 다른 객체 참조
System.out.println(x.equals(y));   // true: 내용 비교
```

- 숫자형 피연산자는 binary numeric promotion 후 비교한다.
- 참조형 `==`는 같은 객체를 가리키는지 비교하고, 문자열 내용 비교에는 `equals`를 사용한다.
- `a == b == c`는 “세 값이 모두 같은가”가 아니라 왼쪽부터 계산되므로 별도 비교식이 필요하다.

Với **1. Java의 `==`는 문맥을 먼저 본다**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **1. Java의 `==`는 문맥을 먼저 본다** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. Python `for`와 `while`의 trace 포인트** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. Python `for`와 `while`의 trace 포인트** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. Python `for`와 `while`의 trace 포인트

Các ý ngay dưới **2. Python `for`와 `while`의 trace 포인트** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “2. Python `for`와 `while`의 trace 포인트” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

```python
items = [1, 2, 3]
total = 0
for value in items:
    if value == 2:
        continue
    total += value
print(total)  # 4
```

`continue`는 현재 반복의 나머지를 건너뛰고 다음 반복으로 이동한다. `break`는 반복문 전체를 종료한다. 문제를 풀 때 초기값, 조건 검사 시점, 증감/자료 갱신 위치를 표로 추적한다.

> **시험 함정:** Java 문자열의 `==`와 `equals`, Python의 `continue`와 `break`를 섞지 않는다.

Với **2. Python `for`와 `while`의 trace 포인트**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **2. Python `for`와 `while`의 trace 포인트**, đừng bắt đầu lại từ số không. **자주 혼동하는 판별 포인트** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **자주 혼동하는 판별 포인트**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 자주 혼동하는 판별 포인트

Bây giờ ta đi vào nội dung của **자주 혼동하는 판별 포인트**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “자주 혼동하는 판별 포인트” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- C 반복문은 초기값·조건·증감식과 실제 접근 인덱스를 따로 표로 적는다. `i += 2`이면 짝수 인덱스만 방문할 수 있다.
- Java의 후위 감소 `y--`는 비교에 현재 값을 사용한 뒤 값을 줄인다. 반복 종료 시점의 변수값을 마지막 조건 평가까지 반영한다.
- Python `split(delimiter)`는 지정한 구분자로 문자열을 나누고, `map(int, ...)`는 각 조각을 정수로 바꾼다.
- IPv6는 128비트 주소와 anycast를 사용한다. IPv6 패킷/헤더 크기를 무제한으로 해석하거나 IPv4의 32비트와 혼동하지 않는다.

Các bullet của **자주 혼동하는 판별 포인트** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **자주 혼동하는 판별 포인트** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **A+ Deep Dive: Java 비교 연산과 Python 제어 흐름** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)

Từ **A+ Deep Dive: Java 비교 연산과 Python 제어 흐름**, ta đã có điểm tựa để bước vào **080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 30/91 trước khi đi vào chi tiết.

Để đọc **080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **C언어 표준 라이브러리**, **예외처리 (Exception Handling)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **C언어 표준 라이브러리**:
  - `stdio.h`: 입출력 (`printf`, `scanf`).
  - `stdlib.h`: 자료형 변환 (`atoi`: char->int).
  - `string.h`: 문자열 처리 (`strlen`, `strcpy`).
  - `math.h`: 수학 함수 (`sqrt`: 제곱근).
- **예외처리 (Exception Handling)**:
  - JAVA: `try { 실행 } catch (예외객체 e) { 에러처리 } finally { 무조건 실행 }`
  - Python: `try: ... except 예외객체: ... finally: ...`
  - 주요 예외객체: `NullPointerException` (객체가 없을 때), `ZeroDivisionError` (0으로 나눌 때).

---

Điểm chốt của **080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **279 - 280. 라이브러리 (Library)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 279 - 280. 라이브러리 (Library)

Ở bước 31/91, **279 - 280. 라이브러리 (Library)** xuất hiện như phần tiếp nối của **080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **279 - 280. 라이브러리 (Library)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **라이브러리**, **C언어 표준 라이브러리 (Header Files)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “279 - 280. 라이브러리 (Library)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **라이브러리**: 자주 사용되는 함수/데이터를 모아 놓은 집합체 (개발 시간 단축, 코드 재사용).
- **C언어 표준 라이브러리 (Header Files)**:
  - `stdio.h`: 입출력 (`printf`, `scanf`)
  - `math.h`: 수학 연산 (`sqrt`, `pow`, `abs`)
  - `string.h`: 문자열 처리
  - `stdlib.h`: 유틸리티, 자료형 변환, 메모리 할당

**Giải thích (Vietnamese):**
Thư viện (Library) giống như siêu thị bán đồ làm sẵn. Bạn không cần tự viết code để tính căn bậc 2, chỉ cần gọi hàm `sqrt` trong thư viện `math.h` là xong.

---

Như vậy, **279 - 280. 라이브러리 (Library)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **스크립트 및 운영체제 (Script Languages & Operating Systems)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 스크립트 및 운영체제 (Script Languages & Operating Systems)

Sau khi đã đặt nền bằng **279 - 280. 라이브러리 (Library)**, ta chuyển sang **스크립트 및 운영체제 (Script Languages & Operating Systems)**. Đây là mắt xích 32/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **스크립트 및 운영체제 (Script Languages & Operating Systems)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **자바스크립트 (JavaScript)**, **PHP**, **파이썬 (Python)**, **쉘 스크립트 (Shell Script)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **193. 스크립트 언어의 종류 (Types of Scripting Languages / Các loại ngôn ngữ kịch bản)**. Hãy xác định **193. 스크립트 언어의 종류 (Types of Scripting Languages / Các loại ngôn ngữ kịch bản)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 193. 스크립트 언어의 종류 (Types of Scripting Languages / Các loại ngôn ngữ kịch bản)

Phần nguồn của **193. 스크립트 언어의 종류 (Types of Scripting Languages / Các loại ngôn ngữ kịch bản)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “193. 스크립트 언어의 종류 (Types of Scripting Languages / Các loại ngôn ngữ kịch bản)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **자바스크립트 (JavaScript)**: 클라이언트용 웹 동작 제어 (Phía client, điều khiển hành vi web).
- **PHP**: 서버용 스크립트 언어 (Phía server, dùng trên Linux, Unix, Windows).
- **파이썬 (Python)**: 대화형 인터프리터 언어 (Ngôn ngữ thông dịch tương tác).
- **쉘 스크립트 (Shell Script)**: 명령어들의 조합 (Tập hợp các lệnh shell).
- **Basic**: 절차지향 대화형 인터프리터 (Thông dịch tương tác, hướng thủ tục).
  - 💡 *Mẹo ghi nhớ*: JS = Client Web, PHP = Server, Python = Thông dịch, Shell = Lệnh HĐH.

Với **193. 스크립트 언어의 종류 (Types of Scripting Languages / Các loại ngôn ngữ kịch bản)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **193. 스크립트 언어의 종류 (Types of Scripting Languages / Các loại ngôn ngữ kịch bản)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **194. 쉘 스크립트 제어문 (Shell Script Control Statements)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **194. 쉘 스크립트 제어문 (Shell Script Control Statements)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 194. 쉘 스크립트 제어문 (Shell Script Control Statements)

Các ý ngay dưới **194. 쉘 스크립트 제어문 (Shell Script Control Statements)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “194. 쉘 스크립트 제어문 (Shell Script Control Statements)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **선택형 (Điều kiện)**: `if`, `case`
- **반복형 (Vòng lặp)**: `for`, `while`, `until`

Các bullet của **194. 쉘 스크립트 제어문 (Shell Script Control Statements)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **194. 쉘 스크립트 제어문 (Shell Script Control Statements)**, đừng bắt đầu lại từ số không. **195. 라이브러리 (Libraries / Thư viện)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **195. 라이브러리 (Libraries / Thư viện)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 195. 라이브러리 (Libraries / Thư viện)

Bây giờ ta đi vào nội dung của **195. 라이브러리 (Libraries / Thư viện)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “195. 라이브러리 (Libraries / Thư viện)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **표준 (Standard)**: 기본적으로 포함된 모듈 (Tích hợp sẵn trong ngôn ngữ).
- **외부 (External)**: 다운받아 설치한 후 사용 (Phải tải và cài đặt từ bên ngoài).
  - 💡 *Mẹo ghi nhớ*: Built-in = Không cần cài, External = Cần pip/npm/v.v.

Với **195. 라이브러리 (Libraries / Thư viện)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

**195. 라이브러리 (Libraries / Thư viện)** vừa cho ta cách đặt câu hỏi. Bây giờ **196. C언어의 stdlib.h (Standard Library in C)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **196. C언어의 stdlib.h (Standard Library in C)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 196. C언어의 stdlib.h (Standard Library in C)

Phần nguồn của **196. C언어의 stdlib.h (Standard Library in C)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “196. C언어의 stdlib.h (Standard Library in C)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 자료형 변환, 난수 발생, 메모리 할당 기능을 제공한다. (Cung cấp chức năng ép kiểu, tạo số ngẫu nhiên, cấp phát bộ nhớ).
- 주요 함수 (Các hàm chính): `atoi`, `atof`, `srand`, `rand`, `malloc`, `free`.

Các bullet của **196. C언어의 stdlib.h (Standard Library in C)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **196. C언어의 stdlib.h (Standard Library in C)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **197. UNIX의 특징 (Features of UNIX / Đặc điểm của UNIX)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **197. UNIX의 특징 (Features of UNIX / Đặc điểm của UNIX)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 197. UNIX의 특징 (Features of UNIX / Đặc điểm của UNIX)

Các ý ngay dưới **197. UNIX의 특징 (Features of UNIX / Đặc điểm của UNIX)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “197. UNIX의 특징 (Features of UNIX / Đặc điểm của UNIX)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

---

Phần **197. UNIX의 특징 (Features of UNIX / Đặc điểm của UNIX)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Sau khi đọc **197. UNIX의 특징 (Features of UNIX / Đặc điểm của UNIX)**, đừng bắt đầu lại từ số không. **206. UNIX의 주요 명령어 (UNIX Commands / Lệnh UNIX)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **206. UNIX의 주요 명령어 (UNIX Commands / Lệnh UNIX)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 206. UNIX의 주요 명령어 (UNIX Commands / Lệnh UNIX)

Bây giờ ta đi vào nội dung của **206. UNIX의 주요 명령어 (UNIX Commands / Lệnh UNIX)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “206. UNIX의 주요 명령어 (UNIX Commands / Lệnh UNIX)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `fork`: 새로운 프로세스 생성 (Tạo tiến trình mới).
- `uname`: 시스템 정보 표시 (Hiển thị thông tin hệ thống).
- `wait`: 자식 프로세스 종료 대기 (Chờ tiến trình con kết thúc).
- `chmod`: 파일 보호 모드 설정 (Đổi quyền truy cập file).
- `ls`: 파일 목록 확인 (Liệt kê file).
- `cat`: 파일 내용 표시 (Xem nội dung file).
- `chown`: 소유자 변경 (Đổi chủ sở hữu file).
  - 💡 *Mẹo ghi nhớ*: fork (nhân bản, nĩa), chmod (change mode), chown (change owner).

Các bullet của **206. UNIX의 주요 명령어 (UNIX Commands / Lệnh UNIX)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **206. UNIX의 주요 명령어 (UNIX Commands / Lệnh UNIX)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **스크립트 및 운영체제 (Script Languages & Operating Systems)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)

Từ **스크립트 및 운영체제 (Script Languages & Operating Systems)**, ta đã có điểm tựa để bước vào **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 33/91 trước khi đi vào chi tiết.

Để đọc **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **최초 적합 (First Fit)**, **최적 적합 (Best Fit)**, **최악 적합 (Worst Fit)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **200. 기억장치의 배치 전략 (Memory Placement Strategies / Chiến lược cấp phát bộ nhớ)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 200. 기억장치의 배치 전략 (Memory Placement Strategies / Chiến lược cấp phát bộ nhớ)

Các ý ngay dưới **200. 기억장치의 배치 전략 (Memory Placement Strategies / Chiến lược cấp phát bộ nhớ)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “200. 기억장치의 배치 전략 (Memory Placement Strategies / Chiến lược cấp phát bộ nhớ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **최초 적합 (First Fit)**: 첫 번째 분할 영역에 배치 (Vị trí trống đầu tiên đủ lớn).
- **최적 적합 (Best Fit)**: 단편화가 가장 작은 영역 (Vị trí trống vừa vặn nhất, để lại ít rác nhất).
- **최악 적합 (Worst Fit)**: 단편화가 가장 큰 영역 (Vị trí trống lớn nhất).
  - 💡 *Mẹo ghi nhớ*: First = Nhanh nhất. Best = Tiết kiệm nhất. Worst = Còn lại khoảng trống lớn nhất.

Với **200. 기억장치의 배치 전략 (Memory Placement Strategies / Chiến lược cấp phát bộ nhớ)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **200. 기억장치의 배치 전략 (Memory Placement Strategies / Chiến lược cấp phát bộ nhớ)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **201. 페이지 교체 알고리즘 - FIFO (Page Replacement - FIFO / Thuật toán thay thế trang)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **201. 페이지 교체 알고리즘 - FIFO (Page Replacement - FIFO / Thuật toán thay thế trang)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 201. 페이지 교체 알고리즘 - FIFO (Page Replacement - FIFO / Thuật toán thay thế trang)

Bây giờ ta đi vào nội dung của **201. 페이지 교체 알고리즘 - FIFO (Page Replacement - FIFO / Thuật toán thay thế trang)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “201. 페이지 교체 알고리즘 - FIFO (Page Replacement - FIFO / Thuật toán thay thế trang)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 가장 먼저 들어와서 가장 오래 있었던 페이지를 교체 (Thay thế trang vào bộ nhớ sớm nhất - First In First Out).

Các bullet của **201. 페이지 교체 알고리즘 - FIFO (Page Replacement - FIFO / Thuật toán thay thế trang)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **201. 페이지 교체 알고리즘 - FIFO (Page Replacement - FIFO / Thuật toán thay thế trang)**, đừng bắt đầu lại từ số không. **202. 스래싱 (Thrashing)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **202. 스래싱 (Thrashing)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 202. 스래싱 (Thrashing)

Phần nguồn của **202. 스래싱 (Thrashing)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “202. 스래싱 (Thrashing)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 프로세스 처리 시간보다 페이지 교체 시간이 더 많아지는 현상 (Hiện tượng mất nhiều thời gian cho việc tráo đổi trang bộ nhớ hơn là thực thi tiến trình).
  - 💡 *Mẹo ghi nhớ*: Thrashing = Kẹt xe bộ nhớ (quá tải).

Với **202. 스래싱 (Thrashing)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

**202. 스래싱 (Thrashing)** vừa cho ta cách đặt câu hỏi. Bây giờ **203. 프로세스 상태 (Process States / Trạng thái tiến trình)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **203. 프로세스 상태 (Process States / Trạng thái tiến trình)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 203. 프로세스 상태 (Process States / Trạng thái tiến trình)

Các ý ngay dưới **203. 프로세스 상태 (Process States / Trạng thái tiến trình)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “203. 프로세스 상태 (Process States / Trạng thái tiến trình)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 제출(Submit) → 접수(Hold) → 준비(Ready) → 실행(Run) → 대기(Wait/Block) → 종료(Exit).
  - 💡 *Mẹo ghi nhớ*: Nộp -> Nhận -> Chờ chạy -> Chạy -> (Tạm dừng nếu cần) -> Xong.

Các bullet của **203. 프로세스 상태 (Process States / Trạng thái tiến trình)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **203. 프로세스 상태 (Process States / Trạng thái tiến trình)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **204. 스케줄링 - SJF (Shortest Job First / Việc ngắn làm trước)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **204. 스케줄링 - SJF (Shortest Job First / Việc ngắn làm trước)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 204. 스케줄링 - SJF (Shortest Job First / Việc ngắn làm trước)

Bây giờ ta đi vào nội dung của **204. 스케줄링 - SJF (Shortest Job First / Việc ngắn làm trước)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “204. 스케줄링 - SJF (Shortest Job First / Việc ngắn làm trước)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 실행 시간이 가장 짧은 프로세스에게 먼저 CPU 할당 (Ưu tiên tiến trình có thời gian thực thi ngắn nhất).

Các bullet của **204. 스케줄링 - SJF (Shortest Job First / Việc ngắn làm trước)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **204. 스케줄링 - SJF (Shortest Job First / Việc ngắn làm trước)**, đừng bắt đầu lại từ số không. **205. 스케줄링 - HRN (Highest Response-ratio Next)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **205. 스케줄링 - HRN (Highest Response-ratio Next)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 205. 스케줄링 - HRN (Highest Response-ratio Next)

Phần nguồn của **205. 스케줄링 - HRN (Highest Response-ratio Next)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “205. 스케줄링 - HRN (Highest Response-ratio Next)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 우선순위 = `(대기 시간 + 서비스 시간) / 서비스 시간`
- (Priority = (Wait time + Service time) / Service time).
  - *Example / Ví dụ*: Đợi 10, Chạy 5 => `(10+5)/5 = 3`.
  - 💡 *Mẹo ghi nhớ*: Công thức = `(Đợi + Chạy) / Chạy`. Số càng lớn càng ưu tiên. Giải quyết nhược điểm của SJF (tiến trình dài bị bỏ đói).

Với **205. 스케줄링 - HRN (Highest Response-ratio Next)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Như vậy, **205. 스케줄링 - HRN (Highest Response-ratio Next)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **082. 운영체제 기능 및 종류 (Operating System OS)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 082. 운영체제 기능 및 종류 (Operating System OS)

Ở bước 34/91, **082. 운영체제 기능 및 종류 (Operating System OS)** xuất hiện như phần tiếp nối của **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **082. 운영체제 기능 및 종류 (Operating System OS)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **운영체제의 주요 프로그램**, **제어 프로그램 (Control Program)**, **처리 프로그램 (Processing Program)**, **쉘(Shell)과 커널(Kernel)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “082. 운영체제 기능 및 종류 (Operating System OS)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **운영체제의 주요 프로그램**:
  - **제어 프로그램 (Control Program)**: 감시(Kernel), 작업 제어, 데이터 관리.
  - **처리 프로그램 (Processing Program)**: 언어 번역(컴파일러), 서비스, 문제 프로그램.
- **쉘(Shell)과 커널(Kernel)**:
  - **쉘 (Shell)**: 사용자의 명령어를 해석하여 커널로 전달 (사용자 인터페이스).
  - **커널 (Kernel)**: 핵심 모듈. 하드웨어/메모리/프로세스를 직접 제어 및 관리.
- **운영체제 종류**:
  - **Windows**: GUI, 선점형 멀티태스킹, PnP(자동 감지) 기능.
  - **Linux / Unix**: 오픈소스 (Linux), 트리 구조 파일 시스템. 시분할 시스템.
  - **Unix 파일 시스템 구조**: 부트 블록 -> 슈퍼 블록 (전체 정보) -> 아이노드(i-node) 블록 (파일 메타데이터) -> 데이터 블록 (실제 파일 내용).

**Giải thích (Vietnamese):**
OS giống như quản gia của máy tính.
- Kernel (Hạt nhân) là bộ não xử lý phần cứng. Shell (Vỏ) là cái dòng lệnh hoặc giao diện để con người nói chuyện với bộ não đó.
- Hệ thống tệp của UNIX chia làm 4 phần: Boot (chứa code khởi động) -> Super (Thông tin tổng quan) -> i-node (Lưu tên file, quyền truy cập...) -> Data (Nội dung file thực tế).

**💡 Mẹo ghi nhớ (Mnemonics):**
**제어 프로그램**: 감작데 (감시, 작업, 데이터). / **처리 프로그램**: 언서문 (언어, 서비스, 문제).

---

Như vậy, **082. 운영체제 기능 및 종류 (Operating System OS)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **282. 운영체제의 정의 및 목적 (Definition & Purpose of OS)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 282. 운영체제의 정의 및 목적 (Definition & Purpose of OS)

Sau khi đã đặt nền bằng **082. 운영체제 기능 및 종류 (Operating System OS)**, ta chuyển sang **282. 운영체제의 정의 및 목적 (Definition & Purpose of OS)**. Đây là mắt xích 35/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **282. 운영체제의 정의 및 목적 (Definition & Purpose of OS)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “282. 운영체제의 정의 및 목적 (Definition & Purpose of OS)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **운영체제(OS)**: 컴퓨터 자원(CPU, 메모리 등)을 효율적으로 관리하고 사용자에게 편리한 환경을 제공하는 소프트웨어 (Windows, Linux 등).
- 목적: 자원 관리, 편리한 인터페이스 제공, 가용성 극대화, 신뢰도 향상.

Ta có thể khép mục **282. 운영체제의 정의 및 목적 (Definition & Purpose of OS)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)

Từ **282. 운영체제의 정의 및 목적 (Definition & Purpose of OS)**, ta đã có điểm tựa để bước vào **283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 36/91 trước khi đi vào chi tiết.

Để đọc **283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **운영체제 구성**, **제어 프로그램**, **처리 프로그램**, **UNIX의 특징** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **운영체제 구성**:
  - **제어 프로그램**: 감시(Supervisor, 핵심), 작업 제어, 데이터 관리.
  - **처리 프로그램**: 언어 번역(컴파일러), 서비스(유틸리티).
- **UNIX의 특징**: 대화식 운영체제, **C언어로 작성**되어 이식성이 높음. 트리(Tree) 구조의 파일 시스템.
  - **커널(Kernel)**: UNIX의 핵심. 하드웨어/메모리/프로세스 관리.
  - **쉘(Shell)**: 사용자의 명령어를 해석하여 커널에 전달하는 인터페이스.
- **파일 디스크립터 (File Descriptor)**: 프로세스가 열린 파일을 참조할 때 사용하는 정수 핸들이다. 파일 속성을 담는 FCB/inode와 동일한 제어 블록이 아니다.
- **UNIX 환경 변수**: `$HOME`(홈 디렉터리), `$PATH`(명령어 검색 경로), `$PWD`(현재 작업 폴더).
- **UNIX 명령어**: `chmod`(권한 변경), `fork`(프로세스 복제).

**Giải thích (Vietnamese):**
- Kernel là não bộ, Shell là lớp vỏ giao tiếp với người dùng.
- Lệnh `fork` trong Unix dùng để nhân bản một Process đang chạy thành một Process con mới.

---

Điểm chốt của **283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)

Ở bước 37/91, **083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)** xuất hiện như phần tiếp nối của **283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **최초 적합 (First fit)**, **최적 적합 (Best fit)**, **최악 적합 (Worst fit)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **최초 적합 (First fit)**: 가장 처음 만나는 빈 공간에 할당 (빠름).
- **최적 적합 (Best fit)**: 자원 낭비(단편화)가 가장 적은 핏(딱 맞는) 공간에 할당.
- **최악 적합 (Worst fit)**: 단편화가 가장 큰(넓은) 공간에 할당 (남은 공간을 다시 쓰기 위해).

**Giải thích (Vietnamese):**
Khi một phần mềm cần RAM, OS sẽ nhét nó vào đâu?
- First fit: Thấy chỗ nào trống nhét vào luôn (Nhanh).
- Best fit: Tìm chỗ nào vừa khít nhất để nhét (Tiết kiệm chỗ).
- Worst fit: Cố tình nhét vào chỗ rộng nhất (Để chừa lại không gian rộng cho các app sau).

---

Như vậy, **083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **289 - 296. 메모리 관리 및 가상 기억장치 (Memory Management)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 289 - 296. 메모리 관리 및 가상 기억장치 (Memory Management)

Sau khi đã đặt nền bằng **083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)**, ta chuyển sang **289 - 296. 메모리 관리 및 가상 기억장치 (Memory Management)**. Đây là mắt xích 38/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **289 - 296. 메모리 관리 및 가상 기억장치 (Memory Management)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **배치 전략 (Placement)**, **페이징(Paging)**, **세그먼테이션(Segmentation)**, **페이지 크기** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “289 - 296. 메모리 관리 및 가상 기억장치 (Memory Management)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **배치 전략 (Placement)**: 최초 적합(First Fit, 빠름), 최적 적합(Best Fit, 단편화 최소), 최악 적합(Worst Fit, 큰 공간 남김).
- **페이징(Paging)**: 메모리를 **동일한 고정 크기**로 나눔. **내부 단편화** 발생 (빈 공간이 남아버림).
- **세그먼테이션(Segmentation)**: 논리적 의미(함수 등)에 따라 **가변 크기**로 나눔. **외부 단편화** 발생 (공간이 작아서 못 들어감).
- **페이지 크기**: 페이지가 작으면 내부 단편화는 줄지만, 맵 테이블이 커져 매핑 속도가 느려짐.
- **스래싱 (Thrashing)**: 빈번한 페이지 교체로 인해 시스템 처리량보다 교체 시간이 더 많아져 CPU 이용률이 급감하는 마비 상태.

**Giải thích (Vietnamese):**
- Paging (Phân trang): Cắt bánh thành các miếng bằng nhau. Điểm yếu: Ăn không hết 1 miếng sẽ dư thừa (Nội phân mảnh).
- Segmentation (Phân đoạn): Cắt bánh theo sức ăn của mỗi người (to nhỏ khác nhau). Điểm yếu: Chừa lại các khoảng trống lắt nhắt không ai nhét vừa (Ngoại phân mảnh).
- Thrashing: Máy quá tải, giật lag do mải lấy dữ liệu từ ổ cứng đắp vào RAM.

---

Ta có thể khép mục **289 - 296. 메모리 관리 및 가상 기억장치 (Memory Management)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **085. 프로세스 및 스레드 (Process & Thread)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 085. 프로세스 및 스레드 (Process & Thread)

Từ **289 - 296. 메모리 관리 및 가상 기억장치 (Memory Management)**, ta đã có điểm tựa để bước vào **085. 프로세스 및 스레드 (Process & Thread)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 39/91 trước khi đi vào chi tiết.

Để đọc **085. 프로세스 및 스레드 (Process & Thread)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **프로세스 상태 (Process States)**, **상태 전이 (State Transitions)**, **Dispatch**, **Timeout (Timer Runout)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “085. 프로세스 및 스레드 (Process & Thread)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **프로세스 상태 (Process States)**: 생성(Create) -> 준비(Ready) -> 실행(Running) -> 대기(Wait/Block) -> 종료(Exit).
- **상태 전이 (State Transitions)**:
  - **Dispatch**: 준비 -> 실행 (CPU 할당받음, 문맥교환 발생).
  - **Timeout (Timer Runout)**: 실행 -> 준비 (할당된 시간 초과).
  - **Block**: 실행 -> 대기 (I/O 작업 요청).
  - **Wake Up**: 대기 -> 준비 (I/O 작업 완료).
- **PCB (Process Control Block)**: OS가 프로세스를 관리하기 위해 유지하는 정보 블록 (상태, 식별자, 스택 정보 등).
- **문맥 교환 (Context Switch)**: CPU가 프로세스를 바꿀 때 현재 상태를 PCB에 저장하고 새 프로세스 상태를 불러오는 작업.
- **스레드 (Thread)**: 커널 수준(느리지만 안정적), 사용자 수준(빠르지만 불안정).

**Giải thích (Vietnamese):**
Process là một chương trình đang chạy.
Khi Process A đang chạy, hết thời gian (Timeout), OS sẽ cất trạng thái của A vào tờ giấy nhớ gọi là "PCB", sau đó gọi Process B lên chạy. Việc chuyển đổi này gọi là "Context Switch" (Chuyển đổi ngữ cảnh). Chuyển đổi càng nhiều máy càng chậm.

**💡 Mẹo ghi nhớ (Mnemonics):**
**디타블웨** (Dispatch, Timeout, Block, WakeUp): Chu trình chuyển trạng thái của Process.

---

Điểm chốt của **085. 프로세스 및 스레드 (Process & Thread)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **086. 프로세스 스케줄링 (Process Scheduling)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 086. 프로세스 스케줄링 (Process Scheduling)

Ở bước 40/91, **086. 프로세스 스케줄링 (Process Scheduling)** xuất hiện như phần tiếp nối của **085. 프로세스 및 스레드 (Process & Thread)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **086. 프로세스 스케줄링 (Process Scheduling)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **선점형 (Preemptive)**, **비선점형 (Non-Preemptive)**, **FCFS**, **SJF** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “086. 프로세스 스케줄링 (Process Scheduling)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **선점형 (Preemptive)**: 운영체제가 CPU를 강제로 뺏을 수 있음. 빠르고 대화식 시스템에 유리하지만 오버헤드 발생. (RR, SRT, MLQ, MLFQ).
- **비선점형 (Non-Preemptive)**: 한 프로세스가 끝나야만 다음 프로세스가 CPU를 씀. 일괄처리에 적합. (FCFS, SJF, HRN).
  - **FCFS**: 먼저 온 놈이 먼저 (First Come First Serve).
  - **SJF**: 짧은 작업 먼저 (Shortest Job First). 긴 작업은 무한 대기(기아 상태) 발생 가능.
  - **HRN**: SJF의 단점(기아 상태) 보완. 우선순위 = (대기시간 + 서비스시간) / 서비스시간. 결과값이 큰 것부터 우선 처리!

**Giải thích (Vietnamese):**
Lập lịch cho CPU:
- Độc quyền (Non-Preemptive): Đang chạy thì không ai được cướp (Giống như đang đi vệ sinh, người khác phải đợi). Ví dụ: FCFS, SJF, HRN.
- Cướp quyền (Preemptive): Đang chạy nhưng có việc khẩn cấp (hoặc hết giờ) thì hệ thống đuổi ra cho người khác vào. Ví dụ: RR, SRT.
- Công thức HRN rất hay thi: `(Thời gian đợi + Thời gian xử lý) / Thời gian xử lý`. Việc đợi càng lâu ưu tiên càng cao.

---

Như vậy, **086. 프로세스 스케줄링 (Process Scheduling)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속

Sau khi đã đặt nền bằng **086. 프로세스 스케줄링 (Process Scheduling)**, ta chuyển sang **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속**. Đây là mắt xích 41/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **교착상태(Deadlock) 4가지 필요충분조건**, **교착상태 해결 방법 (Handling Deadlocks)**, **예방 (Prevention)**, **회피 (Avoidance)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **교착상태(Deadlock) 4가지 필요충분조건**:
  1. **상호배제 (Mutual Exclusion)**: 한 번에 한 프로세스만 자원 사용.
  2. **점유와 대기 (Hold and Wait)**: 자원을 가진 채로 다른 자원을 기다림.
  3. **비선점 (Non-Preemption)**: 남의 자원을 강제로 뺏을 수 없음.
  4. **환형 대기 (Circular Wait)**: 꼬리에 꼬리를 물고 서로의 자원을 기다림.
- **교착상태 해결 방법 (Handling Deadlocks)**:
  - **예방 (Prevention)**: 4가지 조건 중 하나를 부정 (자원 낭비 심함).
  - **회피 (Avoidance)**: 발생 가능성을 피해 자원 할당 (예: **은행원 알고리즘**, 자원 할당 그래프).
  - **발견 (Detection)**: 발생을 허용하고 나중에 감시하여 발견.
  - **복구 (Recovery)**: 발견 후 프로세스를 종료하여 자원 회복 (기아 상태 주의).

**Giải thích (Vietnamese):**
Deadlock (Bế tắc) giống như kẹt xe ở ngã tư. Ai cũng tiến lên một chút (Chiếm giữ), không ai chịu lùi (Không thể cướp quyền), và chờ người kia nhường đường (Vòng tròn chờ đợi).
- Phòng ngừa (Prevention): Xây cầu vượt để không bao giờ kẹt xe (Tốn kém).
- Né tránh (Avoidance): Xem Google Maps, thấy đường đỏ (nguy cơ kẹt) thì không đi vào (Thuật toán Banker).
- Phục hồi (Recovery): Kẹt rồi thì gọi công an đến cẩu bớt 1 xe đi để thông đường.

**💡 Mẹo ghi nhớ (Mnemonics):**
Điều kiện: **상점비환** (Tương - Chiếm - Phi - Hoàn)
Giải quyết: **예회발복** (Dự - Tị - Phát - Phục).

---

Ta có thể khép mục **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)

Từ **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속**, ta đã có điểm tựa để bước vào **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 42/91 trước khi đi vào chi tiết.

Để đọc **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **프로세스(Process)**, **상태 전이**, **Dispatch**, **Timeout** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **프로세스(Process)**: **PCB(Process Control Block)를 가진** 실행 중인 프로그램.
- **상태 전이**:
  - **Dispatch**: 준비(Ready) -> 실행(Run) (CPU 할당 받음).
  - **Timeout**: 실행(Run) -> 준비(Ready) (시간 초과).
  - **Wake Up**: 대기(Wait) -> 준비(Ready) (입출력 완료).
- **스레드(Thread)**: 프로세스 내의 독립적인 실행 흐름 (최소 작업 단위). 프로세스의 자원을 공유하여 병행성 증대 및 문맥 교환 오버헤드 감소.
- **비선점 스케줄링 (Non-Preemptive)**:
  - FCFS: 먼저 온 순서대로.
  - SJF: 실행 시간이 가장 짧은 것 먼저.
  - **HRN**: 대기 시간과 서비스 시간을 고려해 기아(Starvation) 현상 해결. 공식: **(대기시간 + 서비스시간) / 서비스시간** (값이 클수록 우선).

---

Điểm chốt của **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **네트워크 통신 (Network Communication)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 네트워크 통신 (Network Communication)

Ở bước 43/91, **네트워크 통신 (Network Communication)** xuất hiện như phần tiếp nối của **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **네트워크 통신 (Network Communication)** như một bài học cho người mới, hãy giữ câu hỏi: **các thành phần trao đổi dữ liệu theo lớp, quy tắc và điều kiện nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **209. 데이터 링크 계층 (Data Link)**, **210. 네트워크 계층 (Network)**, **211. 전송 계층 (Transport)**, **212. 세션 계층 (Session)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **207. 인터넷 주소 체계 - IPv4 (IPv4 Addressing)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **207. 인터넷 주소 체계 - IPv4 (IPv4 Addressing)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 207. 인터넷 주소 체계 - IPv4 (IPv4 Addressing)

Bây giờ ta đi vào nội dung của **207. 인터넷 주소 체계 - IPv4 (IPv4 Addressing)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “207. 인터넷 주소 체계 - IPv4 (IPv4 Addressing)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 8비트씩 4부분, 총 32비트 (4 phần, mỗi phần 8 bit -> 32 bit). A~E 클래스.

Các bullet của **207. 인터넷 주소 체계 - IPv4 (IPv4 Addressing)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **207. 인터넷 주소 체계 - IPv4 (IPv4 Addressing)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **208. 인터넷 주소 체계 - IPv6 (IPv6 Addressing)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **208. 인터넷 주소 체계 - IPv6 (IPv6 Addressing)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 208. 인터넷 주소 체계 - IPv6 (IPv6 Addressing)

Phần nguồn của **208. 인터넷 주소 체계 - IPv6 (IPv6 Addressing)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “208. 인터넷 주소 체계 - IPv6 (IPv6 Addressing)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 16비트씩 8부분, 총 128비트 (8 phần, mỗi phần 16 bit -> 128 bit, dùng hệ Hex).
- 유니캐스트(Unicast), 멀티캐스트(Multicast), 애니캐스트(Anycast).
  - 💡 *Mẹo ghi nhớ*: IPv4 = 32 bit (dấu `.`). IPv6 = 128 bit (dấu `:`).

Với **208. 인터넷 주소 체계 - IPv6 (IPv6 Addressing)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **208. 인터넷 주소 체계 - IPv6 (IPv6 Addressing)**, đừng bắt đầu lại từ số không. **OSI 7계층 (OSI 7 Layers)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **OSI 7계층 (OSI 7 Layers)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### OSI 7계층 (OSI 7 Layers)

Các ý ngay dưới **OSI 7계층 (OSI 7 Layers)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “OSI 7계층 (OSI 7 Layers)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **209. 데이터 링크 계층 (Data Link)**: 인접 시스템 간 신뢰성 있는 전송. 흐름/오류 제어 (HDLC, PPP). (Truyền tải tin cậy giữa các nút lân cận).
- **210. 네트워크 계층 (Network)**: 경로 설정, 패킷 라우팅. (Định tuyến, chuyển mạch gói).
- **211. 전송 계층 (Transport)**: 종단 간 투명한 데이터 전송. (Truyền tải End-to-End, TCP/UDP).
- **212. 세션 계층 (Session)**: 대화 제어, 동기화 (Quản lý phiên, đồng bộ hóa hội thoại).
  - 💡 *Mẹo ghi nhớ*: Data Link = Frame/MAC. Network = IP/Routing. Transport = TCP/UDP/Port. Session = Dialog/Token.

Với **OSI 7계층 (OSI 7 Layers)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

**OSI 7계층 (OSI 7 Layers)** vừa cho ta cách đặt câu hỏi. Bây giờ **213. 네트워크 관련 주요 장비 (Network Devices / Thiết bị mạng)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **213. 네트워크 관련 주요 장비 (Network Devices / Thiết bị mạng)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 213. 네트워크 관련 주요 장비 (Network Devices / Thiết bị mạng)

Bây giờ ta đi vào nội dung của **213. 네트워크 관련 주요 장비 (Network Devices / Thiết bị mạng)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “213. 네트워크 관련 주요 장비 (Network Devices / Thiết bị mạng)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **리피터 (Repeater)**: 신호 재생 (Khuếch đại tín hiệu).
- **브리지 (Bridge)**: LAN 연결 (Kết nối mạng LAN cùng loại).
- **라우터 (Router)**: 최적 경로 선택 (Chọn đường đi tối ưu).
- **스위치 (Switch)**: 여러 랜선 연결 (Chuyển mạch mạng LAN).
- **브라우터 (Brouter)**: Bridge + Router.

Các bullet của **213. 네트워크 관련 주요 장비 (Network Devices / Thiết bị mạng)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **213. 네트워크 관련 주요 장비 (Network Devices / Thiết bị mạng)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **TCP/IP 프로토콜 (TCP/IP Protocols)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **TCP/IP 프로토콜 (TCP/IP Protocols)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### TCP/IP 프로토콜 (TCP/IP Protocols)

Phần nguồn của **TCP/IP 프로토콜 (TCP/IP Protocols)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “TCP/IP 프로토콜 (TCP/IP Protocols)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **214. MQTT**: IoT에서 사용하는 발행-구독 메시징 (Giao thức Publish/Subscribe cho IoT).
- **215. TCP**: 신뢰성 있는 양방향 연결형 서비스 (Kết nối hai chiều, đáng tin cậy).
- **216. UDP**: 비연결형, 빠른 속도, 실시간 전송 유리 (Không kết nối, truyền nhanh, hợp với Real-time).
  - 💡 *Mẹo ghi nhớ*: TCP = Cẩn thận, chậm mà chắc. UDP = Nhanh, mất gói cũng không sao (Video call, Game).

Với **TCP/IP 프로토콜 (TCP/IP Protocols)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **TCP/IP 프로토콜 (TCP/IP Protocols)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **네트워크 통신 (Network Communication)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **088. 인터넷 구성과 네트워크 - OSI 7계층 (OSI 7 Layer)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 088. 인터넷 구성과 네트워크 - OSI 7계층 (OSI 7 Layer)

Sau khi đã đặt nền bằng **네트워크 통신 (Network Communication)**, ta chuyển sang **088. 인터넷 구성과 네트워크 - OSI 7계층 (OSI 7 Layer)**. Đây là mắt xích 44/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **088. 인터넷 구성과 네트워크 - OSI 7계층 (OSI 7 Layer)** như một bài học cho người mới, hãy giữ câu hỏi: **các thành phần trao đổi dữ liệu theo lớp, quy tắc và điều kiện nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **IEEE 802 표준**, **OSI 7계층 (상위 계층부터)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “088. 인터넷 구성과 네트워크 - OSI 7계층 (OSI 7 Layer)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **IEEE 802 표준**: 802.3 (Ethernet, 유선랜), 802.11 (무선랜, Wi-Fi).
- **OSI 7계층 (상위 계층부터)**:
  7. **응용 계층 (Application)**: 사용자 인터페이스. (HTTP, FTP, DNS) - 데이터 단위: Data.
  6. **표현 계층 (Presentation)**: 암호화, 압축, 포맷 변환. - 데이터 단위: Data.
  5. **세션 계층 (Session)**: 응용 프로그램 간 논리적 연결 생성/유지. - 데이터 단위: Data.
  4. **전송 계층 (Transport)**: 종단 간(End-to-End) 신뢰성 있는 전송. 포트 번호 사용. (TCP, UDP). 장비: L4 스위치. - 데이터 단위: Segment.
  3. **네트워크 계층 (Network)**: 경로 설정(Routing). IP 주소 사용. (IP, ICMP, ARP). 장비: 라우터, L3 스위치. - 데이터 단위: Packet.
  2. **데이터 링크 계층 (Data Link)**: 인접 노드 간 전송 제어, 오류/흐름 제어. MAC 주소 사용. (HDLC, PPP). 장비: 브리지, L2 스위치. - 데이터 단위: Frame.
  1. **물리 계층 (Physical)**: 전기적 신호 전송. 장비: 허브, 리피터. - 데이터 단위: Bit.

**Giải thích (Vietnamese):**
Mô hình OSI 7 lớp chia nhỏ quá trình gửi dữ liệu qua mạng.
Tầng 1 (Cáp mạng, dây điện), Tầng 2 (Truyền giữa 2 máy tính kề nhau qua địa chỉ MAC), Tầng 3 (Tìm đường đi trên mạng Internet qua IP), Tầng 4 (Đảm bảo gói tin không bị rớt qua TCP/UDP), Tầng 5-7 (Phần mềm xử lý hiển thị lên màn hình).

**💡 Mẹo ghi nhớ (Mnemonics):**
Tên 7 tầng từ dưới lên (1->7): **물데네 전세표응** (Vật - Dữ - Mạng - Truyền - Phiên - Biểu - Ứng).
Đơn vị dữ liệu (1->4): **비프패세** (Bit, Frame, Packet, Segment).

---

Ta có thể khép mục **088. 인터넷 구성과 네트워크 - OSI 7계층 (OSI 7 Layer)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어

Từ **088. 인터넷 구성과 네트워크 - OSI 7계층 (OSI 7 Layer)**, ta đã có điểm tựa để bước vào **088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 45/91 trước khi đi vào chi tiết.

Để đọc **088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어** như một bài học cho người mới, hãy giữ câu hỏi: **các thành phần trao đổi dữ liệu theo lớp, quy tắc và điều kiện nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **TCP (Transmission Control Protocol)**, **UDP (User Datagram Protocol)**, **TCP 흐름 제어 (Flow Control)**, **TCP 오류 제어 (Error Control)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **TCP (Transmission Control Protocol)**: 연결 지향, 신뢰성 높음, 흐름 및 오류 제어 지원. 속도는 느림.
- **UDP (User Datagram Protocol)**: 비연결 지향, 신뢰성 낮음(오류 복구 안함). 실시간 전송(스트리밍)에 유리하여 속도가 빠름.
- **TCP 흐름 제어 (Flow Control)**: 수신측이 처리할 수 있는 만큼만 보냄 (Window 크기 사용).
  - Stop and Wait: 1개 보내고 응답 기다림.
  - Sliding Window: 윈도우 크기만큼 한 번에 여러 개 보냄 (효율적).
- **TCP 오류 제어 (Error Control)**:
  - Go Back n: 오류 발생한 패킷부터 **그 이후의 모든 패킷** 재전송.
  - Selective Repeat: 오류가 발생한 **해당 패킷만** 골라서 재전송.

**Giải thích (Vietnamese):**
- TCP giống như gửi thư bảo đảm, phải có người ký nhận mới yên tâm. Chậm nhưng chắc.
- UDP giống như phát loa phóng thanh, cứ phát ra, ai nghe được thì nghe. Phù hợp gọi Video call (Rớt 1 hình cũng không sao, quan trọng là độ trễ thấp).
- Trượt cửa sổ (Sliding Window): Kỹ thuật gửi liên tục nhiều gói tin mà không cần đợi từng gói báo nhận.
- Go Back N: Bị lỗi gói số 3, hệ thống sẽ gửi lại từ gói 3, 4, 5... Selective Repeat: Lỗi gói 3 thì chỉ gửi lại đúng gói 3.

---

Điểm chốt của **088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)

Ở bước 46/91, **309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)** xuất hiện như phần tiếp nối của **088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)** như một bài học cho người mới, hãy giữ câu hỏi: **các thành phần trao đổi dữ liệu theo lớp, quy tắc và điều kiện nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **응용 계층 (Application, 7계층)**, **전송 계층 (Transport, 4계층)**, **TCP**, **UDP** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **응용 계층 (Application, 7계층)**: HTTP(웹), FTP(파일), SMTP(메일), DNS(도메인->IP 변환), SNMP(네트워크 관리).
- **전송 계층 (Transport, 4계층)**:
  - **TCP**: 연결형, 신뢰성 보장, 양방향. 흐름 제어.
  - **UDP**: 비연결형, 신뢰성 낮음. 속도가 빨라 스트리밍에 유리.
- **인터넷/네트워크 계층 (Network, 3계층)**: 라우터 사용.
  - **IP**: 경로 설정.
  - **ICMP**: 오류 보고 및 제어.
  - **ARP**: IP 주소 -> MAC 주소 변환. (**RARP**는 반대).
- **데이터 링크/네트워크 액세스 계층 (Data Link, 2계층)**: Ethernet(CSMA/CD 방식), HDLC.

**Giải thích (Vietnamese):**
- **ARP**: Khi biết địa chỉ IP, dùng ARP để hỏi xem "Máy nào có IP này, cho xin địa chỉ MAC của card mạng (phần cứng)".
- **ICMP**: Lệnh `ping` hay dùng trên máy tính chính là chạy giao thức ICMP để kiểm tra mạng có thông không.

---

Như vậy, **309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)

Sau khi đã đặt nền bằng **309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)**, ta chuyển sang **189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)**. Đây là mắt xích 47/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **모듈화 (Modularity)**, **추상화 (Abstraction)**, **정보 은닉 (Information Hiding)**, **프로그램 구조 (Program Structure)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **모듈화 (Modularity)**: 시스템을 모듈 단위로 나눔.
- **추상화 (Abstraction)**: 포괄적 개념 먼저 설계 후 세분화 (기능, 제어, 자료 추상화).
- **정보 은닉 (Information Hiding)**: 모듈 내부의 세부 정보를 감추어 다른 모듈이 변경하지 못하게 함 (유지보수 용이).
- **프로그램 구조 (Program Structure)**: 제어 계층 구조 (트리 형태).
  - 공유도(Fan-In): 나를 호출하는 상위 모듈 수.
  - 제어도(Fan-Out): 내가 호출하는 하위 모듈 수.

**Giải thích (Vietnamese):**
Khi thiết kế phần mềm, ta chia nhỏ thành các hàm/chức năng (Modularity). Dùng "Che giấu thông tin" (Information Hiding) như tính đóng gói (Encapsulation) trong OOP để các hàm không can thiệp sai vào dữ liệu của nhau.
- Fan-In (Đi vào): Có bao nhiêu hàm gọi đến mình. Fan-In cao là tốt vì tính tái sử dụng cao.
- Fan-Out (Đi ra): Mình gọi bao nhiêu hàm khác. Fan-Out cao nghĩa là hàm này quá phức tạp.

**💡 Mẹo ghi nhớ (Mnemonics):**
**모추정** (Mô - Trừu - Thông): **모**듈화(Modularity), **추**상화(Abstraction), **정**보 은닉(Information Hiding).

---

Ta có thể khép mục **189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)

Từ **189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)**, ta đã có điểm tựa để bước vào **202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 48/91 trước khi đi vào chi tiết.

Để đọc **202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **개념**, **구성 요소**, **데이터 (Data/Attribute)**, **연산/메소드 (Method/Operation)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 현실 세계의 개체(Entity)를 기계 부품(Object)처럼 만들어 조립식으로 소프트웨어 개발. 재사용/확장 용이.
- **구성 요소**:
  - **데이터 (Data/Attribute)**: 객체가 가진 정보 (속성, 상태).
  - **연산/메소드 (Method/Operation)**: 데이터를 처리하는 알고리즘/함수.
  - **클래스 (Class)**: 공통 속성/연산을 갖는 객체들의 집합 (틀, Type). 객체를 '인스턴스(Instance)'라고 함.
  - **메시지 (Message)**: 객체 간 상호작용 수단 (명령).
- **주요 기본 원칙**:
  1. **캡슐화 (Encapsulation)**: 데이터와 함수를 하나로 묶음. 재사용 용이, 결합도 낮아짐.
  2. **정보 은닉 (Information Hiding)**: 내부 정보를 숨기고 연산만을 통해 접근 허용 (Side Effect 최소화).
  3. **상속성 (Inheritance)**: 상위 클래스의 속성/연산을 하위 클래스가 물려받음. (다중 상속도 있음).
  4. **추상화 (Abstraction)**: 불필요한 부분 생략, 중요한 부분만 모델화.
  5. **다형성 (Polymorphism)**: 동일한 메시지(메소드명)에 대해 객체마다 다른 응답(기능)을 함.

**Giải thích (Vietnamese):**
OOP (Lập trình hướng đối tượng) giống như trò chơi xếp hình Lego.
- Class: Bản vẽ thiết kế chiếc xe.
- Object (Instance): Chiếc xe thật được lắp ráp.
- Tính đóng gói (Encapsulation): Gói gọn các bộ phận động cơ vào trong vỏ xe.
- Tính đa hình (Polymorphism): Cùng là lệnh "Kêu", con chó kêu "Gâu", con mèo kêu "Meo".

**💡 Mẹo ghi nhớ (Mnemonics):**
**캡정상추다** (Đóng - Ẩn - Kế - Trừu - Đa): 캡슐화, 정보 은닉, 상속성, 추상화, 다형성.

---

Điểm chốt của **202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **089. IP와 서브네팅, IPv4 vs IPv6 (IP & Subnetting)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 089. IP와 서브네팅, IPv4 vs IPv6 (IP & Subnetting)

Ở bước 49/91, **089. IP와 서브네팅, IPv4 vs IPv6 (IP & Subnetting)** xuất hiện như phần tiếp nối của **202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **089. IP와 서브네팅, IPv4 vs IPv6 (IP & Subnetting)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **IPv4 헤더 필드**, **IPv4 클래스**, **IPv4 vs IPv6**, **데이터 전송 방법** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “089. IP와 서브네팅, IPv4 vs IPv6 (IP & Subnetting)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **IPv4 헤더 필드**: Version, Header Length, TOS, Total Length, TTL (수명), Source/Destination Address 등.
- **IPv4 클래스**:
  - Class A: `0.~` (거대 망)
  - Class B: `128.~` (중형 망)
  - Class C: `192.~` (소형 망)
- **IPv4 vs IPv6**:
  - 주소 길이: IPv4(32비트) -> **IPv6(128비트)** 확장.
  - IPv6 특징: 호스트 주소 자동 설정 지원, 기본 헤더 단순화, 플로 레이블링(QoS) 필드, 이동성 지원. 패킷 크기는 IPv6의 최대 패킷 크기와 경로 MTU 규칙을 따르며, IPsec 지원이 정의되어도 사용 여부는 별도 설정이다.
- **데이터 전송 방법**:
  - **유니캐스트 (Unicast)**: 1:1 통신.
  - **멀티캐스트 (Multicast)**: 1:N (특정 그룹).
  - **브로드캐스트 (Broadcast)**: 1:전체 (IPv4에서만 사용, 과부하 원인).
  - **애니캐스트 (Anycast)**: 1:가장 가까운 1개 노드 (IPv6에서 도입).

**Giải thích (Vietnamese):**
IPv4 sắp hết số (vì chỉ có 32 bit = khoảng 4 tỷ địa chỉ). Nên người ta sinh ra IPv6 (128 bit = số lượng vô hạn). IPv6 bảo mật tốt hơn, không cần cấu hình DHCP phức tạp (tự gán địa chỉ) và loại bỏ Broadcast để tránh nghẽn mạng.

**💡 Mẹo ghi nhớ (Mnemonics):**
Các kiểu truyền:
- Unicast = Nói chuyện riêng.
- Multicast = Nhắn tin vào group chat Zalo.
- Broadcast = Cầm loa hét cho cả trường nghe (Chỉ IPv4).
- Anycast = Gọi tổng đài, ai rảnh thì nhấc máy nghe trước (Chỉ IPv6).

---

Như vậy, **089. IP와 서브네팅, IPv4 vs IPv6 (IP & Subnetting)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **252. 다중 if문 (Multiple if Statement)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 252. 다중 if문 (Multiple if Statement)

Sau khi đã đặt nền bằng **089. IP와 서브네팅, IPv4 vs IPv6 (IP & Subnetting)**, ta chuyển sang **252. 다중 if문 (Multiple if Statement)**. Đây là mắt xích 50/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **252. 다중 if문 (Multiple if Statement)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “252. 다중 if문 (Multiple if Statement)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 처리할 조건이 여러 개일 때 `else if`를 사용해 순차적으로 판단.
- 위에서 조건이 참이면 해당 블록을 실행하고 빠져나옴 (아래 조건은 검사하지 않음).
- 모든 조건이 거짓일 때 마지막 `else`가 실행됨.

---

Ta có thể khép mục **252. 다중 if문 (Multiple if Statement)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **305 - 308. IP 주소 체계 (IPv4 vs IPv6)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 305 - 308. IP 주소 체계 (IPv4 vs IPv6)

Từ **252. 다중 if문 (Multiple if Statement)**, ta đã có điểm tựa để bước vào **305 - 308. IP 주소 체계 (IPv4 vs IPv6)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 51/91 trước khi đi vào chi tiết.

Để đọc **305 - 308. IP 주소 체계 (IPv4 vs IPv6)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **IPv4**, **IPv6**, **IPv6의 특징**, **IPv6 전송 방식** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “305 - 308. IP 주소 체계 (IPv4 vs IPv6)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **IPv4**: 32비트 (8비트씩 4부분). 클래스 A~E로 나뉨.
- **IPv6**: 128비트 (16비트씩 8부분). 콜론(`:`)으로 구분, 16진수 사용.
- **IPv6의 특징**: 무한대에 가까운 주소, 보안 강화, 패킷 크기 확장, PnP(자동 설정).
- **IPv6 전송 방식**: 유니캐스트(1:1), 멀티캐스트(1:N), 애니캐스트(가장 가까운 1:1).

**💡 Mẹo ghi nhớ (Mnemonics):**
IPv6 전송 방식 3총사: **유멀애** (Unicast, Multicast, Anycast). *Broadcast는 IPv4에만 있음!*

---

Điểm chốt của **305 - 308. IP 주소 체계 (IPv4 vs IPv6)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **소프트웨어 공학 및 실무 (Software Engineering & Practice)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 소프트웨어 공학 및 실무 (Software Engineering & Practice)

Ở bước 52/91, **소프트웨어 공학 및 실무 (Software Engineering & Practice)** xuất hiện như phần tiếp nối của **305 - 308. IP 주소 체계 (IPv4 vs IPv6)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **소프트웨어 공학 및 실무 (Software Engineering & Practice)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **Open**, **Assigned**, **Fixed**, **Closed** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **231. 오류 데이터 상태 (Error Data States / Trạng thái dữ liệu lỗi)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **231. 오류 데이터 상태 (Error Data States / Trạng thái dữ liệu lỗi)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 231. 오류 데이터 상태 (Error Data States / Trạng thái dữ liệu lỗi)

Bây giờ ta đi vào nội dung của **231. 오류 데이터 상태 (Error Data States / Trạng thái dữ liệu lỗi)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “231. 오류 데이터 상태 (Error Data States / Trạng thái dữ liệu lỗi)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **Open**: 보고만 됨 (Mới báo cáo).
- **Assigned**: 개발자에게 전달 (Đã giao cho dev).
- **Fixed**: 수정됨 (Đã sửa).
- **Closed**: 테스트 후 문제 없음 (Đóng lại sau khi test OK).
- **Deferred**: 수정 연기 (Hoãn lại).
- **Classified**: 오류 아님 (Xác nhận không phải lỗi).

Các bullet của **231. 오류 데이터 상태 (Error Data States / Trạng thái dữ liệu lỗi)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **231. 오류 데이터 상태 (Error Data States / Trạng thái dữ liệu lỗi)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **232. 배치 프로그램 필수 요소 (Batch Program Elements / Yếu tố của Batch)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **232. 배치 프로그램 필수 요소 (Batch Program Elements / Yếu tố của Batch)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 232. 배치 프로그램 필수 요소 (Batch Program Elements / Yếu tố của Batch)

Phần nguồn của **232. 배치 프로그램 필수 요소 (Batch Program Elements / Yếu tố của Batch)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “232. 배치 프로그램 필수 요소 (Batch Program Elements / Yếu tố của Batch)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 대용량 데이터, 자동화, 견고성, 안정성/신뢰성, 성능. (Khối lượng lớn, Tự động hóa, Độ bền bỉ, Tính Ổn định, Hiệu suất).
  - 💡 *Mẹo ghi nhớ*: Batch là tự động chạy ngầm khối lượng lớn, nên không được chết giữa chừng.

Các bullet của **232. 배치 프로그램 필수 요소 (Batch Program Elements / Yếu tố của Batch)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **232. 배치 프로그램 필수 요소 (Batch Program Elements / Yếu tố của Batch)**, đừng bắt đầu lại từ số không. **233. C/C++ 데이터 타입 크기 추가 (C/C++ Data Type Sizes / Kích thước kiểu dữ liệu C++)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **233. C/C++ 데이터 타입 크기 추가 (C/C++ Data Type Sizes / Kích thước kiểu dữ liệu C++)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 233. C/C++ 데이터 타입 크기 추가 (C/C++ Data Type Sizes / Kích thước kiểu dữ liệu C++)

Các ý ngay dưới **233. C/C++ 데이터 타입 크기 추가 (C/C++ Data Type Sizes / Kích thước kiểu dữ liệu C++)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “233. C/C++ 데이터 타입 크기 추가 (C/C++ Data Type Sizes / Kích thước kiểu dữ liệu C++)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- C++에서는 `long long` (8Byte)와 `double` (8Byte), `long double` (8Byte) 등 확장된 크기를 가짐. (Lưu ý các kiểu dữ liệu mở rộng trong C/C++).

Các bullet của **233. C/C++ 데이터 타입 크기 추가 (C/C++ Data Type Sizes / Kích thước kiểu dữ liệu C++)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **233. C/C++ 데이터 타입 크기 추가 (C/C++ Data Type Sizes / Kích thước kiểu dữ liệu C++)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **소프트웨어 공학 및 실무 (Software Engineering & Practice)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **프로그래밍 언어 종류 및 특징 (Programming Languages Types & Features)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 프로그래밍 언어 종류 및 특징 (Programming Languages Types & Features)

Sau khi đã đặt nền bằng **소프트웨어 공학 및 실무 (Software Engineering & Practice)**, ta chuyển sang **프로그래밍 언어 종류 및 특징 (Programming Languages Types & Features)**. Đây là mắt xích 53/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **프로그래밍 언어 종류 및 특징 (Programming Languages Types & Features)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **C**, **ALGOL**, **COBOL** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **275. 절차적 프로그래밍 언어의 종류 (Procedural Programming Languages / Ngôn ngữ lập trình hướng thủ tục)**. Hãy xác định **275. 절차적 프로그래밍 언어의 종류 (Procedural Programming Languages / Ngôn ngữ lập trình hướng thủ tục)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 275. 절차적 프로그래밍 언어의 종류 (Procedural Programming Languages / Ngôn ngữ lập trình hướng thủ tục)

Phần nguồn của **275. 절차적 프로그래밍 언어의 종류 (Procedural Programming Languages / Ngôn ngữ lập trình hướng thủ tục)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “275. 절차적 프로그래밍 언어의 종류 (Procedural Programming Languages / Ngôn ngữ lập trình hướng thủ tục)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **C**: 1972년 데니스 리치 개발, UNIX 일부 구현, 포인터 제공. 고급+저급 특징 모두 가짐. (Phát triển bởi Dennis Ritchie năm 1972, có con trỏ, kết hợp đặc điểm của ngôn ngữ bậc cao và bậc thấp).
- **ALGOL**: 과학 기술 계산용. PASCAL과 C의 모체. (Ngôn ngữ tính toán khoa học, là tiền thân của Pascal và C).
- **COBOL**: 사무 처리용. 영어 문장 형식, 4개의 DIVISION. (Ngôn ngữ xử lý nghiệp vụ, cú pháp giống tiếng Anh, chia làm 4 phần - DIVISION).

---

Các bullet của **275. 절차적 프로그래밍 언어의 종류 (Procedural Programming Languages / Ngôn ngữ lập trình hướng thủ tục)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **275. 절차적 프로그래밍 언어의 종류 (Procedural Programming Languages / Ngôn ngữ lập trình hướng thủ tục)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Ta có thể khép mục **프로그래밍 언어 종류 및 특징 (Programming Languages Types & Features)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **190. 바람직한 설계의 특징 (Good Design Characteristics / Đặc điểm của thiết kế tốt)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 190. 바람직한 설계의 특징 (Good Design Characteristics / Đặc điểm của thiết kế tốt)

Từ **프로그래밍 언어 종류 및 특징 (Programming Languages Types & Features)**, ta đã có điểm tựa để bước vào **190. 바람직한 설계의 특징 (Good Design Characteristics / Đặc điểm của thiết kế tốt)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 54/91 trước khi đi vào chi tiết.

Để đọc **190. 바람직한 설계의 특징 (Good Design Characteristics / Đặc điểm của thiết kế tốt)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “190. 바람직한 설계의 특징 (Good Design Characteristics / Đặc điểm của thiết kế tốt)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 적당한 모듈 크기를 유지.
- **결합도(Coupling)는 약하게, 응집도(Cohesion)는 강하게 설계한다**.

**Giải thích (Vietnamese):**
Một thiết kế phần mềm chuẩn mực phải đảm bảo: "Mối liên kết giữa các module càng lỏng lẻo càng tốt (Low Coupling), nhưng sự gắn kết nhiệm vụ bên trong một module phải càng chặt chẽ càng tốt (High Cohesion)".

---

Điểm chốt của **190. 바람직한 설계의 특징 (Good Design Characteristics / Đặc điểm của thiết kế tốt)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **191. 결합도 (Coupling / Mức độ phụ thuộc)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 191. 결합도 (Coupling / Mức độ phụ thuộc)

Ở bước 55/91, **191. 결합도 (Coupling / Mức độ phụ thuộc)** xuất hiện như phần tiếp nối của **190. 바람직한 설계의 특징 (Good Design Characteristics / Đặc điểm của thiết kế tốt)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **191. 결합도 (Coupling / Mức độ phụ thuộc)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “191. 결합도 (Coupling / Mức độ phụ thuộc)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 모듈 간에 상호 의존하는 정도. 약할수록 독립성이 높고 품질이 좋음.
- **결합도가 약한 것부터 강한 순서 (Tốt -> Xấu)**:
  1. **자료 (Data)**: 파라미터로 단순 데이터(값)만 전달 (가장 좋음).
  2. **스탬프 (Stamp)**: 배열이나 레코드 등 자료 구조를 전달.
  3. **제어 (Control)**: 제어 신호(Flag)를 전달하여 상대 모듈의 흐름을 제어.
  4. **외부 (External)**: 외부에서 선언된 데이터를 참조.
  5. **공통 (Common)**: 전역 변수(공통 데이터 영역)를 여러 모듈이 사용.
  6. **내용 (Content)**: 다른 모듈의 내부 기능이나 변수를 직접 참조/수정 (가장 나쁨).

**Giải thích (Vietnamese):**
Coupling đánh giá mức độ "dính líu" giữa 2 module. Càng dính líu nhiều, khi sửa module này sẽ làm hỏng module kia.
Tốt nhất là Data (chỉ truyền tham trị như `int a`). Tệ nhất là Content (module A nhảy thẳng vào code của module B để sửa biến).

**💡 Mẹo ghi nhớ (Mnemonics):**
**자스제 외공내** (Tự - Tem - Chế - Ngoại - Công - Nội): 자료 (Data) -> 스탬프 (Stamp) -> 제어 (Control) -> 외부 (External) -> 공통 (Common) -> 내용 (Content). Từ Tốt đến Xấu.

---

Như vậy, **191. 결합도 (Coupling / Mức độ phụ thuộc)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **192. 응집도 (Cohesion / Mức độ gắn kết)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 192. 응집도 (Cohesion / Mức độ gắn kết)

Sau khi đã đặt nền bằng **191. 결합도 (Coupling / Mức độ phụ thuộc)**, ta chuyển sang **192. 응집도 (Cohesion / Mức độ gắn kết)**. Đây là mắt xích 56/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **192. 응집도 (Cohesion / Mức độ gắn kết)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “192. 응집도 (Cohesion / Mức độ gắn kết)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 모듈 안의 요소들이 서로 관련되어 있는 정도. 강할수록 독립성이 높고 품질이 좋음.
- **응집도가 약한 것부터 강한 순서 (Xấu -> Tốt)**:
  1. **우연적 (Coincidental)**: 아무 관련 없는 요소들이 우연히 모임 (가장 나쁨).
  2. **논리적 (Logical)**: 논리적으로 유사한 성격의 작업들을 모음.
  3. **시간적 (Temporal)**: 특정 시간에 같이 처리되는 기능들을 모음 (예: 초기화).
  4. **절차적 (Procedural)**: 기능들이 순차적으로 수행됨.
  5. **교환/통신적 (Communication)**: 동일한 입력/출력 데이터를 사용.
  6. **순차적 (Sequential)**: 앞 활동의 출력 데이터를 다음 활동의 입력 데이터로 사용.
  7. **기능적 (Functional)**: 내부 모든 요소가 단일 목적(기능)만을 위해 존재 (가장 좋음).

**Giải thích (Vietnamese):**
Cohesion đo lường sự tập trung của một module. Nếu một hàm vừa làm toán cộng, vừa in hóa đơn, vừa gửi email -> Quá nhiều việc không liên quan (Xấu). Hàm chỉ làm đúng một việc là "Tính tổng" -> Tuyệt vời (Functional).

**💡 Mẹo ghi nhớ (Mnemonics):**
**우논시절 교순기** (U - Luận - Thời - Tiết - Giao - Tuần - Kỹ): 우연 (Coincidental) -> 논리 (Logical) -> 시간 (Temporal) -> 절차 (Procedural) -> 교환 (Communication) -> 순차 (Sequential) -> 기능 (Functional). Từ Xấu đến Tốt.

---

Ta có thể khép mục **192. 응집도 (Cohesion / Mức độ gắn kết)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **193 - 194. 효과적인 모듈화 설계 방안 & N-S 차트 (Effective Modular Design & Nassi-Schneiderman Chart)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 193 - 194. 효과적인 모듈화 설계 방안 & N-S 차트 (Effective Modular Design & Nassi-Schneiderman Chart)

Từ **192. 응집도 (Cohesion / Mức độ gắn kết)**, ta đã có điểm tựa để bước vào **193 - 194. 효과적인 모듈화 설계 방안 & N-S 차트 (Effective Modular Design & Nassi-Schneiderman Chart)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 57/91 trước khi đi vào chi tiết.

Để đọc **193 - 194. 효과적인 모듈화 설계 방안 & N-S 차트 (Effective Modular Design & Nassi-Schneiderman Chart)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **모듈화 방안**, **N-S 차트** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “193 - 194. 효과적인 모듈화 설계 방안 & N-S 차트 (Effective Modular Design & Nassi-Schneiderman Chart)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **모듈화 방안**: 결합도를 줄이고 응집도를 높임 (Low Coupling, High Cohesion). 모듈 크기는 이해하기 쉽게 분해. 하나의 입구와 하나의 출구를 가짐.
- **N-S 차트**: 논리 기술에 중점을 둔 도형 (박스 다이어그램).
  - 순차, 선택, 반복 구조를 시각적으로 표현.
  - **GOTO나 화살표를 사용하지 않음**.
  - 읽기는 쉽지만 작성하기 어려움.

**Giải thích (Vietnamese):**
Biểu đồ N-S (Nassi-Schneiderman) là loại biểu đồ khối chữ nhật, không dùng mũi tên, không dùng GOTO. Cấu trúc lồng nhau rất dễ đọc logic nhưng vẽ ra thì khó.

---

Điểm chốt của **193 - 194. 효과적인 모듈화 설계 방안 & N-S 차트 (Effective Modular Design & Nassi-Schneiderman Chart)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **195 - 197. 구현 및 구조적 프로그래밍, 제어 흐름도 (Implementation & Structured Programming)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 195 - 197. 구현 및 구조적 프로그래밍, 제어 흐름도 (Implementation & Structured Programming)

Ở bước 58/91, **195 - 197. 구현 및 구조적 프로그래밍, 제어 흐름도 (Implementation & Structured Programming)** xuất hiện như phần tiếp nối của **193 - 194. 효과적인 모듈화 설계 방안 & N-S 차트 (Effective Modular Design & Nassi-Schneiderman Chart)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **195 - 197. 구현 및 구조적 프로그래밍, 제어 흐름도 (Implementation & Structured Programming)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **구현(코딩)**, **구조적 프로그래밍**, **순환 복잡도 (Cyclomatic Complexity)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “195 - 197. 구현 및 구조적 프로그래밍, 제어 흐름도 (Implementation & Structured Programming)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **구현(코딩)**: 설계 명세서를 컴퓨터가 알 수 있는 코드로 변환.
- **구조적 프로그래밍**: 순차(Sequence), 선택(Selection), 반복(Iteration)의 3가지 제어 구조만 사용하여 코딩 (Dijkstra 제안). 신뢰성 향상.
- **순환 복잡도 (Cyclomatic Complexity)**: 프로그램의 논리적 복잡도 척도.
  - V(G) = E - N + 2 (E: 화살표 수, N: 노드 수). 또는 닫힌 영역의 수 + 1.

**Giải thích (Vietnamese):**
Lập trình có cấu trúc chỉ dùng 3 luồng: Chạy tuần tự từ trên xuống (Sequence), Lệnh rẽ nhánh If/Else (Selection), và Vòng lặp For/While (Iteration). Độ phức tạp McCabe tính xem hàm có bao nhiêu đường đi (nhánh) độc lập.

**Ví dụ (Example):**
Nếu biểu đồ luồng có 5 Node (N=5) và 6 Cạnh/Mũi tên (E=6).
Độ phức tạp Cyclomatic V(G) = 6 - 5 + 2 = 3. Số 3 nghĩa là hàm này cần ít nhất 3 test case để phủ toàn bộ các đường đi.

---

Như vậy, **195 - 197. 구현 및 구조적 프로그래밍, 제어 흐름도 (Implementation & Structured Programming)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)

Sau khi đã đặt nền bằng **195 - 197. 구현 및 구조적 프로그래밍, 제어 흐름도 (Implementation & Structured Programming)**, ta chuyển sang **196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)**. Đây là mắt xích 59/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 모듈의 **원시 코드(Source Code)를 오픈시킨 상태**에서 논리적인 모든 경로를 검사.
- 내부 구조, 제어 흐름, 논리 흐름(루프)을 직접 관찰하며 테스트.
- 조건의 참/거짓 경로를 적어도 한 번 이상 실행.
- 테스트 과정 **초기**에 적용됨.
- 종류: 기초 경로 검사 (Basic Path Testing), 조건 검사, 루프 검사, 데이터 흐름 검사.

**Giải thích (Vietnamese):**
Kiểm thử hộp trắng là bạn (thường là Dev) nhìn thấy toàn bộ source code và viết test case để đảm bảo mọi dòng code (if, else, vòng lặp) đều được chạy qua ít nhất 1 lần.

**💡 Mẹo ghi nhớ (Mnemonics):**
Hộp trắng trong suốt -> Nhìn thấu được code bên trong. Trọng tâm là "Logic đường đi" (경로).

---

Ta có thể khép mục **196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)

Từ **196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)**, ta đã có điểm tựa để bước vào **198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 60/91 trước khi đi vào chi tiết.

Để đọc **198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **동치 분할 검사 (Equivalence Partitioning)**, **경계값 분석 (Boundary Value Analysis)**, **원인-효과 그래프 (Cause-Effect Graphing)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **기능 검사**라고도 함. 내부 코드를 보지 않고, 소프트웨어의 인터페이스(입·출력)에서 기능이 완전히 작동하는지 입증.
- 테스트 과정 **후반부**에 적용됨.
- 종류:
  - **동치 분할 검사 (Equivalence Partitioning)**: 타당한 입력과 타당하지 않은 입력 자료의 갯수를 균등하게 나눠 테스트. (Ví dụ: Yêu cầu nhập từ 1-100. Test case: 50 (hợp lệ), 150 (không hợp lệ)).
  - **경계값 분석 (Boundary Value Analysis)**: 경계값에서 오류가 발생할 확률이 높음을 이용. (Ví dụ: Test case: 0, 1, 100, 101).
  - **원인-효과 그래프 (Cause-Effect Graphing)**: 입력(원인)과 출력(효과)의 관계 분석.

Điểm chốt của **198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)

Ở bước 61/91, **199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)** xuất hiện như phần tiếp nối của **198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **단위 검사 (Unit Testing)**, **하향식 통합 검사 (Top-Down Integration)**, **상향식 통합 검사 (Bottom-Up Integration)**, **검증(확인) 검사 (Validation Testing)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **단위 검사 (Unit Testing)**: 코딩 후 최소 단위인 '모듈' 초점 검사 (화이트 박스 기법).
- **하향식 통합 검사 (Top-Down Integration)**: 상위 모듈 -> 하위 모듈 방향. 임시 시험용 모듈인 **스터브(Stub)** 필요.
- **상향식 통합 검사 (Bottom-Up Integration)**: 하위 모듈 -> 상위 모듈 방향. 제어 모듈과 종속 모듈 그룹인 **클러스터(Cluster)**와 드라이버(Driver) 필요. (Stub 불필요).
- **검증(확인) 검사 (Validation Testing)**: 요구사항 충족 여부 확인 (블랙 박스 기법).
  - **알파 검사 (Alpha Test)**: **개발자 환경(장소)**에서 사용자가 테스트 (통제된 환경).
  - **베타 검사 (Beta Test)**: **실제 사용자 환경**에서 여러 사용자가 테스트 (개발자 통제 없음).
- **시스템 검사 (System Test)**: 전체 시스템(하드웨어 포함)에서 완벽히 수행되는지 검사. (복구/보안/강도/성능 검사).

**Giải thích (Vietnamese):**
- Kiểm thử tích hợp từ trên xuống (Top-down) cần làm các module giả (Stub) để thay thế cho module con chưa code xong. Từ dưới lên (Bottom-up) cần nhóm (Cluster/Driver) để gọi module con.
- Alpha Test: Bạn mời khách hàng đến công ty bạn ngồi test app trước mặt bạn.
- Beta Test: Bạn tung app lên store cho người dùng tải về dùng thử và báo lỗi (bạn không ngồi cạnh họ).

**💡 Mẹo ghi nhớ (Mnemonics):**
**하스 상드** (Hạ - Stub, Thượng - Driver): **하**향식 = **스**터브(Stub). **상**향식 = 드라이버(Driver)/클러스터(Cluster).

---

Như vậy, **199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **200. 유지보수 (Maintenance / Bảo trì phần mềm)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 200. 유지보수 (Maintenance / Bảo trì phần mềm)

Sau khi đã đặt nền bằng **199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)**, ta chuyển sang **200. 유지보수 (Maintenance / Bảo trì phần mềm)**. Đây là mắt xích 62/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **200. 유지보수 (Maintenance / Bảo trì phần mềm)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “200. 유지보수 (Maintenance / Bảo trì phần mềm)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 개발 중 가장 많은 노력과 비용이 투입됨.
- **유형 (Phân loại)**:
  1. **수정(Corrective) 보수 (하자 보수)**: 검사 단계에서 못 찾은 '오류(버그) 수정'.
  2. **적응(Adaptive) 보수 (환경 적응)**: OS 변경, 하드웨어 변경 등 '환경 변화에 적응'하기 위한 수정.
  3. **완전화(Perfective) 보수 (기능 개선)**: 새로운 기능 추가, 성능 개선 (유지보수 중 가장 큰 비용 차지).
  4. **예방(Preventive) 보수**: 장래의 오류 발생에 대비하여 미리 예방.

**Giải thích (Vietnamese):**
- Corrective (Sửa lỗi): App bị crash, bạn phải vá lỗi.
- Adaptive (Thích ứng): Apple ra iOS mới, bạn update app để không bị lỗi màn hình tai thỏ.
- Perfective (Hoàn thiện): Thêm tính năng "Chat" vào app, cải tiến tốc độ tải (Chiếm nhiều ngân sách nhất).
- Preventive (Phòng ngừa): Refactor code để sau này dễ nâng cấp.

**💡 Mẹo ghi nhớ (Mnemonics):**
**수적완예** (Tu - Thích - Hoàn - Dự): **수**정, **적**응, **완**전, **예**방.

---

Ta có thể khép mục **200. 유지보수 (Maintenance / Bảo trì phần mềm)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **201. 외계인 코드 (Alien Code / Mã ngoài hành tinh)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 201. 외계인 코드 (Alien Code / Mã ngoài hành tinh)

Từ **200. 유지보수 (Maintenance / Bảo trì phần mềm)**, ta đã có điểm tựa để bước vào **201. 외계인 코드 (Alien Code / Mã ngoài hành tinh)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 63/91 trước khi đi vào chi tiết.

Để đọc **201. 외계인 코드 (Alien Code / Mã ngoài hành tinh)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “201. 외계인 코드 (Alien Code / Mã ngoài hành tinh)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 아주 오래 전에 개발되어(보통 15년 전) 문서화가 제대로 되어 있지 않아 유지보수가 매우 어려운 프로그램.
- 해결책: 문서화(Documentation)를 철저히 해야 함.

**Giải thích (Vietnamese):**
Đó là những đoạn code từ "đời tống", người viết code đã nghỉ việc, code không có comment hay tài liệu giải thích. Người mới đọc vào không hiểu gì như ngôn ngữ ngoài hành tinh, không dám sửa vì sợ sập hệ thống.

---

Điểm chốt của **201. 외계인 코드 (Alien Code / Mã ngoài hành tinh)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)

Ở bước 64/91, **204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)** xuất hiện như phần tiếp nối của **201. 외계인 코드 (Alien Code / Mã ngoài hành tinh)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **객체지향 분석**, **분석 방법론**, **Booch**, **Jacobson** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **객체지향 분석**: 사용자의 요구사항을 분석하여 클래스(객체), 속성, 연산, 관계 등을 정의하는 작업.
- **분석 방법론**:
  - **Booch**: 미시적/거시적 개발 프로세스 모두 사용.
  - **Jacobson**: Use Case 강조.
  - **Coad/Yourdon**: E-R 다이어그램 사용.
  - **Wirfs-Brock**: 분석과 설계 간 구분 없음.
- **🌟 럼바우(Rumbaugh)의 분석 기법 (객체 모델링 기법, OMT)**:
  - 분석 순서: **객동기** (객체 -> 동적 -> 기능).
  1. **객체 모델링 (Object Modeling)**: 객체 식별, 구조 및 관계 규정 (객체 다이어그램 / 정보 모델링).
  2. **동적 모델링 (Dynamic Modeling)**: 시간 흐름에 따른 상태 변화, 제어 흐름 표현 (상태도).
  3. **기능 모델링 (Functional Modeling)**: 데이터 흐름을 중심으로 처리 과정 표현 (자료 흐름도, DFD).

**Giải thích (Vietnamese):**
Phương pháp phân tích của Rumbaugh là kinh điển nhất trong thi. Gồm 3 bước:
1. Object (Khách hàng, Tài khoản).
2. Dynamic (Tài khoản từ Đang mở -> Bị khóa khi nhập sai pass 3 lần).
3. Functional (Dữ liệu tiền chạy từ hệ thống ra ATM như thế nào).

**💡 Mẹo ghi nhớ (Mnemonics):**
**객동기** (Khách - Động - Cơ): **객**체(Object) -> **동**적(Dynamic) -> **기**능(Functional).

---

Như vậy, **204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)

Sau khi đã đặt nền bằng **204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)**, ta chuyển sang **206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)**. Đây là mắt xích 65/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **설계 (OOD)**, **프로그래밍 (OOP)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **설계 (OOD)**: 분석 모델을 설계 모델로 변환 (추상화, 정보 은닉, 상속 등 활용). 가장 중요한 것은 **모듈화**. 설계 명세서를 작성.
- **프로그래밍 (OOP)**: 현실 세계에 가까운 방식으로 프로그래밍. 유지보수/재사용성 향상.
  - 객체지향성 언어: Simula (최초), Smalltalk, C++, Java 등.

---

Ta có thể khép mục **206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)

Từ **206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)**, ta đã có điểm tựa để bước vào **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 66/91 trước khi đi vào chi tiết.

Để đọc **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 이미 개발된 소프트웨어 전체/일부를 다른 개발에 사용하는 것. 개발 시간/비용 단축, 품질 향상.
- **컴포넌트 (Component)**: 객체들의 모임으로 대규모 재사용 단위.
- 모듈 크기가 작고 일반적일수록 재사용률이 높음.
- 문제점: 표준화 부족, 공통 요소 발견의 어려움, 새 코드에 통합하기 어려움.

**Giải thích (Vietnamese):**
Đừng "phát minh lại cái bánh xe". Lấy những module, function đã chạy tốt ở dự án trước để ghép vào dự án này (ví dụ: dùng lại module đăng nhập bằng Google).

---

Điểm chốt của **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)

Ở bước 67/91, **209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)** xuất hiện như phần tiếp nối của **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **주요 활동**, **분석 (Analysis)**, **재구성/개조 (Restructuring)**, **역공학 (Reverse Engineering)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 기존 시스템을 수정 보완하거나 기능을 추가하여 성능을 향상 (예방 유지보수).
- 목적: 유지보수 비용 절감, 품질 향상, 소프트웨어 위기 해결.
- **주요 활동**:
  - **분석 (Analysis)**: 기존 명세서 확인.
  - **재구성/개조 (Restructuring)**: 기능은 그대로 두고 코드 구조만 향상 (Refactoring).
  - **역공학 (Reverse Engineering)**: 기존 코드를 분석하여 설계/명세서(문서)를 다시 뽑아내는 것 (복구). 가장 오래된 형태는 재문서화.
  - **이식 (Migration)**: 다른 OS나 하드웨어 환경으로 변환.

**Giải thích (Vietnamese):**
Reengineering là đập đi xây lại hoặc tu sửa lại nhà cũ cho hiện đại hơn.
- Restructuring: Cấu trúc lại bên trong nhà (mở rộng bếp, đập vách ngăn) nhưng nhìn bề ngoài vẫn là cái nhà đó.
- Reverse Engineering: Có một cái nhà cũ xây từ thời xưa không có bản vẽ. Nhìn vào cái nhà thực tế để vẽ lại bản vẽ kỹ thuật (Dịch ngược code thành tài liệu thiết kế).

**💡 Mẹo ghi nhớ (Mnemonics):**
**분재역이** (Phân - Tái - Nghịch - Di): 분석, 재구성, 역공학, 이식.

---

Như vậy, **209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **210. CASE (Computer-Aided Software Engineering)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 210. CASE (Computer-Aided Software Engineering)

Sau khi đã đặt nền bằng **209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)**, ta chuyển sang **210. CASE (Computer-Aided Software Engineering)**. Đây là mắt xích 68/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **210. CASE (Computer-Aided Software Engineering)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **CASE 정보 저장소 (Repository)**, **분류** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “210. CASE (Computer-Aided Software Engineering)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 소프트웨어 생명주기 전체 또는 일부를 **자동화하는 소프트웨어 도구**.
- 개발 기간 단축, 비용 절감, 품질 및 생산성 향상. 개발 주기의 표준화.
- **CASE 정보 저장소 (Repository)**: 개발 중 모아진 정보 보관 (현재의 Database 역할). 일관성 유지.
- **분류**:
  - 상위 (Upper) CASE: 요구 분석, 설계 단계 지원.
  - 하위 (Lower) CASE: 코드 작성, 테스트 지원.
  - 통합 (Integrated) CASE: 전체 과정 지원.

**Giải thích (Vietnamese):**
CASE là các phần mềm hỗ trợ kỹ sư làm phần mềm. Giống như Excel giúp kế toán tính toán nhanh hơn, CASE (như StarUML, Jira, Eclipse) giúp lập trình viên vẽ biểu đồ, quản lý task, sinh code tự động.

---

# 4과목 프로그래밍 언어 활용 (Phần 4: Ứng dụng ngôn ngữ lập trình)

Ta có thể khép mục **210. CASE (Computer-Aided Software Engineering)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **070. 서버개발 프레임워크 (Server Development Framework)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 070. 서버개발 프레임워크 (Server Development Framework)

Từ **210. CASE (Computer-Aided Software Engineering)**, ta đã có điểm tựa để bước vào **070. 서버개발 프레임워크 (Server Development Framework)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 69/91 trước khi đi vào chi tiết.

Để đọc **070. 서버개발 프레임워크 (Server Development Framework)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **모듈화 (Modularity)**, **재사용성 (Reusability)**, **확장성 (Extensibility)**, **제어 반전 (Inversion of Control, IoC)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “070. 서버개발 프레임워크 (Server Development Framework)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **모듈화 (Modularity)**: 캡슐화로 영향 최소화, 유지보수 용이.
- **재사용성 (Reusability)**: 반복 모듈 제공으로 생산성/품질 향상.
- **확장성 (Extensibility)**: 다형성 통한 인터페이스 확장.
- **제어 반전 (Inversion of Control, IoC)**: 프레임워크가 흐름을 제어하고 사용자(외부) 코드를 호출.

**Giải thích (Vietnamese):**
Framework (như Spring, Django) là một bộ khung có sẵn. Tính năng đặc biệt nhất của Framework là IoC (Đảo ngược quyền điều khiển): Thay vì bạn tự gọi thư viện (Library), thì Framework sẽ là người gọi code của bạn!

---

Điểm chốt của **070. 서버개발 프레임워크 (Server Development Framework)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)

Ở bước 70/91, **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)** xuất hiện như phần tiếp nối của **070. 서버개발 프레임워크 (Server Development Framework)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **버퍼 오버플로 (Buffer Overflow)**, **허상 포인터 (Dangling Pointer)**, **FTP 바운스 공격**, **SQL 삽입 (SQL Injection)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **버퍼 오버플로 (Buffer Overflow)**: 메모리를 다루는 데 오류 발생시켜 덮어쓰는 공격.
- **허상 포인터 (Dangling Pointer)**: 삭제된 객체를 가리키고 있는 포인터 (메모리 보안 위반).
- **FTP 바운스 공격**: FTP 프로토콜 구조 허점 이용.
- **SQL 삽입 (SQL Injection)**: 웹 입력창에 SQL 문법 삽입해 DB 데이터 유출/조작.
- **디렉토리 접근 공격 (Directory Traversal)**: 웹 루트 외 디렉토리 접근 (`../` 문자 사용).
- **포맷 스트링 버그**: `printf()` 등에서 검사되지 않은 입력 통한 공격.
- **코드 인젝션 (Code Injection)**: 유효하지 않은 실행 코드 주입.

**Giải thích (Vietnamese):**
- SQL Injection: Kẻ gian gõ `1' OR '1'='1` vào ô đăng nhập để lừa hệ thống cho phép truy cập.
- Buffer Overflow: Kẻ gian cố tình nhập 100 ký tự vào ô chỉ cho phép 10 ký tự, làm tràn bộ nhớ và sập chương trình.

---

Như vậy, **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **078. 사용자 정의 함수와 클래스 (User Defined Functions & Classes)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 078. 사용자 정의 함수와 클래스 (User Defined Functions & Classes)

Sau khi đã đặt nền bằng **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)**, ta chuyển sang **078. 사용자 정의 함수와 클래스 (User Defined Functions & Classes)**. Đây là mắt xích 71/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **078. 사용자 정의 함수와 클래스 (User Defined Functions & Classes)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **접근 제어자 (JAVA Access Modifiers)**, **클래스와 생성자 (Class & Constructor)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “078. 사용자 정의 함수와 클래스 (User Defined Functions & Classes)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **접근 제어자 (JAVA Access Modifiers)**:
  1. `public`: 모든 접근 허용 (Bất cứ đâu cũng gọi được).
  2. `protected`: 같은 패키지 + 상속받은 자식 클래스만 허용.
  3. `default`: 같은 패키지(폴더) 내에서만 허용.
  4. `private`: 오직 해당 객체 내에서만 허용 (Bảo mật cao nhất).
- **클래스와 생성자 (Class & Constructor)**:
  - JAVA: 생성자 이름은 클래스 이름과 동일하며 반환값이 없음. `this` 키워드로 인스턴스 변수(필드)를 가리킴.
  - Python: `class` 키워드 사용. 생성자는 매직 메소드 `__init__(self, ...)`로 정의. `self`는 객체 자신을 참조(JAVA의 `this`와 유사).

---

Ta có thể khép mục **078. 사용자 정의 함수와 클래스 (User Defined Functions & Classes)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **079. 프로그래밍 언어의 종류 (Types of Programming Languages)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 079. 프로그래밍 언어의 종류 (Types of Programming Languages)

Từ **078. 사용자 정의 함수와 클래스 (User Defined Functions & Classes)**, ta đã có điểm tựa để bước vào **079. 프로그래밍 언어의 종류 (Types of Programming Languages)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 72/91 trước khi đi vào chi tiết.

Để đọc **079. 프로그래밍 언어의 종류 (Types of Programming Languages)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **절차적 언어 (Procedural)**, **객체지향 언어 (Object-Oriented)**, **스크립트 언어 (Scripting)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “079. 프로그래밍 언어의 종류 (Types of Programming Languages)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **절차적 언어 (Procedural)**: 코드를 순차적인 함수(Procedure) 단위로 나누어 해결. (C, FORTRAN, ALGOL 등).
- **객체지향 언어 (Object-Oriented)**: 데이터와 메소드를 묶어 '객체'로 만듦 (캡슐화, 상속, 다형성 지원). (C++, JAVA 등). JAVA는 '가비지 컬렉터(Garbage Collector)'가 메모리를 자동 관리함.
- **스크립트 언어 (Scripting)**: 컴파일 없이 인터프리터 방식으로 바로 실행되는 언어. (Python, JavaScript, PHP, Bash 등).
  - PHP: 웹 서버용 스크립트. `@`를 쓰면 에러 무시.
  - JavaScript: 웹 브라우저 제어 (클래스와 프로토타입 기반).

**Giải thích (Vietnamese):**
- Ngôn ngữ thủ tục (như C) chạy từ trên xuống dưới, gọi các hàm.
- Ngôn ngữ OOP (như Java, C++) nhóm code thành các "Thực thể" (Object). Java có Garbage Collector tự động dọn dẹp RAM không dùng đến.
- Ngôn ngữ Script (Python, JS) không cần biên dịch ra file `.exe` mà chạy trực tiếp, rất linh hoạt.

---

Điểm chốt của **079. 프로그래밍 언어의 종류 (Types of Programming Languages)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)

Ở bước 73/91, **084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)** xuất hiện như phần tiếp nối của **079. 프로그래밍 언어의 종류 (Types of Programming Languages)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **FIFO (First In First Out)**, **OPT (Optimal)**, **LRU (Least Recently Used)**, **LFU (Least Frequently Used)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 메모리가 꽉 찼을 때 어떤 페이지를 내보낼지 결정.
- **FIFO (First In First Out)**: 가장 먼저 들어온 페이지를 교체.
- **OPT (Optimal)**: 앞으로 가장 오랫동안 사용되지 않을 페이지를 교체 (이론상 최적).
- **LRU (Least Recently Used)**: (과거 기준) 가장 오랫동안 사용되지 않은 페이지를 교체.
- **LFU (Least Frequently Used)**: 사용(참조) 횟수가 가장 적은 페이지 교체.
- **NUR (Not Used Recently)**: 참조 비트(R)와 변형/수정 비트(M)를 조합해 페이지를 네 등급으로 나누고 낮은 등급부터 교체한다.
- **지역성 (Locality)**: 프로세스가 특정 메모리 영역을 집중적으로 참조하는 현상.
  - 공간 지역성: 근처 메모리 참조 (배열).
  - 시간 지역성: 방금 참조한 곳 다시 참조 (루프, 변수).
- **스레싱 (Thrashing)**: 실제 CPU 연산보다 페이지 교체에 더 많은 시간이 소요되어 시스템 성능이 뚝 떨어지는 현상.

**Giải thích (Vietnamese):**
Khi RAM đầy, máy phải đẩy tạm dữ liệu ra ổ cứng.
- LRU: Đuổi cái nào lâu nhất không ai thèm đụng tới (Thường xuyên dùng nhất).
- LFU: Đuổi cái nào ít được gọi tên nhất.
- Locality: Chương trình có xu hướng dùng lại những dữ liệu gần nhau (Ví dụ chạy vòng lặp `for`).
- Thrashing: Tình trạng máy tính bị đơ, giật lag vì RAM quá đầy, máy mải mê swap dữ liệu ra vào ổ cứng mà không chịu tính toán xử lý.

---

Như vậy, **084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **교착상태 필요충분조건 1 - 상호배제 (Deadlock Conditions - Mutual Exclusion)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 교착상태 필요충분조건 1 - 상호배제 (Deadlock Conditions - Mutual Exclusion)

Sau khi đã đặt nền bằng **084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)**, ta chuyển sang **교착상태 필요충분조건 1 - 상호배제 (Deadlock Conditions - Mutual Exclusion)**. Đây là mắt xích 74/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **교착상태 필요충분조건 1 - 상호배제 (Deadlock Conditions - Mutual Exclusion)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **교착상태(Deadlock)**, **상호배제 알고리즘 (Mutual Exclusion)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “교착상태 필요충분조건 1 - 상호배제 (Deadlock Conditions - Mutual Exclusion)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **교착상태(Deadlock)**: 두 프로세스가 서로의 자원을 기다리며 멈춰버린 현상.
- **상호배제 알고리즘 (Mutual Exclusion)**: 한 번에 하나의 프로세스만 자원을 쓰게 함.
  - Dekker: 두 프로세스 간 Flag와 Turn 변수 사용.
  - Peterson: 두 프로세스 간 상대방에게 양보.
  - Lamport: 고유 번호(티켓) 부여, 번호순 진입.
  - Semaphore: 정수 변수(P연산, V연산)를 이용해 접근 통제.

Ta có thể khép mục **교착상태 필요충분조건 1 - 상호배제 (Deadlock Conditions - Mutual Exclusion)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **추가: 응용 SW 기초 기술 (4과목 핵심 요약 1)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 추가: 응용 SW 기초 기술 (4과목 핵심 요약 1)

Từ **교착상태 필요충분조건 1 - 상호배제 (Deadlock Conditions - Mutual Exclusion)**, ta đã có điểm tựa để bước vào **추가: 응용 SW 기초 기술 (4과목 핵심 요약 1)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 75/91 trước khi đi vào chi tiết.

Để đọc **추가: 응용 SW 기초 기술 (4과목 핵심 요약 1)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận. Trong khối này, **필수 요소 5가지**, **C/C++**, **JAVA** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **232. 배치 프로그램 (Batch Program)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 232. 배치 프로그램 (Batch Program)

Các ý ngay dưới **232. 배치 프로그램 (Batch Program)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “232. 배치 프로그램 (Batch Program)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 대량의 데이터를 사용자 개입 없이 정해진 순서에 따라 **일괄적으로 처리**하는 방식.
- 야간 시간대 등 자원 소모가 적은 시간에 실행됨.
- **필수 요소 5가지**: 대용량, 자동화, 견고성, 안정성, 성능.

**Giải thích (Vietnamese):**
Chương trình Batch (xử lý hàng loạt) là loại phần mềm tự động chạy ngầm, thường vào ban đêm. Ví dụ: Cuối ngày ngân hàng tổng hợp lại toàn bộ giao dịch trong ngày, xử lý một lúc hàng triệu giao dịch mà không cần người bấm nút.

Các ý về **232. 배치 프로그램 (Batch Program)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **232. 배치 프로그램 (Batch Program)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **233 & 235. 데이터 타입 크기 (Data Type Sizes - C/C++ vs JAVA)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **233 & 235. 데이터 타입 크기 (Data Type Sizes - C/C++ vs JAVA)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 233 & 235. 데이터 타입 크기 (Data Type Sizes - C/C++ vs JAVA)

Bây giờ ta đi vào nội dung của **233 & 235. 데이터 타입 크기 (Data Type Sizes - C/C++ vs JAVA)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “233 & 235. 데이터 타입 크기 (Data Type Sizes - C/C++ vs JAVA)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **C/C++**: `char`(1바이트), `short`(2바이트), `int`(4바이트), `float`(4바이트), `double`(8바이트).
- **JAVA**: `byte`(1바이트), **`char`(2바이트, 유니코드 지원)**, `int`(4바이트), `boolean`(1바이트).

**Giải thích (Vietnamese):**
Lưu ý quan trọng: Trong C, `char` (kí tự) chiếm 1 byte. Nhưng trong Java, `char` chiếm 2 byte vì Java dùng bảng mã Unicode để hỗ trợ mọi ngôn ngữ trên thế giới (kể cả tiếng Hàn, tiếng Việt).

Các bullet của **233 & 235. 데이터 타입 크기 (Data Type Sizes - C/C++ vs JAVA)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **233 & 235. 데이터 타입 크기 (Data Type Sizes - C/C++ vs JAVA)**, đừng bắt đầu lại từ số không. **234. C언어의 구조체 (struct)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **234. C언어의 구조체 (struct)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 234. C언어의 구조체 (struct)

Phần nguồn của **234. C언어의 구조체 (struct)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “234. C언어의 구조체 (struct)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 서로 다른 데이터 타입을 하나로 묶어 관리하는 사용자 정의 자료형. 배열(동일 타입)과의 차이점.
- (Ví dụ: Một `struct SinhVien` có thể chứa Tên(string), Tuổi(int), Điểm(float)).

Các ý về **234. C언어의 구조체 (struct)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

**234. C언어의 구조체 (struct)** vừa cho ta cách đặt câu hỏi. Bây giờ **236. Python 시퀀스 자료형** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **236. Python 시퀀스 자료형** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 236. Python 시퀀스 자료형

Các ý ngay dưới **236. Python 시퀀스 자료형** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “236. Python 시퀀스 자료형” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 리스트(List): `[]` 변경 가능.
- 튜플(Tuple): `()` **변경 불가능(Immutable)**.
- (Ví dụ: Tuple dùng để lưu toạ độ GPS không bao giờ đổi).

Các ý về **236. Python 시퀀스 자료형** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **236. Python 시퀀스 자료형** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **238. 가비지 콜렉터 (Garbage Collector)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **238. 가비지 콜렉터 (Garbage Collector)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 238. 가비지 콜렉터 (Garbage Collector)

Bây giờ ta đi vào nội dung của **238. 가비지 콜렉터 (Garbage Collector)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “238. 가비지 콜렉터 (Garbage Collector)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 사용되지 않는 메모리를 자동으로 해제해주는 기능 (메모리 누수 방지). Java 등 현대 언어의 핵심.

Các bullet của **238. 가비지 콜렉터 (Garbage Collector)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **238. 가비지 콜렉터 (Garbage Collector)**, đừng bắt đầu lại từ số không. **239 - 244. 각종 연산자** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **239 - 244. 각종 연산자**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 239 - 244. 각종 연산자

Phần nguồn của **239 - 244. 각종 연산자** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “239 - 244. 각종 연산자” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 산술(`%`, `++`), 관계(`==`, `!=`), 비트(`&`, `|`, `^`, `<<`), 논리(`&&`, `||`), 대입(`+=`), 조건 삼항연산자.
- `a += 1`은 `a = a + 1`과 같다.
- 비트 XOR(`^`): 두 비트가 다를 때만 1을 반환.

Với **239 - 244. 각종 연산자**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Như vậy, **239 - 244. 각종 연산자** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **추가: 응용 SW 기초 기술 (4과목 핵심 요약 1)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **232. 배치 프로그램 (Batch Program)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 232. 배치 프로그램 (Batch Program)

Ở bước 76/91, **232. 배치 프로그램 (Batch Program)** xuất hiện như phần tiếp nối của **추가: 응용 SW 기초 기술 (4과목 핵심 요약 1)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **232. 배치 프로그램 (Batch Program)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “232. 배치 프로그램 (Batch Program)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 대량의 데이터를 사용자 개입 없이 정해진 순서에 따라 **일괄적으로 처리**하는 방식.
- 야간 시간대 등 자원 소모가 적은 시간에 실행됨.
- **필수 요소 5가지**: 대용량, 자동화, 견고성(오류 시에도 중단 없이 기록/지속), 안정성, 성능.

**Giải thích (Vietnamese):**
Chương trình Batch (xử lý hàng loạt) tự động chạy ngầm để xử lý lượng lớn dữ liệu mà không cần con người can thiệp.
- Tính kiên cố (견고성): Lỡ có 1 dòng dữ liệu bị lỗi, chương trình không bị sập mà sẽ ghi log lại và chạy tiếp dòng khác.

**💡 Mẹo ghi nhớ (Mnemonics):**
**대자견안성** (Đại - Tự - Kiên - An - Tính): 대용량, 자동화, 견고성, 안정성, 성능.

---

Như vậy, **232. 배치 프로그램 (Batch Program)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **234. C언어의 구조체 (struct in C)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 234. C언어의 구조체 (struct in C)

Sau khi đã đặt nền bằng **232. 배치 프로그램 (Batch Program)**, ta chuyển sang **234. C언어의 구조체 (struct in C)**. Đây là mắt xích 77/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **234. C언어의 구조체 (struct in C)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “234. C언어의 구조체 (struct in C)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 서로 다른 데이터 유형을 가진 변수들을 하나로 묶어 관리하는 사용자 정의 자료형.
- 배열(Array)은 **동일한 자료형**만 모으지만, 구조체(Struct)는 **상이한 자료형**을 모을 수 있음.

**Giải thích (Vietnamese):**
Struct (Cấu trúc) dùng để gom nhóm nhiều biến khác kiểu lại với nhau. Ví dụ tạo kiểu `SinhVien` gồm tên (chuỗi) và tuổi (số). Trong khi Mảng (Array) chỉ được lưu cùng một kiểu (hoặc toàn chuỗi, hoặc toàn số).

---

Ta có thể khép mục **234. C언어의 구조체 (struct in C)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **238. 가비지 콜렉터 (Garbage Collector)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 238. 가비지 콜렉터 (Garbage Collector)

Từ **234. C언어의 구조체 (struct in C)**, ta đã có điểm tựa để bước vào **238. 가비지 콜렉터 (Garbage Collector)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 78/91 trước khi đi vào chi tiết.

Để đọc **238. 가비지 콜렉터 (Garbage Collector)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “238. 가비지 콜렉터 (Garbage Collector)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 더 이상 사용되지 않고 메모리를 점유하고 있는 변수/객체를 시스템이 **자동으로 해제**하여 자원을 회수하는 모듈.
- 메모리 누수(Memory Leak)를 방지. JAVA 등에서 사용됨.

**Giải thích (Vietnamese):**
"Người dọn rác" tự động. Bạn cứ việc tạo biến dùng, khi không dùng nữa, hệ thống sẽ tự động xoá nó khỏi RAM để giải phóng bộ nhớ. Trong C/C++ bạn phải tự dọn dẹp, nhưng Java/Python có tính năng này.

---

Điểm chốt của **238. 가비지 콜렉터 (Garbage Collector)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **250. JAVA에서의 표준 출력 (Standard Output in JAVA)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 250. JAVA에서의 표준 출력 (Standard Output in JAVA)

Ở bước 79/91, **250. JAVA에서의 표준 출력 (Standard Output in JAVA)** xuất hiện như phần tiếp nối của **238. 가비지 콜렉터 (Garbage Collector)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **250. JAVA에서의 표준 출력 (Standard Output in JAVA)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “250. JAVA에서의 표준 출력 (Standard Output in JAVA)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `System.out.print()`: 형식 없이 그대로 출력 (줄바꿈 없음).
- `System.out.println()`: 출력 후 자동으로 줄바꿈(Enter) 수행.
- `System.out.printf()`: C언어처럼 서식 문자열(`%d` 등)을 사용하여 출력.
- 문자열과 변수를 섞어 쓸 때 `+` 연산자로 연결 가능.

---

Như vậy, **250. JAVA에서의 표준 출력 (Standard Output in JAVA)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **251. 단순 if문 (Simple if Statement)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 251. 단순 if문 (Simple if Statement)

Sau khi đã đặt nền bằng **250. JAVA에서의 표준 출력 (Standard Output in JAVA)**, ta chuyển sang **251. 단순 if문 (Simple if Statement)**. Đây là mắt xích 80/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **251. 단순 if문 (Simple if Statement)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “251. 단순 if문 (Simple if Statement)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 조건의 참/거짓에 따라 실행할 문장 결정.
- 문장이 두 개 이상이면 반드시 중괄호 `{ }`로 묶어야 함.
- C언어에서는 조건식 결과가 0이면 거짓(False), **0 이외의 모든 값은 참(True)**으로 간주.

---

Ta có thể khép mục **251. 단순 if문 (Simple if Statement)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **253. switch문 (switch Statement)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 253. switch문 (switch Statement)

Từ **251. 단순 if문 (Simple if Statement)**, ta đã có điểm tựa để bước vào **253. switch문 (switch Statement)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 81/91 trước khi đi vào chi tiết.

Để đọc **253. switch문 (switch Statement)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “253. switch문 (switch Statement)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 변수의 값에 따라 일치하는 `case` 문장을 실행하는 다분기 제어문.

Điểm chốt của **253. switch문 (switch Statement)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **254 - 257. 반복문과 제어 키워드 (Loops & Control Keywords)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 254 - 257. 반복문과 제어 키워드 (Loops & Control Keywords)

Ở bước 82/91, **254 - 257. 반복문과 제어 키워드 (Loops & Control Keywords)** xuất hiện như phần tiếp nối của **253. switch문 (switch Statement)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **254 - 257. 반복문과 제어 키워드 (Loops & Control Keywords)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **for문**, **while문**, **do~while문**, **break** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “254 - 257. 반복문과 제어 키워드 (Loops & Control Keywords)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **for문**: 횟수가 정해진 반복(초기화, 조건검사, 증감식). 배열 순회에 주로 사용.
- **while문**: 조건이 참인 동안 반복(선행 판단). 조건이 항상 참이면 무한 루프 발생.
- **do~while문**: **최소 1번은 무조건 실행**한 후 조건을 검사(후행 판단).
- **break**: 현재 실행 중인 루프(블록)를 즉시 완전히 빠져나감.
- **continue**: 루프를 완전히 빠져나가지 않고, **다음 반복 회차로 건너뜀**.

**Giải thích (Vietnamese):**
- `for`: Biết trước số lần lặp (VD: đếm từ 1 đến 10).
- `while`: Lặp cho đến khi điều kiện sai (VD: lặp tới khi game over).
- `break`: Dừng cuộc chơi ngay lập tức, thoát ra ngoài.
- `continue`: Bỏ qua vòng lặp hiện tại, đi tới vòng lặp tiếp theo (VD: đếm từ 1 đến 10, nếu gặp số 5 thì `continue` -> in ra 1 2 3 4 6 7 8 9 10).

---

Như vậy, **254 - 257. 반복문과 제어 키워드 (Loops & Control Keywords)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **275 - 278. 프로그래밍 언어의 종류 (Types of Programming Languages)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 275 - 278. 프로그래밍 언어의 종류 (Types of Programming Languages)

Sau khi đã đặt nền bằng **254 - 257. 반복문과 제어 키워드 (Loops & Control Keywords)**, ta chuyển sang **275 - 278. 프로그래밍 언어의 종류 (Types of Programming Languages)**. Đây là mắt xích 83/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **275 - 278. 프로그래밍 언어의 종류 (Types of Programming Languages)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **절차적 언어**, **객체지향 언어**, **선언형 언어** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “275 - 278. 프로그래밍 언어의 종류 (Types of Programming Languages)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **절차적 언어**: 실행 순서 중시.
  - `COBOL` (사무용), `FORTRAN` (과학 기술 계산용), `C` (시스템 프로그래밍), `ALGOL`.
- **객체지향 언어**: 데이터+기능 캡슐화. 재사용성 높음.
  - `JAVA` (플랫폼 독립성, JVM), `C++` (C의 객체지향 확장), `Smalltalk` (최초 GUI, 순수 객체지향).
- **선언형 언어**: '무엇(What)'을 할지 기술 (함수형/논리형).
  - `LISP` (연결리스트, AI용), `PROLOG` (논리 추론, AI용), `Haskell` (순수 함수형), `XML` (구조화 문서).

---

Ta có thể khép mục **275 - 278. 프로그래밍 언어의 종류 (Types of Programming Languages)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **281. 매시업과 SOA (SW Related Terms: Mashup & SOA)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 281. 매시업과 SOA (SW Related Terms: Mashup & SOA)

Từ **275 - 278. 프로그래밍 언어의 종류 (Types of Programming Languages)**, ta đã có điểm tựa để bước vào **281. 매시업과 SOA (SW Related Terms: Mashup & SOA)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 84/91 trước khi đi vào chi tiết.

Để đọc **281. 매시업과 SOA (SW Related Terms: Mashup & SOA)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **매시업 (Mashup)**, **SOA (Service Oriented Architecture, 서비스 지향 아키텍처)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “281. 매시업과 SOA (SW Related Terms: Mashup & SOA)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **매시업 (Mashup)**: 웹 서비스나 콘텐츠를 조합하여 **새로운 서비스를 만드는 기술** (예: 구글 지도 + 부동산 정보).
- **SOA (Service Oriented Architecture, 서비스 지향 아키텍처)**: 시스템을 **공유/재사용 가능한 서비스 단위**로 구축하는 구조. (계층: 표현, 업무 프로세스, 서비스 중간, 애플리케이션, 데이터 저장).

**Giải thích (Vietnamese):**
- Mashup: Lấy dữ liệu bản đồ của Google kết hợp với dữ liệu danh sách quán ăn để tạo ra app "Tìm quán ăn gần đây". (Trộn lẫn dữ liệu có sẵn để làm ra cái mới).

---

Điểm chốt của **281. 매시업과 SOA (SW Related Terms: Mashup & SOA)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **226 - 227. 데이터베이스 접속 기술 (Database Connectivity)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 226 - 227. 데이터베이스 접속 기술 (Database Connectivity)

Ở bước 85/91, **226 - 227. 데이터베이스 접속 기술 (Database Connectivity)** xuất hiện như phần tiếp nối của **281. 매시업과 SOA (SW Related Terms: Mashup & SOA)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **226 - 227. 데이터베이스 접속 기술 (Database Connectivity)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **JDBC (Java DataBase Connectivity)**, **ODBC (Open DataBase Connectivity)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “226 - 227. 데이터베이스 접속 기술 (Database Connectivity)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **JDBC (Java DataBase Connectivity)**: **자바(Java)** 프로그램 내에서 데이터베이스(DBMS)에 접속하여 SQL 문을 실행하기 위한 표준 API. 운영체제에 독립적.
- **ODBC (Open DataBase Connectivity)**: 프로그래밍 **언어에 관계없이** (C, C++, VB 등) 다양한 DBMS에 접근할 수 있게 마이크로소프트가 만든 개방형 표준 API.

**Giải thích (Vietnamese):**
- JDBC: Dành riêng cho ngôn ngữ Java.
- ODBC: Mở (Open) cho mọi ngôn ngữ khác, dùng chung thông qua một "người quản lý tài xế" (Driver Manager) để dịch lệnh SQL gửi xuống Database.

Như vậy, **226 - 227. 데이터베이스 접속 기술 (Database Connectivity)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)

Sau khi đã đặt nền bằng **226 - 227. 데이터베이스 접속 기술 (Database Connectivity)**, ta chuyển sang **인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)**. Đây là mắt xích 86/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **개념 (Khái niệm)**, **핵심 키워드 (Từ khóa)**, **시험 포인트 (Điểm thi)**, **한 문장 설명 (Tóm tắt)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **TẦNG A – NOTE NÉN (ÔN / ĐI THI)**. Hãy xác định **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### TẦNG A – NOTE NÉN (ÔN / ĐI THI)

Phần nguồn của **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “TẦNG A – NOTE NÉN (ÔN / ĐI THI)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념 (Khái niệm)**: 소스 코드를 컴파일하지 않고 인터프리터(Interpreter)가 한 줄씩 즉시 해석하여 실행하는 프로그래밍 언어. (Ngôn ngữ lập trình dịch và thực thi từng dòng mã nguồn trực tiếp mà không cần biên dịch toàn bộ.)
- **핵심 키워드 (Từ khóa)**: 자바 스크립트 (JavaScript), PHP, 파이썬 (Python), 쉘 스크립트 (Shell script).
- **시험 포인트 (Điểm thi)**: 클라이언트용(Client-side: JS)과 서버용(Server-side: ASP, JSP, PHP) 스크립트 언어를 구분하는 것이 단골 문제. (Phân biệt ngôn ngữ cho Client và Server là câu hỏi thường gặp.)
- **한 문장 설명 (Tóm tắt)**: 컴파일 과정이 없어 수정과 실행 시작이 편리하지만, 반복 실행 성능은 일반적으로 컴파일 방식보다 느릴 수 있다. (Dễ sửa và bắt đầu chạy vì không cần biên dịch trước, nhưng hiệu năng chạy lặp thường có thể chậm hơn kiểu biên dịch.)

Các bullet của **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **TẦNG B – NOTE 보충 (HIỂU SÂU)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **TẦNG B – NOTE 보충 (HIỂU SÂU)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### TẦNG B – NOTE 보충 (HIỂU SÂU)

Các ý ngay dưới **TẦNG B – NOTE 보충 (HIỂU SÂU)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “TẦNG B – NOTE 보충 (HIỂU SÂU)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **자바 스크립트 (JavaScript)**: 웹 브라우저 내에서 동작하며 입력 사항 확인 등 클라이언트 측 제어에 사용. (Chạy trên trình duyệt, kiểm soát phía client như xác thực đầu vào.)
- **PHP**: 서버용 스크립트로 C, Java와 문법이 유사. (Script cho server, cú pháp giống C/Java.)
- **파이썬 (Python)**: 객체지향 지원, 문법이 간단하여 배우기 쉽고 플랫폼 독립적인 대화형 언어. (Hỗ trợ OOP, cú pháp đơn giản, độc lập nền tảng, có tính tương tác.)
- **쉘 스크립트 (Shell Script)**: 유닉스/리눅스의 쉘 명령어를 조합한 관리용. (Kết hợp lệnh shell Linux/Unix để quản trị.)
- **ASP / JSP**: 서버 측 동적 페이지 생성 언어 (ASP의 마이크로소프트, JSP의 자바 기반). (ASP của MS, JSP của Java.)
- **예시 (Ví dụ)**: 브라우저에서 버튼을 누르면 즉시 알림창이 뜨는 JS 코드는 컴파일 없이 바로 실행됨. (Mã JS hiển thị thông báo khi bấm nút trên trình duyệt chạy ngay mà không cần biên dịch.)
- 💡 **Mẹo ghi nhớ**: JS là Client, còn lại PPP (PHP, JSP, ASP) đa số là Server.

Các ý về **TẦNG B – NOTE 보충 (HIỂU SÂU)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Điểm chốt của **TẦNG B – NOTE 보충 (HIỂU SÂU)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **284 & 294. 구역성 (Locality / Tính cục bộ)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 284 & 294. 구역성 (Locality / Tính cục bộ)

Từ **인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)**, ta đã có điểm tựa để bước vào **284 & 294. 구역성 (Locality / Tính cục bộ)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 87/91 trước khi đi vào chi tiết.

Để đọc **284 & 294. 구역성 (Locality / Tính cục bộ)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **개념 (Khái niệm)**, **핵심 키워드 (Từ khóa)**, **시험 포인트 (Điểm thi)**, **한 문장 설명 (Tóm tắt)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### TẦNG A – NOTE NÉN (ÔN / ĐI THI)

Các ý ngay dưới **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “TẦNG A – NOTE NÉN (ÔN / ĐI THI)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념 (Khái niệm)**: 프로세스가 실행되는 동안 주기억장치(Main memory)의 특정 영역만을 집중적으로 참조하는 성질. (Tính chất mà quá trình chỉ tham chiếu tập trung vào một số trang nhất định của bộ nhớ chính khi thực thi.)
- **핵심 키워드 (Từ khóa)**: 시간 구역성 (Temporal locality), 공간 구역성 (Spatial locality), 집중 참조 (Concentrated reference).
- **시험 포인트 (Điểm thi)**: 시간 구역성(Loop, Stack)과 공간 구역성(Array)의 구체적인 사례를 구분하는 것. (Phân biệt ví dụ của cục bộ thời gian và cục bộ không gian.)
- **한 문장 설명 (Tóm tắt)**: 스래싱(Thrashing) 방지를 위한 핵심 이론. (Lý thuyết cốt lõi để ngăn chặn hiện tượng Thrashing.)

Các ý về **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **TẦNG B – NOTE 보충 (HIỂU SÂU)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **TẦNG B – NOTE 보충 (HIỂU SÂU)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### TẦNG B – NOTE 보충 (HIỂU SÂU)

Bây giờ ta đi vào nội dung của **TẦNG B – NOTE 보충 (HIỂU SÂU)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “TẦNG B – NOTE 보충 (HIỂU SÂU)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **시간 구역성 (Temporal locality)**: 한 번 참조된 페이지는 가까운 시간 내에 다시 참조될 가능성이 높음. (Trang vừa dùng sẽ có khả năng cao được dùng lại sớm. Ví dụ: Vòng lặp/Loop, Ngăn xếp/Stack, Biến đếm.)
- **공간 구역성 (Spatial locality)**: 특정 페이지가 참조되면 인근 위치의 페이지가 계속 참조될 가능성이 높음. (Trang vừa dùng thì các trang liền kề nó dễ được gọi theo. Ví dụ: Mảng/Array, duyệt tuần tự.)
- **예시 (Ví dụ)**: 배열 `A[0]`부터 `A[100]`까지 순서대로 읽는 것은 공간 구역성이고, `for`문 안에서 변수 `i`를 계속 증가시키며 쓰는 것은 시간 구역성. (Đọc mảng theo thứ tự là cục bộ không gian; dùng biến i nhiều lần trong vòng lặp là cục bộ thời gian.)
- 💡 **Mẹo ghi nhớ**: **T**emporal = **T**ime (Lặp lại nhiều lần/Loop), **S**patial = **S**pace (Gần nhau/Array).

Với **TẦNG B – NOTE 보충 (HIỂU SÂU)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **TẦNG B – NOTE 보충 (HIỂU SÂU)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **284 & 294. 구역성 (Locality / Tính cục bộ)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **285 & 295. 워킹 셋 (Working Set / Tập làm việc)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 285 & 295. 워킹 셋 (Working Set / Tập làm việc)

Ở bước 88/91, **285 & 295. 워킹 셋 (Working Set / Tập làm việc)** xuất hiện như phần tiếp nối của **284 & 294. 구역성 (Locality / Tính cục bộ)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **285 & 295. 워킹 셋 (Working Set / Tập làm việc)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **개념 (Khái niệm)**, **핵심 키워드 (Từ khóa)**, **시험 포인트 (Điểm thi)**, **예시 (Ví dụ)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### TẦNG A – NOTE NÉN (ÔN / ĐI THI)

Bây giờ ta đi vào nội dung của **TẦNG A – NOTE NÉN (ÔN / ĐI THI)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “TẦNG A – NOTE NÉN (ÔN / ĐI THI)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념 (Khái niệm)**: 프로세스가 원활한 수행을 위해 일정 시간 동안 집중적으로 참조하는 페이지들의 집합. (Tập hợp các trang mà tiến trình tham chiếu tập trung trong một khoảng thời gian để chạy mượt mà.)
- **핵심 키워드 (Từ khóa)**: 데닝 (Denning), Locality 활용 (Ứng dụng Locality), 페이지 부재 감소 (Giảm Page Fault), 동적 변경 (Thay đổi động).
- **시험 포인트 (Điểm thi)**: 자주 참조되는 워킹 셋을 주기억장치에 상주시킴으로써 시스템을 안정화(스래싱 방지)한다는 점. (Giữ Working Set trong bộ nhớ chính giúp hệ thống ổn định và tránh Thrashing.)

Các bullet của **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **TẦNG B – NOTE 보충 (HIỂU SÂU)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **TẦNG B – NOTE 보충 (HIỂU SÂU)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### TẦNG B – NOTE 보충 (HIỂU SÂU)

Phần nguồn của **TẦNG B – NOTE 보충 (HIỂU SÂU)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “TẦNG B – NOTE 보충 (HIỂU SÂU)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 데닝(Denning)이 제안한 모델로, 프로그램의 국부성(Locality)을 이용. (Mô hình do Denning đề xuất dựa trên tính cục bộ.)
- 시간에 따라 참조하는 페이지가 달라지므로 지속적으로 (동적으로) 변경됨. (Thay đổi động theo thời gian.)
- **예시 (Ví dụ)**: 당신이 시험 공부를 할 때 지금 당장 책상 위에 꺼내놓은 책과 필기구들이 '워킹 셋'입니다. 과목이 바뀌면 책상 위 물건(워킹 셋)도 바뀝니다. (Những cuốn sách và bút bạn đang để trên bàn học ngay lúc này chính là 'Working Set'. Khi chuyển môn, đồ trên bàn cũng thay đổi.)
- 💡 **Mẹo ghi nhớ**: Working Set = Những món đồ đang "Working" (Đang dùng) phải để sẵn trên bàn (Memory).

Với **TẦNG B – NOTE 보충 (HIỂU SÂU)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **TẦNG B – NOTE 보충 (HIỂU SÂU)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **285 & 295. 워킹 셋 (Working Set / Tập làm việc)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)

Sau khi đã đặt nền bằng **285 & 295. 워킹 셋 (Working Set / Tập làm việc)**, ta chuyển sang **287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)**. Đây là mắt xích 89/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **개념 (Khái niệm)**, **핵심 키워드 (Từ khóa)**, **시험 포인트 (Điểm thi)**, **커널 (Kernel)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **TẦNG A – NOTE NÉN (ÔN / ĐI THI)**. Hãy xác định **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### TẦNG A – NOTE NÉN (ÔN / ĐI THI)

Phần nguồn của **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “TẦNG A – NOTE NÉN (ÔN / ĐI THI)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념 (Khái niệm)**: 커널(Kernel), 쉘(Shell), 유틸리티(Utility)의 계층적 구조. (Cấu trúc phân tầng gồm Kernel, Shell và Utility.)
- **핵심 키워드 (Từ khóa)**: 커널(Kernel - Hạt nhân), 쉘(Shell - Vỏ), 명령어 해석기 (Trình thông dịch lệnh).
- **시험 포인트 (Điểm thi)**: 커널(핵심 및 상주)과 쉘(명령어 해석기 및 인터페이스)의 역할을 명확히 구분. (Phân biệt vai trò của Kernel và Shell.)

Các bullet của **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **TẦNG B – NOTE 보충 (HIỂU SÂU)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **TẦNG B – NOTE 보충 (HIỂU SÂU)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### TẦNG B – NOTE 보충 (HIỂU SÂU)

Các ý ngay dưới **TẦNG B – NOTE 보충 (HIỂU SÂU)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “TẦNG B – NOTE 보충 (HIỂU SÂU)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **커널 (Kernel)**: 하드웨어를 직접 관리, 프로세스/메모리/파일 관리. 주기억장치에 상주. (Quản lý trực tiếp phần cứng, tiến trình, bộ nhớ. Nằm thường trực trong RAM.)
- **쉘 (Shell)**: 사용자의 명령을 인식하여 수행하는 명령어 해석기 (인터페이스). (Trình biên dịch lệnh, nhận lệnh từ người dùng và gọi chương trình.)
- **유틸리티 (Utility)**: 에디터, 컴파일러 등 응용 프로그램. (Các chương trình ứng dụng như trình soạn thảo, biên dịch.)
- **예시 (Ví dụ)**: 식당에서 사용자가 주문(명령)을 하면 종업원(Shell)이 이를 받아 주방장(Kernel)에게 전달하여 요리(하드웨어 제어)를 하는 구조. (Khách hàng gọi món (Lệnh) -> Phục vụ bàn (Shell) -> Đầu bếp (Kernel) xử lý nấu nướng.)
- 💡 **Mẹo ghi nhớ**: Kernel là **Lõi** (Hardware), Shell là **Vỏ** (Giao tiếp người dùng).

Các ý về **TẦNG B – NOTE 보충 (HIỂU SÂU)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Điểm chốt của **TẦNG B – NOTE 보충 (HIỂU SÂU)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)

Từ **287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)**, ta đã có điểm tựa để bước vào **292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 90/91 trước khi đi vào chi tiết.

Để đọc **292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **개념 (Khái niệm)**, **핵심 키워드 (Từ khóa)**, **시험 포인트 (Điểm thi)**, **OPT (Optimal)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### TẦNG A – NOTE NÉN (ÔN / ĐI THI)

Các ý ngay dưới **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “TẦNG A – NOTE NÉN (ÔN / ĐI THI)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념 (Khái niệm)**: 주기억장치 빈 공간이 없을 때 어떤 페이지를 내보낼지 결정하는 기법. (Kỹ thuật chọn trang để loại bỏ khi bộ nhớ chính đã đầy để nhường chỗ cho trang mới.)
- **핵심 키워드 (Từ khóa)**: OPT, FIFO, LRU, LFU, NUR.
- **시험 포인트 (Điểm thi)**: 각 알고리즘별 교체 대상 선정 기준 묻는 문제. (Tiêu chí chọn trang của từng thuật toán.)

Các bullet của **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **TẦNG B – NOTE 보충 (HIỂU SÂU)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **TẦNG B – NOTE 보충 (HIỂU SÂU)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### TẦNG B – NOTE 보충 (HIỂU SÂU)

Bây giờ ta đi vào nội dung của **TẦNG B – NOTE 보충 (HIỂU SÂU)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “TẦNG B – NOTE 보충 (HIỂU SÂU)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **OPT (Optimal)**: 앞으로 가장 오랫동안 안 쓸 페이지 교체 (이론적 최고). (Thay trang sẽ lâu nhất không được dùng trong tương lai - Tốt nhất nhưng chỉ trên lý thuyết.)
- **FIFO (First-In First-Out)**: 들어온 지 가장 오래된 페이지 교체. (Thay trang vào bộ nhớ sớm nhất.)
- **LRU (Least Recently Used)**: 최근에 가장 오랫동안 안 쓴 페이지 교체. (Thay trang lâu nhất chưa được sử dụng tính từ hiện tại.)
- **LFU (Least Frequently Used)**: 참조 횟수가 가장 적은 페이지 교체. (Thay trang có số lần sử dụng ít nhất.)
- **NUR (Not Used Recently)**: 참조 비트(R)와 변형/수정 비트(M)를 조합해 낮은 등급의 페이지부터 교체한다. (Dùng hai bit R/M để phân loại và thay trang.)
- **예시 (Ví dụ)**: 스마트폰에서 앱을 여러 개 켜다가 램이 부족해지면, 제일 먼저 켰던 앱(FIFO)을 끄거나 최근에 가장 안 본 앱(LRU)을 종료시킴. (Khi điện thoại đầy RAM, nó sẽ tắt app mở đầu tiên (FIFO) hoặc app lâu rồi chưa đụng tới (LRU).)
- 💡 **Mẹo ghi nhớ**: **R**ecently = Lâu không đụng (Thời gian), **F**requently = Ít dùng (Số lần).

Với **TẦNG B – NOTE 보충 (HIỂU SÂU)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **TẦNG B – NOTE 보충 (HIỂU SÂU)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **298. PCB (Process Control Block)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 298. PCB (Process Control Block)

Ở bước 91/91, **298. PCB (Process Control Block)** xuất hiện như phần tiếp nối của **292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **298. PCB (Process Control Block)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **개념 (Khái niệm)**, **핵심 키워드 (Từ khóa)**, **시험 포인트 (Điểm thi)**, **예시 (Ví dụ)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### TẦNG A – NOTE NÉN (ÔN / ĐI THI)

Bây giờ ta đi vào nội dung của **TẦNG A – NOTE NÉN (ÔN / ĐI THI)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “TẦNG A – NOTE NÉN (ÔN / ĐI THI)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념 (Khái niệm)**: 운영체제가 각 프로세스를 관리하기 위해 정보를 저장하는 데이터 구조. (Cấu trúc dữ liệu HĐH dùng để lưu thông tin quản lý từng tiến trình.)
- **핵심 키워드 (Từ khóa)**: 프로세스 상태 (Trạng thái tiến trình), 식별자 (PID), 우선순위 (Priority).
- **시험 포인트 (Điểm thi)**: 프로세스 생성 시 고유하게 생성되며, 종료 시 제거됨. (Được tạo ra duy nhất khi tiến trình bắt đầu và bị xóa khi kết thúc.)

Các bullet của **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **TẦNG B – NOTE 보충 (HIỂU SÂU)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **TẦNG B – NOTE 보충 (HIỂU SÂU)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### TẦNG B – NOTE 보충 (HIỂU SÂU)

Phần nguồn của **TẦNG B – NOTE 보충 (HIỂU SÂU)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “TẦNG B – NOTE 보충 (HIỂU SÂU)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 현재 상태(준비/실행/대기), CPU 레지스터 정보, 자원 정보 포함. (Chứa trạng thái hiện tại, thanh ghi CPU, tài nguyên được cấp.)
- 문맥 교환(Context Switching) 시, 현재까지 진행 상황을 PCB에 저장. (Khi chuyển đổi ngữ cảnh, lưu tiến độ vào PCB để sau này chạy tiếp.)
- **예시 (Ví dụ)**: 병원에서 환자(프로세스)마다 차트(PCB)를 만들어 병력과 현재 상태를 기록하는 것과 같음. 퇴원하면 차트를 닫음. (Giống như Bệnh án (PCB) của từng bệnh nhân (Process), ghi lại tình trạng, xuất viện thì đóng hồ sơ.)
- 💡 **Mẹo ghi nhớ**: PCB giống như "Thẻ căn cước + Hồ sơ bệnh án" của một tiến trình.

Các ý về **TẦNG B – NOTE 보충 (HIỂU SÂU)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Điểm chốt của **TẦNG B – NOTE 보충 (HIỂU SÂU)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Khép lại **298. PCB (Process Control Block)**, điều cần giữ lại là mối quan hệ giữa mục đích, cơ chế và điểm giới hạn của các khái niệm trong nguồn. Khi ôn lại, hãy tự giải thích chúng bằng một câu hoàn chỉnh rồi đối chiếu với các điểm dễ nhầm trước khi chuyển sang bài tổng hợp của môn.