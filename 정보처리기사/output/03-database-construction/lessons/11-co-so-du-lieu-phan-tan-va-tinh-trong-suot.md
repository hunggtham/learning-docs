# 분산 데이터베이스와 4대 투명성 (Cơ Sở Dữ Liệu Phân Tán và 4 Tính Chất Trong Suốt)

## 학습 목표
- Nắm vững triết lý "Logic đơn nhất, Vật lý phân tán" (`논리적 단일, 물리적 분산`), vai trò của Bộ xử lý phân tán (`분산 처리기`), CSDL phân tán (`분산 데이터베이스`), và Mạng truyền thông (`통신 네트워크`).
- Định nghĩa và nhận diện chính xác qua đề thi 4 tính chất trong suốt sống còn: Trong suốt vị trí (`위치 투명성`), Trong suốt nhân bản (`중복/복제 투명성`), Trong suốt đồng thời (`병행 투명성`), và Trong suốt sự cố (`장애 투명성`).
- Phân biệt 3 phương pháp phân mảnh dữ liệu: Phân mảnh ngang (`수평 분할` - dùng phép Select $\sigma$), Phân mảnh dọc (`수직 분할` - dùng phép Project $\pi$ kèm PK), và Phân mảnh hỗn hợp (`혼합 분할`).
- Phân tích cơ chế cam kết nguyên tử 2 pha (2PC) gồm Pha chuẩn bị (`준비 단계 / Prepare Phase`) và Pha cam kết (`커밋 단계 / Commit Phase`).
- So sánh các kiến trúc lưu trữ doanh nghiệp: DAS (trực tiếp qua cáp), NAS (chia sẻ tệp qua mạng LAN), SAN (mạng cáp quang chuyên dụng cấp khối Block-level), và Định lý CAP.

## 핵심 키워드
- 분산 데이터베이스 (CSDL phân tán / Distributed Database / 논리적 단일, 물리적 분산)
- 4대 투명성 (위치 투명성 Location, 중복/복제 투명성 Replication, 병행 투명성 Concurrency, 장애 투명성 Failure)
- 데이터 분할 (수평 분할 Horizontal Select, 수직 분할 Vertical Project, 혼합 분할)
- 2단계 커밋 (2-Phase Commit / 2PC / 조정자 Coordinator, 참여자 Participant, All-or-Nothing)
- 스토리지 아키텍처 (DAS, NAS File-level, SAN Block-level)
- CAP 정리 (Consistency 일관성, Availability 가용성, Partition Tolerance 분할 허용성)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [10-view-index-system-catalog-va-ma-tran-crud.md](10-view-index-system-catalog-va-ma-tran-crud.md), chúng ta đã nghiên cứu các cấu trúc tối ưu truy cập trên một máy chủ đơn lẻ bao gồm View, Index và phân tích tải giao dịch qua Ma trận CRUD.
- **Đang giải quyết gì (Current Problem):** Nhằm vượt qua giới hạn phần cứng của một máy chủ độc lập và phục vụ các hệ thống phân tán địa lý lớn, bài học này giải quyết bài toán thiết kế **Cơ sở dữ liệu phân tán** với **4 tính chất trong suốt** và các giao thức đồng thuận giao dịch toàn cục.
- **Dùng đi đâu (Forward Handoff):** Kiến trúc phân tán và lưu trữ này sẽ kết nối trực tiếp với kỹ thuật phân vùng bảng (Partitioning) và cơ chế mã hóa, bảo mật đa tầng của CSDL ở bài học tiếp theo [12-phan-vung-du-lieu-va-bao-mat-ma-hoa-csdl.md](12-phan-vung-du-lieu-va-bao-mat-ma-hoa-csdl.md).

## 읽는 방법
- Đọc TẦNG A để ghi nhớ chuẩn xác các bẫy trắc nghiệm: nhận diện 4 tính chất trong suốt, phân biệt phép toán $\sigma$ và $\pi$ trong phân mảnh, phân biệt NAS (File-level) vs SAN (Block-level), và nguyên tắc 100% đồng ý trong giao thức 2PC.
- Đọc TẦNG B để nắm chắc cơ chế điều phối của Coordinator trong 2PC, cấu trúc 3 thành phần của CSDL phân tán và sự đánh đổi CP vs AP trong định lý CAP.

---

## 분산 데이터베이스와 4대 투명성

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng nhận diện 4 tính chất trong suốt (4대 투명성)
| Tính trong suốt | Tên tiếng Hàn & Anh | Định nghĩa kỹ thuật | Dấu hiệu nhận diện đề thi |
| :--- | :--- | :--- | :--- |
| **Trong suốt vị trí** | **위치 투명성 (Location)** | Tiếp cận dữ liệu bằng tên logic mà không cần biết máy chủ hoặc IP lưu trữ thực tế | "Chỉ cần biết tên logic, không cần biết vị trí vật lý" |
| **Trong suốt nhân bản** | **중복/복제 투명성 (Replication)** | Dữ liệu nhân bản tại nhiều trạm nhưng người dùng chỉ cảm nhận có duy nhất một bản | "Dữ liệu trùng lặp ở nhiều trạm nhưng coi như một" |
| **Trong suốt đồng thời** | **병행 투명성 (Concurrency)** | Nhiều giao dịch chạy song song không can thiệp, bảo đảm kết quả như chạy tuần tự | "Nhiều transaction chạy đồng thời vẫn bảo đảm 직렬성" |
| **Trong suốt sự cố** | **장애 투명성 (Failure)** | Khi một trạm mạng hoặc server gặp sự cố, toàn cục vẫn bảo toàn tính nguyên tử | "Trạm bị lỗi nhưng hệ thống tự khôi phục, bảo toàn dữ liệu" |

#### 2. Bảng phân mảnh dữ liệu (Data Fragmentation)
| Kiểu phân mảnh | Tên tiếng Hàn & Anh | Phép toán đại số quan hệ | Quy tắc cốt lõi |
| :--- | :--- | :---: | :--- |
| **Phân mảnh ngang** | `수평 분할` (Horizontal) | **Select ($\sigma$)** | Chia theo từng dòng (Tuple); các trạm có chung lược đồ thuộc tính |
| **Phân mảnh dọc** | `수직 분할` (Vertical) | **Project ($\pi$)** | Chia theo từng cột (Attribute); **bắt buộc mọi mảnh đều phải có Khóa chính (PK)** |
| **Phân mảnh hỗn hợp**| `혼합 분할` (Hybrid) | Kết hợp $\sigma$ và $\pi$ | Chia dữ liệu đồng thời theo cả dòng và cột dạng lưới ma trận |

#### 3. Đối chiếu 3 kiến trúc lưu trữ: DAS vs NAS vs SAN
| Tiêu chí | DAS (Direct Attached) | NAS (Network Attached) | SAN (Storage Area Network) |
| :--- | :--- | :--- | :--- |
| **Phương thức nối** | Cáp chuyên dụng (SATA, SAS) cắm trực tiếp vào máy chủ | Kết nối qua mạng LAN / Ethernet thông thường | Mạng cáp quang chuyên dụng (Fibre Channel Switch) |
| **Cấp độ truy cập** | Cấp độ khối (Block-level) | **Cấp độ tệp (File-level)** (NFS, CIFS) | **Cấp độ khối (Block-level)** (SCSI over FC) |
| **Chia sẻ dữ liệu** | **Không thể chia sẻ** trực tiếp với máy chủ khác | Chia sẻ tệp dễ dàng giữa nhiều máy chủ | Chia sẻ tài nguyên khối đĩa với hiệu năng cao nhất |
| **Môi trường DB** | DB nhỏ độc lập | Lưu trữ backup, tệp phi cấu trúc | **Hệ RDBMS doanh nghiệp lớn (Oracle RAC, DB2)** |

#### 4. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Ghép cặp 4 tính chất trong suốt:**
  - Nhắc tới *"không cần biết IP, tên trạm hay vị trí máy chủ"* $\rightarrow$ **위치 투명성 (Location)**.
  - Nhắc tới *"dữ liệu sao chép nhiều bản nhưng người dùng thấy như 1"* $\rightarrow$ **중복/복제 투명성 (Replication)**.
- **Bẫy 2: Phép toán đại số trong phân mảnh:**
  - Phân mảnh ngang dùng phép **Select ($\sigma$)**, phân mảnh dọc dùng phép **Project ($\pi$)**.
  - Muốn khôi phục phân mảnh dọc thành bảng gốc, các mảnh bắt buộc phải chứa **Khóa chính (Primary Key)** để Join.
- **Bẫy 3: Giao thức Cam kết 2 pha (2PC):**
  - Khẳng định: "Chỉ cần quá bán các trạm đồng ý thì Điều phối viên (Coordinator) sẽ phát lệnh Commit" $\rightarrow$ **SAI**. 2PC đòi hỏi **100% tất cả các trạm phải bầu chọn READY** (`All-Ready`); chỉ cần 1 trạm thất bại là lập tức Rollback toàn cục.
- **Bẫy 4: NAS vs SAN:** NAS truy xuất cấp độ tệp (**File-level**); SAN truy xuất cấp độ khối (**Block-level**) qua mạng cáp quang.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Kiến trúc 3 thành phần của CSDL phân tán
- Sơ đồ tương tác:
  ```
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
  ```
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
- **3 đặc tính của Eric Brewer:**
  1. `Consistency (Tính nhất quán)`: Mọi nút đều nhìn thấy cùng một dữ liệu tại cùng một thời điểm.
  2. `Availability (Tính sẵn sàng)`: Mọi truy vấn không bị lỗi đều nhận được phản hồi (dù có thể không phải dữ liệu mới nhất).
  3. `Partition Tolerance (Tính dung thứ phân vùng mạng)`: Hệ thống vẫn tiếp tục hoạt động dù mạng giữa các nút bị ngắt kết nối.
- **Sự đánh đổi thực tế:** Do mạng thực tế luôn có khả năng đứt đoạn (bắt buộc phải có P), hệ thống buộc phải chọn giữa **CP (ưu tiên Nhất quán - RDBMS phân tán, HBase)** hoặc **AP (ưu tiên Sẵn sàng - Cassandra, CouchDB)**.

---

### 복습 체크리스트
- [ ] Phân tích được triết lý "Logic đơn nhất, Vật lý phân tán" của CSDL phân tán.
- [ ] Nằm lòng 4 tính chất trong suốt: `위치`, `중복/복제`, `병행`, `장애 투명성`.
- [ ] Nhớ rõ phân mảnh ngang dùng phép toán $\sigma$, phân mảnh dọc dùng phép toán $\pi$ và bắt buộc phải giữ lại Khóa chính.
- [ ] Trình bày 2 pha của giao thức 2PC và nhớ nguyên tắc bắt buộc phải có 100% phiếu thuận mới được Global Commit.
- [ ] So sánh NAS (cấp độ File qua mạng LAN) và SAN (cấp độ Block qua cáp quang).
- [ ] Giải thích nguyên lý đánh đổi giữa tính nhất quán (C) và tính sẵn sàng (A) theo định lý CAP.
