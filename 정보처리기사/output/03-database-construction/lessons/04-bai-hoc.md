# 163-167. 데이터베이스 설계 순서 (Database Design Process)

## 학습 목표 (Mục tiêu)
- Nắm vững trình tự 5 giai đoạn phát triển cơ sở dữ liệu: `요구 조건 분석 → 개념적 설계 → 논리적 설계 → 물리적 설계 → 구현`.
- Phân biệt rõ nhiệm vụ và sản phẩm đầu ra của từng giai đoạn để trả lời chính xác các câu hỏi sắp xếp thứ tự và phân loại hoạt động trong đề thi.
- Nắm vững câu hỏi bẫy kinh điển về tính độc lập công nghệ qua từng bước (độc lập DBMS vs phụ thuộc DBMS vs phụ thuộc phần cứng).

## 핵심 키워드 (Từ khóa)
- 데이터베이스 설계 순서 (Trình tự thiết kế CSDL / Database Design Process)
- 요구 조건 분석 (Phân tích yêu cầu / Requirements Analysis)
- 개념적 설계 (Thiết kế khái niệm / Conceptual Design)
- 논리적 설계 (Thiết kế logic / Logical Design)
- 물리적 설계 (Thiết kế vật lý / Physical Design)
- 구현 (Cài đặt / Implementation)
- DDL (Ngôn ngữ định nghĩa dữ liệu / Data Definition Language)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([101. 개념적 설계](01-bai-hoc.md), [102. 논리적 설계](02-bai-hoc.md), [103. 물리적 설계](03-bai-hoc.md)):** Sau khi đã đi qua chi tiết từng bước thiết kế riêng lẻ, bài học này đóng vai trò bản đồ tổng hợp (Bird's-eye view), kết nối các mắt xích thành một quy trình phát triển CSDL hoàn chỉnh từ yêu cầu người dùng đến hệ thống chạy thật.
- **Tiếp nối sang các bài sau ([06-bai-hoc.md](06-bai-hoc.md)):** Sau khi nắm vững toàn cảnh quy trình, ta sẽ đi sâu vào các yếu tố chi tiết của mô hình dữ liệu (cấu trúc, ràng buộc toàn vẹn) và chi tiết lược đồ quan hệ.

## 읽는 방법 (Cách đọc)
- Học thuộc câu thần chú ghi nhớ: **"Yêu - Khái - Lo - Vật - Cài"** (Yêu cầu → Khái niệm → Logic → Vật lý → Cài đặt).
- Bám sát bảng đối chiếu ở TẦNG A để biết chính xác từng sản phẩm (Artifact) thuộc về bước nào.

---

## 163-167. 데이터베이스 설계 순서 (Database Design Process)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Định nghĩa):** Là quy trình kỹ thuật gồm 5 giai đoạn liên tiếp nhằm chuyển đổi nhu cầu lưu trữ và quản lý thông tin của tổ chức thành một cơ sở dữ liệu hoạt động ổn định, hiệu năng cao trên máy tính.
- **5 giai đoạn chuẩn theo đề thi (설계 5단계 순서):**
  1. **요구 조건 분석 (Phân tích yêu cầu):** Thu thập nhu cầu người dùng, phân tích quy trình nghiệp vụ và lập Bản đặc tả yêu cầu (`요구 조건 명세서`).
  2. **개념적 설계 (Thiết kế khái niệm - 164):** Trừu tượng hóa thế giới thực thành Sơ đồ E-R (`E-R 다이어그램`), mô hình hóa giao dịch, **độc lập hoàn toàn với DBMS (`DBMS 독립적`)**.
  3. **논리적 설계 (Thiết kế logic - 165):** Ánh xạ sơ đồ E-R sang bảng/lược đồ logic (`논리 스키마`), thiết kế giao diện giao dịch, **thực hiện Chuẩn hóa (`정규화`)**. Phụ thuộc mô hình DBMS nhưng độc lập phần cứng lưu trữ.
  4. **물리적 설계 (Thiết kế vật lý - 166):** Chuyển đổi sang cấu trúc lưu trữ trên đĩa, thiết kế định dạng bản ghi lưu trữ (`저장 레코드 양식`), đường dẫn truy cập (`인덱스/액세스 경로`), phân tích gom nhóm (`레코드 집중`). Phụ thuộc cụ thể vào DBMS và phần cứng.
  5. **구현 (Cài đặt / Triển khai):** Sử dụng ngôn ngữ định nghĩa dữ liệu (`DDL`) của DBMS mục tiêu để tạo bảng, tạo index, view và nạp dữ liệu thật.
- **시험 포인트 (Điểm thi trọng tâm):**
  - **Bảng đối chiếu nhiệm vụ và sản phẩm đầu ra:**
    | Giai đoạn | Hành động cốt lõi | Sản phẩm đầu ra (Artifact) | Tính phụ thuộc |
    |---|---|---|---|
    | **1. 요구조건 분석** | Phỏng vấn, khảo sát người dùng | `요구 조건 명세서` | Độc lập hoàn toàn |
    | **2. 개념적 설계** | E-R Modeling + Transaction Modeling | `개념 스키마` (E-R 다이어그램) | Độc lập DBMS & Phần cứng |
    | **3. 논리적 설계** | Ánh xạ E-R sang Table + Chuẩn hóa | `논리 스키마` (Bảng quan hệ) | Phụ thuộc DBMS, độc lập Phần cứng |
    | **4. 물리적 설계** | Quyết định lưu trữ đĩa + Index | `물리 스키마` (Cấu trúc file/index) | Phụ thuộc cả DBMS và Phần cứng |
    | **5. 구현** | Viết code DDL, tạo DB | Database thật chạy trên server | Hiện thực hóa trên máy chủ |
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** Tráo đổi thứ tự Logic và Vật lý: Đề thi thường đưa ra thứ tự sai như `개념적 → 물리적 → 논리적` để lừa thí sinh. Nhớ rõ: **Phải Logic (tạo bảng) xong rồi mới Vật lý (lưu xuống đĩa)**.
  - **Bẫy 2:** Vị trí của Chuẩn hóa: Luôn nhớ **Chuẩn hóa (정규화) thuộc bước 논리적 설계**.
  - **Bẫy 3:** Vị trí của DDL: Việc sinh code DDL để tạo DB thuộc bước **구현 (Implementation)**, không phải bước thiết kế.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Yêu - Khái - Lo - Vật - Cài" (Yêu cầu làm rõ, Khái niệm vẽ E-R, Logic tạo bảng, Vật lý làm đĩa, Cài đặt gõ DDL).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cơ chế chuyển tiếp giữa các tầng:**
  - Quy trình này đi từ **mức độ trừu tượng cao nhất** (suy nghĩ của con người) xuống **mức độ cụ thể nhất** (các bit 0 và 1 trên đĩa cứng từ tính/SSD).
  - Nếu phát hiện lỗi thiết kế ở bước sau, ta phải quay lại (feedback loop) bước trước đó để hiệu chỉnh: ví dụ khi chạy thử ở bước Cài đặt thấy truy vấn quá chậm, DBA có thể quay lại bước Thiết kế vật lý để thêm Index hoặc gom cụm bản ghi (clustering); nếu bảng vẫn bị trùng lặp dữ liệu, phải quay lại bước Thiết kế logic để chuẩn hóa lại.
- **Ví dụ chuỗi phát triển một tính năng:**
  1. *Yêu cầu:* "Hệ thống cần lưu lại thông tin sinh viên và các môn sinh viên đã thi đậu."
  2. *Khái niệm:* Vẽ thực thể `SinhVien`, thực thể `MonHoc`, và quan hệ `KetQuaThi`.
  3. *Logic:* Tạo bảng `SINH_VIEN(MSSV, HoTen)`, bảng `MON_HOC(MaMH, TenMH)`, và bảng `KET_QUA(MSSV, MaMH, DiemSo)`. Chuẩn hóa đến BCNF.
  4. *Vật lý:* Chọn `MSSV` kiểu `CHAR(8)`, `DiemSo` kiểu `DECIMAL(4,2)`. Tạo Clustered Index trên cột `MSSV` để tra cứu bảng điểm sinh viên siêu tốc.
  5. *Cài đặt:* Mở terminal PostgreSQL, gõ `CREATE TABLE KET_QUA (...)` và `CREATE INDEX ...`.

### 복습 체크리스트
- [ ] Đọc vanh vách 5 bước thiết kế CSDL: 요구 조건 분석 → 개념적 설계 → 논리적 설계 → 물리적 설계 → 구현.
- [ ] Xác định đúng giai đoạn diễn ra Chuẩn hóa (정규화 - bước Logic).
- [ ] Xác định đúng giai đoạn diễn ra tạo Index và cấu trúc lưu trữ (bước Vật lý).
- [ ] Xác định đúng giai đoạn dùng câu lệnh DDL (bước Cài đặt).
