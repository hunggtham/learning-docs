# 116 & 117: 형상 관리 도구 (SVN vs Git)

## 학습 목표 (Mục tiêu)
- So sánh đối đầu toàn diện giữa hai công cụ quản lý phiên bản đại diện cho hai trường phái kiến trúc: Subversion (SVN - Tập trung) và Git (Phân tán).
- Nắm vững cấu trúc thư mục kinh điển của SVN (Trunk, Branches, Tags) và cơ chế tăng chỉ số hiệu chỉnh (Revision).
- Hiểu rõ cơ chế lưu trữ ảnh chụp trạng thái (스냅샷 - Snapshot) của Git và quy trình luân chuyển dữ liệu qua 3 vùng làm việc: Working Directory $\rightarrow$ Staging Area $\rightarrow$ Local Repository $\rightarrow$ Remote Repository.

## 핵심 키워드 (Từ khóa)
- 형상 관리 도구 (Version Control Tools)
- Subversion (SVN / 중앙 집중형 Client-Server)
- 트렁크 (Trunk) & 브랜치 (Branches) & 태그 (Tags)
- 리비전 (Revision / 1씩 증가)
- Git (깃 / 분산 저장소 방식)
- 스냅샷 (Snapshot / Linus Torvalds)
- 스테이징 영역 (Staging Area / Index)
- 원격 저장소 (Remote Repo) vs 로컬 저장소 (Local Repo)

## 선행·연결 개념 (Kiến thức liên kết)
- [36-bai-hoc.md](36-bai-hoc.md): Khái niệm tổng quan về SCM và các thao tác Check-Out/Commit.
- [37-bai-hoc.md](37-bai-hoc.md): 3 mô hình kiến trúc phiên bản (Shared Folder, C/S, Distributed).
- [41-bai-hoc.md](41-bai-hoc.md): Đóng gói phần mềm (Software Packaging) và hướng dẫn cài đặt.

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh khi làm bài trắc nghiệm:
  - Thấy **"Trunk, Branches, Revision số nguyên tăng dần 1 đơn vị"** $\rightarrow$ **SVN (Subversion)**.
  - Thấy **"Phân tán (분산), Snapshot (스냅샷), do Linus Torvalds phát minh"** $\rightarrow$ **Git**.
- Nhớ quy trình Git 3 bước: `git add` (đưa vào Staging) $\rightarrow$ `git commit` (vào Local repo) $\rightarrow$ `git push` (lên Remote repo).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh chi tiết đối đầu giữa SVN và Git:**

| Tiêu chí so sánh | Subversion (SVN) | Git (깃) |
| :--- | :--- | :--- |
| **Mô hình kiến trúc** | **클라이언트 / 서버 (Client / Server tập trung)** | **분산 저장소 (Distributed Repository phân tán)** |
| **Tác giả / Năm phát hành** | Apache Software Foundation (2000) | **Linus Torvalds (2005)** |
| **Cơ chế lưu trữ dữ liệu** | **Lưu chênh lệch dòng (Delta / Diff-based)** giữa các phiên bản | **Lưu ảnh chụp toàn diện (스냅샷 - Snapshot)** của toàn bộ hệ thống tệp |
| **Đánh số phiên bản** | **Chỉ số Revision là số nguyên tăng dần** ($1, 2, 3 \dots$) trên toàn bộ kho lưu trữ | **Mã băm SHA-1 (40 ký tự hexa)** không theo thứ tự số học |
| **Cấu trúc phân nhánh** | Quy ước thư mục: `trunk` (chính), `branches` (con), `tags` (mốc đóng băng) | Nhánh là con trỏ siêu nhẹ (Lightweight Pointer) trỏ tới một commit |
| **Khả năng làm việc Offline** | **Không thể commit hay xem lịch sử** nếu mất mạng hoặc máy chủ tắt | **Làm việc offline hoàn toàn bình thường**, commit và tạo nhánh trên Local Repo |
| **Tốc độ và Hiệu năng** | Chậm hơn do phụ thuộc vào băng thông mạng khi tương tác với máy chủ | Cực nhanh do hầu hết thao tác diễn ra trực tiếp trên ổ cứng cục bộ |

- **Cấu trúc quản lý 3 vùng làm việc trong Git:**
  1. **Working Directory (작업 디렉터리):** Thư mục làm việc thực tế chứa các tệp mã nguồn đang được chỉnh sửa.
  2. **Staging Area / Index (스테이징 영역):** Vùng chuẩn bị lưu trữ tạm thời các thay đổi sẽ được đưa vào commit kế tiếp (thực hiện qua lệnh `git add`).
  3. **Local Repository (로컬 저장소):** Kho lưu trữ cục bộ nằm ngay trong thư mục ẩn `.git` trên máy tính cá nhân, ghi nhận vĩnh viễn commit (thực hiện qua lệnh `git commit`).
  4. **Remote Repository (원격 저장소):** Kho lưu trữ chia sẻ chung trên máy chủ (GitHub, GitLab, Bitbucket) để đồng bộ nhóm (thực hiện qua lệnh `git push / git pull`).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tại sao Git lại dùng mã băm SHA-1 thay cho số Revision tuần tự?**
  - Trong mô hình phân tán (Distributed), hàng chục lập trình viên có thể cùng commit offline trên máy tính cá nhân của mình cùng một lúc mà không cần máy chủ trung tâm.
  - Nếu dùng số tuần tự 1, 2, 3... thì khi gộp lại sẽ xảy ra trùng lặp số hiệu ngay lập tức.
  - Việc dùng mã băm SHA-1 (160-bit) bảo đảm tính duy nhất tuyệt đối trên toàn cầu và đồng thời chống giả mạo toàn vẹn dữ liệu mã nguồn.

### 복습 체크리스트
- [ ] Phân biệt được mô hình tập trung của SVN và mô hình phân tán của Git.
- [ ] Nhớ 3 thư mục quy ước của SVN: `trunk` (chính), `branches` (nhánh), `tags` (đóng băng).
- [ ] Nhớ Git lưu trữ theo cơ chế Snapshot và gán mã phiên bản bằng mã băm SHA-1.
- [ ] Vẽ được luồng di chuyển: Working Directory $\rightarrow$ Staging Area $\rightarrow$ Local Repo $\rightarrow$ Remote Repo.
