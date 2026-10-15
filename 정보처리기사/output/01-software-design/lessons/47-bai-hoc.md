# 4. 병행 제어 (Concurrency Control)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và mục tiêu của Kiểm soát đồng thời (`병행 제어 - Concurrency Control`) trong việc đảm bảo tính toàn vẹn khi nhiều giao dịch chạy song song.
- Thuộc nằm lòng 4 hiện tượng bất thường nghiêm trọng xảy ra nếu không kiểm soát đồng thời: Mất mát cập nhật (`갱신 분실`), Mâu thuẫn dữ liệu (`모순성`), Quay lui dây chuyền (`연쇄 복귀`), và Đọc dữ liệu rác (`비인가 변화 / Dirty Read`).
- Nắm vững 4 kỹ thuật kiểm soát đồng thời kinh điển: Khóa (`로킹 - Locking` và giao thức `2PL`), Nhãn thời gian (`타임스탬프`), Kiểm soát lạc quan (`낙관적 검증`), và Đa phiên bản (`MVCC`).

## 핵심 키워드 (Từ khóa)
- 병행 제어 (Kiểm soát đồng thời / Concurrency Control)
- 갱신 분실 (Lost Update / 덮어쓰기 오류)
- 모순성 (Inconsistency / 불일치성)
- 연쇄 복귀 (Cascading Rollback / 연쇄 철회)
- 비인가 변화 (Dirty Read / 미완료 데이터 판독)
- 로킹 (Locking / S-Lock vs X-Lock)
- 2단계 로킹 규약 (2PL - Two-Phase Locking / 확장 단계 + 축소 단계)
- 타임스탬프 순서 (Timestamp Ordering)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([3. 트랜잭션의 상태 (Transaction States)](46-bai-hoc.md)):** Sau khi xem xét trạng thái vòng đời của một giao dịch đơn lẻ, bài này giải quyết bài toán xung đột tài nguyên khi hàng nghìn giao dịch cùng đọc/ghi đồng thời.
- **Tiếp nối sang bài sau ([5. 보안 및 암호화 (Security & Encryption)](48-bai-hoc.md)):** Chuyển từ tầng kiểm soát truy cập đồng thời sang tầng bảo mật, mã hóa dữ liệu và phân quyền người dùng (DAC, MAC, RBAC).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc 4 hiện tượng bất thường (갱신 분실, 모순성, 연쇄 복귀, 비인가 변화) và phân biệt S-Lock (khóa chia sẻ cho phép nhiều người cùng đọc) vs X-Lock (khóa độc quyền cấm tiệt người khác).
- Đọc TẦNG B để hiểu cơ chế 2 pha của giao thức 2PL: Pha mở rộng chỉ được xin khóa (cấm nhả khóa), Pha thu hẹp chỉ được nhả khóa (cấm xin thêm khóa mới).

---

## 4. 병행 제어 (Concurrency Control)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Định nghĩa Kiểm soát đồng thời):**
  - Là kỹ thuật do DBMS thực hiện nhằm điều phối và kiểm soát việc nhiều giao dịch (`다중 트랜잭션`) cùng thực thi đồng thời và chia sẻ dữ liệu chung, nhằm **tối đa hóa thông lượng (`처리량 - Throughput`)**, **tối thiểu hóa thời gian đáp ứng (`응답 시간 - Response Time`)**, và **bảo vệ tính toàn vẹn, nhất quán của cơ sở dữ liệu**.
- **4 hiện tượng bất thường khi KHÔNG kiểm soát đồng thời:**
  1. `갱신 분실 (Lost Update - Mất mát cập nhật)`:
     - Hai giao dịch cùng truy cập một mẩu dữ liệu; giao dịch chạy sau ghi đè kết quả lên dữ liệu đã được cập nhật bởi giao dịch chạy trước, làm cho kết quả của giao dịch trước **hoàn toàn bị biến mất (`갱신 결과가 무효화됨`)**.
  2. `모순성 (Inconsistency - Tính mâu thuẫn / 불일치성)`:
     - Một giao dịch đọc cùng một bản ghi nhiều lần trong khi giao dịch khác xen vào sửa đổi dữ liệu giữa chừng, dẫn đến việc các lần đọc cho ra kết quả không nhất quán hoặc tổng giá trị bị sai lệch.
  3. `연쇄 복귀 / 연쇄 철회 (Cascading Rollback - Quay lui dây chuyền)`:
     - Giao dịch $T_1$ đọc dữ liệu tạm thời chưa commit của giao dịch $T_2$. Khi $T_2$ gặp lỗi và thực hiện Rollback, giao dịch $T_1$ cũng **bị buộc phải Rollback theo**, kéo theo hàng loạt giao dịch khác đang chờ cũng bị hủy bỏ dây chuyền.
  4. `비인가 변화 / 판독 불가 (Dirty Read / Uncommitted Dependency)`:
     - Giao dịch đọc phải dữ liệu bị lỗi hoặc chưa được commit chính thức của một giao dịch khác đang thực thi dở dang.
- **4 kỹ thuật kiểm soát đồng thời kinh điển:**
  - **1. 로킹 (Locking - Kỹ thuật khóa):**
     - Trước khi truy xuất dữ liệu, giao dịch phải xin cấp quyền khóa; sau khi xong phải mở khóa (Unlock).
     - `공유 로크 (Shared Lock / S-Lock - Khóa chia sẻ)`: Dùng khi **ĐỌC dữ liệu**. Nhiều giao dịch có thể cùng giữ S-Lock trên một dữ liệu (cho phép cùng đọc), nhưng không ai được ghi.
     - `전속 로크 (Exclusive Lock / X-Lock - Khóa độc quyền)`: Dùng khi **GHI/SỬA dữ liệu**. Chỉ duy nhất một giao dịch được giữ X-Lock; không cho phép bất kỳ ai khác đọc hay ghi.
     - `2단계 로킹 규약 (2PL - Two-Phase Locking Protocol)`:
       - Đảm bảo tính tuần tự khả thi (Serializability). Gồm 2 pha:
         - **확장 단계 (Growing Phase - Pha mở rộng):** Chỉ được xin thêm khóa (`Lock만 가능`), cấm nhả khóa.
         - **축소 단계 (Shrinking Phase - Pha thu hẹp):** Chỉ được nhả khóa (`Unlock만 가능`), cấm xin thêm khóa mới.
       - *Nhược điểm:* Vẫn có thể xảy ra hiện tượng **Bế tắc (`교착 상태 - Deadlock`)**.
  - **2. 타임스탬프 순서 (Timestamp Ordering - Nhãn thời gian):**
     - Gán nhãn thời gian duy nhất cho từng giao dịch lúc bắt đầu; nếu có xung đột, giao dịch nào đến trước sẽ được ưu tiên thực thi trước, loại bỏ hoàn toàn nguy cơ Deadlock.
  - **3. 낙관적 병행 제어 (Optimistic Concurrency Control):**
     - Giả định rằng rất hiếm khi xảy ra xung đột; cho phép các giao dịch tự do đọc/ghi trên bộ đệm cục bộ, chỉ kiểm tra tính hợp lệ (Validation) tại thời điểm chuẩn bị Commit.
  - **4. 다중 버전 병행 제어 (MVCC - Multi-Version Concurrency Control):**
     - Lưu trữ nhiều phiên bản lịch sử của cùng một bản ghi dữ liệu, giúp giao dịch đọc luôn nhìn thấy ảnh chụp nhất quán mà không bao giờ bị chặn bởi giao dịch ghi.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Hiện tượng giao dịch sau ghi đè làm mất kết quả của giao dịch trước gọi là gì?"* -> **갱신 분실 (Lost Update)**.
  - **Bẫy 2:** *"Trong giao thức 2PL, pha thu hẹp (Shrinking Phase) có được phép xin thêm khóa mới không?"* -> **Tuyệt đối KHÔNG**. Pha thu hẹp chỉ được phép nhả khóa (Unlock).
  - **Bẫy 3:** *"Giao thức 2PL có đảm bảo loại bỏ hoàn toàn bế tắc (Deadlock) không?"* -> **KHÔNG loại bỏ được Deadlock (교착상태 발생 가능)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Không kiểm soát sinh ra 4 họa: Mất cập nhật, Mâu thuẫn, Quay lui dây chuyền, Đọc bẩn; Kiểm soát dùng Khóa 2PL (mở rộng xin khóa, thu hẹp nhả khóa), Nhãn thời gian, Lạc quan và MVCC".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tương tác tương thích giữa các loại khóa (Lock Compatibility Matrix):**
  - Nếu đối tượng $A$ đang bị giữ **S-Lock**: Giao dịch khác xin thêm S-Lock $\rightarrow$ **Được chấp thuận**; xin X-Lock $\rightarrow$ **Bị chặn (Wait)**.
  - Nếu đối tượng $A$ đang bị giữ **X-Lock**: Giao dịch khác xin S-Lock hoặc X-Lock $\rightarrow$ **Đều bị chặn hoàn toàn (Wait)** cho đến khi X-Lock được nhả.

### 복습 체크리스트
- [ ] Kể tên đủ 4 hiện tượng bất thường khi không kiểm soát đồng thời: 갱신 분실, 모순성, 연쇄 복귀, 비인가 변화.
- [ ] Phân biệt được quyền hạn của S-Lock (chỉ đọc) và X-Lock (độc quyền đọc ghi).
- [ ] Giải thích được 2 giai đoạn của giao thức 2PL: 확장 단계 (chỉ lock) và 축소 단계 (chỉ unlock).
- [ ] Khẳng định được 2PL vẫn có thể phát sinh 교착 상태 (Deadlock).
