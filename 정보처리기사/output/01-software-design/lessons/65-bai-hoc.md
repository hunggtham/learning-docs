# 4. 응집도 (Cohesion - Độ gắn kết)

## 학습 목표 (Mục tiêu)
- Định nghĩa chính xác khái niệm 응집도 (Cohesion - Độ gắn kết nội tại của mô-đun) và nguyên lý thiết kế chất lượng cao: 응집도는 높을수록(강할수록) 좋다.
- Nằm lòng thứ tự phân hạng 7 cấp độ 응집도 từ mạnh nhất (tốt nhất) đến yếu nhất (tồi tệ nhất): 기능 > 순차 > 교환 > 절차 > 시간 > 논리 > 우연.
- Phân biệt đặc trưng cơ bản và tình huống thực tế của từng cấp độ 응집도 để xử lý chính xác các câu hỏi thi trắc nghiệm và thực hành.

## 핵심 키워드 (Từ khóa)
- 응집도 (Cohesion)
- 기능적 응집도 (Functional Cohesion)
- 순차적 응집도 (Sequential Cohesion)
- 교환적 / 통신적 응집도 (Communication Cohesion)
- 절차적 응집도 (Procedural Cohesion)
- 시간적 응집도 (Temporal Cohesion)
- 논리적 응집도 (Logical Cohesion)
- 우연적 응집도 (Coincidental Cohesion)
- 기-순-교-절-시-논-우

## 선행·연결 개념 (Kiến thức liên kết)
- [64-bai-hoc.md](64-bai-hoc.md): Độ ghép nối 결합도 (Coupling) - Càng thấp càng tốt (자-스-제-외-공-내).
- [66-bai-hoc.md](66-bai-hoc.md): Fan-In / Fan-Out - Đo lường độ phức tạp và tái sử dụng mô-đun.
- [32-bai-hoc.md](32-bai-hoc.md): Thiết kế mô-đun hóa độc lập (High Cohesion, Loose Coupling).

## 읽는 방법 (Cách đọc)
- Học thuộc lòng thần chú mnemonic: **기-순-교-절-시-논-우** (Kì-Sun-Kiều-Chul-Shi-Non-U).
- Đối chiếu cặp khái niệm: Cohesion là mối quan hệ giữa các thành phần **bên trong** một mô-đun (càng cao càng tốt), khác với Coupling là quan hệ **giữa các mô-đun khác nhau** (càng thấp càng tốt).
- Tập trung vào từ khóa nhận diện đặc trưng trong đề thi trắc nghiệm: 단일 기능 (기능), 출력$\rightarrow$입력 (순차), 동일 입출력/동일 자료구조 (교환), 실행 순서/흐름 (절차), 동시 실행/초기화 (시간), 유사 기능 묶음 (논리), 무관 (우연).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Định nghĩa cốt lõi:**
  - **응집도 (Cohesion):** Mức độ liên kết chặt chẽ và tập trung vào một mục đích chung của các phần tử (hàm, biến, câu lệnh) **bên trong một mô-đun**.
  - **Quy tắc vàng:** **응집도는 높을수록 (강할수록) 품질이 좋다** (Độ gắn kết nội tại càng cao/mạnh thì mô-đun càng độc lập, dễ bảo trì và tái sử dụng).
- **Thứ tự 7 cấp độ 응집도 (Từ mạnh nhất đến yếu nhất):**
  $$\text{기능 (Functional)} > \text{순차 (Sequential)} > \text{교환 (Communication)} > \text{절차 (Procedural)} > \text{시간 (Temporal)} > \text{논리 (Logical)} > \text{우연 (Coincidental)}$$
  - **Mẹo ghi nhớ:** **기-순-교-절-시-논-우** (*Kì - Sun - Kiều - Chul - Shi - Non - U*).

| Cấp độ 응집도 (Tên Hàn / Anh) | Mức độ chất lượng | Đặc điểm nhận diện cốt lõi (Từ khóa đề thi) | Ví dụ minh họa thực tế |
| :--- | :--- | :--- | :--- |
| **기능적 (Functional)** | Cao nhất (Mạnh nhất - Tốt nhất) | Tất cả phần tử bên trong mô-đun cùng phối hợp giải quyết duy nhất **một chức năng bài toán duy nhất (단일 기능)** | Hàm tính căn bậc hai `sqrt()`, hàm tính sin `sin()`, hàm mã hóa mật khẩu `hashPassword()` |
| **순차적 (Sequential)** | Rất cao | **Đầu ra (Output) của hoạt động trước trở thành đầu vào (Input) của hoạt động kế tiếp** ngay trong cùng một mô-đun | Hàm đọc file rồi lấy nội dung đó đem đi phân tích parse dữ liệu |
| **교환적 / 통신적 (Communication)** | Cao | Các hoạt động khác nhau cùng thao tác trên **chung một tập dữ liệu đầu vào hoặc đầu ra (동일 입출력 / 동일 자료구조)** | Một hàm nhận vào danh sách đơn hàng rồi vừa tính tổng tiền vừa in hóa đơn ra giấy |
| **절차적 (Procedural)** | Trung bình | Các phần tử được gom lại vì phải thực thi theo một **trình tự các bước xác định (순차적 수행 / 순서)** | Chuỗi bước xử lý nghiệp vụ: Nhập mật khẩu $\rightarrow$ Kiểm tra quyền $\rightarrow$ Ghi log đăng nhập |
| **시간적 (Temporal)** | Thấp | Các phần tử được gom lại vì chúng được thực thi vào **cùng một thời điểm (특정 시간 / 동시 실행)** | Hàm khởi tạo hệ thống `initialize()`, hàm đóng kết nối và giải phóng tài nguyên lúc tắt máy `cleanup()` |
| **논리적 (Logical)** | Kém | Gom các phần tử có **tính chất hoặc định dạng logic tương tự nhau (유사한 성격 / 형태)** vào chung một hàm | Hàm `printAll()` xử lý in ấn cho cả văn bản, bảng biểu, ảnh bằng cách dùng switch-case chia nhánh |
| **우연적 (Coincidental)** | Tồi tệ nhất (Yếu nhất) | Các phần tử được gom lại hoàn toàn **ngẫu nhiên, không hề có mối quan hệ ngữ nghĩa hay chức năng (아무 관련 없음)** | File tiện ích `Utility.java` chứa linh tinh các hàm không liên quan: tính thuế, vẽ hình tròn, gửi email |

- **Bẫy đề thi trắc nghiệm:**
  - **Bẫy 1:** *"Độ gắn kết nào mà đầu ra của bước trước là đầu vào của bước sau?"* $\rightarrow$ Đáp án chắc chắn là **순차적 응집도 (Sequential Cohesion)**.
  - **Bẫy 2:** *"Một mô-đun chứa các câu lệnh khởi tạo biến, mở kết nối DB lúc khởi động hệ thống là gì?"* $\rightarrow$ Đáp án là **시간적 응집도 (Temporal Cohesion)**.
  - **Bẫy 3:** *"Các hàm khác nhau nhưng cùng dùng chung một cấu trúc dữ liệu hoặc bảng DB là gì?"* $\rightarrow$ Đáp án là **교환적(통신적) 응집도 (Communication Cohesion)**.
  - **Bẫy 4:** *"Thứ tự sắp xếp đúng từ mạnh đến yếu?"* $\rightarrow$ Phải viết ngay thần chú **기-순-교-절-시-논-우** ra nháp để dò đáp án.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **So sánh trực quan Functional vs Procedural vs Logical:**
  - **Functional (Mạnh nhất):** Hàm chỉ làm đúng 1 việc `calculateTax(income)`. Rất dễ viết Unit Test độc lập.
  - **Procedural (Trung bình):** Hàm gom một chuỗi thao tác theo quy trình `processOrder()` gồm kiểm kho $\rightarrow$ trừ tiền $\rightarrow$ gửi mail. Nếu một bước thay đổi, hàm dễ bị sửa đổi.
  - **Logical (Kém):** Hàm `handleInput(int eventType)` nhận sự kiện chuột, bàn phím, màn hình cảm ứng rồi switch-case xử lý. Khi thêm loại sự kiện mới phải sửa hàm này, vi phạm nguyên lý Open-Closed (OCP).
- **Mối tương quan với 결합도 (Coupling):**
  - Khi thiết kế hệ thống đạt tiêu chuẩn vàng **High Cohesion, Loose Coupling**:
    - Mô-đun nội bộ liên kết rất bền chặt (Cohesion cao: Functional, Sequential).
    - Giữa các mô-đun chỉ trao đổi qua tham số dữ liệu cần thiết (Coupling thấp: Data Coupling).

### 복습 체크리스트
- [ ] Nhớ nguyên lý thiết kế: 응집도는 높을수록 (강할수록) 좋다.
- [ ] Đọc vanh vách thứ tự 7 cấp độ: 기능 > 순차 > 교환 > 절차 > 시간 > 논리 > 우연 (기-순-교-절-시-논-우).
- [ ] Phân biệt được 순차적 응집도 (Đầu ra thành đầu vào bước kế) và 교환적 응집도 (Dùng chung dữ liệu vào/ra).
- [ ] Nhận biết 시간적 응집도 qua ví dụ hàm khởi tạo (Initialization) hoặc giải phóng tài nguyên.
- [ ] Chỉ ra 우연적 응집도 là cấp độ tồi tệ nhất cần tuyệt đối tránh trong lập trình phần mềm.
