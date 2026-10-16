# 분산 데이터베이스와 4대 투명성 (Cơ Sở Dữ Liệu Phân Tán và 4 Tính Chất Trong Suốt)

## 학습 목표 (Mục tiêu)
- Nắm vững triết lý "Logic đơn nhất, Vật lý phân tán" (`논리적 단일, 물리적 분산`), cấu trúc 3 thành phần: Bộ xử lý phân tán (`분산 처리기`), CSDL phân tán (`분산 데이터베이스`), và Mạng truyền thông (`통신 네트워크`).
- Định nghĩa và nhận diện chính xác các tính chất trong suốt sống còn: Trong suốt vị trí (`위치 투명성` / Location), Trong suốt phân mảnh (`분할 투명성` / Fragmentation), Trong suốt nhân bản/sao lưu (`중복/복제 투명성` / Replication), Trong suốt đồng thời (`병행 투명성` / Concurrency), và Trong suốt sự cố (`장애 투명성` / Failure).
- Phân biệt 3 phương pháp phân mảnh dữ liệu: Phân mảnh ngang (`수평 분할` - dùng phép Select $\sigma$), Phân mảnh dọc (`수직 분할` - dùng phép Project $\pi$ kèm Khóa chính PK), và Phân mảnh hỗn hợp (`혼합 분할`).
- Phân tích cơ chế cam kết nguyên tử 2 pha (2PC) gồm Pha chuẩn bị (`준비 단계` / Prepare Phase) và Pha cam kết (`커밋 단계` / Commit Phase) với nguyên tắc 100% phiếu thuận.
- So sánh các kiến trúc lưu trữ doanh nghiệp: DAS, NAS, SAN và làm chủ Định lý CAP (Consistency, Availability, Partition tolerance).

## 핵심 키워드 (Từ khóa)
- 분산 데이터베이스 (CSDL phân tán / Distributed Database / 논리적 단일, 물리적 분산)
- 투명성 (Tính trong suốt / Transparency: 위치, 분할, 복제, 병행, 장애 투명성)
- 데이터 분할 (Phân mảnh dữ liệu: 수평 분할 Select, 수직 분할 Project, 혼합 분할)
- 2단계 커밋 (2-Phase Commit / 2PC / All-Ready 원칙)
- 스토리지 아키텍처 (DAS, NAS File-level, SAN Block-level)
- CAP 정리 (Consistency 일관성, Availability 가용성, Partition Tolerance 분할 허용성)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [10-view-index-system-catalog-va-ma-tran-crud.md](10-view-index-system-catalog-va-ma-tran-crud.md), chúng ta đã nghiên cứu các cấu trúc tối ưu truy cập trên một máy chủ đơn lẻ bao gồm View, Index và phân tích tải giao dịch qua Ma trận CRUD.
- **Đang giải quyết gì (Current Problem):** Nhằm vượt qua giới hạn phần cứng của một máy chủ độc lập và phục vụ các hệ thống phân tán địa lý lớn, bài học này giải quyết bài toán thiết kế **Cơ sở dữ liệu phân tán** với **các tính chất trong suốt** bảo vệ người dùng và các giao thức đồng thuận giao dịch toàn cục.
- **Dùng đi đâu (Forward Handoff):** Kiến trúc phân tán và lưu trữ này sẽ kết nối trực tiếp với kỹ thuật phân vùng bảng (Partitioning) và cơ chế mã hóa, bảo mật đa tầng của CSDL ở bài học tiếp theo [12-phan-vung-du-lieu-va-bao-mat-ma-hoa-csdl.md](12-phan-vung-du-lieu-va-bao-mat-ma-hoa-csdl.md).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để ghi nhớ chuẩn xác các bẫy trắc nghiệm: nhận diện 4-5 tính chất trong suốt, phân biệt phép toán $\sigma$ và $\pi$ trong phân mảnh, phân biệt NAS (File-level) vs SAN (Block-level), và nguyên tắc 100% đồng ý trong giao thức 2PC.
- Đọc TẦNG B để nắm chắc cơ chế điều phối của Coordinator trong 2PC, cấu trúc 3 thành phần của CSDL phân tán và sự đánh đổi CP vs AP trong định lý CAP.

---

## 분산 데이터베이스와 4대 투명성

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng nhận diện các tính chất trong suốt (분산 데이터베이스 투명성)

Tính trong suốt (**투명성** / Transparency) nghĩa là hệ thống tự động xử lý sự phức tạp ngầm bên dưới, người dùng và lập trình viên ứng dụng nhìn hệ thống phân tán như một CSDL tập trung thông thường:

| Tính trong suốt | Tên tiếng Hàn & Anh | Định nghĩa kỹ thuật | Dấu hiệu nhận diện đề thi |
| :--- | :--- | :--- | :--- |
| **Trong suốt vị trí** | **위치 투명성 (Location)** | Tiếp cận dữ liệu bằng tên logic mà không cần biết máy chủ hoặc IP lưu trữ thực tế | "Chỉ cần biết tên logic, không cần biết vị trí vật lý hay trạm lưu trữ" |
| **Trong suốt phân mảnh**| **분할 투명성 (Fragmentation)**| Bảng bị chia nhỏ thành nhiều mảnh nhưng người dùng truy vấn như một bảng nguyên vẹn | "Không cần biết bảng bị cắt ngang hay cắt dọc như thế nào" |
| **Trong suốt nhân bản** | **중복/복제 투명성 (Replication)** | Dữ liệu nhân bản tại nhiều trạm nhưng người dùng chỉ cảm nhận có duy nhất một bản | "Dữ liệu sao chép ở nhiều trạm khác nhau nhưng coi như một" |
| **Trong suốt đồng thời**| **병행 투명성 (Concurrency)** | Nhiều giao dịch chạy song song qua các trạm không can thiệp lẫn nhau | "Nhiều transaction phân tán chạy đồng thời vẫn bảo đảm tính tuần tự" |
| **Trong suốt sự cố** | **장애 투명성 (Failure)** | Khi một trạm mạng hoặc server gặp sự cố, toàn cục vẫn bảo toàn tính nguyên tử | "Trạm bị lỗi mạng nhưng hệ thống tự chuyển hướng hoặc phục hồi" |

#### 2. Bảng phân mảnh dữ liệu (Data Fragmentation)

| Kiểu phân mảnh | Tên tiếng Hàn & Anh | Phép toán đại số quan hệ | Quy tắc cốt lõi |
| :--- | :--- | :---: | :--- |
| **Phân mảnh ngang** | `수평 분할` (Horizontal) | **Select ($\sigma$)** | Chia bảng theo từng dòng (Tuple); các trạm con có cùng chung danh sách cột. |
| **Phân mảnh dọc** | `수직 분할` (Vertical) | **Project ($\pi$)** | Chia bảng theo từng cột (Attribute); **bắt buộc mọi mảnh đều phải có Khóa chính (PK)** để Join lại. |
| **Phân mảnh hỗn hợp**| `혼합 분할` (Hybrid) | Kết hợp $\sigma$ và $\pi$ | Chia dữ liệu đồng thời theo cả dòng và cột tạo thành lưới ma trận các khối dữ liệu. |

#### 3. Đối chiếu 3 kiến trúc lưu trữ: DAS vs NAS vs SAN

| Tiêu chí | DAS (Direct Attached Storage) | NAS (Network Attached Storage) | SAN (Storage Area Network) |
| :--- | :--- | :--- | :--- |
| **Phương thức nối** | Cáp chuyên dụng (SATA, SAS) cắm trực tiếp vào máy chủ | Kết nối qua mạng LAN / Ethernet thông thường | Mạng cáp quang chuyên dụng (Fibre Channel Switch) |
| **Cấp độ truy cập** | Cấp độ khối (Block-level) | **Cấp độ tệp (File-level)** (NFS, CIFS/SMB) | **Cấp độ khối (Block-level)** (Fibre Channel, iSCSI) |
| **Chia sẻ dữ liệu** | **Không thể chia sẻ** trực tiếp với máy chủ khác | Chia sẻ tệp dễ dàng giữa nhiều máy chủ qua mạng | Chia sẻ vùng nhớ khối đĩa hiệu năng cực cao giữa các cụm server |
| **Môi trường DB** | Máy chủ đơn lẻ, CSDL nhỏ | Lưu trữ file tĩnh, tài liệu, bản sao lưu backup | **Hệ RDBMS doanh nghiệp lớn (Oracle RAC, clustered DB)** |

#### 4. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)

- **Bẫy 1: Ghép cặp các tính chất trong suốt:**
  - Nhắc tới *"không cần biết IP, tên trạm hay vị trí máy chủ"* $\rightarrow$ **위치 투명성 (Location)**.
  - Nhắc tới *"bảng bị chia nhỏ nhưng câu truy vấn viết như bình thường"* $\rightarrow$ **분할 투명성 (Fragmentation)**.
  - Nhắc tới *"dữ liệu sao chép nhiều bản nhưng người dùng thấy như 1"* $\rightarrow$ **중복/복제 투명성 (Replication)**.
- **Bẫy 2: Phép toán đại số trong phân mảnh:**
  - Phân mảnh ngang dùng phép **Select ($\sigma$)**, phân mảnh dọc dùng phép **Project ($\pi$)**.
  - Muốn khôi phục phân mảnh dọc thành bảng gốc, các mảnh bắt buộc phải chứa **Khóa chính (Primary Key)** để Join.
- **Bẫy 3: Giao thức Cam kết 2 pha (2PC - 2-Phase Commit):**
  - Khẳng định: "Chỉ cần đa số (quá bán) các trạm đồng ý thì Điều phối viên (Coordinator) sẽ phát lệnh Commit" $\rightarrow$ **SAI**. 2PC đòi hỏi **100% tất cả các trạm tham gia phải phản hồi READY (Yes)**; chỉ cần 1 trạm thất bại hoặc timeout là lập tức phát lệnh **Global Abort**.
- **Bẫy 4: NAS vs SAN:** NAS truy xuất cấp độ tệp (**File-level**); SAN truy xuất cấp độ khối (**Block-level**) qua mạng cáp quang.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Kiến trúc 3 thành phần của CSDL phân tán
- Sơ đồ tương tác:
  ```text
                    [ 통신 네트워크 (Mạng truyền thông) ]
                         │                   │
           ┌─────────────┴────────┐ ┌────────┴────────────┐
           ▼                      ▼ ▼                     ▼
    [ 사이트 1 (Hà Nội) ]                 [ 사이트 2 (TP. Hồ Chí Minh) ]
    • 분산 처리기 (Processor)             • 분산 처리기 (Processor)
    • 분산 데이터베이스 (DB)              • 분산 데이터베이스 (DB)
    • 지역 자치성 (Local Autonomy)         • 지역 자치성 (Local Autonomy)
  ```
- **Tính tự trị cục bộ (`지역 자치성`):** Mỗi trạm vẫn có quyền quản lý và xử lý các giao dịch nội bộ của riêng mình mà không bị phụ thuộc vào trạm khác khi không có giao dịch liên vùng.

#### 2. Giao thức Cam kết 2 pha (2-Phase Commit Protocol, 2PC)
- **Tiến trình trao đổi thông điệp:**
  ```text
  [ 조정자 (Coordinator) ]                       [ 참여자 (Participants) ]
            │                                              │
            │ ── 1. Chuẩn bị (Prepare / Can you commit?) ─> │ (Pha 1: Chuẩn bị)
            │ <── 2. Bầu chọn (Vote Yes / Ready) ───────── │
            │                                              │
            │ ── 3. Chốt quyết định (Global Commit/Abort) ─> │ (Pha 2: Cam kết)
            │ <── 4. Xác nhận hoàn tất (Acknowledge) ───── │
  ```
- **Xử lý tình huống sự cố:**
  - Nếu bất kỳ trạm nào gửi thông điệp `Abort` hoặc không phản hồi sau thời gian timeout ở Pha 1, Coordinator sẽ gửi lệnh `Global Abort` tới tất cả các trạm để khôi phục trạng thái ban đầu.

#### 3. Định lý CAP trong hệ thống phân tán (CAP Theorem)

Định lý do Eric Brewer đề xuất khẳng định rằng một hệ thống phân tán chia sẻ dữ liệu chỉ có thể đồng thời thỏa mãn tối đa **2 trong 3 yếu tố sau**:

```text
                  ┌────────────────────────────────────────┐
                  │               ĐỊNH LÝ CAP              │
                  └──────────────────┬─────────────────────┘
                                     │
         ┌───────────────────────────┼───────────────────────────┐
         ▼                           ▼                           ▼
1. Consistency (Nhất quán)   2. Availability (Sẵn sàng)  3. Partition Tolerance
- Mọi node thấy cùng dữ liệu - Mọi request đều nhận       - Mạng đứt đoạn giữa các node
  tại cùng một thời điểm       phản hồi thành công          hệ thống vẫn chạy được
```

- **Sự đánh đổi thực tế trong môi trường phân tán:**
  - Trong thực tế mạng máy tính, rủi ro phân vùng mạng (Partition P) là điều không thể tránh khỏi (đứt cáp, switch lỗi, rớt gói tin).
  - Do đó, hệ thống bắt buộc phải hỗ trợ `P` và phải chọn giữa:
    1. **Hệ thống CP (Consistency + Partition Tolerance):** Khi mạng phân vùng xảy ra, hệ thống từ chối hoặc khóa truy cập để bảo đảm tính nhất quán dữ liệu tuyệt đối (Ví dụ: Bigtable, HBase, MongoDB cấu hình an toàn, RDBMS phân tán).
    2. **Hệ thống AP (Availability + Partition Tolerance):** Khi mạng phân vùng xảy ra, mọi node vẫn tiếp tục trả lời người dùng dù dữ liệu có thể chưa kịp đồng bộ mới nhất (Tính nhất quán cuối cùng - Eventual Consistency). Ví dụ: Cassandra, CouchDB, DynamoDB.
    3. **Hệ thống CA (Consistency + Availability):** Chỉ tồn tại trong các hệ thống tập trung không phân tán qua mạng (Single node RDBMS).

---

### 복습 체크리스트
- [ ] Phân tích được triết lý "Logic đơn nhất, Vật lý phân tán" của CSDL phân tán.
- [ ] Nằm lòng các tính chất trong suốt: `위치` (Vị trí), `분할` (Phân mảnh), `복제` (Nhân bản), `병행` (Đồng thời), `장애` (Sự cố).
- [ ] Nhớ rõ: Phân mảnh ngang dùng phép toán $\sigma$, phân mảnh dọc dùng phép toán $\pi$ và bắt buộc phải giữ lại Khóa chính (PK).
- [ ] Trình bày 2 pha của giao thức 2PC và nhớ nguyên tắc bắt buộc phải có 100% phiếu thuận mới được Global Commit.
- [ ] So sánh NAS (cấp độ File qua mạng LAN) và SAN (cấp độ Block qua cáp quang).
- [ ] Giải thích nguyên lý đánh đổi giữa tính nhất quán (C) và tính sẵn sàng (A) theo định lý CAP khi xảy ra sự cố mạng (P).
