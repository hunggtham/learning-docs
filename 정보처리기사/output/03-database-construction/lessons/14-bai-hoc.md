# 14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **115. 무결성 (Integrity)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **5. 스키마 (Schema - Lược đồ)**에서 만든 기준을 이어받아 **14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)** và nối nó với **115. 무결성 (Integrity)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)

Sau khi đã đặt nền bằng **5. 스키마 (Schema - Lược đồ)**, ta chuyển sang **14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)**. Đây là mắt xích 14/56 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **키(Key) 종류 (Các loại Khóa)**. Hãy xác định **키(Key) 종류 (Các loại Khóa)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 키(Key) 종류 (Các loại Khóa)

Phần nguồn của **키(Key) 종류 (Các loại Khóa)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

| 종류 (Loại) | 설명 (Mô tả) | Tính chất (VN) |
|---|---|---|
| **슈퍼키 (Super Key)** | 튜플을 구별할 수 있는 속성 집합. | **Tính duy nhất (유일성).** |
| **후보키 (Candidate Key)** | 기본키가 될 수 있는 키 (유일성 + 최소성). | **Duy nhất + Tối thiểu (최소성).** (Không dư thừa thuộc tính). |
| **기본키 (Primary Key)** | 후보키 중 선택된 주키. NULL 불가. | Khóa chính. **Không được trùng, Không được NULL.** |
| **대체키 (Alternate Key)** | 기본키로 선택되지 못한 나머지 후보키. | Khóa thay thế (Khóa phụ). |
| **외래키 (Foreign Key)** | 다른 릴레이션의 기본키를 참조하는 속성. | Khóa ngoại. Dùng để liên kết 2 bảng. |

Bảng trong **키(Key) 종류 (Các loại Khóa)** không phải danh sách rời. Hãy đọc theo từng cột để nhận ra tiêu chí so sánh, rồi tự diễn đạt bằng một câu: đối tượng nào khác nhau ở điểm nào và trong điều kiện nào sự khác biệt đó có ý nghĩa.

Ta vừa chốt **키(Key) 종류 (Các loại Khóa)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **무결성 (Integrity - Tính toàn vẹn / chính xác)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **무결성 (Integrity - Tính toàn vẹn / chính xác)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 무결성 (Integrity - Tính toàn vẹn / chính xác)

Các ý ngay dưới **무결성 (Integrity - Tính toàn vẹn / chính xác)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **개체 무결성 (Entity):** Khóa chính (Primary Key) không được trùng lặp và **không được NULL**.
- **참조 무결성 (Referential):** Khóa ngoại (Foreign Key) phải khớp với Khóa chính của bảng tham chiếu, hoặc có thể là NULL.
- **도메인 무결성 (Domain):** Giá trị phải nằm trong phạm vi định nghĩa (ví dụ: Giới tính chỉ là Nam/Nữ).
- **사용자 정의 무결성 (User-defined):** Phải thỏa mãn các điều kiện do người dùng tự định nghĩa.

---

Các ý về **무결성 (Integrity - Tính toàn vẹn / chính xác)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Điểm chốt của **무결성 (Integrity - Tính toàn vẹn / chính xác)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **115. 무결성 (Integrity)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.