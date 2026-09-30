# 프로그래밍 언어 기초 (Mở rộng) (Programming Language Basics - Extended)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **프로그래밍 언어 기초 (Mở rộng) (Programming Language Basics - Extended)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **프로그래밍 언어 기초 (Mở rộng) (Programming Language Basics - Extended)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

프로그래밍, 언어, 기초

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **프로그래밍 언어 기초 (Programming Language Basics)**에서 만든 기준을 이어받아 **프로그래밍 언어 기초 (Mở rộng) (Programming Language Basics - Extended)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **프로그래밍 언어 기초 (Mở rộng) (Programming Language Basics - Extended)** và nối nó với **072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

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