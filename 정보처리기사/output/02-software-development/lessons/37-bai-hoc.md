# 40. 형상 관리 (SCM) 및 버전 관리 방식 (Version Control Methods)

## 학습 목표 (Mục tiêu)
- Nắm vững 3 mô hình kiến trúc quản lý phiên bản trong công nghệ phần mềm: Mô hình thư mục chia sẻ (공유 폴더 방식), Mô hình Máy khách/Máy chủ tập trung (클라이언트/서버 방식) và Mô hình kho lưu trữ phân tán (분산 저장소 방식).
- So sánh sự khác nhau về độ an toàn, tính sẵn sàng và cơ chế lưu trữ giữa SVN (mô hình tập trung, lưu delta) và Git (mô hình phân tán, lưu snapshot).
- Hiểu rõ các thao tác điều hướng nhánh và tích hợp: Trunk (nhánh chính), Branches (nhánh tính năng) và Merge (hợp nhất).

## 핵심 키워드 (Từ khóa)
- 버전 관리 방식 (Version Control Methods)
- 공유 폴더 방식 (Shared Folder: SCCS, RCS)
- 클라이언트/서버 방식 (Client/Server: CVS, SVN)
- 분산 저장소 방식 (Distributed Repository: Git)
- 리비전 (Revision / SVN số tăng dần)
- 스냅샷 (Snapshot / Git lưu trạng thái toàn diện)
- 트렁크 (Trunk) & 브랜치 (Branches) & 병합 (Merge)

## 선행·연결 개념 (Kiến thức liên kết)
- [36-bai-hoc.md](36-bai-hoc.md): Khái niệm tổng quan về SCM và các thao tác Check-Out/Check-In.
- [38-bai-hoc.md](38-bai-hoc.md): Quản lý cấu hình và Môi trường phát triển tích hợp (IDE).
- [40-bai-hoc.md](40-bai-hoc.md): So sánh chi tiết kỹ thuật chuyên sâu giữa SVN và Git.

## 읽는 방법 (Cách đọc)
- Nhớ đại diện kinh điển của 3 mô hình:
  - Thư mục chia sẻ $\rightarrow$ **RCS, SCCS**.
  - Client/Server tập trung $\rightarrow$ **CVS, SVN (Subversion)**.
  - Phân tán $\rightarrow$ **Git**.
- Phân biệt điểm yếu của SVN (Server chết thì mọi người đứng hình) với thế mạnh của Git (Server chết vẫn commit bình thường vào Local repo).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh 3 mô hình kiến trúc quản lý phiên bản:**

| Mô hình quản lý | Tên tiếng Hàn & Anh | Cơ chế vận hành kiến trúc | Công cụ tiêu biểu | Ưu / Nhược điểm chính |
| :--- | :--- | :--- | :--- | :--- |
| **Thư mục chia sẻ** | **공유 폴더 방식 (Shared Folder)** | Sử dụng một thư mục chia sẻ nội bộ trên mạng cục bộ (LAN), các lập trình viên cùng truy cập copy tệp | **SCCS, RCS** | Đơn giản nhưng dễ bị ghi đè nhầm lẫn, không kiểm soát được xung đột |
| **Máy khách / Máy chủ** | **클라이언트/서버 방식 (Client/Server)** | Có duy nhất **một máy chủ trung tâm (Central Server)** chứa kho lưu trữ. Các máy khách chỉ chứa mã nguồn đang làm việc | **CVS, SVN (Subversion)** | Quản lý tập trung dễ kiểm soát; nhưng nếu máy chủ bị hỏng hoặc mất mạng thì **toàn bộ việc commit bị tê liệt (Single Point of Failure)** |
| **Kho lưu trữ phân tán** | **분산 저장소 방식 (Distributed)** | Mỗi máy cá nhân của lập trình viên đều chứa **một bản sao đầy đủ (Full Clone) của toàn bộ kho lưu trữ** | **Git, Mercurial, BitKeeper** | **Làm việc offline thoải mái**, tốc độ cực nhanh; nếu server chết thì mọi máy cá nhân đều có thể khôi phục lại kho |

- **Đặc trưng cốt lõi của SVN vs Git:**
  - **SVN (Subversion):**
    - Cấu trúc thư mục: `trunk` (nhánh chính phục vụ phát hành), `branches` (nhánh con phát triển tính năng), `tags` (mốc đóng băng phiên bản).
    - Mỗi lần Commit thành công lên máy chủ trung tâm, số chỉ mục phiên bản (**Revision**) của toàn dự án tự động tăng lên 1 đơn vị ($1, 2, 3 \dots$).
  - **Git:**
    - Do Linus Torvalds phát minh năm 2005 để quản lý mã nguồn nhân Linux.
    - Cơ chế lưu trữ: Sử dụng **Ảnh chụp trạng thái (스냅샷 - Snapshot)** thay vì chỉ lưu chênh lệch dòng thay đổi (Delta).
    - Lập trình viên commit vào Local Repository trước, sau đó mới đẩy (`push`) lên Remote Repository khi có kết nối mạng.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Snapshot (Git) vs Delta-based (SVN):**
  - SVN lưu trữ lịch sử dưới dạng tệp gốc ban đầu cộng với một chuỗi các tệp vá chênh lệch (Deltas: dòng nào thêm, dòng nào bớt).
  - Git coi dữ liệu như một chuỗi các ảnh chụp (Snapshot) của toàn bộ hệ thống tệp. Nếu tệp không thay đổi, Git chỉ lưu một liên kết trỏ tới tệp đã lưu trước đó $\rightarrow$ Thao tác chuyển đổi nhánh (`git checkout / switch`) diễn ra gần như tức thì $O(1)$.

### 복습 체크리스트
- [ ] Phân biệt được 3 mô hình: Thư mục chia sẻ (RCS), Client/Server (SVN) và Phân tán (Git).
- [ ] Nhớ đặc trưng SVN: Quản lý tập trung, chia `trunk`/`branches`, chỉ số Revision tăng dần.
- [ ] Nhớ đặc trưng Git: Lưu trữ phân tán, lưu theo Snapshot, hỗ trợ làm việc offline.
- [ ] Nhận diện nguy cơ Single Point of Failure trong mô hình Client/Server.
