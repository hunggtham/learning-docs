# 195-196. 분산 데이터베이스 목표 (Distributed DB Goals)

## 학습 목표 (Mục tiêu)
- Nắm vững 4 mục tiêu thiết kế cốt lõi của Cơ sở dữ liệu phân tán thông qua Bộ tứ tính chất Trong suốt (`4대 투명성 / 4 Transparencies`): **Trong suốt vị trí (`위치 투명성`)**, **Trong suốt nhân bản (`중복 / 복제 투명성`)**, **Trong suốt đồng thời (`병행 투명성`)**, và **Trong suốt sự cố (`장애 투명성`)**.
- Phân tích chi tiết định nghĩa kỹ thuật và ngữ cảnh xuất hiện của từng loại tính chất trong suốt trong đề thi Kỹ sư xử lý thông tin Hàn Quốc.
- Nắm vững 3 kỹ thuật phân mảnh dữ liệu phân tán (`분할 / Fragmentation`): Phân mảnh ngang (`수평 분할`), Phân mảnh dọc (`수직 분할`), và Phân mảnh hỗn hợp (`혼합 분할`).

## 핵심 키워드 (Từ khóa)
- 분산 데이터베이스 목표 (Mục tiêu CSDL phân tán / Distributed DB Goals)
- 투명성 (Tính trong suốt / Transparency)
- 위치 투명성 (Trong suốt vị trí / Location Transparency)
- 중복 투명성 (Trong suốt nhân bản / Replication Transparency)
- 병행 투명성 (Trong suốt đồng thời / Concurrency Transparency)
- 장애 투명성 (Trong suốt sự cố / Failure Transparency)
- 수평 분할 (Phân mảnh ngang / Horizontal Fragmentation: phép Select)
- 수직 분할 (Phân mảnh dọc / Vertical Fragmentation: phép Project)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([16-bai-hoc.md](16-bai-hoc.md), [34-bai-hoc.md](34-bai-hoc.md)):** 4 mục tiêu trong suốt bảo đảm rằng người dùng cuối và ứng dụng không phải thay đổi mã lệnh truy vấn ngay cả khi cấu trúc mạng và vị trí lưu trữ phân tán của CSDL thay đổi.
- **Tiếp nối sang bài sau ([36-bai-hoc.md](36-bai-hoc.md)):** Để đạt được 4 tính chất trong suốt này, hệ thống phải trả giá bằng chi phí vận hành và bài toán quản lý bộ nhớ đệm phân tán.

## 읽는 방법 (Cách đọc)
- Học thuộc bảng 4 định nghĩa trong suốt ở TẦNG A:
  - Chỉ cần nhớ tên logic, không cần biết máy chủ ở đâu $\rightarrow$ **위치 투명성**.
  - Dữ liệu copy nhiều trạm nhưng cảm giác chỉ có 1 bản duy nhất $\rightarrow$ **중복 투명성**.
  - Nhiều giao dịch chạy song song không làm sai kết quả $\rightarrow$ **병행 투명성**.
  - Máy chủ hay mạng bị đứt mà giao dịch vẫn xử lý chính xác $\rightarrow$ **장애 투명성**.
- Nhớ kỹ thuật chia bảng: Chia theo dòng $\rightarrow$ **수평 분할 (Ngang)**; Chia theo cột $\rightarrow$ **수직 분할 (Dọc)**.

---

## 195-196. 분산 데이터베이스 목표 (Distributed DB Goals)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng phân tích chi tiết 4 tính chất Trong suốt của CSDL phân tán:**
  | Tên tính chất trong suốt | Tên tiếng Hàn & Anh | Cơ chế hoạt động trong hệ thống | Dấu hiệu nhận diện đề thi |
  |---|---|---|---|
  | **Trong suốt vị trí** | `위치 투명성` (Location Transparency) | Người dùng truy cập dữ liệu chỉ cần dùng **tên logic của đối tượng**, hoàn toàn không cần biết địa chỉ IP, tên máy chủ, hay vị trí địa lý của trạm lưu trữ dữ liệu. | Đề thi nhắc đến: *"액세스하려는 데이터베이스의 실제 위치를 알 필요 없이 논리적인 명칭만으로 액세스"* |
  | **Trong suốt nhân bản** | `중복 / 복제 투명성` (Replication Transparency) | Một bảng dữ liệu có thể được sao chép thành nhiều bản lưu trữ tại nhiều trạm khác nhau để tăng tốc độ đọc và khả năng chịu lỗi, nhưng **người dùng chỉ thấy duy nhất một bản**, hệ thống tự động đồng bộ hóa các bản sao khi có cập nhật. | Đề thi nhắc đến: *"동일 데이터가 여러 곳에 중복되어 있더라도 하나의 데이터만 존재하는 것처럼 사용"* |
  | **Trong suốt đồng thời** | `병행 투명성` (Concurrency Transparency) | Nhiều giao dịch phân tán từ các trạm khác nhau cùng truy cập và thao tác đồng thời trên cơ sở dữ liệu phân tán nhưng **kết quả luôn nhất quán và không can thiệp làm sai lệch lẫn nhau**. | Đề thi nhắc đến: *"다수의 트랜잭션들이 동시에 실현되더라도 그 결과는 영향을 받지 않음"* |
  | **Trong suốt sự cố** | `장애 투명성` (Failure Transparency) | Khi có sự cố hỏng hóc xảy ra ở một số máy tính, phần mềm DBMS hoặc đường truyền mạng, **hệ thống vẫn bảo toàn tính nguyên tử của giao dịch** và tự động phục hồi chính xác. | Đề thi nhắc đến: *"트랜잭션, DBMS, 네트워크, 컴퓨터 장애에도 불구하고 트랜잭션을 정확하게 처리"* |

- **2. Ba phương pháp Phân mảnh dữ liệu phân tán (데이터 분할 / Fragmentation):**
  - **수평 분할 (Phân mảnh ngang / Horizontal Fragmentation):**
    - Chia nhỏ bảng dữ liệu dựa theo các **bộ (hàng / tuple)** bằng phép toán đại số quan hệ **Select ($\sigma$)**.
    - Mỗi mảnh phân đoạn chứa một tập các hàng riêng biệt (ví dụ: chia bảng Khách hàng thành mảnh Miền Bắc, Miền Trung, Miền Nam).
  - **수직 분할 (Phân mảnh dọc / Vertical Fragmentation):**
    - Chia nhỏ bảng dữ liệu dựa theo các **thuộc tính (cột / attribute)** bằng phép toán đại số quan hệ **Project ($\pi$)**.
    - Mỗi mảnh phân đoạn chứa một số cột nhất định kèm theo Khóa chính của bảng để có thể ghép lại không mất mát thông tin.
  - **혼합 분할 (Phân mảnh hỗn hợp / Hybrid Fragmentation):**
    - Kết hợp cả hai phương pháp phân mảnh ngang và dọc trên cùng một bảng.
- **주의/함정 (Bẫy đề thi):**
  - Đề hỏi: *"Mục tiêu nào giúp người dùng truy cập dữ liệu mà không cần biết IP hay vị trí máy chủ?"* $\rightarrow$ Đáp án: **위치 투명성 (Location Transparency)**.
  - Phân mảnh ngang dùng phép **Select ($\sigma$)**, còn phân mảnh dọc dùng phép **Project ($\pi$)**. Không được nhầm lẫn giữa hai phép toán này!

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tình huống thi trắc nghiệm điển hình:**
  - *"Một công ty có trụ sở chính tại Seoul và hai chi nhánh tại Busan và Daegu. Bảng NHAN_VIEN được chia thành 3 phần: nhân viên Seoul lưu tại máy chủ Seoul, nhân viên Busan lưu tại Busan, nhân viên Daegu lưu tại Daegu. Giám đốc tại Seoul khi tra cứu toàn bộ nhân viên công ty chỉ cần gõ `SELECT * FROM NHAN_VIEN` mà không cần quan tâm dữ liệu lấy từ máy chủ nào."*
  - **Phân tích:**
    - Cách chia bảng theo khu vực địa lý ở trên là: **수평 분할 (Phân mảnh ngang)**.
    - Việc giám đốc chỉ gõ tên bảng logic `NHAN_VIEN` mà xem được dữ liệu toàn quốc thể hiện: **위치 투명성 (Location Transparency)**.

### 복습 체크리스트
- [ ] Kể tên và giải thích chính xác 4 loại tính chất trong suốt: 위치, 중복/복제, 병행, 장애 투명성.
- [ ] Phân biệt được 수평 분할 (chia hàng bằng Select) và 수직 분할 (chia cột bằng Project).
- [ ] Nêu được cơ chế đảm bảo của 장애 투명성 khi mạng gặp sự cố.
- [ ] Tự giải thích được tình huống thực tế về 위치 투명성.
