# 091-1: 절차형 SQL (Procedural SQL)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **091-1: 절차형 SQL (Procedural SQL)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối procedural SQL với control flow, cursor, transaction và database state, để logic chạy gần dữ liệu.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **091-1: 절차형 SQL (Procedural SQL)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **091-1: 절차형 SQL (Procedural SQL)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **097 & 120: 통합 개발 환경 (IDE - Integrated Development Environment)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **091-1: 절차형 SQL (Procedural SQL)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

절차형, SQL

> **Chuyển mạch:** Ở chặng này của **091-1: 절차형 SQL (Procedural SQL)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **091: 스키마 (Schema)**에서 만든 기준을 이어받아 **091-1: 절차형 SQL (Procedural SQL)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **091-1: 절차형 SQL (Procedural SQL)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **091-1: 절차형 SQL (Procedural SQL)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **091-1: 절차형 SQL (Procedural SQL)**, **091-1: 절차형 SQL (Procedural SQL)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 091-1: 절차형 SQL (Procedural SQL)

Từ **091: 스키마 (Schema)**, ta đã có điểm tựa để bước vào **091-1: 절차형 SQL (Procedural SQL)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 96/101 trước khi đi vào chi tiết.

Để đọc **091-1: 절차형 SQL (Procedural SQL)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

C, JAVA처럼 분기/반복 (If/For)이 가능한 SQL (SQL có thêm logic lập trình - PL/SQL). Bọc trong khối `BEGIN ~ END`.

| 종류 (Loại) | 특징 (Đặc điểm) | ví dụ (Ví dụ sử dụng) |
|---|---|---|
| **프로시저 (Procedure)** | Gọi thủ công (`CALL`). Thực thi một chuỗi nghiệp vụ (Insert/Update nhiều bảng). KHÔNG có `RETURN`. | Chuyển tiền (Trừ A, Cộng B). |
| **트리거 (Trigger)** | Tự động chạy khi có sự kiện (Insert/Update/Delete). KHÔNG thể gọi thủ công. | Tự động ghi log khi có người xóa dữ liệu, tự trừ số lượng kho khi có đơn hàng. |
| **사용자 정의 함수 (User Defined Function)** | Dùng trong câu `SELECT`. BẮT BUỘC có `RETURN` 1 giá trị. | Hàm tính thuế VAT 10% từ giá gốc. |

- **Vietnamese Explanation:** SQL bình thường rất phèn, chỉ biết lấy dữ liệu ra. Procedural SQL thông minh hơn. Procedure như một cuốn kịch bản bạn bắt nó diễn. Trigger như cái bẫy chuột, có chuột (sự kiện) là tự sập. Function giống hệt hàm trong Toán học, đưa X trả về Y.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Procedure = Gọi mới chạy. Trigger = Tự động (Event). Function = Trả về giá trị (Return).

Để không đọc **절차형 SQL의 테스트와 디버깅 (Testing & Debugging Procedural SQL)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 절차형 SQL의 테스트와 디버깅 (Testing & Debugging Procedural SQL)

Các ý ngay dưới **절차형 SQL의 테스트와 디버깅 (Testing & Debugging Procedural SQL)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “절차형 SQL의 테스트와 디버깅 (Testing & Debugging Procedural SQL)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 절차형 SQL은 DBMS 내부에서 직접 실행되므로, 애플리케이션과 DB 사이의 데이터 전송량을 줄일 수 있어 효율적임. (Chạy trực tiếp trong DBMS nên giảm nghẽn mạng).
- **Quy trình Test & Debug:** `CREATE` (Biên dịch) -> Sửa lỗi cú pháp -> Comment các lệnh `INSERT/UPDATE/DELETE` (Tránh làm hỏng DB thật) -> Dùng `DBMS_OUTPUT` in giá trị ra màn hình để kiểm tra -> `EXEC / CALL` -> Xác nhận kết quả.

---

Các bullet của **절차형 SQL의 테스트와 디버깅 (Testing & Debugging Procedural SQL)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **절차형 SQL의 테스트와 디버깅 (Testing & Debugging Procedural SQL)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Điểm chốt của **091-1: 절차형 SQL (Procedural SQL)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **097 & 120: 통합 개발 환경 (IDE - Integrated Development Environment)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **091-1: 절차형 SQL (Procedural SQL)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
