# 22. 기타 주요 개념 (Các khái niệm quan trọng khác)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **22. 기타 주요 개념 (Các khái niệm quan trọng khác)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **22. 기타 주요 개념 (Các khái niệm quan trọng khác)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **phần tổng hợp của môn** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

기타, 주요, 개념

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)**에서 만든 기준을 이어받아 **22. 기타 주요 개념 (Các khái niệm quan trọng khác)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 22. 기타 주요 개념 (Các khái niệm quan trọng khác)

Ở bước 55/55, **22. 기타 주요 개념 (Các khái niệm quan trọng khác)** xuất hiện như phần tiếp nối của **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **22. 기타 주요 개념 (Các khái niệm quan trọng khác)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **CRUD 분석 (Phân tích CRUD)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **CRUD 분석 (Phân tích CRUD)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### CRUD 분석 (Phân tích CRUD)

Bây giờ ta đi vào nội dung của **CRUD 분석 (Phân tích CRUD)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- Tạo ma trận (Matrix) giữa **Process (Tiến trình)** và **Table (Bảng)**.
- Đánh dấu **C**reate, **R**ead, **U**pdate, **D**elete để xem bảng nào bị thao tác nhiều/ít, phát hiện bảng bị bỏ sót (ít nhất mỗi bảng phải có 1 thao tác).

Các bullet của **CRUD 분석 (Phân tích CRUD)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **CRUD 분석 (Phân tích CRUD)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **MyBatis (프레임워크)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **MyBatis (프레임워크)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### MyBatis (프레임워크)

Phần nguồn của **MyBatis (프레임워크)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- Khung làm việc (Framework) giúp đơn giản hóa JDBC trong Java.
- **Đặc điểm:** Tách mã SQL ra khỏi mã Java (lưu trong file XML hoặc Annotation), thân thiện với lập trình viên SQL.

Các bullet của **MyBatis (프레임워크)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **MyBatis (프레임워크)**, đừng bắt đầu lại từ số không. **시스템 카탈로그 (System Catalog)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **시스템 카탈로그 (System Catalog)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 시스템 카탈로그 (System Catalog)

Các ý ngay dưới **시스템 카탈로그 (System Catalog)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **Định nghĩa:** CSDL đặc biệt chứa "dữ liệu về dữ liệu" (Metadata / Data Dictionary).
- **Đặc điểm:** Chỉ có hệ thống (DBMS) mới được quyền cập nhật (Tự động cập nhật). Người dùng chỉ có quyền **SELECT (Đọc)**.

Các bullet của **시스템 카탈로그 (System Catalog)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**시스템 카탈로그 (System Catalog)** vừa cho ta cách đặt câu hỏi. Bây giờ **연산자 우선순위 (Thứ tự ưu tiên toán tử trong SQL)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **연산자 우선순위 (Thứ tự ưu tiên toán tử trong SQL)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 연산자 우선순위 (Thứ tự ưu tiên toán tử trong SQL)

Bây giờ ta đi vào nội dung của **연산자 우선순위 (Thứ tự ưu tiên toán tử trong SQL)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 산술 연산자 (Toán học: `* / + -`) **>** 관계 연산자 (So sánh: `< > = !=`) **>** 논리 연산자 (Logic: `NOT > AND > OR`).

> 💡 **Mẹo ghi nhớ:** **Toán - Quan - Lo** (Toán học - Quan hệ - Logic). Nhân chia trước, cộng trừ sau, rồi đến so sánh, cuối cùng là AND/OR.

EOF

Với **연산자 우선순위 (Thứ tự ưu tiên toán tử trong SQL)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **연산자 우선순위 (Thứ tự ưu tiên toán tử trong SQL)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Khép lại **22. 기타 주요 개념 (Các khái niệm quan trọng khác)**, điều cần giữ lại là mối quan hệ giữa mục đích, cơ chế và điểm giới hạn của các khái niệm trong nguồn. Khi ôn lại, hãy tự giải thích chúng bằng một câu hoàn chỉnh rồi đối chiếu với các điểm dễ nhầm trước khi chuyển sang bài tổng hợp của môn.