# 103. 물리적 설계 (Physical Design)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và vai trò của thiết kế vật lý (물리적 설계) trong quy trình thiết kế cơ sở dữ liệu.
- Phân biệt rõ ranh giới giữa thiết kế khái niệm (개념적 설계), thiết kế logic (논리적 설계) và thiết kế vật lý (물리적 설계) để không mắc bẫy đề thi.
- Nhớ chính xác các hạng mục bắt buộc phải quyết định ở tầng vật lý (저장 레코드 양식, 액세스 경로/인덱스, 레코드 집중) và 3 tiêu chí đánh giá hiệu năng (반응 시간, 공간 활용도, 트랜잭션 처리량).

## 핵심 키워드 (Từ khóa)
- 물리적 구조 (Cấu trúc vật lý / Physical Structure)
- 저장 레코드 양식 (Định dạng bản ghi lưu trữ / Stored Record Format)
- 액세스 경로 (Đường dẫn truy cập / Access Path)
- 인덱스 (Chỉ mục / Index)
- 레코드 집중 / 클러스터링 (Record Clustering)
- 반응 시간 (Thời gian phản hồi / Response Time)
- 공간 활용도 (Mức độ sử dụng không gian lưu trữ / Space Utilization)
- 트랜잭션 처리량 (Thông lượng giao dịch / Transaction Throughput)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([102. 논리적 설계](02-bai-hoc.md)):** Sau khi hoàn thành thiết kế logic (chuẩn hóa bảng, xác định khóa chính/ngoại, độc lập với phần cứng), ta có lược đồ logic (Logical Schema). Nhưng lược đồ này chưa thể lưu trữ trực tiếp xuống đĩa cứng một cách tối ưu nếu không có cấu trúc vật lý.
- **Tiếp nối sang bài sau ([163-167. 데이터베이스 설계 순서](04-bai-hoc.md)):** Sau khi chốt thiết kế vật lý, hệ thống bước vào giai đoạn cài đặt (구현 - Implementation) bằng DDL để tạo cơ sở dữ liệu thật trên DBMS mục tiêu.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nắm chắc 3 từ khóa ăn điểm trong đề thi: `저장 레코드 양식`, `액세스 경로 (인덱스)`, và `3 tiêu chí đánh giá hiệu năng`.
- Đọc TẦNG B để hiểu rõ tại sao cùng một lược đồ logic nhưng khi sang tầng vật lý lại cần đánh đổi giữa không gian lưu trữ và tốc độ truy vấn, giúp giải quyết các câu hỏi tình huống trong đề thi.

---

## 103. 물리적 설계 (Physical Design)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Định nghĩa):** Là quá trình chuyển đổi cấu trúc dữ liệu logic (được xác định ở bước thiết kế logic) thành cấu trúc dữ liệu vật lý có thể lưu trữ trên các thiết bị lưu trữ thứ cấp (như ổ đĩa cứng) phù hợp với DBMS mục tiêu.
- **핵심 키워드 (Từ khóa nhận diện đề thi):**
  - `물리적 저장장치` (thiết bị lưu trữ vật lý)
  - `저장 레코드의 양식 설계` (thiết kế định dạng bản ghi lưu trữ: kiểu dữ liệu, kích thước, phân bố dữ liệu)
  - `액세스 경로 / 인덱스` (đường dẫn truy cập / index, băm)
  - `레코드 집중 (Record Clustering)` (phân tích và gom nhóm các bản ghi thường truy xuất cùng lúc vào cùng block)
- **시험 포인트 (Điểm thi trọng tâm):**
  - **Nội dung bắt buộc phải làm ở bước vật lý:**
    1. Thiết kế định dạng bản ghi lưu trữ (`저장 레코드의 양식 설계`: xác định kiểu dữ liệu, phân bố giá trị, tần suất truy cập).
    2. Phân tích và thiết kế gom nhóm bản ghi (`레코드 집중의 분석 및 설계`).
    3. Thiết kế cấu trúc lưu trữ và đường dẫn truy cập (`저장 구조 및 액세스 경로`: cấu trúc index, hashing).
  - **3 tiêu chí lựa chọn phương án thiết kế vật lý (옵션 선택 시 고려사항):**
    1. `반응 시간 (Response Time)`: Thời gian từ lúc yêu cầu thực hiện giao dịch đến khi nhận được kết quả xử lý.
    2. `공간 활용도 (Space Utilization)`: Dung lượng lưu trữ bị chiếm dụng bởi file CSDL và cấu trúc đường dẫn truy cập.
    3. `트랜잭션 처리량 (Transaction Throughput)`: Số lượng giao dịch trung bình hệ thống xử lý được trong một đơn vị thời gian (TPS).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** Đề bài hỏi *"Chuẩn hóa (정규화) thuộc bước nào?"* → **Đáp án là Thiết kế Logic (논리적 설계)**, KHÔNG PHẢI thiết kế vật lý.
  - **Bẫy 2:** Đề bài hỏi *"Sơ đồ E-R thuộc bước nào?"* → **Đáp án là Thiết kế Khái niệm (개념적 설계)**.
  - **Bẫy 3:** Tính độc lập của tầng: Thiết kế logic độc lập với phần cứng/thiết bị lưu trữ; trong khi **thiết kế vật lý phụ thuộc chặt chẽ vào phần cứng và DBMS mục tiêu cụ thể** (`특정 DBMS 및 하드웨어 종속`).
- **한 문장 설명 (Câu chốt ghi nhớ):** "Logic tạo bảng - Vật lý tạo đĩa & index" (Thiết kế vật lý là quyết định cách dữ liệu nằm trên đĩa và đường đi để tìm nó nhanh nhất).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cơ chế và các yếu tố cần cân nhắc khi thiết kế vật lý:**
  - **Phân tích xu hướng giao dịch (트랜잭션 분석):** Xem xét tỷ lệ giữa thao tác đọc (`SELECT / 참조`) và thao tác ghi (`INSERT/UPDATE/DELETE / 갱신`). Nếu ứng dụng đọc nhiều, ưu tiên tạo nhiều Index; nếu ứng dụng ghi liên tục, quá nhiều Index sẽ làm chậm quá trình ghi do phải cập nhật cây chỉ mục.
  - **Kích thước và số lượng bản ghi (레코드 크기 및 개수):** Ước tính kích thước khối (block/page size) để giảm số lần I/O đĩa.
  - **Đánh đổi cốt lõi (Trade-off):** Tối ưu `Response Time` và `Throughput` thường đòi hỏi đánh đổi `Space Utilization` (ví dụ: tạo thêm index hoặc clustering tiêu tốn thêm bộ nhớ đĩa).
- **Ví dụ đúng bản chất:**
  - Một bảng `HOC_SINH` có 1.000.000 dòng. Ở tầng Logic, ta chỉ cần biết `HOC_SINH` có các thuộc tính `ma_hs`, `ho_ten`, `ngay_sinh`. Nhưng ở tầng Vật lý, DBA quyết định trường `ma_hs` dùng kiểu `CHAR(10)`, lưu trên ổ đĩa phân vùng riêng, tạo `B+ Tree Index` trên cột `ma_hs` và gom nhóm (clustering) theo `ngay_nhap_hoc` để tối ưu hóa truy vấn tìm kiếm sinh viên theo niên khóa.
- **Liên hệ mạch kiến thức:**
  - Từ **Khái niệm (Conceptual)**: "Thế giới thực có đối tượng gì?" (Sơ đồ E-R).
  - Sang **Logic**: "Mô hình quan hệ biểu diễn đối tượng đó thành bảng và khóa thế nào?" (Bảng, Quan hệ, Chuẩn hóa).
  - Đến **Vật lý (Physical)**: "Bảng đó lưu vào block nào trên ổ cứng, dùng index nào để quét nhanh nhất?" (Lưu trữ, Access Path, Clustered Index).
  - Chuyển tiếp sang **Cài đặt (Implementation)**: Dùng lệnh DDL (`CREATE TABLE`, `CREATE INDEX`) để hiện thực hóa thiết kế vật lý trên DBMS.

### 복습 체크리스트
- [ ] Định nghĩa được 물리적 설계 là gì (chuyển đổi dữ liệu logic thành cấu trúc lưu trữ vật lý trên đĩa).
- [ ] Kể tên 3 hạng mục cốt lõi của thiết kế vật lý: 저장 레코드 양식, 레코드 집중, 액세스 경로 (인덱스).
- [ ] Phân biệt được 3 tiêu chí đánh giá hiệu năng: 반응 시간, 공간 활용도, 트랜잭션 처리량.
- [ ] Phân biệt rõ tính phụ thuộc phần cứng của 물리적 설계 so với tính độc lập của 개념적/논리적 설계.
