# 형상 관리(SCM)와 버전 관리 도구 (Quản lý cấu hình SCM và Git)

## 학습 목표
- Nắm vững định nghĩa Quản lý cấu hình phần mềm (`형상 관리 / SCM - Software Configuration Management`), vai trò bảo đảm tính hiển thị (`가시성`), khả năng truy vết nguồn gốc (`추적성`), và các Hạng mục cấu hình (`형상 항목 / SCI`).
- Hiểu rõ bản chất của Đường cơ sở (`베이스라인 / Baseline`), 4 mốc Baseline tiêu biểu trong SDLC (Functional, Allocated, Design, Product) và vai trò thẩm quyền của Hội đồng kiểm soát thay đổi (`형상 통제 위원회 / CCB`).
- Thuộc lòng quy trình 4 bước quản lý cấu hình chuẩn theo mô hình: Nhận dạng (`형상 식별`) $\rightarrow$ Kiểm soát (`형상 통제`) $\rightarrow$ Kiểm toán (`형상 감사`) $\rightarrow$ Ghi chép / Báo cáo (`형상 기록/보고`).
- So sánh đối đầu 3 mô hình kiến trúc công cụ kiểm soát phiên bản: Chia sẻ thư mục (`폴더 공유`), Máy chủ tập trung (`클라이언트/서버` - CVS, SVN), và Phân tán (`분산 저장소` - Git, Mercurial).
- Nắm vững các câu lệnh thao tác cơ bản trong hệ thống kiểm soát phiên bản Git (`init`, `clone`, `add`, `commit`, `branch`, `merge`, `push`, `pull`, `checkout`).

## 핵심 키워드
- 형상 관리 (Quản lý cấu hình / SCM / Software Configuration Management)
- 형상 항목 (Hạng mục cấu hình / SCI / Software Configuration Item)
- 베이스라인 (Đường cơ sở / Baseline / 무절제한 변경 방지)
- CCB (형상 통제 위원회 / Configuration Control Board / 변경 승인·반려)
- SCM 4단계 (식별 Identification, 통제 Control, 감사 Audit, 기록/보고 Status Accounting)
- 버전 관리 도구 (SVN 중앙 집중식 vs Git 분산 저장소 방식)
- Git 명령어 (commit, push, pull, branch, merge, checkout)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [11-dong-goi-phan-mem-va-drm.md](11-dong-goi-phan-mem-va-drm.md), chúng ta đã khảo sát quy trình đóng gói và phát hành phần mềm.
- **Đang giải quyết gì (Current Problem):** Trong quá trình phát triển liên tục, hàng trăm tệp tài liệu và mã nguồn thay đổi dễ dẫn đến ghi đè mã, mất phiên bản hoạt động. Bài học này thiết lập quy trình kiểm soát thay đổi chặt chẽ qua SCM/CCB và công cụ kiểm soát phiên bản Git/SVN.
- **Dùng đi đâu (Forward Handoff):** Sau khi quản lý mã nguồn bằng Git, bài học tiếp theo [13-ide-va-tu-dong-hoa-build.md](13-ide-va-tu-dong-hoa-build.md) sẽ đưa người học sang môi trường phát triển tích hợp IDE và các công cụ tự động hóa build/CI/CD (Maven, Gradle, Jenkins).

## 읽는 방법
- Đọc TẦNG A để thuộc lòng bảng 4 bước SCM chuẩn, bảng so sánh SVN vs Git, bảng lệnh Git cơ bản và các bẫy trắc nghiệm.
- Đọc TẦNG B để hiểu sâu 4 mốc Baseline trong SDLC, thẩm quyền của CCB và chi tiết kiến trúc phân tán của Git.

---

## 형상 관리(SCM)와 버전 관리 도구

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Quy trình 4 bước quản lý cấu hình chuẩn (SCM 4단계)
```
[1. 형상 식별] ────► [2. 형상 통제] ────► [3. 형상 감사] ────► [4. 형상 기록 / 보고]
(Identification)      (Control / CCB)       (Audit / V&V)       (Status Accounting)
```

| Bước | Tên tiếng Hàn (English) | Nội dung hoạt động cốt lõi | Từ khóa đề thi |
| :---: | :--- | :--- | :--- |
| **1** | **형상 식별 (Identification)** | Xác định danh mục các hạng mục cấu hình (SCI), đặt mã định danh duy nhất, phân cấp cây cấu trúc, thiết lập **Baseline ban đầu** | 베이스라인 설정, 항목 식별, 트리 구조 |
| **2** | **형상 통제 (Control)** | Tiếp nhận phiếu yêu cầu thay đổi (CR), **Hội đồng CCB** thẩm định và phê duyệt; áp dụng cơ chế Check-in/Check-out | **CCB 변경 통제 위원회**, 변경 승인/반려 |
| **3** | **형상 감사 (Audit)** | Đánh giá độc lập xem các thay đổi có thực hiện đúng phê chuẩn không; xác minh tính toàn vẹn cấu hình (**V&V**) | **무결성 검증**, 베이스라인 일치 검사, V&V |
| **4** | **형상 기록 / 보고 (Accounting)** | Ghi nhận nhật ký lịch sử mọi thay đổi, lưu trữ biên bản họp CCB, báo cáo tình trạng cấu hình cho các bên | **상태 보고**, 이력 기록, 변경 통계 집계 |

#### 2. Đối chiếu mô hình quản lý phiên bản: SVN vs Git
| Tiêu chuẩn so sánh | 클라이언트/서버 방식 (SVN - Subversion) | 분산 저장소 방식 (Git) |
| :--- | :--- | :--- |
| **Kiến trúc kho lưu trữ** | **Chỉ có duy nhất 1 kho trung tâm (Central Server)** | **Mỗi máy trạm của lập trình viên là một kho hoàn chỉnh (Local Repo)** |
| **Làm việc Offline** | Không thể; bắt buộc phải kết nối mạng liên tục với server | **Hoàn toàn làm việc offline**, commit trên máy cá nhân rồi mới đẩy lên mạng |
| **Tốc độ thực thi** | Chậm do phụ thuộc vào băng thông mạng | **Cực nhanh** vì mọi thao tác đọc/ghi lịch sử diễn ra trực tiếp trên ổ cứng nội bộ |
| **Điểm lỗi đơn (SPOF)** | Nếu server trung tâm bị hỏng thì toàn bộ dự án tê liệt | An toàn tuyệt đối; nếu server hỏng, mọi máy trạm đều có bản sao lưu đầy đủ |

#### 3. Bảng lệnh thao tác Git cơ bản chuẩn đề thi
| Lệnh Git | Ý nghĩa chức năng kỹ thuật |
| :--- | :--- |
| `git init` | Khởi tạo một kho lưu trữ Git cục bộ mới ngay tại thư mục hiện hành |
| `git clone [url]` | Sao chép toàn bộ kho lưu trữ từ máy chủ từ xa (Remote Repo) về máy cá nhân |
| `git add [file]` | Đưa tệp tin từ vùng làm việc (Working Directory) vào vùng chờ chuẩn bị commit (**Staging Area**) |
| `git commit -m [msg]` | Lưu vĩnh viễn ảnh chụp trạng thái từ Staging Area vào kho lưu trữ cục bộ (**Local Repository**) |
| `git push [remote] [branch]` | Đẩy các bản commit từ Local Repository lên máy chủ từ xa (**Remote Repository**) |
| `git pull [remote] [branch]` | Kéo các thay đổi mới nhất từ Remote Repository về và tự động gộp (**Merge**) vào nhánh hiện tại |
| `git branch [name]` | Tạo hoặc hiển thị danh sách các nhánh rẽ phát triển độc lập |
| `git merge [branch]` | Gộp mã nguồn từ một nhánh khác vào nhánh hiện tại đang đứng |
| `git checkout [branch]` | Chuyển đổi không gian làm việc sang một nhánh khác hoặc khôi phục tệp |

#### 4. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Thứ tự 4 bước SCM:** Thần chú: **"Nhận dạng $\rightarrow$ Kiểm soát $\rightarrow$ Kiểm toán $\rightarrow$ Ghi chép"** (`식별 → 통제 → 감사 → 기록`).
- **Bẫy 2: Vai trò của CCB:** Cơ quan duy nhất có thẩm quyền chính thức phê duyệt (Approve) hoặc bác bỏ (Reject) các yêu cầu thay đổi Đường cơ sở Baseline là **형상 통제 위원회 (CCB)**.
- **Bẫy 3: Bản chất của Git:** Trong mô hình của Git, thao tác `git commit` chỉ lưu dữ liệu vào **kho cục bộ (Local Repository)** trên máy cá nhân, chưa hề đẩy lên máy chủ. Phải chạy tiếp lệnh `git push` thì mã nguồn mới được đồng bộ lên máy chủ từ xa.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Tiến hóa 3 thế hệ hệ thống quản lý cấu hình
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

#### 2. Vòng đời 4 tầng dữ liệu trong Git
```
[Working Directory] ──(git add)──► [Staging Area / Index] ──(git commit)──► [Local Repository] ──(git push)──► [Remote Repository]
  (Mã đang sửa)                       (Vùng chuẩn bị commit)                     (Kho máy cục bộ)                 (Kho GitHub/GitLab)
```

#### 3. Bốn mốc Đường cơ sở (Baseline) tiêu biểu trong SDLC
1. **기능 베이스라인 (Functional Baseline):** Thiết lập sau khi hoàn thành phân tích yêu cầu phần mềm (SRS).
2. **분배 베이스라인 (Allocated Baseline):** Thiết lập sau giai đoạn thiết kế kiến trúc hệ thống tổng thể.
3. **설계 베이스라인 (Design Baseline):** Thiết lập sau khi hoàn thành thiết kế chi tiết từng module.
4. **제품 베이스라인 (Product Baseline):** Thiết lập khi đóng gói sản phẩm hoàn chỉnh để nghiệm thu và bàn giao.

---

### 복습 체크리스트
- [ ] Thuộc lòng thứ tự 4 bước SCM: 형상 식별 $\rightarrow$ 형상 통제 $\rightarrow$ 형상 감사 $\rightarrow$ 형상 기록/보고.
- [ ] Định nghĩa Baseline là trạng thái được phê duyệt chính thức, không được tự ý sửa đổi.
- [ ] Nhớ CCB là hội đồng duy nhất có quyền duyệt hoặc bác bỏ yêu cầu thay đổi (CR).
- [ ] Phân biệt SVN (máy chủ tập trung, không làm việc offline) và Git (kho phân tán, làm việc offline).
- [ ] Nắm vững cú pháp và chức năng các lệnh Git: init, clone, add, commit, push, pull, branch, merge, checkout.
