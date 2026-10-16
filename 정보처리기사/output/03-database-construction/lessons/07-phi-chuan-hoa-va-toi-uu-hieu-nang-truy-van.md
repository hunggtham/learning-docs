# 반정규화와 쿼리 성능 최적화 (Phi Chuẩn Hóa và Tối Ưu Hóa Hiệu Năng Truy Vấn)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm Phi chuẩn hóa (`반정규화` / `역정규화` / Denormalization) và bản chất đánh đổi kỹ thuật (Trade-off) cốt lõi giữa Tốc độ đọc (SELECT) và Chi phí ghi (INSERT, UPDATE, DELETE) cùng nguy cơ vi phạm toàn vẹn dữ liệu.
- Làm chủ 5 nhóm kỹ thuật phi chuẩn hóa: Gộp bảng 1:1 và 1:N (`테이블 통합`), Tách bảng dọc và tách bảng ngang (`테이블 분할`), Thêm cột dư thừa (`중복 속성 추가`), Thêm cột tính toán tổng hợp (`파생 속성 추가`), và Thêm bảng tổng hợp (`집계 테이블 추가`).
- Phân biệt sâu sắc cơ chế hoạt động của Bộ tối ưu hóa truy vấn (`옵티마이저` / Optimizer): Bộ tối ưu hóa theo quy tắc (RBO) vs Bộ tối ưu hóa theo chi phí (CBO).
- Nhận diện các bẫy trắc nghiệm về mục đích phi chuẩn hóa, phân vùng ngang vs dọc và vai trò của thông tin thống kê trong CBO.

## 핵심 키워드 (Từ khóa)
- 반정규화 (Phi chuẩn hóa / Denormalization / 역정규화)
- 테이블 통합 (Gộp bảng: 1:1 통합, 1:N 통합, 슈퍼/서브타입)
- 테이블 분할 (Tách bảng: 수평 분할 Horizontal vs 수직 분할 Vertical)
- 중복 속성 추가 (Thêm cột dư thừa / Redundant Attribute)
- 파생 속성 추가 (Thêm cột tính toán tổng hợp / Derived Attribute)
- 트레이드오프 (Đánh đổi: Hiệu năng Đọc SELECT vs Chi phí Ghi CUD)
- 옵티마이저 (Bộ tối ưu hóa: RBO vs CBO)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Ở [06-bat-thuong-du-lieu-phu-thuoc-ham-va-chuan-hoa-1nf-5nf.md](06-bat-thuong-du-lieu-phu-thuoc-ham-va-chuan-hoa-1nf-5nf.md), chúng ta đã phân rã quan hệ thành nhiều bảng nhỏ từ 1NF đến 5NF để triệt tiêu hoàn toàn sự dư thừa dữ liệu.
- **Đang giải quyết gì (Current Problem):** Việc chuẩn hóa quá cao khiến một truy vấn đơn giản phải kết nối (JOIN) quá nhiều bảng, làm bùng nổ số lượng thao tác đọc đĩa I/O và nghẽn CPU. Bài học này giải quyết bài toán tái cân bằng hiệu năng bằng kỹ thuật **Phi chuẩn hóa (Denormalization)** và tối ưu hóa câu lệnh thông qua **Bộ tối ưu hóa (Optimizer)**.
- **Dùng đi đâu (Forward Handoff):** Khi cấu trúc bảng đã được tinh chỉnh hiệu năng, [08-giao-dich-trang-thai-acid-va-dieu-khien-dong-thoi.md](08-giao-dich-trang-thai-acid-va-dieu-khien-dong-thoi.md) sẽ thiết lập các cơ chế đảm bảo tính toàn vẹn giao dịch (ACID) và kiểm soát đồng thời khi nhiều người dùng cùng truy xuất dữ liệu.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nắm chắc 5 kỹ thuật phi chuẩn hóa, bảng phân tích đánh đổi Đọc vs Ghi và bảng đối chiếu đối đầu RBO vs CBO.
- Đọc TẦNG B để hiểu sâu từng ca tình huống thực tế: khi nào gộp bảng 1:1, khi nào tách bảng dọc để tối ưu bộ đệm RAM và kịch bản phát sinh dị thường khi thêm cột dư thừa.

---

## 반정규화와 쿼리 성능 최적화

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Các kỹ thuật Phi chuẩn hóa cốt lõi (반정규화의 핵심 기법)

Phi chuẩn hóa (**반정규화** / Denormalization) là quá trình chủ động chấp nhận dư thừa dữ liệu có kiểm soát nhằm giảm bớt các phép JOIN phức tạp, tối ưu hóa tốc độ truy vấn đọc:

```text
[ Chuẩn hóa cao (1NF-5NF) ] ── (Join nhiều bảng, I/O chậm) ──> [ Phi chuẩn hóa (반정규화) ]
- Toàn vẹn tuyệt đối                                           - Giảm Join, đọc siêu nhanh
- Không dư thừa dữ liệu                                        - Chấp nhận dư thừa có kiểm soát
- Tốc độ đọc (SELECT) bị suy giảm                              - Đánh đổi: Ghi (CUD) chậm hơn
```

| Kỹ thuật phi chuẩn hóa | Phân loại chi tiết | Mục đích & Cơ chế kỹ thuật | Ví dụ thực tế |
| :--- | :--- | :--- | :--- |
| **1. 테이블 통합 (Gộp bảng)** | • Gộp bảng quan hệ 1:1 • Gộp bảng quan hệ 1:N • Gộp bảng Super/Sub-type | Triệt tiêu hoàn toàn phép JOIN để lấy toàn bộ dữ liệu qua 1 lần quét khối nhớ. | Gộp bảng `NHAN_VIEN` và bảng `HO_SO_LUONG` (1:1) thành một bảng duy nhất. |
| **2. 테이블 분할 (Tách bảng)** | • **수평 분할 (Ngang)**: Chia theo hàng • **수직 분할 (Dọc)**: Chia theo cột | • **Ngang**: Giảm số dòng quét đĩa theo thời gian/khu vực. • **Dọc**: Tách các cột lớn (LOB/TEXT) khỏi cột tra cứu thường xuyên. | • Ngang: Tách bảng `GIAO_DICH` theo từng năm. • Dọc: Tách cột `hinh_anh_goc` sang bảng phụ. |
| **3. 중복 속성 추가 (Thêm cột dư thừa)** | Sao chép cột từ bảng cha sang bảng con | Ngăn chặn việc phải JOIN ngược lên bảng cha chỉ để lấy 1-2 cột hiển thị. | Thêm cột `TenKhachHang` vào bảng `DON_HANG` (vốn đã có `MaKhachHang`). |
| **4. 파생 속성 추가 (Thêm cột tính toán)** | Lưu sẵn kết quả tính toán hoặc tổng hợp | Tránh việc phải chạy hàm `SUM()`, `COUNT()` liên tục trên tập dữ liệu hàng triệu dòng. | Thêm cột `TongTien` trong bảng `HOA_DON` (bằng tổng tiền các chi tiết). |
| **5. 중복 테이블 추가 (Thêm bảng trùng lặp)** | • Bảng tổng hợp (집계 테이블) • Bảng dữ liệu gần nhất | Lưu sẵn dữ liệu báo cáo định kỳ cho các truy vấn thống kê lớn. | Tạo bảng `DOANH_THU_THANG` tính sẵn dữ liệu cho Dashboard quản trị. |

#### 2. Bản chất Đánh đổi kỹ thuật (Trade-off): Hiệu năng Đọc vs Chi phí Ghi

| Khía cạnh vận hành | Hệ thống Chuẩn hóa cao (Normalized) | Hệ thống Phi chuẩn hóa (Denormalized) |
| :--- | :--- | :--- |
| **Hiệu năng Đọc (SELECT)** | Chậm hơn khi truy vấn phức tạp do phải thực hiện nhiều phép JOIN qua nhiều bảng. | **Rất nhanh**, giảm thiểu tối đa phép JOIN, đọc trực tiếp từ một bảng hoặc cột tính sẵn. |
| **Chi phí Ghi (INSERT, UPDATE, DELETE)** | **Nhanh và an toàn**, chỉ cần ghi dữ liệu vào một vị trí duy nhất. | **Chậm hơn đáng kể**, phải cập nhật đồng thời ở nhiều bảng và nhiều cột dư thừa. |
| **Tính toàn vẹn dữ liệu (Data Integrity)** | Đảm bảo tuyệt đối, không có dư thừa, không phát sinh dị thường. | **Nguy cơ cao phát sinh dị thường sửa (Update Anomaly)** và mâu thuẫn dữ liệu. |
| **Dung lượng lưu trữ đĩa** | Tối ưu, dung lượng đĩa tối thiểu. | Tốn nhiều không gian đĩa do lưu trùng lặp dữ liệu và các bảng phụ trợ. |

#### 3. So sánh đối đầu: RBO vs CBO (Bộ tối ưu hóa truy vấn)

```text
[ Câu lệnh SQL ] ──> [ Parser ] ──> [ Optimizer ] ──> [ Kế hoạch thực thi Execution Plan ]
                                          │
                          ┌───────────────┴───────────────┐
                          ▼                               ▼
                  규칙 기반 (RBO)                 비용 기반 (CBO)
```

| Tiêu chí so sánh | RBO (규칙 기반 / Rule-Based) | CBO (비용 기반 / Cost-Based) |
| :--- | :--- | :--- |
| **Tiêu chí tối ưu** | Dựa trên **thứ bậc ưu tiên cố định (1~15)** (Ví dụ: ROWID ưu tiên cao hơn Unique Index). | Tính toán **chi phí tài nguyên ước tính (Cost)** để chọn phương án tối thiểu. |
| **Yếu tố quyết định** | Phụ thuộc hoàn toàn vào **cú pháp viết SQL** của lập trình viên. | Phụ thuộc vào **thông tin thống kê (Statistics Info)** trong System Catalog. |
| **Chi phí phần cứng** | Không tính toán tài nguyên I/O đĩa hay CPU thực tế. | Tính toán chi tiết số block I/O, thời gian CPU và bộ nhớ RAM cần dùng. |
| **Độ dự đoán** | Cố định, dễ dàng phán đoán kế hoạch thực thi. | Biến động linh hoạt theo kích thước dữ liệu và tần suất phân bố (Histogram). |

#### 4. Bẫy đề thi kinh điển (시험 대비 함정 포인트)
- **Bẫy 1: Khẳng định sai về Phi chuẩn hóa:**
  - *Mệnh đề:* "Phi chuẩn hóa giúp cải thiện toàn diện mọi mặt của cơ sở dữ liệu."
  - *Đánh giá:* **SAI HOÀN TOÀN**. Phi chuẩn hóa chỉ cải thiện tốc độ ĐỌC, nhưng làm suy giảm tốc độ GHI và tăng nguy cơ vi phạm toàn vẹn dữ liệu.
- **Bẫy 2: Phân biệt Tách bảng ngang vs Tách bảng dọc:**
  - Tách theo hàng (Row) $\rightarrow$ **수평 분할 (Horizontal Partitioning)**.
  - Tách theo cột (Column) $\rightarrow$ **수직 분할 (Vertical Partitioning)**.
- **Bẫy 3: CBO phụ thuộc vào yếu tố nào:**
  - *Câu hỏi:* "Bộ tối ưu CBO cần yếu tố gì để hoạt động chính xác?"
  - *Đáp án đúng:* **Thông tin thống kê mới nhất (최신 통계 정보)** của bảng và chỉ mục. Nếu không cập nhật thống kê định kỳ, CBO có thể chọn kế hoạch thực thi rất tồi.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Phân tích chi tiết 5 kỹ thuật phi chuẩn hóa

##### 1.1. Gộp bảng (테이블 통합)
- **Gộp bảng quan hệ 1:1:** Thường áp dụng khi hai bảng luôn được truy vấn cùng nhau (ví dụ bảng `KHACH_HANG` và bảng `THONG_TIN_MO_RONG`). Gộp lại giúp loại bỏ hoàn toàn 1 phép JOIN.
- **Gộp bảng quan hệ 1:N:** Áp dụng khi dữ liệu phía 1 rất ít và thường xuyên cần xem kèm dữ liệu phía N. Tuy nhiên cần cẩn trọng vì dữ liệu phía 1 sẽ bị lặp lại ở nhiều dòng phía N.

##### 1.2. Tách bảng (테이블 분할)
- **Tách bảng ngang (수평 분할 - Horizontal Partitioning):**
  - Bảng chứa 100 triệu dòng hóa đơn được chia theo năm: bảng `HOA_DON_2024`, `HOA_DON_2025`, `HOA_DON_2026`. Khi người dùng tra cứu đơn hàng năm nay, DBMS chỉ cần quét trên phân vùng năm 2026, loại bỏ 70% khối dữ liệu không cần thiết.
- **Tách bảng dọc (수직 분할 - Vertical Partitioning):**
  - Bảng `BAI_VIET(id, tieu_de, ngay_dang, luot_xem, noi_dung_chi_tiet, video_dinh_kem)`.
  - Các cột `id, tieu_de, ngay_dang, luot_xem` có dung lượng nhỏ và được truy vấn hàng nghìn lần mỗi giây khi duyệt danh sách bài viết.
  - Cột `noi_dung_chi_tiet` và `video_dinh_kem` rất nặng (CLOB/BLOB). Tách riêng 2 cột này sang bảng `BAI_VIET_NOI_DUNG` giúp bảng chính nén được nhiều dòng hơn vào mỗi Block đĩa, tăng vọt tỷ lệ trúng cache RAM (Buffer Cache Hit Ratio).

##### 1.3. Thêm cột dư thừa (중복 속성 추가)
- Trong hệ thống bán hàng, bảng `CHI_TIET_DON_HANG` có `MaSanPham`. Mỗi lần hiển thị giỏ hàng, ứng dụng lại phải JOIN sang bảng `SAN_PHAM` chỉ để lấy cột `TenSanPham`.
- Kỹ thuật: Thêm trực tiếp cột `TenSanPham` vào bảng `CHI_TIET_DON_HANG`.
- Điểm đánh đổi: Khi sản phẩm đổi tên, phải chạy lệnh UPDATE trên hàng triệu dòng chi tiết đơn hàng cũ, nếu không sẽ bị mâu thuẫn tên sản phẩm.

##### 1.4. Thêm cột tính toán tổng hợp (파생 속성 추가)
- Bảng `HOA_DON` thêm cột `TongThanhTien`. Cột này được tính toán sẵn từ:
  $$\text{TongThanhTien} = \sum (\text{DonGia} \times \text{SoLuong}) - \text{GiamGia}$$
- Giúp báo cáo doanh thu không cần duyệt qua toàn bộ bảng chi tiết đơn hàng.

---

### 복습 체크리스트
- [ ] Định nghĩa được Phi chuẩn hóa (`반정규화`) và giải thích bản chất đánh đổi: Đọc nhanh vs Ghi chậm + Rủi ro mất toàn vẹn.
- [ ] Phân biệt được 5 kỹ thuật phi chuẩn hóa: Gộp bảng, Tách bảng ngang/dọc, Thêm cột dư thừa, Thêm cột tính toán tổng hợp, Thêm bảng tổng hợp.
- [ ] Hiểu rõ sự khác biệt giữa Tách bảng ngang (수평 분할 - chia Row) và Tách bảng dọc (수직 분할 - chia Column).
- [ ] Nắm vững cơ chế của 2 loại Optimizer: RBO (dựa trên quy tắc ưu tiên cố định) vs CBO (dựa trên chi phí và thông tin thống kê).
- [ ] Nhận diện được nguy cơ phát sinh dị thường sửa (Update Anomaly) khi thêm cột dư thừa.
