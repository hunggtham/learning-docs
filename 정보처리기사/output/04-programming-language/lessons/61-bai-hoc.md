# 추가: 응용 SW 기초 기술 (4과목 핵심 요약 1)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **추가: 응용 SW 기초 기술 (4과목 핵심 요약 1)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **추가: 응용 SW 기초 기술 (4과목 핵심 요약 1)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **232. 배치 프로그램 (Batch Program)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

추가, 응용, 기초, 기술

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **교착상태 필요충분조건 1 - 상호배제 (Deadlock Conditions - Mutual Exclusion)**에서 만든 기준을 이어받아 **추가: 응용 SW 기초 기술 (4과목 핵심 요약 1)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 추가: 응용 SW 기초 기술 (4과목 핵심 요약 1)

Ở bước 61/77, **추가: 응용 SW 기초 기술 (4과목 핵심 요약 1)** xuất hiện như phần tiếp nối của **교착상태 필요충분조건 1 - 상호배제 (Deadlock Conditions - Mutual Exclusion)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **추가: 응용 SW 기초 기술 (4과목 핵심 요약 1)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận. Trong khối này, **필수 요소 5가지**, **C/C++**, **JAVA** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **232. 배치 프로그램 (Batch Program)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **232. 배치 프로그램 (Batch Program)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 232. 배치 프로그램 (Batch Program)

Bây giờ ta đi vào nội dung của **232. 배치 프로그램 (Batch Program)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 대량의 데이터를 사용자 개입 없이 정해진 순서에 따라 **일괄적으로 처리**하는 방식.
- 야간 시간대 등 자원 소모가 적은 시간에 실행됨.
- **필수 요소 5가지**: 대용량, 자동화, 견고성, 안정성, 성능.

**Giải thích (Vietnamese):**
Chương trình Batch (xử lý hàng loạt) là loại phần mềm tự động chạy ngầm, thường vào ban đêm. Ví dụ: Cuối ngày ngân hàng tổng hợp lại toàn bộ giao dịch trong ngày, xử lý một lúc hàng triệu giao dịch mà không cần người bấm nút.

Các ý về **232. 배치 프로그램 (Batch Program)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **232. 배치 프로그램 (Batch Program)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **233 & 235. 데이터 타입 크기 (Data Type Sizes - C/C++ vs JAVA)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **233 & 235. 데이터 타입 크기 (Data Type Sizes - C/C++ vs JAVA)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 233 & 235. 데이터 타입 크기 (Data Type Sizes - C/C++ vs JAVA)

Phần nguồn của **233 & 235. 데이터 타입 크기 (Data Type Sizes - C/C++ vs JAVA)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **C/C++**: `char`(1바이트), `short`(2바이트), `int`(4바이트), `float`(4바이트), `double`(8바이트).
- **JAVA**: `byte`(1바이트), **`char`(2바이트, 유니코드 지원)**, `int`(4바이트), `boolean`(1바이트).

**Giải thích (Vietnamese):**
Lưu ý quan trọng: Trong C, `char` (kí tự) chiếm 1 byte. Nhưng trong Java, `char` chiếm 2 byte vì Java dùng bảng mã Unicode để hỗ trợ mọi ngôn ngữ trên thế giới (kể cả tiếng Hàn, tiếng Việt).

Các bullet của **233 & 235. 데이터 타입 크기 (Data Type Sizes - C/C++ vs JAVA)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **233 & 235. 데이터 타입 크기 (Data Type Sizes - C/C++ vs JAVA)**, đừng bắt đầu lại từ số không. **234. C언어의 구조체 (struct)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **234. C언어의 구조체 (struct)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 234. C언어의 구조체 (struct)

Các ý ngay dưới **234. C언어의 구조체 (struct)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 서로 다른 데이터 타입을 하나로 묶어 관리하는 사용자 정의 자료형. 배열(동일 타입)과의 차이점.
- (Ví dụ: Một `struct SinhVien` có thể chứa Tên(string), Tuổi(int), Điểm(float)).

Các ý về **234. C언어의 구조체 (struct)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

**234. C언어의 구조체 (struct)** vừa cho ta cách đặt câu hỏi. Bây giờ **236. Python 시퀀스 자료형** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **236. Python 시퀀스 자료형**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 236. Python 시퀀스 자료형

Bây giờ ta đi vào nội dung của **236. Python 시퀀스 자료형**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 리스트(List): `[]` 변경 가능.
- 튜플(Tuple): `()` **변경 불가능(Immutable)**.
- (Ví dụ: Tuple dùng để lưu toạ độ GPS không bao giờ đổi).

Các ý về **236. Python 시퀀스 자료형** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **236. Python 시퀀스 자료형** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **238. 가비지 콜렉터 (Garbage Collector)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **238. 가비지 콜렉터 (Garbage Collector)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 238. 가비지 콜렉터 (Garbage Collector)

Phần nguồn của **238. 가비지 콜렉터 (Garbage Collector)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 사용되지 않는 메모리를 자동으로 해제해주는 기능 (메모리 누수 방지). Java 등 현대 언어의 핵심.

Các bullet của **238. 가비지 콜렉터 (Garbage Collector)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **238. 가비지 콜렉터 (Garbage Collector)**, đừng bắt đầu lại từ số không. **239 - 244. 각종 연산자** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **239 - 244. 각종 연산자** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 239 - 244. 각종 연산자

Các ý ngay dưới **239 - 244. 각종 연산자** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 산술(`%`, `++`), 관계(`==`, `!=`), 비트(`&`, `|`, `^`, `<<`), 논리(`&&`, `||`), 대입(`+=`), 조건 삼항연산자.
- `a += 1`은 `a = a + 1`과 같다.
- 비트 XOR(`^`): 두 비트가 다를 때만 1을 반환.

Với **239 - 244. 각종 연산자**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Như vậy, **239 - 244. 각종 연산자** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **추가: 응용 SW 기초 기술 (4과목 핵심 요약 1)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **232. 배치 프로그램 (Batch Program)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.