# 7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, cơ chế và các kỹ thuật phục hồi cơ sở dữ liệu (**회복 - Recovery**): Phục hồi dựa trên nhật ký (**Log-based: Cập nhật tức thời Immediate Update vs Cập nhật trì hoãn Deferred Update**), Điểm kiểm tra (**Checkpoint**), và Phân trang bóng (**Shadow Paging**).
- Thấu hiểu mối quan hệ đánh đổi (Trade-off) của độ mịn khóa (**로킹 단위 - Locking Granularity**) trong kiểm soát đồng thời (Concurrency Control): Khóa quy mô lớn (dễ quản lý nhưng đồng thời thấp) vs Khóa quy mô nhỏ (đồng thời cao nhưng tốn overhead).
- Nắm vững giao thức khóa hai pha (**2PL - Two-Phase Locking**) bảo đảm tính khả tuần tự và giải thuật phòng tránh bế tắc Nhà băng (**Banker's Algorithm**).

## 핵심 키워드 (Từ khóa)
- 데이터베이스 회복 (Database Recovery - REDO & UNDO)
- 즉각 갱신 기법 (Immediate Update - REDO/UNDO 필요)
- 연기 갱신 기법 (Deferred Update - REDO만 필요, UNDO 불필요)
- 검사점 기법 (Checkpoint - 회복 시간 단축)
- 그림자 페이징 (Shadow Paging)
- 로킹 단위 (Locking Granularity - 크면 병행성 저하, 작으면 오버헤드 증가)
- 2단계 로킹 규약 (2PL - Two-Phase Locking Protocol: 확장 단계, 축소 단계)
- 교착상태 회피 (Deadlock Avoidance - 은행원 알고리즘 Banker's Algorithm)

## 선행·연결 개념 (Kiến thức liên kết)
- [23-bai-hoc.md](23-bai-hoc.md): Các giao thức chính theo tầng mạng TCP/IP.
- [25-bai-hoc.md](25-bai-hoc.md): Các công nghệ dữ liệu mới (Hadoop, MapReduce, Big Data, OLAP).
- [74-bai-hoc.md](74-bai-hoc.md): 4 điều kiện bế tắc Deadlock và thuật toán loại trừ lẫn nhau.

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh trong các câu hỏi đề thi:
  - **즉각 갱신 (Immediate Update):** Dữ liệu được ghi ngay vào DB trước khi commit $\rightarrow$ Khi gặp sự cố: Transaction nào đã ghi lệnh Commit trong Log thì thực hiện **REDO (làm lại)**; Transaction nào chưa kịp Commit thì bắt buộc phải thực hiện **UNDO (hủy bỏ, quay về trạng thái cũ)**.
  - **연기 갱신 (Deferred Update):** Dữ liệu chỉ ghi tạm vào Log, chỉ khi nào Commit thành công mới ghi vào DB thực $\rightarrow$ Khi gặp sự cố: Chỉ cần **REDO** các transaction đã commit, **HOÀN TOÀN KHÔNG CẦN UNDO** các transaction dở dang vì DB thực tế chưa bị chạm vào.
  - **로킹 단위 (Độ lớn của Khóa):**
    - Khóa to (Cả bảng DB) $\rightarrow$ Ít khóa, dễ quản lý, nhưng **người khác phải đợi lâu (병행성 저하 - Mức độ đồng thời thấp)**.
    - Khóa nhỏ (Từng dòng record) $\rightarrow$ **Nhiều người cùng làm việc một lúc (병행성 증가 - Đồng thời cao)**, nhưng tốn bộ nhớ lưu khóa và hệ thống dễ bị quá tải.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu các phương pháp phục hồi dữ liệu (Recovery Techniques):**

| Kỹ thuật phục hồi | Cơ chế ghi đĩa & Nhật ký Log | Thao tác khi xảy ra sự cố (Failure) |
| :--- | :--- | :--- |
| **즉각 갱신 기법** (Immediate Update) | Ghi thay đổi vào CSDL thực tế ngay trong lúc giao dịch đang chạy; bắt buộc phải tuân thủ nguyên tắc ghi nhật ký trước (**WAL - Write-Ahead Logging**). | Transaction **đã có bản ghi Commit** trong Log: Thực hiện **REDO** (Chạy lại để bảo đảm bền vững); Transaction **chưa có bản ghi Commit**: Thực hiện **UNDO** (Khôi phục lại giá trị cũ từ Log). |
| **연기 갱신 기법** (Deferred Update) | Trong suốt quá trình thực thi, mọi thao tác sửa đổi chỉ được ghi tạm thời vào bộ đệm Log; **chỉ sau khi giao dịch đã Commit hoàn tất mới bắt đầu ghi thực sự vào CSDL**. | Transaction **đã có Commit**: Thực hiện **REDO**; Transaction **chưa có Commit**: **Không cần làm gì (UNDO 불필요)**, chỉ việc hủy bỏ dữ liệu tạm trong Log buffer. |
| **검사점 기법** (Checkpoint) | Định kỳ lưu toàn bộ trạng thái bộ đệm Log và dữ liệu ra đĩa cứng tại các mốc kiểm tra (**Checkpoint**). | Khi có lỗi, hệ thống **chỉ cần quét ngược lại đến điểm Checkpoint gần nhất** để phục hồi, giúp rút ngắn thời gian khôi phục hệ thống đáng kể. |
| **그림자 페이징** (Shadow Paging) | Duy trì 2 bảng trang: Bảng trang hiện hành (Current Page Table) và Bảng trang bóng cố định (Shadow Page Table). | Khi xảy ra lỗi giữa chừng, hệ thống chỉ việc hủy bỏ bảng trang hiện hành và **trỏ con trỏ cơ sở dữ liệu quay trở lại Bảng trang bóng**, không cần dùng Log. |

- **2. Bảng quy luật đánh đổi của Độ mịn khóa (Locking Granularity):**

| Kích thước đơn vị khóa | Số lượng khóa (Locks) | Chi phí quản lý (Overhead) | Mức độ đồng thời (Concurrency) |
| :--- | :---: | :---: | :---: |
| **Đơn vị LỚN** (Cả Database, Cả Bảng Table) | **Ít** | **Thấp / Dễ quản lý** | **Giảm / Kém** (Nhiều tiến trình bị chặn đợi) |
| **Đơn vị NHỎ** (Từng Bản ghi Record, Từng Trường Field) | **Nhiều** | **Cao / Phức tạp** | **Tăng / Tối ưu** (Nhiều giao dịch chạy song song) |

- **3. Giao thức khóa hai pha (2PL - Two-Phase Locking):**
  - **Giai đoạn mở rộng (확장 단계 - Growing Phase):** Giao dịch **chỉ được phép yêu cầu cấp phát thêm khóa mới**, tuyệt đối không được phép giải phóng bất kỳ khóa nào.
  - **Giai đoạn co hẹp (축소 단계 - Shrinking Phase):** Giao dịch **chỉ được phép giải phóng (Unlock) các khóa đang giữ**, tuyệt đối không được phép yêu cầu cấp thêm bất kỳ khóa mới nào nữa.
  - **Ý nghĩa:** Đảm bảo tính khả tuần tự (Serializability) cho các giao dịch đồng thời, nhưng **không ngăn chặn được bế tắc (Deadlock)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Thuật toán Nhà băng (Banker's Algorithm - Dijkstra):**
  - Là thuật toán kinh điển dùng để **Tránh bế tắc (Deadlock Avoidance)** trong cơ sở dữ liệu và hệ điều hành.
  - Nguyên lý: Khi một tiến trình yêu cầu tài nguyên, hệ thống sẽ chạy thuật toán giả định cấp phát để kiểm tra xem hệ thống có duy trì được **Trạng thái an toàn (Safe State)** hay không. Nếu sau khi cấp phát mà tồn tại ít nhất một chuỗi an toàn (Safe Sequence) đảm bảo mọi tiến trình đều có thể hoàn tất, hệ thống mới chính thức cấp tài nguyên; ngược lại sẽ từ chối hoặc bắt tiến trình phải đợi.

### 복습 체크리스트
- [ ] Phân biệt được: Immediate Update cần cả REDO và UNDO, Deferred Update chỉ cần REDO (không cần UNDO).
- [ ] Ghi nhớ quy luật Locking Granularity: Đơn vị khóa lớn thì quản lý dễ nhưng tính đồng thời thấp.
- [ ] Nhớ 2 giai đoạn của 2PL: Growing Phase (chỉ khóa, không nhả) và Shrinking Phase (chỉ nhả, không khóa).
- [ ] Ghi nhớ thuật toán Nhà băng (Banker's Algorithm) của Dijkstra dùng để TRÁNH bế tắc (Deadlock Avoidance).
