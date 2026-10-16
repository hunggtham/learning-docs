# 소프트웨어 형상 관리와 버전 제어 (Quản lý cấu hình phần mềm SCM và Git/SVN)

## 학습 목표
- Nắm vững định nghĩa và mục tiêu cốt lõi của Quản lý cấu hình phần mềm (`형상 관리 / SCM`): Tính hiển thị (`가시성`), Tính truy vết (`추적성`), và Ngăn ngừa thay đổi tùy tiện.
- Hiểu rõ khái niệm Đường cơ sở (`베이스라인 / Baseline`) và vai trò tối cao của Hội đồng kiểm soát thay đổi (`형상 통제 위원회 / CCB`) trong việc phê duyệt yêu cầu thay đổi (CR).
- Thuộc nằm lòng quy trình 4 bước SCM chuẩn: 형상 식별 (Identification) $\rightarrow$ 형상 통제 (Control) $\rightarrow$ 형상 감사 (Audit / V&V) $\rightarrow$ 형상 기록/보고 (Status Accounting).
- Phân biệt 3 mô hình kiến trúc công cụ quản lý phiên bản: Thư mục chia sẻ (`공유 폴더` - SCCS, RCS), Máy chủ tập trung (`클라이언트/서버` - CVS, SVN), và Phân tán (`분산 저장소` - Git).
- So sánh đối đầu giữa SVN (Delta, số Revision nguyên tăng dần, Trunk/Branches/Tags) vs Git (Snapshot, SHA-1 Hash, phân nhánh nhẹ, làm việc Offline hoàn hảo).

## 핵심 키워드
- 형상 관리 (Quản lý cấu hình / SCM / Software Configuration Management)
- 베이스라인 (Đường cơ sở / Baseline / 공식 승인된 기준점)
- CCB (형상 통제 위원회 / Configuration Control Board / 변경 승인·반려)
- SCM 4단계 (식별 Identification, 통제 Control, 감사 Audit, 기록·보고 Status Accounting)
- 버전 관리 도구 (공유 폴더 SCCS, 클라이언트/서버 SVN, 분산 저장소 Git)
- SVN vs Git (차이점 Delta vs 스냅샷 Snapshot / 리비전 Revision vs SHA-1 해시)
- Git 영역 (Working Directory, Staging Area, Local Repository, Remote Repository)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [11-dong-goi-phan-mem-va-drm.md](11-dong-goi-phan-mem-va-drm.md), chúng ta đã khảo sát quy trình đóng gói phần mềm phát hành và công nghệ bảo vệ bản quyền số DRM.
- **Đang giải quyết gì (Current Problem):** Khi phần mềm tiến hóa liên tục với hàng ngàn lần chỉnh sửa mã nguồn và tài liệu, nguy cơ ghi đè mã và mất kiểm soát phiên bản tăng vọt. Bài học này giải quyết việc thiết lập quy trình quản lý cấu hình có kỷ luật (SCM), kiểm soát qua Hội đồng CCB và sử dụng các công cụ kiểm soát phiên bản hiện đại (Git/SVN).
- **Dùng đi đâu (Forward Handoff):** Mã nguồn được quản lý an toàn trên kho Git sẽ làm đầu vào trực tiếp cho môi trường phát triển tích hợp (IDE) và các đường ống tự động hóa biên dịch, đóng gói CI/CD tại [13-ide-va-tu-dong-hoa-build.md](13-ide-va-tu-dong-hoa-build.md).

## 읽는 방법
- Đọc TẦNG A để thuộc lòng thứ tự 4 bước SCM (식별 $\rightarrow$ 통제 $\rightarrow$ 감사 $\rightarrow$ 기록/보고), vai trò của CCB và bảng so sánh trực diện SVN vs Git.
- Đọc TẦNG B để nắm chắc luồng dữ liệu 3 vùng làm việc của Git (`git add`, `git commit`, `git push`) và các mốc Baseline trong vòng đời phần mềm.

---

## 소프트웨어 형상 관리와 버전 제어

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Quy trình 4 bước quản lý cấu hình chuẩn (SCM 4단계 절차)
```
[1. 형상 식별] ────> [2. 형상 통제] ────> [3. 형상 감사] ────> [4. 형상 기록 / 보고]
(Identification)      (Control / CCB)       (Audit / V&V)       (Status Accounting)
```

| Bước | Tên tiếng Hàn & Anh | Nội dung hoạt động cốt lõi | Từ khóa nhận diện đề thi |
| :---: | :--- | :--- | :--- |
| **1** | **형상 식별 (Identification)** | Định danh các hạng mục cấu hình (SCI), cấu trúc phân cấp, thiết lập **Baseline ban đầu** | 베이스라인 설정, 항목 식별 |
| **2** | **형상 통제 (Control)** | Tiếp nhận phiếu CR; **Hội đồng CCB** thẩm định và phê duyệt; kiểm soát phiên bản | **CCB 변경 통제 위원회**, 변경 승인/반려 |
| **3** | **형상 감사 (Audit)** | Đánh giá độc lập xem thay đổi có đúng phê duyệt CCB không; kiểm tra tính toàn vẹn (**V&V**) | **무결성 검증**, 베이스라인 일치 확인 |
| **4** | **형상 기록 / 보고 (Accounting)**| Ghi nhận nhật ký lịch sử, biên bản họp CCB và báo cáo tình trạng cấu hình | **상태 보고**, 이력 기록, 변경 통계 |

#### 2. So sánh đối đầu kỹ thuật: SVN vs Git
| Tiêu chí so sánh | Subversion (SVN) | Git (깃) |
| :--- | :--- | :--- |
| **Kiến trúc** | **클라이언트/서버 방식 (Tập trung)** | **분산 저장소 방식 (Phân tán)** |
| **Cơ chế lưu trữ** | Lưu trữ sai biệt giữa các phiên bản (**Delta / Diff**) | Chụp lại toàn bộ trạng thái hệ thống tệp (**스냅샷 - Snapshot**) |
| **Đánh chỉ số phiên bản** | Số nguyên tăng dần 1 đơn vị (**리비전 - Revision**: r1, r2, r3) | Mã băm an toàn 40 ký tự (**SHA-1 Hash**) |
| **Cấu trúc nhánh** | **Trunk** (nhánh chính), **Branches**, **Tags** | Phân nhánh nhẹ (Lightweight Branching), nhánh `main`/`master` |
| **Làm việc Offline** | Không thể (mọi commit/log bắt buộc nối mạng server) | Hoàn hảo (mọi commit, branch, diff, log thực hiện trên Local Repo) |
| **Tác giả khởi xướng** | Quỹ phần mềm Apache (CollabNet) | **Linus Torvalds** (người sáng tạo nhân Linux) |

#### 3. Bảng phân loại 3 mô hình kiến trúc công cụ phiên bản
| Mô hình | Nguyên lý vận hành | Ưu điểm & Nhược điểm | Công cụ đại diện |
| :--- | :--- | :--- | :--- |
| **Thư mục chia sẻ** | Đặt tệp mã nguồn chung trong thư mục mạng LAN | Đơn giản; **Dễ bị ghi đè mất mã**, không hỗ trợ nhánh phức tạp | SCCS, RCS, PVCS |
| **Client/Server** | Máy chủ trung tâm (**Central Repo**) lưu toàn bộ lịch sử | Quản lý tập trung; **Điểm lỗi đơn (SPOF)**, mất mạng là ngừng việc | **CVS, SVN (Subversion)** |
| **Phân tán** | Mỗi máy cá nhân là một kho đầy đủ (**Local Repo**) | Tốc độ cực nhanh, làm việc offline, an toàn cao | **Git**, Mercurial |

#### 4. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Vai trò của CCB:** Hội đồng kiểm soát thay đổi (**형상 통제 위원회 / CCB**) có quyền tiếp nhận, thẩm định và phê duyệt (Approve/Reject) các yêu cầu thay đổi (CR), diễn ra trong bước **형상 통제 (Configuration Control)**.
- **Bẫy 2: Thứ tự 4 bước SCM:** Bắt buộc nhớ câu thần chú: **식별 (Identification) $\rightarrow$ 통제 (Control) $\rightarrow$ 감사 (Audit) $\rightarrow$ 기록/보고 (Accounting)**.
- **Bẫy 3: Cơ chế lưu trữ Snapshot của Git:** Git quản lý phiên bản bằng cơ chế **스냅샷 (Snapshot)**, không phải lưu trữ chênh lệch từng dòng delta như SVN.
- **Bẫy 4: Quản lý Baseline:** Khi đã đạt trạng thái Baseline, **không ai được phép tự ý sửa trực tiếp**, mọi thay đổi bắt buộc phải qua CCB phê duyệt.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Luồng di chuyển dữ liệu trong Git: 3 vùng làm việc
```
[Working Directory] ──(git add)──► [Staging Area / Index] ──(git commit)──► [Local Repository] ──(git push)──► [Remote Repository]
  (Mã đang sửa)                       (Vùng chuẩn bị commit)                     (Kho máy cục bộ)                 (Kho GitHub/GitLab)
```
- `Working Directory`: Thư mục chứa các tệp mã nguồn mà lập trình viên đang trực tiếp soạn thảo trên máy.
- `Staging Area (Index)`: Vùng đệm chứa ảnh chụp các tệp đã được đánh dấu sẵn sàng để ghi vào lịch sử (`git add`).
- `Local Repository`: Kho lưu trữ hoàn chỉnh nằm ẩn trong thư mục `.git`, lưu trữ vĩnh viễn các commit kèm mã băm SHA-1 trên máy trạm (`git commit`).
- `Remote Repository`: Kho lưu trữ máy chủ dùng chung (GitHub, GitLab) để chia sẻ mã nguồn với nhóm (`git push` / `git pull`).

#### 2. Các mốc Đường cơ sở (Baseline) trong SDLC
1. `기능 베이스라인 (Functional Baseline)`: Thiết lập sau khi hoàn thành phân tích yêu cầu SRS.
2. `분배 베이스라인 (Allocated Baseline)`: Thiết lập sau giai đoạn thiết kế kiến trúc tổng thể.
3. `설계 베이스라인 (Design Baseline)`: Thiết lập sau khi hoàn thành thiết kế chi tiết từng module.
4. `제품 베이스라인 (Product Baseline)`: Thiết lập khi đóng gói sản phẩm hoàn chỉnh để bàn giao.

---

### 복습 체크리스트
- [ ] Định nghĩa mục tiêu của SCM: Tính hiển thị, Tính truy vết, Ngăn ngừa thay đổi tùy tiện.
- [ ] Nhớ Đường cơ sở (Baseline) là mốc chuẩn đã được phê duyệt, cấm tự ý sửa đổi.
- [ ] Nắm rõ vai trò của Hội đồng CCB trong bước 형상 통제.
- [ ] Thuộc lòng thứ tự 4 bước: 형상 식별 $\rightarrow$ 형상 통제 $\rightarrow$ 형상 감사 $\rightarrow$ 형상 기록/보고.
- [ ] Phân loại 3 kiến trúc: Thư mục chia sẻ, Client/Server (SVN - SPOF), Phân tán (Git - Local Repo).
- [ ] So sánh SVN (Delta, số Revision) vs Git (Snapshot, SHA-1 Hash, tác giả Linus Torvalds).
- [ ] Nắm vững luồng 3 vùng làm việc của Git: Working Directory $\rightarrow$ Staging Area $\rightarrow$ Local Repo $\rightarrow$ Remote Repo.
