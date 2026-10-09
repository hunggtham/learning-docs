# 088-2: 데이터베이스 (Database) & 089: DBMS

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **088-2: 데이터베이스 (Database) & 089: DBMS**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối database với DBMS, storage, query, transaction và authorization, để hệ quản trị được đọc qua các trách nhiệm.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **088-2: 데이터베이스 (Database) & 089: DBMS**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **088-2: 데이터베이스 (Database) & 089: DBMS** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **090-1: 데이터의 독립성 (Data Independence)** khi chuyển sang phần tiếp theo.

Mục tiêu vừa đặt database và DBMS vào cùng câu hỏi về tổ chức, truy vấn và kiểm soát dữ liệu. Phần **핵심 키워드 (Từ khóa)** sau đây giữ lại thuật ngữ trung tâm trước khi phân biệt đặc trưng của database với trách nhiệm của DBMS.

## 핵심 키워드 (Từ khóa)

데이터베이스

Từ khóa trên gọi tên kho dữ liệu, còn phần **선행·연결 개념 (Kiến thức liên kết)** sẽ nối nó với kỹ thuật reuse ở bài trước để làm rõ khi nào dữ liệu và phần mềm quản lý có thể được dùng lại mà vẫn giữ quy tắc.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)**에서 만든 기준을 이어받아 **088-2: 데이터베이스 (Database) & 089: DBMS**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

Sau khi nối database với tiêu chí tái sử dụng và kiểm soát, **읽는 방법 (Cách đọc)** sẽ hướng dẫn tách đối tượng, chức năng và hệ quả, để không trộn lẫn đặc trưng của database với chức năng của DBMS.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

Với trình tự đọc vừa xác lập, phần **088-2: 데이터베이스 (Database) & 089: DBMS** lần lượt giải thích bốn đặc trưng của database và ba nhóm chức năng của DBMS. Hãy giữ ranh giới giữa dữ liệu và phần mềm quản lý khi chuyển sang data independence.

## 088-2: 데이터베이스 (Database) & 089: DBMS

Từ **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)**, ta đã có điểm tựa để bước vào **088-2: 데이터베이스 (Database) & 089: DBMS**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 93/101 trước khi đi vào chi tiết.

Để đọc **088-2: 데이터베이스 (Database) & 089: DBMS** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **데이터베이스의 4가지 특징 (ISOS - 4 Đặc trưng của DB)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 데이터베이스의 4가지 특징 (ISOS - 4 Đặc trưng của DB)

Các ý ngay dưới **데이터베이스의 4가지 특징 (ISOS - 4 Đặc trưng của DB)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để xác nhận cách hiểu.

Phần “데이터베이스의 4가지 특징 (ISOS - 4 Đặc trưng của DB)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **통합된 데이터 (Integrated Data):** 중복 배제 (Không trùng lặp).
- **저장된 데이터 (Stored Data):** 저장 매체에 저장 (Lưu trên máy tính).
- **운영 데이터 (Operational Data):** 반드시 필요한 고유 업무 자료 (Dữ liệu bắt buộc phải có để tổ chức hoạt động, không phải rác).
- **공용 데이터 (Shared Data):** 공동으로 소유 (Nhiều người/app dùng chung).

Các bullet của **데이터베이스의 4가지 특징 (ISOS - 4 Đặc trưng của DB)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **데이터베이스의 4가지 특징 (ISOS - 4 Đặc trưng của DB)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **DBMS (Database Management System)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **DBMS (Database Management System)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### DBMS (Database Management System)

Bây giờ ta đi vào nội dung của **DBMS (Database Management System)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “DBMS (Database Management System)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 소프트웨어 (Là phần mềm quản lý DB, ví dụ: MySQL, Oracle).
- **3대 기능 (3 Chức năng chính):**
  - **정의 (Definition / DDL):** Tạo cấu trúc, bảng (Table).
  - **조작 (Manipulation / DML):** Thêm, sửa, xóa, tìm kiếm (CRUD).
  - **제어 (Control / DCL):** Bảo mật, phân quyền, tính toàn vẹn.

- 💡 **Mẹo ghi nhớ (Mnemonics):** ISOS (Integrated, Stored, Operational, Shared) - Nhớ chữ O = Operational (Vận hành/Thiết yếu). DBMS có 3 chữ D-M-C (Định nghĩa, Thao tác, Điều khiển).

---

Với **DBMS (Database Management System)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **DBMS (Database Management System)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **088-2: 데이터베이스 (Database) & 089: DBMS** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **090-1: 데이터의 독립성 (Data Independence)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **088-2: 데이터베이스 (Database) & 089: DBMS**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
