# 3. 트랜잭션의 상태 (Transaction States)

## 학습 목표 (Mục tiêu)
- Nắm vững chu trình vòng đời và 5 trạng thái kỹ thuật của Giao dịch (`트랜잭션 5대 상태`): Đang hoạt động (`활동`), Hoàn tất một phần (`부분 완료`), Hoàn tất vĩnh viễn (`완료`), Thất bại (`실패`), và Bị hủy bỏ (`철회`).
- Phân biệt rõ sự khác nhau cốt lõi giữa trạng thái `부분 완료 (Partially Committed)` và trạng thái `완료 (Committed)`.
- Hiểu chính xác sơ đồ chuyển đổi trạng thái của giao dịch khi gặp sự cố phần mềm hoặc phần cứng.

## 핵심 키워드 (Từ khóa)
- 트랜잭션 상태 (Trạng thái giao dịch / Transaction States)
- 활동 (Active / Đang thực thi)
- 부분 완료 (Partially Committed / Chưa ghi đĩa)
- 완료 (Committed / Ghi đĩa vĩnh viễn)
- 실패 (Failed / Phát sinh lỗi)
- 철회 (Aborted / Đã Rollback xong)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([2. Commit & Rollback 연산](45-bai-hoc.md)):** Sau khi xem xét hai thao tác Commit và Rollback, bài này hệ thống hóa các trạng thái nội tại bên trong của giao dịch do DBMS quản lý.
- **Tiếp nối sang bài sau ([4. 병행 제어 (Concurrency Control)](47-bai-hoc.md)):** Khảo sát các kỹ thuật điều phối và kiểm soát khi có hàng nghìn giao dịch cùng chuyển đổi trạng thái đồng thời.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nhớ điều kiện của trạng thái "Hoàn tất một phần" (Partially Committed): câu lệnh cuối cùng đã chạy xong nhưng dữ liệu mới nằm ở RAM/Buffer, CHƯA GHI ĐĨA; nếu mất điện ở bước này vẫn bị nhảy sang Failed!
- Đọc TẦNG B để theo dõi sơ đồ chuyển trạng thái logic chuẩn hóa dạng Mermaid.

---

## 3. 트랜잭션의 상태 (Transaction States)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **5 trạng thái trong vòng đời giao dịch (트랜잭션의 5가지 상태):**
  1. **활동 (Active - Đang hoạt động):**
     - Giao dịch đang trong quá trình thực thi các câu lệnh đọc (`READ`) và ghi (`WRITE`) dữ liệu.
  2. **부분 완료 (Partially Committed - Hoàn tất một phần):**
     - **Câu lệnh thao tác cuối cùng của giao dịch đã thực thi xong (`마지막 연산이 실행된 직후`)**, nhưng các thay đổi mới chỉ tạm thời nằm trong bộ đệm RAM (Buffer), **CHƯA ĐƯỢC GHI CHÍNH THỨC XUỐNG ĐĨA CỨNG**.
     - Ở trạng thái này, nếu hệ thống bị mất điện đột ngột hoặc xảy ra sự cố phần cứng, giao dịch vẫn có thể bị chuyển sang trạng thái Thất bại (`실패 - Failed`).
  3. **완료 (Committed - Hoàn tất vĩnh viễn):**
     - Thao tác COMMIT đã được thực thi thành công trọn vẹn, toàn bộ dữ liệu thay đổi đã được **ghi nhận vĩnh viễn xuống đĩa cứng (`데이터베이스에 영구적으로 반영됨`)**. Giao dịch kết thúc thành công.
  4. **실패 (Failed - Thất bại):**
     - Quá trình thực thi giao dịch không thể tiếp tục diễn ra bình thường do phát sinh lỗi phần mềm, lỗi logic, tràn bộ nhớ hoặc sự cố phần cứng (`더 이상 정상적인 실행을 진행할 수 없는 상태`).
  5. **철회 (Aborted - Bị hủy bỏ / Đã quay lui xong):**
     - Giao dịch đã bị dừng lại và hệ thống đã **thực hiện xong thao tác ROLLBACK (`롤백 연산 수행 완료`)**, đưa cơ sở dữ liệu quay trở về trạng thái ban đầu trước khi giao dịch bắt đầu. Sau khi Aborted, giao dịch có thể được khởi động lại (Restart) hoặc bị hủy bỏ hoàn toàn (Kill).
- **Sơ đồ chuyển đổi trạng thái cốt lõi:**
  - $\text{Active} \longrightarrow \text{Partially Committed} \longrightarrow \text{Committed}$ (Luồng thành công trọn vẹn).
  - $\text{Active} \longrightarrow \text{Failed} \longrightarrow \text{Aborted}$ (Gặp lỗi ngay khi đang chạy).
  - $\text{Partially Committed} \longrightarrow \text{Failed} \longrightarrow \text{Aborted}$ (Lệnh cuối chạy xong nhưng gặp lỗi khi đang ghi đĩa).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Trạng thái nào diễn ra ngay sau khi câu lệnh cuối cùng của giao dịch thực thi xong nhưng dữ liệu chưa được ghi vĩnh viễn xuống đĩa?"* -> **부분 완료 (Partially Committed)**, KHÔNG PHẢI 완료 (Committed).
  - **Bẫy 2:** *"Trạng thái Aborted (철회) diễn ra trước hay sau thao tác Rollback?"* -> **Sau khi thao tác Rollback đã hoàn tất (롤백 연산이 수행된 후)**.
  - **Bẫy 3:** *"Từ trạng thái Partially Committed có thể bị rơi vào Failed không?"* -> **Có thể (가능함)**, nếu quá trình ghi đĩa cuối cùng gặp sự cố phần cứng.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Active đang chạy, Partially Committed lệnh cuối xong chưa ghi đĩa, Committed ghi đĩa vĩnh viễn, Failed sinh lỗi, Aborted đã rollback xong".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Sơ đồ luồng chuyển trạng thái trực quan:**
  ```text
  [ 활동 (Active) ] ────(Lệnh cuối thực thi xong)────> [ 부분 완료 (Partially Committed) ] ────(Ghi đĩa thành công)────> [ 완료 (Committed) ]
         │                                                      │
         │ (Gặp lỗi giữa chừng)                                  │ (Lỗi khi đang ghi đĩa)
         ▼                                                      ▼
  [ 실패 (Failed) ] <───────────────────────────────────────────┘
         │
         │ (Thực hiện ROLLBACK khôi phục CSDL)
         ▼
  [ 철회 (Aborted) ]
  ```

### 복습 체크리스트
- [ ] Kể tên đủ 5 trạng thái của giao dịch: 활동, 부분 완료, 완료, 실패, 철회.
- [ ] Định nghĩa chuẩn trạng thái 부분 완료 (Partially Committed).
- [ ] Giải thích tại sao từ 부분 완료 vẫn có thể bị chuyển sang 실패 (Failed).
- [ ] Nhớ trạng thái 철회 (Aborted) là trạng thái sau khi đã hoàn tất Rollback.
