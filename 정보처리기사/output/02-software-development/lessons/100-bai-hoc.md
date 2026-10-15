# 113 ~ 115: 버전 관리 도구 방식 (Version Control Tool Types)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm và vai trò của các công cụ quản lý phiên bản mã nguồn (버전 관리 도구 - Version Control Tools / SCM).
- Phân biệt sâu sắc và toàn diện 3 thế hệ kiến trúc công cụ quản lý phiên bản trong đề thi: Phương thức thư mục chia sẻ (공유 폴더 방식), Phương thức Máy khách / Máy chủ tập trung (클라이언트/서버 방식), và Phương thức Kho lưu trữ phân tán (분산 저장소 방식).
- Nhớ tên, cơ chế hoạt động, cùng ưu và nhược điểm kỹ thuật của từng công cụ đại diện: SCCS, RCS, CVS, SVN, và Git.

## 핵심 키워드 (Từ khóa)
- 버전 관리 도구 (Version Control Tools)
- 공유 폴더 방식 (Shared Folder / SCCS, RCS, PVCS)
- 클라이언트/서버 방식 (Client/Server / CVS, SVN, ClearCase)
- 분산 저장소 방식 (Distributed Repository / Git, Mercurial, BitKeeper)
- 중앙 집중형 (Centralized Architecture / 단일 장애점 SPOF)
- 로컬 저장소 vs 원격 저장소 (Local Repo vs Remote Repo)
- Commit & Push (로컬 커밋 후 원격 전송)

## 선행·연결 개념 (Kiến thức liên kết)
- [99-bai-hoc.md](99-bai-hoc.md): Tài liệu hướng dẫn sử dụng và cài đặt phần mềm.
- [101-bai-hoc.md](101-bai-hoc.md): Phân loại phần mềm và giấy phép bản quyền.
- [37-bai-hoc.md](37-bai-hoc.md): Ba mô hình kiến trúc quản lý phiên bản SCM.

## 읽는 방법 (Cách đọc)
- Ghi nhớ 3 thế hệ tiến hóa của công cụ quản lý phiên bản:
  - **Thế hệ 1 - 공유 폴더 (Thư mục chia sẻ):** Đặt code chung trên 1 thư mục mạng LAN. Ai muốn sửa thì ghi đè trực tiếp $\rightarrow$ Cực kỳ nguy hiểm, dễ ghi đè mất code của nhau (Đại diện: SCCS, RCS, PVCS).
  - **Thế hệ 2 - 클라이언트/서버 (C/S tập trung):** Có một máy chủ trung tâm (Server) nắm giữ kho code chính. Lập trình viên tải về sửa rồi commit thẳng lên Server. Nếu máy chủ Server bị sập, toàn bộ đội ngũ phải ngừng làm việc (Đại diện: CVS, SVN).
  - **Thế hệ 3 - 분산 저장소 (Phân tán):** Mỗi máy tính cá nhân của lập trình viên là một kho lưu trữ hoàn chỉnh (Local Repository) có đầy đủ toàn bộ lịch sử commit. Server sập vẫn commit bình thường trên máy cá nhân, khi nào có mạng hoặc server sống lại thì mới đẩy (Push) lên (Đại diện: Git, Mercurial).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh 3 mô hình công cụ quản lý phiên bản:**

| Mô hình quản lý | Cơ chế hoạt động cốt lõi | Ưu điểm | Nhược điểm (Bẫy đề thi) | Công cụ đại diện |
| :--- | :--- | :--- | :--- | :--- |
| **공유 폴더 방식 (Thư mục chia sẻ)** | Chia sẻ một thư mục qua mạng cục bộ; lập trình viên tự sao chép tệp để sửa đổi | Rất đơn giản, không cần cấu hình máy chủ phức tạp | Nguy cơ xung đột và **ghi đè mất dữ liệu (데이터 덮어쓰기)** rất cao | **SCCS, RCS, PVCS** |
| **클라이언트/서버 방식 (Client / Server)** | Kho lưu trữ đặt tập trung tại **máy chủ Server duy nhất (중앙 집중형)**; Client checkout về sửa rồi commit lên | Kiểm soát tập trung tốt, dễ quản trị quyền hạn truy cập | **Điểm lỗi đơn (SPOF)**; nếu Server chết hoặc đứt mạng thì lập trình viên không thể commit | **CVS, SVN (Subversion)**, ClearCase |
| **분산 저장소 방식 (Kho phân tán)** | Mỗi máy lập trình viên sở hữu một **Local Repository độc lập**; đồng bộ với Remote Repository | Làm việc Offline thoải mái; tốc độ commit tức thì; sao lưu an toàn tuyệt đối | Cấu trúc phân nhánh (Branching) phức tạp, đòi hỏi kỹ năng xử lý Merge Conflict | **Git**, Mercurial, BitKeeper |

- **So sánh trực diện giữa SVN và Git:**

| Tiêu chí | SVN (Subversion - C/S tập trung) | Git (Phân tán) |
| :--- | :--- | :--- |
| **Bản sao lịch sử** | Chỉ lưu lịch sử trên Server trung tâm | Mọi máy Client đều lưu toàn bộ lịch sử commit |
| **Khả năng làm việc ngoại tuyến** | Không thể làm việc hay xem lịch sử khi mất mạng | Làm việc độc lập bình thường (Offline Commit) |
| **Thao tác lưu mã** | `Commit` đẩy thẳng lên Server trung tâm | `Commit` ghi vào Local Repo; `Push` mới gửi lên Remote |
| **Quản lý dữ liệu** | Quản lý theo từng tệp thay đổi (Delta-based) | Quản lý theo bản chụp trạng thái (**Snapshot**) |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Mô hình luồng công việc của Git (Git Workflow):**
  - Git chia không gian làm việc thành 3 khu vực: Working Directory (thư mục làm việc thực tế) $\rightarrow$ Staging Area (vùng đệm chuẩn bị commit qua lệnh `git add`) $\rightarrow$ Local Repository (kho lưu trữ cục bộ qua lệnh `git commit`).
  - Lệnh `git push` thực hiện đồng bộ nhánh từ Local Repository lên Remote Repository (GitHub, GitLab).

### 복습 체크리스트
- [ ] Phân loại chính xác công cụ: RCS/PVCS (thư mục chia sẻ), CVS/SVN (Client/Server), Git/Mercurial (phân tán).
- [ ] Nhớ nhược điểm SPOF của mô hình Client/Server khi máy chủ trung tâm gặp sự cố.
- [ ] Giải thích được tại sao Git vẫn commit được khi mất kết nối mạng Internet.
- [ ] Nắm được chu trình: Working Directory $\rightarrow$ Staging Area $\rightarrow$ Local Repo $\rightarrow$ Remote Repo.
