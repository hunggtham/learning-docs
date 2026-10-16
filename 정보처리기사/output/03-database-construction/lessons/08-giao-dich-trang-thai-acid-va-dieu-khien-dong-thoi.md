# 트랜잭션, ACID 특성과 동시성 제어 (Giao dịch, Đặc tính ACID và Điều khiển đồng thời)

## 학습 목표
- Nắm vững bản chất đơn vị thao tác logic (`논리적 작업 단위`), cơ chế "All or Nothing" của tính nguyên tử (`원자성`), tính nhất quán (`일관성`), tính cô lập (`격리성/독립성`), và tính bền vững (`영속성`).
- Phân tích sơ đồ chuyển đổi 5 trạng thái vòng đời giao dịch: Đang hoạt động (`활동`), Hoàn thành một phần (`부분 완료`), Hoàn tất (`완료`), Thất bại (`실패`), và Bị hủy bỏ (`철회`).
- Nhận diện chính xác 4 sự cố khi thiếu kiểm soát đồng thời: Mất cập nhật (`갱신 분실`), Mâu thuẫn dữ liệu (`모순성`), Hoàn tác dây chuyền (`연쇄 복귀`), và Đọc rác (`비완료 의존성 / Dirty Read`).
- So sánh các kỹ thuật kiểm soát đồng thời: Cơ chế khóa S-Lock vs X-Lock, đánh đổi đơn vị khóa (`로킹 단위`), Giao thức khóa 2 pha (`2PL`), Gán mốc thời gian (`타임스탬프`), và Kiểm soát lạc quan.
- Phân biệt cơ chế Redo và Undo trong các kỹ thuật phục hồi: Cập nhật trì hoãn (`연기 갱신`), Cập nhật tức thì (`즉각 갱신`), Điểm kiểm tra (`검사점 / Checkpoint`), và Phân trang bóng (`그림자 페이징`).

## 핵심 키워드
- 트랜잭션 (Giao dịch / Transaction / 논리적 작업 단위)
- ACID 특성 (Bộ 4 đặc tính: 원자성 Atomicity, 일관성 Consistency, 격리성 Isolation, 영속성 Durability)
- 트랜잭션 상태 (활동, 부분 완료, 완료, 실패, 철회)
- 병행 제어 (Điều khiển đồng thời / Concurrency Control / 갱신 분실, 모순성, 연쇄 복귀, 비완료 의존성)
- 로킹 (Khóa / Locking / 공유 락 S-Lock, 배타 락 X-Lock, 로킹 단위)
- 2단계 로킹 규약 (Khóa 2 pha / 2PL / 직렬성 보장 / 교착상태 미방지)
- 회복 기법 (Phục hồi CSDL / REDO / UNDO / 연기 갱신 / 즉각 갱신 / Checkpoint)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [07-phi-chuan-hoa-va-toi-uu-hieu-nang-truy-van.md](07-phi-chuan-hoa-va-toi-uu-hieu-nang-truy-van.md), chúng ta đã khảo sát các kỹ thuật phi chuẩn hóa để tăng tốc truy vấn và cơ chế lập kế hoạch thực thi của Optimizer.
- **Đang giải quyết gì (Current Problem):** Trong môi trường đa người dùng truy cập song song, bài học này giải quyết bài toán chống xung đột, chống mất mát dữ liệu khi có sự cố thông qua cơ chế quản trị giao dịch nguyên tử **ACID**, các giao thức **Điều khiển đồng thời (Concurrency Control)** và cơ chế **Phục hồi (Recovery)**.
- **Dùng đi đâu (Forward Handoff):** Nguyên lý giao dịch này sẽ được hiện thực hóa trực tiếp bằng các câu lệnh SQL điều khiển giao dịch TCL (COMMIT, ROLLBACK) và thủ tục lưu trữ (Stored Procedure) ở bài học tiếp theo [09-ngon-ngu-sql-ddl-dml-dcl-va-procedural-sql.md](09-ngon-ngu-sql-ddl-dml-dcl-va-procedural-sql.md).

## 읽는 방법
- Đọc TẦNG A để nắm chắc bảng nén các bẫy đề thi trắc nghiệm hay gặp nhất (phân biệt phần 완료 vs 완료, đánh đổi đơn vị khóa, lưu ý Deadlock trong 2PL, và cơ chế REDO/UNDO trong 연기 갱신).
- Đọc TẦNG B để hiểu sâu toàn diện lý thuyết kỹ thuật, bảng đối chiếu chi tiết 4 đặc tính ACID, sơ đồ chuyển trạng thái, 4 thảm họa đồng thời và cơ chế phục hồi hệ thống.

---

## 트랜잭션, ACID 특성과 동시성 제어

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng nén 4 đặc tính ACID cốt lõi
| Đặc tính | Tiếng Hàn / Anh | Định nghĩa kỹ thuật | Cơ chế bảo đảm |
| :--- | :--- | :--- | :--- |
| **Nguyên tử** | **원자성 (Atomicity)** | "All or Nothing" (thành công toàn bộ hoặc hủy bỏ toàn bộ) | Recovery Manager, Undo Log |
| **Nhất quán** | **일관성 (Consistency)** | Giữ nguyên các ràng buộc toàn vẹn và miền giá trị sau giao dịch | Integrity Constraints, Trigger |
| **Cô lập** | **격리성 (Isolation)** | Giao dịch chạy đồng thời không can thiệp kết quả trung gian của nhau | Locking, Timestamp, MVCC |
| **Bền vững** | **영속성 (Durability)** | Kết quả COMMIT được ghi nhớ vĩnh viễn dù có sự cố điện/OS | Non-volatile Storage, Redo Log |

#### 2. Sơ đồ 5 trạng thái vòng đời giao dịch
```
       [ 활동 (Active) ] ───────────┐
              │                     │
              ▼                     ▼
     [ 부분 완료 (Partially     [ 실패 (Failed) ]
        Committed) ]                │
              │                     ▼
              ├──────────────> [ 철회 (Aborted) ]
              ▼
        [ 완료 (Committed) ]
```

#### 3. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Trạng thái 부분 완료 (Partially Committed):**
  - *Câu hỏi:* Trạng thái sau khi toàn bộ câu lệnh SQL đã chạy xong trong RAM nhưng chưa ghi hoàn tất xuống đĩa gọi là gì?
  - *Đáp án:* **부분 완료 (Partially Committed)**, không phải `완료 (Committed)`.
- **Bẫy 2: Giao thức khóa 2 pha (2PL - 2단계 로킹 규약):**
  - *Khẳng định:* "2PL vừa đảm bảo 직렬성 (tính tuần tự) vừa ngăn chặn hoàn toàn Deadlock" $\rightarrow$ **SAI**. 2PL bảo đảm 직렬성 nhưng **VẪN CÓ THỂ XẢY RA DEADLOCK (교착상태)**.
- **Bẫy 3: Đánh đổi đơn vị khóa (로킹 단위 트레이드오프):**
  - Đơn vị khóa Càng lớn (DB, Bảng): Số lượng khóa ít, Chi phí quản lý giảm/đơn giản, nhưng **Mức độ đồng thời GIẢM mạnh**.
  - Đơn vị khóa Càng nhỏ (Dòng, Cột): Số lượng khóa nhiều, Chi phí quản lý tăng/phức tạp, nhưng **Mức độ đồng thời TĂNG cao**.
- **Bẫy 4: Kỹ thuật phục hồi 연기 갱신 (Deferred Update):**
  - *Khẳng định:* "Trong 연기 갱신 기법, khi gặp sự cố hệ thống phải thực hiện cả REDO và UNDO" $\rightarrow$ **SAI**. Vì 연기 갱신 chỉ ghi vào DB sau khi Commit nên **CHỈ CẦN REDO, KHÔNG BAO GIỜ CẦN UNDO**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Định nghĩa và 4 đặc tính ACID chi tiết
- **트랜잭션(Transaction):** Là đơn vị thao tác logic cơ bản (`논리적 작업 단위 / Logical Unit of Work`) thực hiện chức năng biến đổi trạng thái CSDL.
- **4 đặc tính ACID:**
  1. `원자성 (Atomicity)`: Mọi thao tác trong giao dịch phải hoàn tất trọn vẹn (Commit). Nếu xảy ra lỗi giữa chừng, toàn bộ các biến đổi trước đó phải bị hủy bỏ hoàn toàn (Rollback).
  2. `일관성 (Consistency)`: Sau khi giao dịch kết thúc, CSDL luôn bảo đảm tính đúng đắn theo mọi quy tắc nghiệp vụ và ràng buộc toàn vẹn (Khóa chính, Khóa ngoại, CHECK).
  3. `격리성 / 독립성 (Isolation)`: Các giao dịch chạy song song không được nhìn thấy dữ liệu trung gian chưa Commit của nhau.
  4. `영속성 (Durability)`: Dữ liệu sau khi đã Commit sẽ không bị mất mát ngay cả khi máy chủ mất điện hoặc gặp sự cố phần cứng.

#### 2. Chi tiết 5 trạng thái vòng đời giao dịch
- `활동 (Active)`: Trạng thái ban đầu khi giao dịch khởi động và đang thực thi tuần tự các câu lệnh.
- `부분 완료 (Partially Committed)`: Trạng thái ngay sau khi câu lệnh cuối cùng hoàn thành nhưng thao tác ghi đĩa vật lý chưa xong.
- `완료 (Committed)`: Trạng thái giao dịch hoàn tất thành công, dữ liệu đã lưu trữ an toàn vĩnh viễn trên đĩa.
- `실패 (Failed)`: Trạng thái phát sinh lỗi trong quá trình thực thi làm gián đoạn tiến trình.
- `철회 (Aborted)`: Trạng thái sau khi DBMS thực thi xong lệnh ROLLBACK để đưa CSDL về trạng thái ban đầu trước giao dịch.

#### 3. 4 sự cố khi thiếu điều khiển đồng thời (병행 제어 미수행 4대 문제점)
| Tên sự cố | Tên tiếng Hàn & Anh | Bản chất kỹ thuật |
| :--- | :--- | :--- |
| **Mất cập nhật** | **Lost Update (갱신 분실)** | Hai giao dịch cùng sửa một dữ liệu; giao dịch kết thúc sau ghi đè và làm mất trắng kết quả của giao dịch trước. |
| **Tính mâu thuẫn** | **Inconsistency (모순성 / 불일치)** | Một giao dịch sửa nhiều dòng, giao dịch khác đọc xen kẽ dẫn đến trạng thái dữ liệu trước và sau không khớp nhau. |
| **Hoàn tác dây chuyền** | **Cascading Rollback (연쇄 복귀)** | Giao dịch $T_2$ đọc dữ liệu của $T_1$; khi $T_1$ lỗi và Rollback thì $T_2$ cũng bị buộc Rollback theo dây chuyền. |
| **Đọc rác** | **Dirty Read (비완료 의존성)** | Giao dịch đọc giá trị tạm thời chưa Commit của giao dịch khác; giá trị đó sau đó bị hủy bỏ khiến việc đọc trở nên vô nghĩa. |

#### 4. Kỹ thuật điều khiển đồng thời (병행 제어 주요 기법)
- **로킹 (Locking):**
  - `공유 락 (Shared Lock, S-Lock)`: Cho phép nhiều giao dịch cùng giữ khóa để đọc dữ liệu (Read-only), ngăn chặn thao tác ghi.
  - `배타 락 (Exclusive Lock, X-Lock)`: Dành riêng cho thao tác ghi (Write), chỉ một giao dịch duy nhất được nắm giữ và chặn toàn bộ đọc/ghi của giao dịch khác.
- **2단계 로킹 규약 (2-Phase Locking Protocol, 2PL):**
  - `확장 단계 (Growing Phase)`: Chỉ xin cấp phát khóa mới, không được giải phóng bất kỳ khóa nào.
  - `축소 단계 (Shrinking Phase)`: Chỉ giải phóng khóa hiện có, không được xin cấp thêm khóa mới.
  - Bảo đảm tính tuần tự (`직렬성`), nhưng **vẫn có thể phát sinh Deadlock (교착 상태)**.
- **타임스탬프 순서 (Timestamp Ordering):** Gán nhãn thời gian cho từng giao dịch; sắp xếp thứ tự thao tác dựa trên tem thời gian mà không dùng khóa, do đó **không phát sinh Deadlock**.
- **낙관적 검증 (Optimistic Concurrency Control):** Giả định ít xung đột, cho phép thực thi tự do trên bộ đệm cục bộ và chỉ kiểm tra tính hợp lệ tại pha thẩm định (Validation Phase) trước khi ghi thật.
- **MVCC (Multi-Version Concurrency Control):** Tạo bản sao phiên bản dữ liệu có gắn nhãn thời gian, giúp thao tác đọc không bao giờ bị nghẽn bởi thao tác ghi.

#### 5. Kỹ thuật phục hồi cơ sở dữ liệu (데이터베이스 회복 기법)
- **Cơ chế phục hồi:**
  - `REDO (재실행)`: Đọc log để chạy lại các giao dịch đã Commit trước sự cố nhằm bảo đảm tính bền vững (`영속성`).
  - `UNDO (취소/원상복구)`: Đọc log để hủy bỏ các biến đổi của giao dịch chưa Commit tại thời điểm gặp sự cố nhằm bảo đảm tính nguyên tử (`원자성`).
- **So sánh 4 kỹ thuật phục hồi:**
  - `연기 갱신 기법 (Deferred Update)`: Hoãn ghi vào DB cho đến khi Commit; khi gặp sự cố chỉ cần **REDO**, không bao giờ cần UNDO.
  - `즉각 갱신 기법 (Immediate Update)`: Ghi trực tiếp vào DB ngay trong khi chạy; khi gặp sự cố phải thực hiện cả **REDO và UNDO**.
  - `검사점 기법 (Checkpoint)`: Định kỳ xả dữ liệu từ RAM xuống đĩa; khi phục hồi chỉ cần quét từ mốc Checkpoint gần nhất giúp rút ngắn thời gian khôi phục.
  - `그림자 페이징 (Shadow Paging)`: Duy trì 2 bảng trang (bảng hiện hành và bảng bóng); khi phục hồi chỉ cần trỏ lại bảng bóng mà không cần quét file log.

---

### 복습 체크리스트
- [ ] Thuộc lòng 4 đặc tính ACID (`원자성`, `일관성`, `격리성`, `영속성`) và cơ chế bảo đảm tương ứng.
- [ ] Vẽ lại sơ đồ 5 trạng thái giao dịch và phân biệt rõ `부분 완료` với `완료`.
- [ ] Phân tích 4 sự cố khi thiếu kiểm soát đồng thời: `갱신 분실`, `모순성`, `연쇄 복귀`, `비완료 의존성`.
- [ ] So sánh Shared Lock (S-Lock) và Exclusive Lock (X-Lock).
- [ ] Nắm vững quy luật đánh đổi của `로킹 단위` (Lớn: quản lý nhẹ nhưng đồng thời thấp; Nhỏ: quản lý nặng nhưng đồng thời cao).
- [ ] Trình bày 2 pha của 2PL (`확장 단계`, `축소 단계`) và nhớ rõ 2PL vẫn có thể bị Deadlock.
- [ ] Phân biệt rõ 연기 갱신 (chỉ REDO) và 즉각 갱신 (cả REDO và UNDO).
