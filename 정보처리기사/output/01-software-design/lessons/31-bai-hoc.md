# 2. 모듈 (Module) & 독립성 (Independence)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm Tính độc lập chức năng (`기능적 독립성`) và nguyên tắc vàng của thiết kế mô-đun: **Giảm độ kết hợp (`결합도 낮춤`) và Tăng độ gắn kết (`응집도 높임`)**.
- Thuộc nằm lòng thứ tự 7 cấp độ của Độ gắn kết (`응집도 - Cohesion`) từ mạnh nhất (tốt nhất) đến yếu nhất (tồi tệ nhất): Chức năng > Tuần tự > Giao tiếp/Trao đổi > Thủ tục > Thời gian > Logic > Ngẫu nhiên.
- Phân biệt bản chất của từng loại 응집도 qua các ví dụ thực tế trong đề thi trắc nghiệm (như hàm khởi tạo, luồng xử lý đầu ra nối đầu vào).

## 핵심 키워드 (Từ khóa)
- 기능적 독립성 (Tính độc lập chức năng / Functional Independence)
- 응집도 (Độ gắn kết nội bộ / Cohesion / 높을수록 좋음)
- 기능적 응집도 (Functional Cohesion / 단일 기능 수행 / Tốt nhất)
- 순차적 응집도 (Sequential Cohesion / 출력물이 입력물로 사용)
- 통신적·교환적 응집도 (Communicational Cohesion / 동일 자료 대상)
- 절차적 응집도 (Procedural Cohesion / 순차 실행)
- 시간적 응집도 (Temporal Cohesion / 특정 시간에 동시 실행)
- 논리적 응집도 (Logical Cohesion / 유사한 성격 묶음)
- 우연적 응집도 (Coincidental Cohesion / 아무 관련 없음 / Tồi tệ nhất)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([3. 모듈](30-bai-hoc.md)):** Sau khi xem xét Độ kết hợp (Coupling giữa các mô-đun), bài này khảo sát mặt đối trọng sống còn bên trong nội bộ mô-đun: Độ gắn kết (Cohesion).
- **Tiếp nối sang bài sau ([7. 공통 모듈](32-bai-hoc.md)):** Áp dụng nguyên lý gắn kết cao và kết hợp thấp vào việc thiết kế Mô-đun dùng chung (`공통 모듈`) và 5 nguyên tắc đặc tả chính xác.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc làu thần chú 7 chữ cái kinh điển: **기 - 순 - 교 - 절 - 시 - 논 - 우** (Chức năng > Tuần tự > Giao tiếp > Thủ tục > Thời gian > Logic > Ngẫu nhiên).
- Đọc TẦNG B để phân biệt sự khác nhau giữa Sequential Cohesion (Đầu ra là đầu vào) và Communicational Cohesion (Cùng thao tác trên 1 dữ liệu).

---

## 2. 모듈 (Module) & 독립성 (Independence)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. 기능적 독립성 (Tính độc lập chức năng của mô-đun):**
  - Là tiêu chuẩn vàng đánh giá chất lượng phần mềm khi áp dụng kỹ thuật mô-đun hóa. Một mô-đun có tính độc lập cao khi nó chỉ thực hiện một chức năng duy nhất và ít tương tác phụ thuộc vào các mô-đun khác.
  - **Công thức vàng cốt lõi:**
    $$\mathbf{결합도 \downarrow (Giảm\ Coupling)} \quad \text{và} \quad \mathbf{응집도 \uparrow (Tăng\ Cohesion)}$$
- **2. 응집도 (Cohesion - Độ gắn kết nội bộ):**
  - **Định nghĩa:** Là thước đo mức độ liên kết chặt chẽ và tập trung giữa các câu lệnh, phương thức và biến dữ liệu bên trong nội bộ của một mô-đun duy nhất (`모듈 내부 요소들의 관련성`).
  - **Nguyên tắc thiết kế:** **응집도는 높을수록 좋다 (Độ gắn kết CÀNG CAO CÀNG TỐT)**.
- **Thứ tự 7 cấp độ 응집도 (Từ Cao nhất/Tốt nhất $\rightarrow$ Thấp nhất/Xấu nhất):**
  $$\text{기능적 (Functional)} > \text{순차적 (Sequential)} > \text{통신적/교환적 (Communicational)} > \text{절차적 (Procedural)} > \text{시간적 (Temporal)} > \text{논리적 (Logical)} > \text{우연적 (Coincidental)}$$
  - 💡 **Thần chú ghi nhớ:** **기 - 순 - 교 - 절 - 시 - 논 - 우** (Kỹ sư giỏi quyết chỉ nâng uy tín).
- **Đặc trưng chi tiết của 7 cấp độ:**
  1. **기능적 응집도 (Functional Cohesion - Gắn kết chức năng - TỐT NHẤT):**
     - Mọi phần tử trong mô-đun đều tập trung hoàn thành **duy nhất một chức năng đơn lẻ trọn vẹn (`단 하나의 기능만 수행`)**. Ví dụ: hàm tính số mũ `pow(x, y)` hoặc hàm tính căn bậc hai.
  2. **순차적 응집도 (Sequential Cohesion - Gắn kết tuần tự):**
     - **Đầu ra của một hoạt động này được sử dụng làm đầu vào trực tiếp cho hoạt động kế tiếp (`한 활동의 출력 데이터가 다음 활동의 입력 데이터로 사용`)** bên trong mô-đun.
  3. **통신적 / 교환적 응집도 (Communicational Cohesion - Gắn kết giao tiếp/trao đổi):**
     - Các câu lệnh/hàm bên trong mô-đun thực hiện các thao tác khác nhau nhưng **cùng sử dụng chung một tập dữ liệu đầu vào hoặc cùng sinh ra một tập dữ liệu đầu ra chung (`동일한 입력 자료를 사용하여 서로 다른 기능을 수행`)**.
  4. **절차적 응집도 (Procedural Cohesion - Gắn kết thủ tục):**
     - Các phần tử trong mô-đun được nhóm lại với nhau chỉ vì chúng phải được **thực thi theo một trình tự các bước xác định (`정해진 순서대로 실행`)**.
  5. **시간적 응집도 (Temporal Cohesion - Gắn kết thời gian):**
     - Các hoạt động được gom vào một mô-đun chỉ vì chúng **diễn ra vào cùng một thời điểm (`특정 시간에 처리`)**. Ví dụ: hàm khởi tạo hệ thống `initialize()` hoặc hàm đóng hệ thống lúc tắt máy.
  6. **논리적 응집도 (Logical Cohesion - Gắn kết logic):**
     - Các phần tử có tính chất logic tương tự nhau được gom vào một chỗ nhưng thực tế thực hiện các công việc riêng biệt được lựa chọn qua một tham số điều khiển.
  7. **우연적 응집도 (Coincidental Cohesion - Gắn kết ngẫu nhiên - TỒI TỆ NHẤT):**
     - Các phần tử được gom vào một mô-đun **hoàn toàn ngẫu nhiên, không hề có bất kỳ mối quan hệ ý nghĩa hay luồng dữ liệu nào liên kết với nhau (`서로 관련 없는 요소들로 구성`)**.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Cấp độ gắn kết nào là cao nhất mang lại chất lượng thiết kế tốt nhất?"* -> **기능적 응집도 (Functional Cohesion)**.
  - **Bẫy 2:** *"Đặc trưng của 순차적 응집도 (Sequential Cohesion) là gì?"* -> **Đầu ra của bước này là đầu vào của bước kia (출력물이 다음의 입력물로 사용)**.
  - **Bẫy 3:** *"Hàm khởi tạo initialize() vừa nạp cấu hình vừa mở DB thuộc cấp độ nào?"* -> **시간적 응집도 (Temporal Cohesion)**.
  - **Bẫy 4:** *"Cấp độ gắn kết nào là tồi tệ nhất?"* -> **우연적 응집도 (Coincidental Cohesion)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Độc lập chức năng cần Cohesion cao Coupling thấp; Cohesion từ tốt đến xấu: Chức năng 1 việc, Tuần tự ra vào, Giao tiếp chung data, Thủ tục theo bước, Thời gian cùng lúc, Logic na ná, Ngẫu nhiên gom bừa".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **So sánh trực quan qua kịch bản nghiệp vụ:**
  - **Sequential (Tuần tự):** Hàm `processInvoice()` gồm: Bước 1 tính tổng tiền hóa đơn $\rightarrow$ lấy tổng tiền đó làm tham số cho Bước 2 tính thuế VAT.
  - **Communicational (Giao tiếp):** Hàm `queryCustomerInfo()` nhận vào `Mã khách hàng`, từ mã này vừa hiển thị thông tin cá nhân lên màn hình vừa xuất lịch sử mua hàng ra file PDF (chung dữ liệu đầu vào nhưng làm 2 việc khác nhau).
  - **Temporal (Thời gian):** Hàm `onStart()` khi mở app: khởi tạo camera, kiểm tra kết nối mạng 4G, load dữ liệu cache (chẳng liên quan gì nhau nhưng làm cùng lúc khi app bật lên).

### 복습 체크리스트
- [ ] Khẳng định được công thức vàng: 결합도는 낮추고 응집도는 높인다.
- [ ] Đọc vanh vách 7 cấp độ 응집도 từ cao đến thấp: 기 > 순 > 교 > 절 > 시 > 논 > 우.
- [ ] Nhận diện được ví dụ của 기능적 응집도 (làm 1 việc duy nhất trọn vẹn).
- [ ] Nhận diện được ví dụ của 순차적 응집도 (đầu ra là đầu vào).
- [ ] Nhận diện được ví dụ của 시간적 응집도 (hàm khởi tạo đồng thời).
