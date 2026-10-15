# 11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)

## 학습 목표 (Mục tiêu)
- Nắm vững bản chất và mục đích tổng quát của thiết kế cơ sở dữ liệu (데이터베이스 설계).
- So sánh nhanh và nhận diện chính xác phạm vi hoạt động của 4 giai đoạn thiết kế chính: Yêu cầu (`요구조건 분석`), Khái niệm (`개념적 설계`), Logic (`논리적 설계`), và Vật lý (`물리적 설계`).
- Phân biệt các đặc tính kỹ thuật cốt lõi dễ thi: Độc lập DBMS vs Phụ thuộc DBMS; Vị trí của Chuẩn hóa (Normalization); Vị trí của Access Path và Index.

## 핵심 키워드 (Từ khóa)
- 데이터베이스 설계 (Thiết kế cơ sở dữ liệu / Database Design)
- 요구조건 분석 (Phân tích yêu cầu / Requirements Analysis)
- 개념적 설계 (Thiết kế khái niệm / Conceptual Design)
- 논리적 설계 (Thiết kế logic / Logical Design)
- 물리적 설계 (Thiết kế vật lý / Physical Design)
- 정규화 (Chuẩn hóa / Normalization)
- 접근 경로 (Đường dẫn truy cập / Access Path)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([01-bai-hoc.md](01-bai-hoc.md) - [04-bai-hoc.md](04-bai-hoc.md)):** Sau khi đã khảo sát các bước kỹ thuật chi tiết, bài học này cung cấp góc nhìn tổng hợp đối chiếu dạng bảng, giúp củng cố phản xạ nhận diện câu hỏi trắc nghiệm tổng hợp về thiết kế CSDL.
- **Tiếp nối sang bài sau ([06-bai-hoc.md](06-bai-hoc.md)):** Sau khi nắm vững khung thiết kế, bài kế tiếp sẽ đi sâu vào 3 thành phần cốt lõi của một mô hình dữ liệu (`구조 - 연산 - 제약 조건`).

## 읽는 방법 (Cách đọc)
- Ôn tập bảng so sánh ở TẦNG A để thuộc lòng 4 giai đoạn và mẹo ghi nhớ "Yêu - Khái - Lo - Vật".
- Đọc TẦNG B để hiểu rõ tại sao sai sót ở giai đoạn đầu (yêu cầu, khái niệm) lại gây thiệt hại lớn gấp hàng chục lần so với sai sót ở giai đoạn vật lý.

---

## 11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Định nghĩa):** Là toàn bộ quy trình phân tích nhu cầu dữ liệu của người dùng và chuyển đổi thành cấu trúc dữ liệu lưu trữ vật lý trên hệ quản trị cơ sở dữ liệu cụ thể nhằm phục vụ khai thác thông tin hiệu quả, nhất quán và an toàn.
- **Bảng đối chiếu 4 giai đoạn thiết kế CSDL (설계 4단계 비교):**
  | 단계 (Giai đoạn) | 설명 (Mô tả & Hoạt động cốt lõi) | Giải thích tiếng Việt & Điểm thi |
  |---|---|---|
  | **1. 요구조건 분석** | 목적 파악, 요구조건 식별, 요구조건 명세서 작성 | **Phân tích yêu cầu:** Khảo sát người dùng cần quản lý dữ liệu gì. Đầu ra là Bản đặc tả yêu cầu. |
  | **2. 개념적 설계** | 개념 스키마, E-R 다이어그램, 트랜잭션 모델링 | **Thiết kế Khái niệm:** Độc lập hoàn toàn với DBMS. Vẽ sơ đồ E-R (Thực thể - Mối quan hệ). |
  | **3. 논리적 설계** | 논리 스키마, **정규화(Normalization)**, 트랜잭션 인터페이스 | **Thiết kế Logic:** Chuyển đổi E-R sang Bảng (Table). **Bắt buộc thực hiện Chuẩn hóa**. |
  | **4. 물리적 설계** | 물리적 구조, 저장 레코드 양식, **접근 경로(Access Path / Index)** | **Thiết kế Vật lý:** Cấu trúc file trên đĩa cứng, tạo Index, tối ưu hiệu năng (Response time, Throughput). |
- **시험 포인트 (Điểm thi trọng tâm):**
  - **Điểm ăn điểm 1:** Chuẩn hóa (`정규화`) luôn diễn ra ở **Thiết kế Logic**.
  - **Điểm ăn điểm 2:** Tạo chỉ mục (`인덱스`), đường dẫn truy cập (`접근 경로`), gom cụm bản ghi (`레코드 집중`) luôn thuộc **Thiết kế Vật lý**.
  - **Điểm ăn điểm 3:** Mô hình E-R (`E-R 모델`) luôn là sản phẩm của **Thiết kế Khái niệm**.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - Đề thi hay hỏi: *"Giai đoạn nào độc lập với hệ quản trị CSDL (DBMS 독립적)?"* → Đáp án là **개념적 설계 (Thiết kế Khái niệm)**.
  - Đề hỏi: *"Giai đoạn nào phụ thuộc vào phần cứng và thiết bị lưu trữ cụ thể?"* → Đáp án là **물리적 설계 (Thiết kế Vật lý)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Yêu - Khái - Lo - Vật" (Yêu cầu nắm ý, Khái niệm vẽ E-R, Logic tạo bảng & chuẩn hóa, Vật lý làm đĩa & index).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tầm quan trọng của chi phí sửa lỗi qua các giai đoạn:**
  - Nếu phân tích sai ở bước **Yêu cầu** hoặc **Khái niệm**, khi hệ thống đã đi đến bước Vật lý hoặc Cài đặt (Implementation) thì chi phí đập đi xây lại cấu trúc bảng là cực kỳ lớn. Do đó, việc mô hình hóa khái niệm cẩn thận giúp bảo vệ toàn bộ kiến trúc dữ liệu lâu dài.
- **Phân định rõ ranh giới giữa Logic và Vật lý:**
  - Ở tầng **Logic**, nhà thiết kế chỉ quan tâm dữ liệu có bị lặp lại không, khóa chính là gì, bảng liên kết ra sao để không bị bất thường khi Insert/Update/Delete (bằng phương pháp chuẩn hóa từ 1NF đến BCNF).
  - Sang tầng **Vật lý**, DBA mới bắt đầu tính toán xem bảng đó có bao nhiêu triệu dòng, mỗi ngày có bao nhiêu nghìn lượt query, cần ổ đĩa RAID mấy, đánh index trên cột nào để query trả về dưới 100ms.
- **Liên hệ mạch kiến thức:**
  - Khung 4 giai đoạn này là nền tảng xuyên suốt toàn bộ Môn 3. Các bài tiếp theo sẽ bóc tách chi tiết từng thành phần: Cấu trúc mô hình dữ liệu (Bài 06), Mô hình quan hệ (Bài 07-08), Ký hiệu sơ đồ E-R (Bài 09-10).

### 복습 체크리스트
- [ ] Kể tên tuần tự 4 giai đoạn thiết kế CSDL: 요구조건 분석 → 개념적 설계 → 논리적 설계 → 물리적 설계.
- [ ] Chỉ ra đúng giai đoạn thực hiện chuẩn hóa (정규화).
- [ ] Chỉ ra đúng giai đoạn thiết lập đường dẫn truy cập (접근 경로/인덱스).
- [ ] Phân biệt được tính độc lập DBMS ở tầng khái niệm so với tính phụ thuộc phần cứng ở tầng vật lý.
