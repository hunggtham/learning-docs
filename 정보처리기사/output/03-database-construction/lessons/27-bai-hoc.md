# 3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)

> **Mạch đọc:** [README](../README.md) là owner của **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)**; giữ bài trong tuyến database language trước các loại cú pháp SQL và transaction. Từ **학습 목표 (Mục tiêu)** sang **핵심 키워드 (Từ khóa)**, nối relational data với procedural control flow, variables, functions/procedures, triggers và transaction boundaries, rồi dùng **선행·연결 개념 (Kiến thức liên kết)** để thấy khi nào logic nên ở database hay application.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **4. SQL 문법의 종류 (Các loại cú pháp SQL)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

데이터베이스와, 절차형, SQL

> **Chuyển mạch:** Ở chặng này của **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **143-145. SQL 분류 (SQL Categories)**에서 만든 기준을 이어받아 **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)**, **읽는 방법 (Cách đọc)** nêu điều cần giải thích; **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)

Từ **143-145. SQL 분류 (SQL Categories)**, ta đã có điểm tựa để bước vào **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 27/54 trước khi đi vào chi tiết.

Để đọc **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 종류 (Loại) | 설명 (Mô tả) | Ví dụ & Giải thích (VN) |
|---|---|---|
| **트리거 (Trigger)** | 테이블 이벤트(Insert, Update, Delete)에 반응해 **자동**으로 실행되는 작업. (Thực thi tự động khi có sự kiện). | _Ví dụ:_ Khi xóa 1 nhân viên khỏi bảng NhânViên, một trigger tự động lưu thông tin nhân viên đó vào bảng NhanVien_NghiViec (Audit log). |
| **프로시저 (Procedure)** | 어떤 행동을 수행하기 위한 일련의 작업 순서. (Một chuỗi các thao tác lưu sẵn để thực thi chung). | _Ví dụ:_ Một procedure `Tinh_Luong_Thang` chạy cuối tháng để tính lương cho toàn bộ công ty. |
| **사용자 정의 함수 (User-Defined Function)** | 단일 값으로 반환할 수 있도록 수행. (Hàm do người dùng định nghĩa, trả về một giá trị duy nhất). | _Ví dụ:_ Hàm `GET_AGE(ngay_sinh)` tự động tính và trả về tuổi. |

---

Điểm chốt của **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **4. SQL 문법의 종류 (Các loại cú pháp SQL)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
