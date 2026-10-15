# 187-189. 트랜잭션의 상태와 특성 (Transaction State & ACID)

## 학습 목표 (Mục tiêu)
- Nắm vững sơ đồ chuyển đổi 5 trạng thái vòng đời của Giao dịch (`트랜잭션의 5가지 상태`): Đang hoạt động (`활동 / Active`), Hoàn thành một phần (`부분 완료 / Partially Committed`), Đã hoàn tất (`완료 / Committed`), Thất bại (`실패 / Failed`), và Bị hủy bỏ (`철회 / Aborted`).
- Phân biệt điểm khác nhau mấu chốt giữa **Hoàn thành một phần (Partially Committed - `부분 완료`)** và **Đã hoàn tất (Committed - `완료`)**.
- Hiểu rõ cơ chế xử lý khi giao dịch rơi vào trạng thái Thất bại (`실패`) dẫn đến hành động Hủy bỏ / Phục hồi (`철회 / Rollback`).

## 핵심 키워드 (Từ khóa)
- 트랜잭션 상태 (Trạng thái giao dịch / Transaction States)
- 활동 (Đang hoạt động / Active)
- 부분 완료 (Hoàn thành một phần / Partially Committed)
- 완료 (Đã hoàn tất / Committed)
- 실패 (Thất bại / Failed)
- 철회 (Hủy bỏ hoàn tác / Aborted)
- 상태 전이도 (Sơ đồ chuyển đổi trạng thái / State Transition Diagram)
- Commit / Rollback

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([21-bai-hoc.md](21-bai-hoc.md), [22-bai-hoc.md](22-bai-hoc.md)):** Để bảo đảm đặc tính ACID của giao dịch, hệ quản trị cơ sở dữ liệu phải liên tục theo dõi và chuyển đổi chính xác từng trạng thái trong bộ nhớ và nhật ký (Log).
- **Tiếp nối sang các bài sau ([24-bai-hoc.md](24-bai-hoc.md), [25-bai-hoc.md](25-bai-hoc.md)):** Trạng thái giao dịch quyết định thời điểm giải phóng các Khóa tài nguyên (`Lock`) và điều phối tranh chấp trong cơ chế kiểm soát đồng thời.

## 읽는 방법 (Cách đọc)
- Học thuộc sơ đồ 2 nhánh rẽ trạng thái ở TẦNG A:
  - Nhánh thành công: **활동 (Active) $\rightarrow$ 부분 완료 (Partially Committed) $\rightarrow$ 완료 (Committed)**.
  - Nhánh thất bại: **활동 / 부분 완료 $\rightarrow$ 실패 (Failed) $\rightarrow$ 철회 (Aborted)**.
- Ghi nhớ câu phân biệt trắc nghiệm: **부분 완료 là trạng thái sau khi chạy xong lệnh cuối cùng NHƯNG TRƯỚC KHI THỰC HIỆN COMMIT LÊN ĐĨA CỨNG**.

---

## 187-189. 트랜잭션의 상태와 특성 (Transaction State & ACID)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Năm trạng thái trong vòng đời của Giao dịch (트랜잭션 5대 상태):**
  | Trạng thái | Tên tiếng Hàn & Anh | Khái niệm kỹ thuật chính xác | Thao tác tiếp theo |
  |---|---|---|---|
  | **Đang hoạt động** | `활동` (Active) | Trạng thái ban đầu khi giao dịch bắt đầu và đang trong quá trình thực thi các câu lệnh đọc/ghi dữ liệu. | Chuyển sang Hoàn thành một phần (nếu hết lệnh) hoặc Thất bại (nếu lỗi). |
  | **Hoàn thành một phần** | `부분 완료` (Partially Committed) | Trạng thái ngay sau khi câu lệnh cuối cùng của giao dịch đã thực thi xong, **nhưng thao tác ghi xác nhận (Commit) vật lý xuống đĩa cứng chưa hoàn tất**. | Nếu ghi đĩa thành công $\rightarrow$ Chuyển sang `완료`. Nếu lỗi I/O đĩa $\rightarrow$ Chuyển sang `실패`. |
  | **Đã hoàn tất** | `완료` (Committed) | Giao dịch đã thực thi thành công toàn bộ, lệnh `COMMIT` đã được xác nhận và dữ liệu đã được ghi an toàn vĩnh viễn vào CSDL. | Kết thúc giao dịch thành công. |
  | **Thất bại** | `실패` (Failed) | Trạng thái khi có sự cố phát sinh (lỗi logic, vi phạm toàn vẹn, lỗi phần cứng, chết tắc Deadlock) khiến giao dịch không thể tiếp tục thực thi bình thường. | DBMS chuẩn bị tiến hành thao tác hủy bỏ Rollback. |
  | **Bị hủy bỏ** | `철회` (Aborted) | Giao dịch đã bị chấm dứt dị thường và DBMS đã thực hiện xong lệnh `ROLLBACK` để hoàn tác toàn bộ dữ liệu trở về đúng trạng thái trước khi giao dịch bắt đầu. | Sau khi 철회, hệ thống có thể chọn: Khởi động lại giao dịch (Restart) hoặc Hủy bỏ hẳn (Kill). |

- **2. Sơ đồ luân chuyển trạng thái (상태 전이도):**
  $$\text{활동 (Active)} \longrightarrow \text{부분 완료 (Partially Committed)} \longrightarrow \mathbf{완료\ (Committed)}$$
  $$\downarrow \quad \qquad \qquad \qquad \qquad \downarrow$$
  $$\text{실패 (Failed)} \quad \longleftarrow \longleftarrow \longleftarrow \longleftarrow \longleftarrow \longleftarrow$$
  $$\downarrow$$
  $$\mathbf{철회\ (Aborted)}$$
- **주의/함정 (Bẫy đề thi hay gặp):**
  - Đề hỏi: *"Trạng thái sau khi chạy xong câu lệnh cuối cùng nhưng trước khi lệnh Commit hoàn tất được gọi là gì?"* $\rightarrow$ Đáp án: **부분 완료 (Partially Committed)**.
  - Đề hỏi: *"Sau khi giao dịch rơi vào trạng thái thất bại (실패), thao tác nào được thực hiện để đưa về trạng thái 철회?"* $\rightarrow$ Đáp án: **Rollback 연산 (Thao tác Rollback / Hoàn tác)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Vì sao cần tồn tại trạng thái "Hoàn thành một phần" (부분 완료)?**
  - Khi thực hiện các câu lệnh SQL trong ứng dụng, dữ liệu mới chỉ được cập nhật tạm thời trên bộ đệm RAM (Database Buffer Cache).
  - Ngay cả khi câu lệnh cuối cùng trong khối lệnh chạy xong, nếu chưa ghi thành công nhật ký và dữ liệu xuống đĩa cứng vật lý (Disk Flush / Redo Log Flush), hệ thống vẫn có thể bị sập nguồn.
  - Do đó, DBMS duy trì trạng thái **부분 완료** nhằm đảm bảo chỉ khi đĩa cứng xác nhận ghi thành công 100% thì mới công bố trạng thái **완료 (Committed)**.

### 복습 체크리스트
- [ ] Vẽ lại được sơ đồ chuyển đổi giữa 5 trạng thái giao dịch.
- [ ] Định nghĩa chính xác trạng thái 부분 완료 (Partially Committed).
- [ ] Phân biệt được 실패 (Failed) và 철회 (Aborted).
- [ ] Nêu được 2 hướng xử lý sau khi một giao dịch bị 철회 (khởi động lại hoặc hủy bỏ).
