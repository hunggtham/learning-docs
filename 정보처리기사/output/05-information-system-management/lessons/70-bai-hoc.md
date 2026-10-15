# DB 회복 및 병행 제어 (Phục hồi Dữ liệu & Kiểm soát Đồng thời DB)

## 학습 목표 (Mục tiêu)
- Nắm vững 4 kỹ thuật phục hồi cơ sở dữ liệu khi xảy ra sự cố: Cập nhật trì hoãn (연기 갱신 - Deferred Update), Cập nhật tức thì (즉각 갱신 - Immediate Update), Trang bóng (그림자 페이지 - Shadow Paging), và Điểm kiểm tra (검사점 - Checkpoint).
- Hiểu rõ 3 vấn đề bất nhất quán dữ liệu phát sinh khi không kiểm soát đồng thời: Mất cập nhật (갱신 분실), Đọc dữ liệu sai lệch (모순성 / Dirty Read), và Thu hồi dây chuyền (연쇄 복귀).
- Phân tích cơ chế khóa dữ liệu (Locking: Shared Lock vs Exclusive Lock), sự đánh đổi về kích thước đơn vị khóa (Locking Granularity), và Giao thức khóa 2 pha (2PL).
- Phân biệt kỹ thuật dán nhãn thời gian (Time Stamp Ordering) với ưu điểm triệt tiêu hoàn toàn bế tắc (Deadlock).

## 핵심 키워드 (Từ khóa)
- **회복 기법 (Recovery)**: 연기 갱신 (chỉ dùng Redo), 즉각 갱신 (dùng cả Undo và Redo), 그림자 페이지 (dùng bảng trang bóng, không cần Log), 검사점 (Checkpoint).
- **병행 제어 문제**: 갱신 분실 (Lost Update), 모순성 (Inconsistency), 연쇄 복귀 (Cascading Rollback).
- **로킹 (Locking)**: Shared Lock (khóa đọc chia sẻ), Exclusive Lock (khóa ghi độc quyền), 로킹 단위 (Granularity).
- **2단계 로킹 (2PL)**: Growing Phase (chỉ xin khóa) và Shrinking Phase (chỉ nhả khóa) $\rightarrow$ Đảm bảo tính khả tuần tự (Serializability).
- **타임스탬프 (Time Stamp)**: Xếp thứ tự giao dịch theo nhãn thời gian $\rightarrow$ Triệt tiêu Deadlock.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [24-bai-hoc.md](24-bai-hoc.md) (Công nghệ cốt lõi cơ sở dữ liệu và giao dịch ACID).
- Liên kết với [71-bai-hoc.md](71-bai-hoc.md) (Hiện tượng bế tắc Deadlock trong hệ thống).
- Liên kết với [03-database-construction/12-bai-hoc.md](../../03-database-construction/lessons/12-bai-hoc.md) (Giao dịch và thuộc tính ACID).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh kỹ thuật phục hồi:
  - "Hoãn ghi vào DB cho đến khi Commit, chỉ cần làm lại (Redo)" $\rightarrow$ **연기 갱신 기법 (Deferred Update)**.
  - "Ghi vào DB ngay lập tức, cần cả Undo và Redo" $\rightarrow$ **즉각 갱신 기법 (Immediate Update)**.
  - "Không cần dùng tệp nhật ký Log, lưu 2 bảng trang Current và Shadow" $\rightarrow$ **그림자 페이지 (Shadow Paging)**.
  - "Kỹ thuật kiểm soát đồng thời nào đảm bảo không bao giờ xảy ra bế tắc Deadlock?" $\rightarrow$ Chọn **타임스탬프 순서 (Time Stamp Ordering)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng so sánh 4 Kỹ thuật Phục hồi Cơ sở Dữ liệu (Recovery Techniques)
| Kỹ thuật (KR / EN) | Thời điểm ghi vào DB thực tế | Thao tác phục hồi khi có lỗi | Sử dụng tệp Log |
| :--- | :--- | :--- | :--- |
| **연기 갱신 기법 / (Deferred Update)** | Hoãn lại, **chỉ ghi vào DB sau khi Transaction Commit** thành công | **Chỉ dùng REDO** (làm lại các giao dịch đã commit); Không cần Undo vì chưa hề ghi vào DB | Có ghi Log tạm thời |
| **즉각 갱신 기법 / (Immediate Update)** | Ghi trực tiếp vào DB **ngay khi đang thực thi** giao dịch | **Dùng cả UNDO và REDO** (Undo hủy bỏ giao dịch dở dang, Redo chạy lại giao dịch đã commit) | Bắt buộc ghi Log trước khi ghi DB (WAL - Write-Ahead Logging) |
| **그림자 페이지 / (Shadow Paging)** | Ghi dữ liệu vào các trang bộ nhớ mới trong bảng trang hiện tại | Chuyển con trỏ bảng trang quay về trỏ vào **bảng trang bóng (Shadow Page)** | **Không sử dụng Log** |
| **검사점 기법 / (Checkpoint)** | Ghi cưỡng bức toàn bộ bộ đệm RAM xuống đĩa tại thời điểm đánh dấu | Chỉ cần quét ngược Log từ **mốc Checkpoint gần nhất** thay vì quét toàn bộ lịch sử Log | Có kết hợp Log và Checkpoint |

#### 2. Ba vấn đề phát sinh khi không Kiểm soát Đồng thời (Concurrency Issues)
- **갱신 분실 (Lost Update - Mất cập nhật)**: Hai giao dịch cùng sửa đổi một trường dữ liệu song song; kết quả của giao dịch kết thúc sau ghi đè và làm mất hoàn toàn kết quả của giao dịch trước.
- **모순성 (Inconsistency / Dirty Read - Đọc dữ liệu sai lệch)**: Giao dịch này đọc dữ liệu tạm thời chưa được commit của giao dịch khác, mà sau đó giao dịch đó lại bị Rollback hủy bỏ.
- **연쇄 복귀 (Cascading Rollback - Thu hồi dây chuyền)**: Một giao dịch bị hủy buộc hàng loạt các giao dịch khác đã đọc dữ liệu từ nó cũng phải bị hủy dây chuyền theo.

#### 3. Kỹ thuật Khóa dữ liệu (Locking) và Giao thức 2PL
- **Hai loại khóa cơ bản**:
  - **Shared Lock (Khóa chia sẻ - $S$)**: Dùng cho thao tác **Đọc (Read)**. Nhiều giao dịch có thể cùng giữ khóa $S$ trên cùng một dữ liệu.
  - **Exclusive Lock (Khóa độc quyền - $X$)**: Dùng cho thao tác **Ghi (Write)**. Chỉ duy nhất một giao dịch được giữ khóa $X$; các giao dịch khác không được đọc hay ghi.
- **Kích thước đơn vị khóa (Locking Granularity)**:
  - *Đơn vị khóa lớn (Toàn bộ DB, Bảng)*: Quản lý số lượng khóa ít, đơn giản; nhưng mức độ xử lý đồng thời (Concurrency) bị suy giảm nghiêm trọng.
  - *Đơn vị khóa nhỏ (Bản ghi Record, Trường Field)*: Mức độ đồng thời rất cao; nhưng số lượng khóa bùng nổ, quản lý phức tạp và tốn nhiều RAM lưu khóa.
- **Giao thức khóa 2 pha (2-Phase Locking Protocol - 2PL)**:
  - **Pha mở rộng (Growing Phase)**: Giao dịch chỉ được phép yêu cầu thêm các khóa mới, **không được nhả bất kỳ khóa nào**.
  - **Pha thu hẹp (Shrinking Phase)**: Giao dịch chỉ được phép giải phóng (nhả) các khóa, **không được yêu cầu thêm khóa mới**.
  - *Đặc điểm*: Đảm bảo tính khả tuần tự (Serializability) nhưng **vẫn có nguy cơ xảy ra Deadlock**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ cơ chế hoạt động của Checkpoint (검사점)
```
Thời gian ─────────────────────────────────────────────────────────────►
  [Log ghi...] ──► [MỐC CHECKPOINT] ──► [Giao dịch T1 (Commit)] ──► [SỰ CỐ HỎNG HÓC]
                          │             [Giao dịch T2 (Chưa)]   ──► [SỰ CỐ HỎNG HÓC]
                          ▼
            Toàn bộ dữ liệu trước mốc này
            đã nằm an toàn trên đĩa cứng!
            └── Chỉ cần quét Log từ Checkpoint: REDO T1, UNDO T2.
```

#### 2. Kỹ thuật Dán nhãn thời gian (Time Stamp Ordering)
- Mỗi giao dịch $T_i$ khi khởi tạo được hệ thống cấp một nhãn thời gian duy nhất $TS(T_i)$ dựa trên đồng hồ hệ thống.
- Khi có xung đột truy cập, giao dịch có nhãn thời gian nhỏ hơn (đến sớm hơn) luôn được ưu tiên thực thi trước.
- **Ưu thế vượt trội**: Mọi giao dịch đều được sắp xếp theo trật tự thời gian tuyến tính cố định, do đó **hoàn toàn loại trừ khả năng xảy ra bế tắc (Deadlock-Free)**.

---

### 복습 체크리스트
- [ ] Phân biệt sự khác nhau giữa thao tác phục hồi của 연기 갱신 (Deferred Update) và 즉각 갱신 (Immediate Update)?
- [ ] Khi đơn vị khóa (Locking Granularity) có kích thước càng lớn thì mức độ xử lý đồng thời của hệ thống sẽ tăng hay giảm?
- [ ] Giao thức khóa hai pha (2PL) có thể đảm bảo tính chất gì và tại sao vẫn có thể xảy ra Deadlock?
- [ ] Tại sao kỹ thuật kiểm soát đồng thời bằng nhãn thời gian (Time Stamp Ordering) lại không bao giờ gặp phải hiện tượng Deadlock?
