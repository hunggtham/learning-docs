# 반정규화와 쿼리 성능 최적화 (Phi Chuẩn Hóa và Tối Ưu Hóa Hiệu Năng Truy Vấn)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm Phi chuẩn hóa (`반정규화 / Denormalization`) và bản chất đánh đổi (Trade-off) giữa hiệu năng đọc (SELECT) và tính toàn vẹn dữ liệu / chi phí ghi (CUD).
- Làm chủ 4 kỹ thuật phi chuẩn hóa cốt lõi: Gộp bảng (`테이블 통합`), Chia bảng (`테이블 분할` - ngang/dọc), Thêm bảng trùng lặp (`중복 테이블 추가`), và Thêm thuộc tính trùng lặp (`중복 속성 추가`).
- Phân biệt sâu sắc cơ chế hoạt động của Bộ tối ưu hóa truy vấn (`옵티마이저 / Optimizer`): Bộ tối ưu hóa theo quy tắc (RBO) và Bộ tối ưu hóa theo chi phí (CBO).
- Nhận diện các bẫy trắc nghiệm về thông tin thống kê trong CBO và tác động hai mặt của phi chuẩn hóa.

## 핵심 키워드 (Từ khóa)
- 반정규화 (Phi chuẩn hóa / Denormalization / 역정규화)
- 테이블 통합, 테이블 분할 (Gộp bảng, Chia bảng: 수평 vs 수직)
- 중복 테이블, 중복 속성 (Bảng trùng lặp, Cột trùng lặp)
- 트레이드오프 (Đánh đổi: Tốc độ đọc vs Chi phí ghi CUD)
- 옵티마이저 (Bộ tối ưu hóa: RBO vs CBO)
- 실행 계획, APM (Execution Plan, Quản lý hiệu năng ứng dụng)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Ở [06-bat-thuong-du-lieu-phu-thuoc-ham-va-chuan-hoa-1nf-5nf.md](06-bat-thuong-du-lieu-phu-thuoc-ham-va-chuan-hoa-1nf-5nf.md), chúng ta đã nắm vững quy trình chuẩn hóa từ 1NF đến 5NF nhằm phân rã triệt để quan hệ để loại trừ hoàn toàn dư thừa dữ liệu và 3 loại dị thường.
- **Đang giải quyết gì (Current Problem):** Việc chuẩn hóa quá đà chia cắt dữ liệu thành quá nhiều bảng nhỏ, khiến các câu truy vấn thông thường phải thực hiện nhiều phép Join phức tạp và gây thắt cổ chai I/O đĩa. Bài học này giải quyết bài toán tái cân bằng hiệu năng bằng kỹ thuật **Phi chuẩn hóa (Denormalization)** và tối ưu truy vấn thông qua **Bộ tối ưu hóa (Optimizer)**.
- **Dùng đi đâu (Forward Handoff):** Cấu trúc bảng và đường dẫn tối ưu được thiết lập ở bài học này sẽ là nền móng vận hành để xử lý an toàn các giao dịch đa người dùng và kiểm soát đồng thời (Concurrency Control) ở [08-giao-dich-trang-thai-acid-va-dieu-khien-dong-thoi.md](08-giao-dich-trang-thai-acid-va-dieu-khien-dong-thoi.md).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nắm vững 4 kỹ thuật phi chuẩn hóa, bảng so sánh đối đầu RBO vs CBO và các bẫy trắc nghiệm hay gài nhất.
- Đọc TẦNG B để hiểu sâu bản chất đánh đổi giữa tốc độ đọc và chi phí ghi, kỹ thuật phân vùng ngang/dọc và cơ chế Optimizer.

---

## 반정규화와 쿼리 성능 최적화

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng 4 kỹ thuật Phi chuẩn hóa chính (반정규화의 4대 기법)

| Phương pháp (기법) | Kỹ thuật chi tiết (세부 기법) | Giải thích & Mục đích tối ưu (설명 및 목적) |
| :--- | :--- | :--- |
| **테이블 통합** (Gộp bảng) | • Gộp bảng quan hệ 1:1 • Gộp bảng quan hệ 1:N • Gộp bảng Super/Sub-type | Triệt tiêu hoàn toàn phép Join để lấy dữ liệu qua 1 lần đọc I/O duy nhất. Tuy nhiên làm kích thước bảng phình to, tăng chi phí Full Table Scan. |
| **테이블 분할** (Chia bảng) | • **수평 분할 (Horizontal)**: Chia theo hàng (Row) • **수직 분할 (Vertical)**: Chia theo cột (Column) | • **Phân chia ngang**: Thu hẹp phạm vi quét đĩa theo chu kỳ/khu vực. • **Phân chia dọc**: Tách cột tra cứu thường xuyên khỏi các cột LOB/TEXT dung lượng lớn. |
| **중복 테이블 추가** (Thêm bảng trùng) | • **집계 테이블**: Bảng kết quả tổng hợp sẵn • **진행 테이블**: Bảng tiến độ • **특정 부분 테이블**: Bảng tập con dữ liệu | Giữ sẵn kết quả tính toán định kỳ (SUM, COUNT), không phải tính lại nhiều lần, giải phóng tải CPU máy chủ. |
| **중복 속성 추가** (Thêm cột trùng) | • Sao chép cột từ bảng khác • Thêm cột phái sinh (Derived Column) • Tích hợp khóa ngoại | Chặn đứng việc phải Join cả bảng chỉ để lấy 1-2 cột thông tin. Điểm nóng dễ phát sinh dị thường sửa (Update Anomaly). |

#### 2. So sánh đối đầu: RBO vs CBO (규칙 기반 vs 비용 기반 옵티마이저)

```
[ SQL 작성 ] ──> [ Parser ] ──> [ Optimizer ] ──> [ Execution Plan ] ──> [ Execution Engine ]
                                     │
                     ┌───────────────┴───────────────┐
                     ▼                               ▼
             규칙 기반 (RBO)                 비용 기반 (CBO)
```

| Tiêu chí so sánh (구분) | RBO (규칙 기반 옵티마이저 / Rule-Based) | CBO (비용 기반 옵티마이저 / Cost-Based) |
| :--- | :--- | :--- |
| **Tiêu chí tối ưu** | Xác định đường đi dựa trên **thứ bậc ưu tiên cố định (1~15)** | Tính toán **chi phí tài nguyên ước tính (Cost)** để chọn phương án tối thiểu |
| **Yếu tố phụ thuộc** | Phụ thuộc tuyệt đối vào **cách viết SQL và cấu trúc Index** của lập trình viên | Phụ thuộc vào **độ chính xác của thông tin thống kê (Statistics Info)** trong từ điển CSDL |
| **Xét chi phí tài nguyên** | Hoàn toàn không quan tâm đến chi phí I/O hay tải CPU | Dự đoán toàn diện số lần đọc đĩa I/O, mức chiếm dụng CPU và bộ nhớ RAM |
| **Độ dự đoán** | Cố định và rất dễ đoán định kế hoạch thực thi | Biến động động theo quy mô dữ liệu và biểu đồ phân bố (Histogram) |

#### 3. Bẫy đề thi và bài tập nhận diện (시험 대비 함정 & 실전 포인트)

- **Bẫy định nghĩa RBO vs CBO:**
  - *Câu hỏi:* "Bộ tối ưu hóa nào sử dụng thông tin thống kê (통계 정보) và phân bố dữ liệu để lập kế hoạch?" $\rightarrow$ Chọn **CBO (비용 기반 옵티마이저)**.
  - *Câu hỏi:* "Bộ tối ưu nào đưa ra kế hoạch thực thi phụ thuộc hoàn toàn vào thứ tự viết câu lệnh của lập trình viên?" $\rightarrow$ Chọn **RBO (규칙 기반 옵티마이저)**.
- **Bẫy mục đích 반정규화:**
  - Khẳng định: *"Phi chuẩn hóa luôn luôn làm tăng hiệu năng toàn diện của hệ thống trong mọi trường hợp"* $\rightarrow$ **SAI**. Phi chuẩn hóa chỉ tăng tốc độ ĐỌC (SELECT), nhưng làm GIẢM hiệu năng GHI (INSERT, UPDATE, DELETE) và tăng nguy cơ bất nhất quán dữ liệu.
- **Phân biệt 수평 분할 vs 수직 분할:**
  - Chia theo dòng (Row / Record) $\rightarrow$ **수평 분할 (Horizontal Partitioning)**.
  - Chia theo cột (Column / Attribute) $\rightarrow$ **수직 분할 (Vertical Partitioning)**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bản chất Phi chuẩn hóa và Đánh đổi (Trade-off)
```
[ Mô hình Chuẩn hóa cao ]  --- (Join nhiều, I/O chậm) --->  [ Áp dụng 반정규화 ]
(Ưu tiên: Toàn vẹn, không dị thường)                   (Ưu tiên: Tốc độ đọc, giảm Join)
```

- [한국어]: **반정규화(Denormalization)**는 시스템의 성능 향상 및 운영 편의성을 위해 정규화된 데이터 모델을 통합, 중복, 분할하는 과정이다. 무조건적인 정규화가 아닌, **데이터 무결성과 시스템 성능 간의 균형(Trade-off)**을 맞추는 엔지니어링 의사결정이다.
- [Tiếng Việt]: **Phi chuẩn hóa (Denormalization)** là quá trình tích hợp, tạo trùng lặp hoặc phân chia các mô hình dữ liệu đã được chuẩn hóa nhằm nâng cao hiệu năng hệ thống và độ tiện lợi trong vận hành. Đây là quyết định kỹ thuật nhằm cân bằng giữa **tính toàn vẹn dữ liệu** và **tốc độ đáp ứng hệ thống**.

##### Trường hợp cần xem xét phi chuẩn hóa
1. Khi các truy vấn thường xuyên xuất hiện nhiều phép kết nối bảng (Join) gây suy giảm hiệu năng nghiêm trọng.
2. Khi phải liên tục thực hiện các phép tính toán tổng hợp (SUM, AVG, COUNT) trên tập dữ liệu khổng lồ.
3. Khi việc đọc một phạm vi dữ liệu cụ thể đòi hỏi phải quét qua quá nhiều khối đĩa vật lý.

##### Rủi ro khi phi chuẩn hóa quá đà
1. **Tái phát dị thường dữ liệu:** Dư thừa dữ liệu làm tái xuất hiện các dị thường thêm, xóa, sửa.
2. **Suy giảm tính nhất quán:** Khi dữ liệu ở bảng chính thay đổi mà trường trùng lặp chưa kịp cập nhật, hệ thống rơi vào trạng thái xung đột dữ liệu.
3. **Tốn bộ nhớ & Chậm thao tác ghi (CUD):** Mọi thao tác INSERT/UPDATE/DELETE phải đồng bộ trên nhiều bảng và cột trùng lặp, khiến tốc độ ghi giảm mạnh.

#### 2. So sánh sâu: Phân vùng ngang vs Phân vùng dọc

- **수평 분할 (Horizontal Partitioning / Phân vùng ngang):** Chia bảng theo hàng (Row) dựa trên các tiêu chí như khoảng thời gian, chi nhánh, trạng thái dữ liệu (ví dụ: dữ liệu 3 tháng gần nhất tách riêng khỏi kho lưu trữ lịch sử).
- **수직 분할 (Vertical Partitioning / Phân vùng dọc):** Chia bảng theo cột (Column) khi bảng có quá nhiều thuộc tính hoặc chứa các trường dữ liệu dung lượng lớn (LOB/TEXT), giúp tăng mật độ bản ghi trên mỗi khối đĩa, tối ưu bộ đệm (Buffer Cache).

#### 3. Công cụ APM (Application Performance Management)

- **Định nghĩa:** Công cụ quản lý hiệu năng ứng dụng, theo dõi theo thời gian thực để phát hiện các câu truy vấn thắt cổ chai (Slow Query), rò rỉ kết nối (Connection Leak) và tắc nghẽn giao dịch trong hệ thống cơ sở dữ liệu.

---

### 복습 체크리스트
- [ ] Định nghĩa được 반정규화 và giải thích tại sao nó là một sự đánh đổi giữa hiệu năng và tính toàn vẹn.
- [ ] Phân biệt rõ ràng 4 nhóm kỹ thuật: 테이블 통합, 테이블 분할, 중복 테이블 추가, 중복 속성 추가.
- [ ] Giải thích được sự khác biệt cốt lõi giữa 수평 분할 (Row) và 수직 분할 (Column).
- [ ] Trình bày được bản chất của 2 cơ chế 옵티마이저: RBO (Rule-Based) và CBO (Cost-Based).
- [ ] Nhận biết vai trò của công cụ APM trong việc phát hiện 병목 쿼리 (Slow Query).
