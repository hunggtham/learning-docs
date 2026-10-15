# CASE (Computer Aided Software Engineering)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, mục đích và các lợi ích cốt lõi của công cụ hỗ trợ công nghệ phần mềm bằng máy tính (CASE - Computer Aided Software Engineering).
- Phân loại toàn diện 3 nhóm công cụ CASE: Upper CASE (상위 CASE), Lower CASE (하위 CASE), và Integrated CASE (통합 CASE).
- Hiểu rõ vai trò hạt nhân của Kho lưu trữ trung tâm (Central Repository) trong việc quản lý tính nhất quán của toàn bộ tài sản dự án phần mềm.

## 핵심 키워드 (Từ khóa)
- **CASE 도구**: Tự động hóa các giai đoạn trong chu trình sống phát triển phần mềm (SDLC).
- **상위 CASE (Upper CASE)**: Hỗ trợ phân tích yêu cầu và thiết kế kiến trúc (DFD, ERD, Dictionary).
- **하위 CASE (Lower CASE)**: Hỗ trợ tự động sinh mã nguồn, biên dịch và kiểm thử (Code Generation, Testing).
- **통합 CASE (I-CASE)**: Tích hợp xuyên suốt vòng đời SDLC thông qua kho dữ liệu chung.
- **Repository (저장소)**: Trung tâm lưu trữ và kiểm tra tính nhất quán giữa các tài liệu kỹ thuật.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [37-bai-hoc.md](37-bai-hoc.md) (Khái niệm CASE và tái kỹ nghệ phần mềm).
- Liên kết với [67-bai-hoc.md](67-bai-hoc.md) (Tổng quan phương pháp luận phát triển phần mềm).
- Liên kết với [74-bai-hoc.md](74-bai-hoc.md) (Các mô hình vòng đời phát triển phần mềm SDLC).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh phân loại CASE trong đề thi:
  - "Hỗ trợ vẽ DFD, ERD, phân tích yêu cầu nghiệp vụ" $\rightarrow$ Chọn **상위 CASE (Upper CASE)**.
  - "Tự động sinh mã nguồn (Code Generation), kiểm thử" $\rightarrow$ Chọn **하위 CASE (Lower CASE)**.
  - "Thành phần lưu trữ thông tin chung và kiểm tra tính mâu thuẫn dữ liệu" $\rightarrow$ Chọn **Repository (정보 저장소)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Khái niệm và Lợi ích của Công cụ CASE
- **Định nghĩa**: Bộ công cụ phần mềm chuyên dụng hỗ trợ các kỹ sư tự động hóa toàn bộ hoặc một phần các hoạt động kỹ thuật trong suốt chu trình phát triển phần mềm (từ khảo sát yêu cầu, thiết kế, lập trình đến kiểm thử và bảo trì).
- **Lợi ích mang lại**:
  - **Chuẩn hóa quy trình**: Áp dụng các quy chuẩn thống nhất về ký hiệu biểu đồ và tài liệu kỹ thuật.
  - **Nâng cao năng suất và chất lượng**: Tự động hóa các thao tác thủ công lặp lại, phát hiện sớm các lỗi mâu thuẫn logic thiết kế ngay từ pha phân tích.
  - **Dễ dàng bảo trì**: Tài liệu thiết kế và mã nguồn luôn được đồng bộ hóa, tạo điều kiện thuận lợi cho việc tái sử dụng và nâng cấp.

#### 2. Phân loại 3 nhóm công cụ CASE
| Phân loại công cụ | Các pha SDLC phục vụ | Chức năng kỹ thuật chính | Sản phẩm đầu ra tiêu biểu |
| :--- | :--- | :--- | :--- |
| **상위 CASE / (Upper CASE)** | - Lập kế hoạch / - Phân tích yêu cầu / - Thiết kế kiến trúc | Vẽ lược đồ phân rã chức năng, mô hình hóa luồng dữ liệu và quan hệ thực thể, tạo từ điển dữ liệu | Biểu đồ luồng dữ liệu (DFD), Sơ đồ quan hệ thực thể (ERD), Từ điển dữ liệu (DD) |
| **하위 CASE / (Lower CASE)** | - Cài đặt mã nguồn / - Biên dịch / - Kiểm thử phần mềm | Tự động sinh khung mã nguồn (Skeleton code), kiểm tra cú pháp, gỡ lỗi (Debugging), chạy test tự động | Mã nguồn chương trình (`.c`, `.java`), Kịch bản kiểm thử, Báo cáo lỗi |
| **통합 CASE / (Integrated CASE)** | Toàn bộ chu trình SDLC (từ đầu đến cuối) | Kết nối liên thông công cụ Upper và Lower CASE thông qua một cơ sở dữ liệu dùng chung duy nhất | Toàn bộ tài liệu, mô hình và mã nguồn được đồng bộ hóa xuyên suốt dự án |

#### 3. Vai trò cốt lõi của Kho lưu trữ trung tâm (Central Repository)
- **Định nghĩa**: Cơ sở dữ liệu trung tâm trong môi trường tích hợp I-CASE, lưu giữ toàn bộ các định nghĩa đối tượng dữ liệu, biểu đồ mô hình hóa, quy tắc nghiệp vụ, mã nguồn và lịch sử sửa đổi.
- **Tính năng kiểm tra mâu thuẫn (Consistency & Contradiction Checking)**:
  - Tự động đối chiếu chéo giữa sơ đồ thiết kế và từ điển dữ liệu.
  - Cảnh báo ngay lập tức nếu một trường dữ liệu xuất hiện trên biểu đồ DFD nhưng lại chưa được định nghĩa trong từ điển dữ liệu hoặc ERD.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ kiến trúc môi trường tích hợp I-CASE
```
   [상위 CASE: Phân tích & Thiết kế]          [하위 CASE: Lập trình & Kiểm thử]
         │ (Lưu sơ đồ DFD, ERD)                     │ (Truy xuất đặc tả sinh code)
         ▼                                          ▼
   ┌──────────────────────────────────────────────────────────────────┐
   │             KHO LƯU TRỮ TRUNG TÂM (CENTRAL REPOSITORY)           │
   │  - Từ điển dữ liệu (Data Dictionary)                             │
   │  - Lược đồ cấu trúc cơ sở dữ liệu                                │
   │  - Kiểm toán tính nhất quán & Chống mâu thuẫn (Consistency Check)│
   └──────────────────────────────────────────────────────────────────┘
```

#### 2. Nguyên lý tự động sinh mã nguồn (Automatic Code Generation)
- Từ mô hình lớp UML (Class Diagram) được thiết kế bằng công cụ Upper CASE, công cụ Lower CASE có thể tự động sinh ra cấu trúc các lớp (Class), khai báo các thuộc tính (Attributes) và chữ ký phương thức (Method Signatures) bằng ngôn ngữ Java hoặc C++ tương ứng, giúp lập trình viên tiết kiệm thời gian thiết lập khung ban đầu.

---

### 복습 체크리스트
- [ ] Mục đích sử dụng chính của các công cụ CASE trong công nghệ phần mềm là gì?
- [ ] Phân biệt sự khác nhau về phạm vi phục vụ giữa 상위 CASE (Upper CASE) và 하위 CASE (Lower CASE)?
- [ ] Kho lưu trữ trung tâm (Repository) trong môi trường CASE đóng vai trò kỹ thuật gì?
- [ ] Tính năng kiểm tra tính nhất quán (Consistency Check) của CASE giúp phát hiện loại lỗi nào?
