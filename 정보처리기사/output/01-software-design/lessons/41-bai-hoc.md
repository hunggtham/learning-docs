# 4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối relational database structure với table, key, constraint và relation, để cấu trúc logic gắn với dữ liệu thật.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **5. 관계 데이터 연산 및 정규화 (Phép toán quan hệ & Chuẩn hóa)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

관계형, 데이터베이스, 구조

> **Chuyển mạch:** Ở chặng này của **4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **14. 미들웨어 (Middleware)**에서 만든 기준을 이어받아 **4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)**, **4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)

Sau khi đã đặt nền bằng **14. 미들웨어 (Middleware)**, ta chuyển sang **4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)**. Đây là mắt xích 41/69 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **릴레이션 (Relation / Table) 구성 요소**. Hãy xác định **릴레이션 (Relation / Table) 구성 요소** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 릴레이션 (Relation / Table) 구성 요소

Phần nguồn của **릴레이션 (Relation / Table) 구성 요소** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “릴레이션 (Relation / Table) 구성 요소” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **튜플 (Tuple):** 행(Row), 레코드(Record).
  - 튜플의 수 = **카디널리티 (Cardinality)** = 기수. (Số lượng dòng).
- **속성 (Attribute):** 열(Column), 필드(Field).
  - 속성의 수 = **디그리 (Degree)** = 차수. (Số lượng cột).
- **도메인 (Domain):** 하나의 속성이 취할 수 있는 같은 타입의 원자값들의 집합. (Tập hợp các giá trị hợp lệ của 1 cột. VD: Cột 'Giới tính' có Domain là 'Nam' và 'Nữ').
- 💡 **Mẹo ghi nhớ (Mnemonic):** **TCTD** (Tuple-Card, Thuộc-Deg): **Tính Cẩn Thận Đi** -> Tuple đi với Cardinality, Cột(속성) đi với Degree.

Với **릴레이션 (Relation / Table) 구성 요소**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **릴레이션 (Relation / Table) 구성 요소** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **릴레이션의 4가지 특징 (4 Đặc trưng của Bảng quan hệ)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **릴레이션의 4가지 특징 (4 Đặc trưng của Bảng quan hệ)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 릴레이션의 4가지 특징 (4 Đặc trưng của Bảng quan hệ)

Các ý ngay dưới **릴레이션의 4가지 특징 (4 Đặc trưng của Bảng quan hệ)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “릴레이션의 4가지 특징 (4 Đặc trưng của Bảng quan hệ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 튜플의 유일성: 한 릴레이션에 포함된 튜플들은 모두 상이하다. (Không có 2 dòng nào hoàn toàn giống nhau).
- 튜플의 무순서: 튜플 사이에는 순서가 없다. (Thứ tự các dòng không quan trọng).
- 속성의 무순서: 속성들 간의 순서는 중요하지 않다. (Thứ tự các cột không quan trọng).
- 속성값의 원자성: 속성은 더 이상 쪼갤 수 없는 원자값만 저장한다. (Giá trị mỗi ô phải là nguyên tử, không chứa mảng hay list).

Các bullet của **릴레이션의 4가지 특징 (4 Đặc trưng của Bảng quan hệ)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **릴레이션의 4가지 특징 (4 Đặc trưng của Bảng quan hệ)**, đừng bắt đầu lại từ số không. **키(Key)의 종류 (Các loại Khóa)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **키(Key)의 종류 (Các loại Khóa)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 키(Key)의 종류 (Các loại Khóa)

Bây giờ ta đi vào nội dung của **키(Key)의 종류 (Các loại Khóa)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “키(Key)의 종류 (Các loại Khóa)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **후보키 (Candidate Key):** 튜플을 유일하게 식별하기 위해 사용하는 속성. **유일성**과 **최소성**을 모두 만족해야 함. (Khóa ứng viên: Duy nhất và Ít thuộc tính nhất).
- **기본키 (Primary Key - PK):** 후보키 중에서 선택한 주키. NULL 값을 가질 수 없고 중복 불가. (Khóa chính: Chọn từ Candidate Key, cấm NULL).
- **대체키 (Alternate Key):** 후보키가 둘 이상일 때 기본키를 제외한 나머지 후보키. (Khóa thay thế: Khóa ứng viên không được chọn làm PK).
- **슈퍼키 (Super Key):** 튜플을 구별할 수 있는 속성들의 집합. 유일성은 만족하지만, 최소성은 만족하지 않음. (Siêu khóa: Gom nhiều cột lại để phân biệt, dư thừa cột cũng không sao).
- **외래키 (Foreign Key - FK):** 참조되는 릴레이션의 기본키와 대응되는 속성. (Khóa ngoại: Dùng để liên kết 2 bảng).

Các bullet của **키(Key)의 종류 (Các loại Khóa)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**키(Key)의 종류 (Các loại Khóa)** vừa cho ta cách đặt câu hỏi. Bây giờ **무결성 (Integrity / Tính toàn vẹn) 제약조건** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **무결성 (Integrity / Tính toàn vẹn) 제약조건**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 무결성 (Integrity / Tính toàn vẹn) 제약조건

Phần nguồn của **무결성 (Integrity / Tính toàn vẹn) 제약조건** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “무결성 (Integrity / Tính toàn vẹn) 제약조건” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개체 무결성 (Entity Integrity):** 기본키는 NULL이나 중복값을 가질 수 없다. (PK không được NULL hoặc trùng lặp).
- **참조 무결성 (Referential Integrity):** 외래키 값은 NULL이거나 참조 릴레이션의 기본키 값과 동일해야 한다. (FK phải có giá trị tồn tại trong PK bảng mẹ, hoặc NULL).
- **도메인 무결성 (Domain Integrity):** 특정 속성의 값이 그 속성이 정의된 도메인에 속한 값이어야 한다. (Giá trị phải nằm trong khoảng/định dạng hợp lệ).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **TTD** (Thực - Tham - Domain): **Thích Thì Dùng**.

Các bullet của **무결성 (Integrity / Tính toàn vẹn) 제약조건** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **무결성 (Integrity / Tính toàn vẹn) 제약조건**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Ta có thể khép mục **4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **5. 관계 데이터 연산 및 정규화 (Phép toán quan hệ & Chuẩn hóa)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
