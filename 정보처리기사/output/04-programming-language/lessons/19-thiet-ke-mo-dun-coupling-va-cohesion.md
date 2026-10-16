# 모듈화 설계, 결합도 및 응집도 (Thiết kế mô-đun, Coupling & Cohesion)

## 학습 목표 (Mục tiêu)
- Nắm vững nguyên lý Mô-đun hóa (모듈화 - Modularity) và tiêu chí thiết kế phần mềm độc lập tối ưu: Ghép nối yếu (약한 결합도 - Loose Coupling) và Gắn kết mạnh (강한 응집도 - High Cohesion), cùng cách phân tích chỉ số Fan-in và Fan-out.
- Thuộc lòng thứ tự xếp hạng Độ ghép nối từ tốt nhất đến tồi nhất theo khẩu quyết **자스제외공내** (Data > Stamp > Control > External > Common > Content).
- Thuộc lòng thứ tự xếp hạng Độ gắn kết từ mạnh nhất đến yếu nhất theo khẩu quyết **기순교절시논우** (Functional > Sequential > Communicational > Procedural > Temporal > Logical > Coincidental).
- Thấu hiểu đặc trưng của Biểu đồ N-S Chart (không mũi tên, cấm GOTO) và tính toán chính xác Độ phức tạp chu trình McCabe $V(G) = E - N + 2 = P + 1$.

## 핵심 키워드 (Từ khóa)
- 약한 결합도 & 강한 응집도 (Loose Coupling & High Cohesion) — Tiêu chuẩn vàng của thiết kế phần mềm độc lập.
- 결합도 6단계 (Coupling 6 Levels) — 자료, 스탬프, 제어, 외부, 공통, 내용 (자스제외공내).
- 응집도 7단계 (Cohesion 7 Levels) — 기능적, 순차적, 교환적, 절차적, 시간적, 논리적, 우연적 (기순교절시논우).
- 팬인 vs 팬아웃 (Fan-In vs Fan-Out) — Số module gọi đến nó vs Số module do nó gọi trực tiếp.
- N-S 차트 (Nassi-Schneiderman Chart) — Biểu đồ hình hộp có cấu trúc, không mũi tên, cấm dùng lệnh GOTO.
- 맥케이브 순환 복잡도 (McCabe Cyclomatic Complexity) — $V(G) = E - N + 2 = P + 1$.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa từ các cấu trúc rẽ nhánh, vòng lặp đã học ở `04-cau-truc-dieu-khien-re-nhanh-va-vong-lap.md` và nguyên lý đóng gói hướng đối tượng ở `08-lap-trinh-huong-doi-tuong-java-oop.md`.
- **Đang giải quyết gì (Current Problem):** Giải quyết câu hỏi kiến trúc phần mềm cốt lõi: Làm sao chia tách một hệ thống phức tạp thành các khối mã nguồn nhỏ để khi thay đổi tính năng không làm đổ vỡ các phần còn lại, và đo lường độ phức tạp của mã nguồn bằng công thức nào.
- **Dùng đi đâu (Forward Handoff):** Độ phức tạp chu trình $V(G)$ tính toán được từ biểu đồ luồng điều khiển của bài học này chính là số lượng trường hợp kiểm thử đường cơ sở bắt buộc phải thực thi trong Kiểm thử Hộp trắng ở bài `20-kiem-thu-phan-mem-va-vong-doi-loi.md`.

## 읽는 방법 (Cách đọc)
- **Khẩu quyết Kết hợp (결합도 - Coupling):** Càng YẾU càng TỐT $\rightarrow$ **자·스·제·외·공·내** (자료 Data $\rightarrow$ 스탬프 Stamp $\rightarrow$ 제어 Control $\rightarrow$ 외부 External $\rightarrow$ 공통 Common $\rightarrow$ 내용 Content).
- **Khẩu quyết Gắn kết (응집도 - Cohesion):** Càng MẠNH càng TỐT $\rightarrow$ **기·순·교·절·시·논·우** (기능적 Functional $\rightarrow$ 순차적 Sequential $\rightarrow$ 교환적 Communicational $\rightarrow$ 절차적 Procedural $\rightarrow$ 시간적 Temporal $\rightarrow$ 논리적 Logical $\rightarrow$ 우연적 Coincidental).
- **N-S Chart:** Cứ thấy đặc điểm **"Không có đường mũi tên (화살표 없음)"** và **"Không có GOTO (GOTO 없음)"** $\rightarrow$ Chọn ngay **N-S 차트 (Nassi-Schneiderman)**.

---

## 모듈화 설계, 결합도 및 응집도

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `바람직한 소프트웨어 설계는 결합도를 약하게(자스제외공내), 응집도를 강하게(기순교절시논우) 해야 한다. N-S 차트는 화살표와 GOTO문이 없는 구조적 도표이며, 맥케이브 순환 복잡도 계산식은 V(G) = E - N + 2 = P + 1이다.`
  - [Tiếng Việt]: Thiết kế phần mềm tốt phải giảm độ ghép nối Coupling (자스제외공내) và tăng độ gắn kết Cohesion (기순교절시논우). Biểu đồ N-S không có mũi tên và cấm GOTO; độ phức tạp chu trình McCabe tính bằng V(G) = E - N + 2 = P + 1.

- **1. Bảng 6 cấp độ ghép nối Coupling (결합도 - 자스제외공내):**
*(Xếp hạng từ YẾU NHẤT / TỐT NHẤT $\rightarrow$ MẠNH NHẤT / TỒI NHẤT)*

| Cấp độ | Tên tiếng Hàn & Anh | Bản chất cơ chế phụ thuộc | Đánh giá chất lượng |
| :---: | :--- | :--- | :---: |
| **1 (Tốt nhất)**| **자료 결합도** (Data Coupling) | Hai module chỉ trao đổi dữ liệu thuần túy qua **danh sách tham số đối số**. | **Yếu nhất (Tốt nhất)** |
| **2** | **스탬프 결합도** (Stamp Coupling) | Truyền **cấu trúc dữ liệu tổng hợp** (Mảng, Struct, Record); module nhận chỉ dùng 1 phần. | Tốt vừa |
| **3** | **제어 결합도** (Control Coupling) | Module này truyền **cờ điều khiển (Flag, Switch)** để chi phối luồng logic của module kia. | Trung bình |
| **4** | **외부 결합도** (External Coupling) | Các module cùng chia sẻ giao thức ngoài hoặc biến dữ liệu do hệ thống thứ 3 quy định. | Khá tồi |
| **5** | **공통 결합도** (Common Coupling) | Các module **cùng chia sẻ chung một vùng dữ liệu toàn cục (Global Variable)**. | Rất tồi |
| **6 (Tồi nhất)**| **내용 결합도** (Content Coupling) | Module này **can thiệp trực tiếp vào mã nguồn hoặc dữ liệu nội bộ** của module khác. | **Mạnh nhất (Tồi nhất)** |

- **2. Bảng 7 cấp độ gắn kết Cohesion (응집도 - 기순교절시논우):**
*(Xếp hạng từ MẠNH NHẤT / TỐT NHẤT $\rightarrow$ YẾU NHẤT / TỒI NHẤT)*

| Cấp độ | Tên tiếng Hàn & Anh | Mối quan hệ giữa các câu lệnh bên trong module | Đánh giá chất lượng |
| :---: | :--- | :--- | :---: |
| **1 (Tốt nhất)**| **기능적 응집도** (Functional) | **Mọi câu lệnh cùng thực hiện một nhiệm vụ logic duy nhất** (ví dụ: hàm tính căn bậc hai `sqrt()`). | **Mạnh nhất (Tốt nhất)** |
| **2** | **순차적 응집도** (Sequential) | **Đầu ra của câu lệnh/bước này là đầu vào trực tiếp** của câu lệnh/bước tiếp theo. | Rất tốt |
| **3** | **교환적 응집도** (Communicational)| Các thao tác khác nhau nhưng **cùng xử lý trên một cấu trúc dữ liệu chung**. | Khá tốt |
| **4** | **절차적 응집도** (Procedural) | Các thao tác được thực hiện tuần tự theo một **quy trình nghiệp vụ xác định**. | Trung bình |
| **5** | **시간적 응집도** (Temporal) | Các thao tác được gom chung vì **cùng diễn ra tại một thời điểm** (ví dụ: hàm khởi tạo `init()`). | Khá yếu |
| **6** | **논리적 응집도** (Logical) | Các thao tác tương tự nhau về mặt logic được gom chung (ví dụ hàm xử lý tất cả sự kiện chuột/phím).| Yếu |
| **7 (Tồi nhất)**| **우연적 응집도** (Coincidental) | Các câu lệnh gom chung một chỗ mà **hoàn toàn không có bất kỳ mối liên hệ nào**. | **Yếu nhất (Tồi nhất)** |

- **3. Phân biệt Fan-In vs Fan-Out trong cấu trúc điều khiển phân cấp:**

| Chỉ số | Khái niệm kỹ thuật | Ý nghĩa đo lường chất lượng |
| :--- | :--- | :--- |
| **Fan-In (Quạt vào)** | **Số lượng module gọi trực tiếp đến module này**. | **Fan-In cao là rất tốt** (thể hiện tính tái sử dụng cao); nhưng cần kiểm thử cẩn thận vì nếu module này lỗi sẽ ảnh hưởng lan truyền. |
| **Fan-Out (Quạt ra)** | **Số lượng module do module này trực tiếp gọi đi**. | **Fan-Out quá cao là không tốt** (thể hiện cấu trúc quá phức tạp, ôm đồm nhiều việc); nên tái cấu trúc thành các module trung gian. |

- **4. Công thức Độ phức tạp chu trình McCabe (순환 복잡도):**
  $$V(G) = E - N + 2 = P + 1$$
  - $E$: Số cạnh (Cung - Edges) trong Biểu đồ luồng điều khiển.
  - $N$: Số nút (Đỉnh - Nodes) trong Biểu đồ luồng điều khiển.
  - $P$: Số nút vị từ điều kiện (Predicate Nodes - các nút chứa điều kiện `if`, `while`).

- **주의/함정 (Bẫy đề thi):**
  - **Nhầm chiều ưu tiên:** Đề thi hỏi *"Đâu là thiết kế mong muốn?"* $\rightarrow$ Đáp án đúng là **약한 결합도 (Coupling yếu)** và **강한 응집도 (Cohesion mạnh)**. Chọn Coupling mạnh là sai bẫy.
  - **Đặc trưng N-S Chart:** Biểu đồ N-S có tính trực quan cao, chỉ dùng 3 cấu trúc chuẩn (Tuần tự, Lựa chọn, Lặp); **tuyệt đối không dùng mũi tên tự do và cấm lệnh nhảy GOTO**.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"자스제외공내 Coupling càng yếu càng êm; 기순교절시논우 Cohesion càng mạnh càng bền; N-S cấm GOTO, McCabe E trừ N cộng 2."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bài toán trắc nghiệm tính Độ phức tạp chu trình McCabe chuẩn đề thi HRDK:
- **Đề bài:** Một đồ thị luồng điều khiển (Control Flow Graph) của một hàm kiểm tra đơn hàng có **11 cạnh ($E = 11$)** và **8 nút ($N = 8$)**. Hỏi:
  1. Độ phức tạp chu trình $V(G)$ của đoạn mã này là bao nhiêu?
  2. Số lượng nút vị từ điều kiện ($P$) xuất hiện trong mã nguồn là bao nhiêu?

- **Phân tích thay công thức:**
  - Áp dụng công thức 1:
    $$V(G) = E - N + 2 = 11 - 8 + 2 = 3 + 2 = \mathbf{5}.$$
  - Áp dụng công thức 2 liên hệ với nút điều kiện:
    $$V(G) = P + 1 \implies 5 = P + 1 \implies P = 5 - 1 = \mathbf{4}.$$
- **Đáp án:** Độ phức tạp chu trình $V(G) = \mathbf{5}$; số nút điều kiện $P = \mathbf{4}$. Ý nghĩa: Lập trình viên cần thiết kế tối thiểu **5 trường hợp kiểm thử (Test Cases)** để phủ toàn bộ các đường dẫn độc lập cơ bản.

#### 2. Minh họa trực quan 3 loại cấu trúc trong Biểu đồ N-S (Nassi-Schneiderman):
```
+-----------------------------------+
|       Thao tác 1 (Tuần tự)        |
+-----------------------------------+
|          Điều kiện (if)           |
|        /                \         |
|      ĐÚNG                SAI      |
|  Thao tác 2A         Thao tác 2B  |
+-----------------------------------+
|      LẶP (While / For)            |
|  +-----------------------------+  |
|  |    Thân vòng lặp lặp lại    |  |
|  +-----------------------------+  |
+-----------------------------------+
```
*(Toàn bộ nằm gọn trong các khối hộp chữ nhật, không hề có mũi tên liên kết rời rạc).*

---

### 복습 체크리스트
- [ ] Ghi nhớ tiêu chí thiết kế chuẩn: 약한 결합도 (Coupling yếu) và 강한 응집도 (Cohesion mạnh).
- [ ] Thuộc lòng 6 cấp độ Coupling: **자스제외공내** (자료 > 스탬프 > 제어 > 외부 > 공통 > 내용).
- [ ] Thuộc lòng 7 cấp độ Cohesion: **기순교절시논우** (기능 > 순차 > 교환 > 절차 > 시간 > 논리 > 우연).
- [ ] Phân biệt được: Fan-In cao là tốt (tái sử dụng), Fan-Out cao là xấu (quá phức tạp).
- [ ] Nhớ đặc trưng N-S Chart: Không mũi tên, cấm dùng GOTO.
- [ ] Thuộc lòng công thức McCabe: $V(G) = E - N + 2 = P + 1$.
