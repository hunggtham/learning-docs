# 12. Quản lý cấu hình phần mềm (SCM) và Công cụ kiểm soát phiên bản (Git, SVN)

## 1. Tổng quan về Quản lý cấu hình phần mềm (SCM 개요)

Trong suốt vòng đời phát triển phần mềm (SDLC), hàng trăm tệp tài liệu, yêu cầu nghiệp vụ, sơ đồ thiết kế, mã nguồn và kịch bản kiểm thử liên tục thay đổi theo thời gian. Nếu không có cơ chế quản trị chặt chẽ, các nhà phát triển sẽ dễ dàng ghi đè mã nguồn của nhau, làm mất phiên bản hoạt động ổn định và không thể truy vết nguyên nhân gây lỗi.

**형상 관리 (Software Configuration Management - SCM: Quản lý cấu hình phần mềm)** là quy trình kỹ nghệ quản lý có hệ thống mọi thay đổi phát sinh đối với tất cả các sản phẩm trung gian và sản phẩm bàn giao (Artifacts) trong toàn bộ vòng đời phát triển.

### 1.1. Mục tiêu cốt lõi của SCM
- **Tính hiển thị (가시성 - Visibility):** Giúp toàn bộ nhóm phát triển và các bên liên quan nắm bắt được trạng thái tiến độ hiện tại của từng thành phần.
- **Tính truy vết nguồn gốc (추적성 - Traceability):** Cho phép truy cứu nguồn gốc của từng dòng mã: Ai đã sửa? Sửa vào thời điểm nào? Vì lý do nghiệp vụ gì?
- **Ngăn ngừa thay đổi tùy tiện (무절제한 변경 방지):** Đảm bảo mọi sự thay đổi đều phải được xem xét, phê duyệt chính thức trước khi áp dụng vào sản phẩm.

### 1.2. Hạng mục cấu hình phần mềm (형상 항목 - Software Configuration Item / SCI)
SCM không chỉ quản lý mã nguồn (Source Code) mà quản trị tất cả các sản phẩm trí tuệ trong dự án:
- Bản đặc tả yêu cầu người dùng (SRS).
- Tài liệu thiết kế kiến trúc và mô tả dữ liệu.
- Mã nguồn lập trình (Source Files, Scripts, SQL DDL/DML).
- Kịch bản kiểm thử (Test Cases), dữ liệu kiểm thử và kết quả chạy test.
- Tài liệu hướng dẫn sử dụng và ghi chú phát hành (Manuals, Release Notes).

---

## 2. Đường cơ sở (Baseline) và Hội đồng kiểm soát thay đổi (CCB)

### 2.1. Đường cơ sở (베이스라인 - Baseline)
- **Định nghĩa:** Baseline là trạng thái được chính thức thẩm định và phê chuẩn (Formally Reviewed & Agreed Upon) của một hoặc nhiều hạng mục cấu hình tại một mốc thời gian cụ thể.
- **Nguyên tắc kỹ thuật:** Khi một sản phẩm đã đạt đến trạng thái Baseline, **không ai được phép tự ý chỉnh sửa trực tiếp**. Mọi sửa đổi sau đó đều phải tuân theo một quy trình kiểm soát thay đổi nghiêm ngặt và tạo ra một Baseline mới.
- **Các mốc Baseline tiêu biểu trong SDLC:**
  1. *기능 베이스라인 (Functional Baseline):* Thiết lập sau khi hoàn thành phân tích yêu cầu.
  2. *분배 베이스라인 (Allocated Baseline):* Thiết lập sau giai đoạn thiết kế kiến trúc tổng thể.
  3. *설계 베이스라인 (Design Baseline):* Thiết lập sau khi hoàn thành thiết kế chi tiết từng module.
  4. *제품 베이스라인 (Product Baseline):* Thiết lập khi đóng gói sản phẩm hoàn chỉnh để bàn giao.

### 2.2. Hội đồng kiểm soát thay đổi (형상 통제 위원회 - CCB: Configuration Control Board)
- **Định nghĩa:** Là nhóm chuyên gia và đại diện các bên liên quan (Project Manager, Lead Developer, QA Manager, Khách hàng) có thẩm quyền cao nhất trong việc quản trị cấu hình.
- **Vai trò thi:** Tiếp nhận các Phiếu yêu cầu thay đổi (**CR - Change Request**), phân tích mức độ ảnh hưởng kỹ thuật/chi phí/tiến độ, và ra quyết định chính thức: **Phê duyệt (Approve)** hoặc **Bác bỏ (Reject)** sự thay đổi đối với Baseline.

---

## 3. Quy trình 4 bước quản lý cấu hình chuẩn (형상 관리 4단계 절차)

Đề thi Kỹ sư xử lý thông tin luôn kiểm tra thứ tự và nội dung chuẩn của 4 bước SCM theo mô hình: **"Nhận dạng $\rightarrow$ Kiểm soát $\rightarrow$ Kiểm toán $\rightarrow$ Ghi chép / Báo cáo"** (식별 $\rightarrow$ 통제 $\rightarrow$ 감사 $\rightarrow$ 기록).

```
[1. 형상 식별] ────► [2. 형상 통제] ────► [3. 형상 감사] ────► [4. 형상 기록 / 보고]
(Identification)      (Control / CCB)       (Audit / V&V)       (Status Accounting)
```

| Bước | Tên tiếng Hàn (English) | Nội dung hoạt động cốt lõi | Từ khóa thi |
| :--- | :--- | :--- | :--- |
| **1** | **형상 식별 (Configuration Identification)** | Xác định danh mục các hạng mục cấu hình (SCI), đặt mã định danh duy nhất, phân cấp cấu trúc và thiết lập **Baseline ban đầu** | 베이스라인 설정, 항목 식별, 트리 구조 정의 |
| **2** | **형상 통제 (Configuration Control)** | Tiếp nhận yêu cầu thay đổi (CR), **Hội đồng CCB** thẩm định và phê duyệt; áp dụng cơ chế Check-in/Check-out để kiểm soát phiên bản | **CCB 변경 통제 위원회**, 변경 승인/반려, 버전 제어 |
| **3** | **형상 감사 (Configuration Audit)** | Đánh giá độc lập xem các thay đổi có được thực hiện đúng theo phê chuẩn của CCB hay không; xác minh tính toàn vẹn cấu hình (**V&V**) | **무결성 검증**, 베이스라인 일치 검사, V&V |
| **4** | **형상 기록 / 보고 (Configuration Status Accounting)** | Ghi nhận nhật ký lịch sử mọi thay đổi, lưu trữ biên bản họp CCB và lập báo cáo định kỳ tình trạng cấu hình cho các bên liên quan | **상태 보고**, 이력 기록, 변경 통계 집계 |

---

## 4. Ba mô hình kiến trúc công cụ quản lý phiên bản (버전 관리 도구 방식)

Lịch sử phát triển của các hệ thống kiểm soát phiên bản (Version Control System - VCS) trải qua 3 thế hệ kiến trúc:

```
[Thế hệ 1: Thư mục chia sẻ]      [Thế hệ 2: Client / Server]        [Thế hệ 3: Phân tán (Distributed)]
      (Shared Folder)                  (Centralized)                            (Decentralized)
  ┌──────────────────┐             ┌──────────────────┐             ┌─────────────┐   ┌─────────────┐
  │ Thư mục mạng LAN │             │ Máy chủ trung tâm│             │ Máy Dev A   │   │ Máy Dev B   │
  │ (SCCS, RCS, PVCS)│             │ (CVS, SVN)       │             │ (Local Repo)│   │ (Local Repo)│
  └──────────────────┘             └────────▲─────────┘             └──────▲──────┘   └──────▲──────┘
    ▲              ▲                        │                              │                 │
    │ (Ghi đè dễ   │ (Mất mạng =            │ Commit / Update              └────────┬────────┘
    │  xung đột)   │  ngừng việc)           │                                       │ Push / Pull
  ┌─┴──────┐    ┌──┴─────┐             ┌────┴─────┐ ┌────────┐                ┌─────▼──────────┐
  │ Dev A  │    │ Dev B  │             │ Dev A    │ │ Dev B  │                │ Remote Server  │
  └────────┘    └────────┘             └──────────┘ └────────┘                │ (GitHub, Git)  │
                                                                              └────────────────┘
```

| Mô hình | Nguyên lý vận hành | Ưu điểm & Nhược điểm | Công cụ đại diện |
| :--- | :--- | :--- | :--- |
| **공유 폴더 방식 (Shared Folder)** | Đặt tệp mã nguồn chung trong một thư mục mạng LAN; các lập trình viên cùng truy cập và chỉnh sửa trực tiếp | Đơn giản, không cần cấu hình phức tạp; **Dễ bị ghi đè mất mã nguồn**, không hỗ trợ rẽ nhánh phức tạp | **SCCS, RCS, PVCS** |
| **클라이언트/서버 방식 (Client/Server)** | Một máy chủ trung tâm (**Central Repository**) lưu trữ toàn bộ lịch sử; client kéo mã về, sửa đổi rồi commit trực tiếp lên server | Quản lý tập trung, phân quyền chặt chẽ; **Điểm lỗi đơn (SPOF - Single Point of Failure)**, mất kết nối mạng là không thể làm việc | **CVS, SVN (Subversion)**, ClearCase |
| **분산 저장소 방식 (Distributed Repo)** | Mỗi máy cá nhân của lập trình viên là một kho lưu trữ đầy đủ (**Local Repository**); đồng bộ qua lại với kho từ xa (**Remote Repo**) | Tốc độ cực nhanh, làm việc offline hoàn toàn; an toàn cao (mỗi máy là một bản backup); đòi hỏi hiểu sâu quy trình nhánh | **Git**, Mercurial, BitKeeper |

---

## 5. So sánh đối đầu kỹ thuật: SVN vs Git (형상 관리 도구 비교)

Trong các bài thi trắc nghiệm Kỹ sư xử lý thông tin, hai công cụ đại diện tiêu biểu nhất cho trường phái Tập trung và Phân tán luôn được đem ra so sánh:

| Tiêu chí so sánh | Subversion (SVN) | Git (깃) |
| :--- | :--- | :--- |
| **Kiến trúc** | **클라이언트/서버 방식 (Tập trung)** | **분산 저장소 방식 (Phân tán)** |
| **Cơ chế lưu trữ** | Lưu trữ sự sai biệt giữa các phiên bản (**Delta / Diff**) | Chụp lại toàn bộ trạng thái hệ thống tệp (**스냅샷 - Snapshot**) |
| **Đánh chỉ số phiên bản** | Sử dụng số nguyên tăng dần 1 đơn vị (**리비전 - Revision**: r1, r2, r3...) | Sử dụng mã băm an toàn 40 ký tự (**SHA-1 Hash**) |
| **Cấu trúc nhánh kinh điển** | **Trunk** (nhánh chính), **Branches** (nhánh rẽ), **Tags** (nhãn mốc) | Phân nhánh nhẹ (Lightweight Branching), nhánh mặc định `main` (hoặc `master`) |
| **Khả năng làm việc Offline** | Không thể (mọi thao tác commit/log đều bắt buộc phải nối mạng với máy chủ) | Hoàn hảo (mọi thao tác commit, branch, diff, log thực hiện trên Local Repo) |
| **Tác giả khởi xướng** | Quỹ phần mềm Apache (CollabNet) | **Linus Torvalds** (người sáng lập nhân hệ điều hành Linux) |

### 5.1. Luồng di chuyển dữ liệu trong Git: 3 vùng làm việc
Git tổ chức quy trình quản lý mã nguồn qua 3 vùng làm việc cục bộ và 1 kho từ xa:

```
[Working Directory] ──(git add)──► [Staging Area / Index] ──(git commit)──► [Local Repository] ──(git push)──► [Remote Repository]
  (Mã đang sửa)                       (Vùng chuẩn bị commit)                     (Kho máy cục bộ)                 (Kho GitHub/GitLab)
```

- **Working Directory:** Thư mục chứa các tệp mã nguồn mà lập trình viên đang trực tiếp soạn thảo trên máy.
- **Staging Area (Index):** Vùng đệm chứa ảnh chụp các tệp đã được đánh dấu sẵn sàng để ghi vào lịch sử (`git add`).
- **Local Repository:** Kho lưu trữ hoàn chỉnh nằm ẩn trong thư mục `.git`, lưu trữ vĩnh viễn các commit kèm mã băm SHA-1 trên máy trạm (`git commit`).
- **Remote Repository:** Kho lưu trữ máy chủ dùng chung (GitHub, GitLab, Bitbucket) để chia sẻ mã nguồn với cả nhóm (`git push` / `git pull`).

---

## 6. Câu hỏi ôn tập và bẫy đề thi thực tế

1. **Nhận diện vai trò của CCB:**
   - *Câu hỏi:* Trong quy trình quản lý cấu hình phần mềm SCM, tổ chức nào có thẩm quyền chính thức tiếp nhận, thẩm định và phê duyệt các Phiếu yêu cầu thay đổi (CR - Change Request) đối với Baseline?
   - *Đáp án chuẩn thi:* **형상 통제 위원회 (CCB - Configuration Control Board)**, diễn ra trong bước **형상 통제 (Configuration Control)**.
2. **Thần chú 4 bước SCM:**
   - *Bẫy đề thi:* Sắp xếp thứ tự: "Kiểm toán $\rightarrow$ Nhận dạng $\rightarrow$ Kiểm soát $\rightarrow$ Báo cáo" $\rightarrow$ **SAI**. Thứ tự chuẩn bắt buộc phải là: **형상 식별 (Identification) $\rightarrow$ 형상 통제 (Control) $\rightarrow$ 형상 감사 (Audit) $\rightarrow$ 형상 기록 / 보고 (Status Accounting)**.
3. **Cơ chế lưu trữ của Git vs SVN:**
   - *Câu hỏi:* Git quản lý các phiên bản tệp tin bằng cơ chế nào sau đây?
   - *Đáp án chuẩn thi:* **스냅샷 (Snapshot)** — chụp lại toàn bộ trạng thái cây tệp tin tại thời điểm commit, thay vì chỉ lưu trữ phần chênh lệch delta từng dòng như các hệ thống cũ.
4. **Đặc trưng của công cụ SVN:**
   - *Câu hỏi:* Một công cụ kiểm soát phiên bản theo mô hình Client/Server, quản lý lịch sử thông qua số Revision nguyên tăng dần theo từng lượt commit và tổ chức cây thư mục dạng Trunk, Branches, Tags là công cụ nào?
   - *Đáp án chuẩn thi:* **Subversion (SVN)**.

---

## 7. Liên kết bài học tiếp theo

Bên cạnh việc quản lý mã nguồn bằng SCM, quy trình phát triển phần mềm hiện đại phụ thuộc chặt chẽ vào Môi trường phát triển tích hợp (IDE) và các Công cụ tự động hóa quá trình biên dịch, đóng gói và tích hợp liên tục (CI/CD). Tiếp tục với **[13-ide-va-tu-dong-hoa-build.md](13-ide-va-tu-dong-hoa-build.md)** để tìm hiểu về Eclipse, IntelliJ, Maven, Gradle và Jenkins.
