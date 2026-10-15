# 136-137. 분산 데이터베이스 (Distributed DB)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa của Cơ sở dữ liệu phân tán (`분산 데이터베이스 / Distributed Database`): Về mặt logic là một hệ thống CSDL duy nhất (`논리적으로 하나의 시스템`), nhưng về mặt vật lý được lưu trữ phân tán trên nhiều trạm máy tính (`사이트 / Site`) liên kết qua mạng viễn thông.
- Phân biệt 3 thành phần cấu tạo cốt lõi: Bộ xử lý phân tán (`분산 처리기`), Cơ sở dữ liệu phân tán (`분산 데이터베이스`), và Mạng truyền thông (`통신 네트워크`).
- Hiểu rõ 4 mục tiêu trong suốt sống còn: **Trong suốt vị trí (`위치 투명성`)**, **Trong suốt nhân bản (`중복 투명성`)**, **Trong suốt đồng thời (`병행 투명성`)**, và **Trong suốt sự cố (`장애 투명성`)**.
- Phân tích các ưu điểm (tính tự trị cục bộ, độ tin cậy cao) và nhược điểm (chi phí phát triển lớn, độ phức tạp cao) của hệ thống phân tán.

## 핵심 키워드 (Từ khóa)
- 분산 데이터베이스 (Cơ sở dữ liệu phân tán / Distributed Database)
- 분산 처리기 (Bộ xử lý phân tán / Distributed Processor)
- 통신 네트워크 (Mạng truyền thông / Communication Network)
- 투명성 (Tính trong suốt / Transparency)
- 위치 투명성 (Trong suốt vị trí / Location Transparency)
- 중복 투명성 (Trong suốt nhân bản / Replication Transparency)
- 병행 투명성 (Trong suốt đồng thời / Concurrency Transparency)
- 장애 투명성 (Trong suốt sự cố / Failure Transparency)
- 지역 자치성 (Tính tự trị cục bộ / Local Autonomy)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([03-bai-hoc.md](03-bai-hoc.md), [25-bai-hoc.md](25-bai-hoc.md), [33-bai-hoc.md](33-bai-hoc.md)):** Để mở rộng quy mô hệ thống vượt khỏi giới hạn của một máy chủ vật lý duy nhất, kiến trúc CSDL chuyển đổi từ tập trung (Centralized) sang phân tán (Distributed).
- **Tiếp nối sang bài sau ([35-bai-hoc.md](35-bai-hoc.md)):** Bài học tiếp theo sẽ đào sâu vào cơ chế định danh và phân tích các dạng bài tập thi cử liên quan đến 4 tính chất trong suốt.

## 읽는 방법 (Cách đọc)
- Khắc sâu định nghĩa cốt lõi: **Logic là MỘT, Vật lý là NHIỀU (논리적 단일, 물리적 분산)**.
- Ghi nhớ 4 từ khóa trong suốt: **Vị trí (Location) - Nhân bản (Replication) - Đồng thời (Concurrency) - Sự cố (Failure)**.
- Nhớ ưu điểm nổi bật nhất: **지역 자치성 (Tính tự trị cục bộ cao)** - mỗi chi nhánh tự quản lý dữ liệu riêng của mình.

---

## 136-137. 분산 데이터베이스 (Distributed DB)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Định nghĩa và Bản chất CSDL phân tán (분산 데이터베이스의 정의):**
  - Là hệ thống cơ sở dữ liệu mà về mặt **logic thuộc về một hệ thống duy nhất**, nhưng về mặt **vật lý lại được phân bố trên nhiều trạm máy tính (`사이트 / Site`)** đặt ở các vị trí địa lý khác nhau và kết nối thông qua mạng truyền thông.
  - Người dùng truy cập vào hệ thống cảm thấy hoàn toàn giống như đang sử dụng một CSDL cục bộ duy nhất trên máy tính của mình.
- **2. Ba thành phần cấu tạo chính (분산 데이터베이스 3대 구성요소):**
  - **분산 처리기 (Bộ xử lý phân tán):** Các máy tính độc lập tại mỗi trạm có năng lực tính toán và xử lý riêng.
  - **분산 데이터베이스 (Cơ sở dữ liệu phân tán):** Các tệp cơ sở dữ liệu vật lý được lưu trữ phân tán tại từng trạm.
  - **통신 네트워크 (Mạng truyền thông):** Hệ thống cáp mạng, router, switch liên kết các trạm xử lý lại với nhau.
- **3. Bốn tính chất trong suốt bắt buộc thuộc lòng (4대 투명성):**
  | Tính chất trong suốt | Tên tiếng Hàn & Anh | Khái niệm kỹ thuật cần nhớ |
  |---|---|---|
  | **Trong suốt vị trí** | `위치 투명성` (Location Transparency) | Người dùng khi truy cập dữ liệu **chỉ cần dùng tên logic của dữ liệu**, hoàn toàn không cần biết dữ liệu đó đang được lưu trữ vật lý ở máy chủ nào hay thành phố nào. |
  | **Trong suốt nhân bản** | `중복 / 복제 투명성` (Replication Transparency) | Dữ liệu có thể được sao chép nhân bản thành nhiều bản lưu ở nhiều trạm khác nhau, nhưng người dùng cảm thấy như chỉ có **duy nhất một bản**, hệ thống tự động đồng bộ mọi bản sao. |
  | **Trong suốt đồng thời** | `병행 투명성` (Concurrency Transparency) | Nhiều giao dịch thực hiện đồng thời trên khắp các trạm phân tán nhưng **kết quả không bị ảnh hưởng hay can thiệp lẫn nhau**, luôn đảm bảo tính khả tuần tự. |
  | **Trong suốt sự cố** | `장애 투명성` (Failure Transparency) | Khi một số trạm máy tính, đường truyền mạng hoặc phần mềm DBMS gặp sự cố hỏng hóc, **các giao dịch toàn cục vẫn được xử lý chính xác và toàn vẹn**. |

- **4. Đánh giá Ưu điểm và Nhược điểm:**
  - **Ưu điểm:** Tính tự trị cục bộ cao (`지역 자치성`), tăng tính sẵn sàng (`가용성`) và độ tin cậy, dễ dàng mở rộng dung lượng từng bước (`점진적 확장 용이`). Sự cố ở một máy chủ trung tâm không làm sập toàn bộ hệ thống.
  - **Nhược điểm:** Thiết kế CSDL phức tạp, chi phí phần mềm và truyền thông tăng cao, tiềm ẩn nhiều nguy cơ lỗi đồng bộ dữ liệu.
- **주의/함정 (Bẫy đề thi):**
  - Đề hỏi: *"Người dùng truy cập dữ liệu chỉ cần dùng tên logic mà không cần biết vị trí máy chủ lưu trữ là tính chất gì?"* $\rightarrow$ Đáp án: **위치 투명성 (Location Transparency)**.
  - Đề hỏi: *"Khi một trạm trong mạng bị mất điện mà hệ thống vẫn xử lý giao dịch chính xác là tính chất gì?"* $\rightarrow$ Đáp án: **장애 투명성 (Failure Transparency)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa thực tế về Vị trí trong suốt (Location Transparency):**
  - Khách hàng ngân hàng ở Hà Nội mở ứng dụng chuyển tiền cho tài khoản mở tại chi nhánh TP. Hồ Chí Minh.
  - Khách hàng chỉ cần nhập `SoTaiKhoan = 123456`, không cần quan tâm máy chủ chứa số tài khoản này đặt tại Data Center Hà Nội, Đà Nẵng hay TP. Hồ Chí Minh. Đó chính là **위치 투명성**.
- **Cơ chế sao chép dữ liệu (Replication):**
  - Bảng tỷ giá ngoại tệ được nhân bản lưu sẵn ở cả 100 chi nhánh trên toàn quốc để truy vấn nhanh không nghẽn mạng; khi tỷ giá đổi, DBMS tự phát tín hiệu cập nhật ngầm cho 100 bản sao mà khách hàng không nhận ra. Đó là **중복 투명성**.

### 복습 체크리스트
- [ ] Nêu định nghĩa cốt lõi của 분산 데이터베이스 (logic đơn nhất, vật lý phân tán).
- [ ] Kể tên 3 thành phần: 분산 처리기, 분산 데이터베이스, 통신 네트워크.
- [ ] Thuộc lòng 4 loại 투명성: 위치, 중복/복제, 병행, 장애 투명성.
- [ ] Phân tích ưu điểm lớn nhất: 지역 자치성 (tự trị cục bộ).
