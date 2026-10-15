# 191. 결합도 (Coupling / Mức độ phụ thuộc)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và vai trò của độ kết hợp (Coupling / 결합도) trong việc đánh giá mức độ phụ thuộc lẫn nhau giữa các module phần mềm.
- Thuộc lòng thứ tự 6 cấp độ kết hợp từ **Yếu nhất (Tốt nhất - Ưu tiên thiết kế)** đến **Mạnh nhất (Xấu nhất - Tuyệt đối tránh)**.
- Phân biệt bản chất kỹ thuật của từng loại kết hợp qua cách các module truyền tải dữ liệu, cờ trạng thái hay chia sẻ bộ nhớ.

## 핵심 키워드 (Từ khóa)
- 결합도 (Coupling)
- 모듈 간 상호 의존성 (Inter-module Dependency)
- 자료 결합도 (Data Coupling - Cực tốt)
- 스탬프 결합도 (Stamp Coupling)
- 제어 결합도 (Control Coupling)
- 외부 결합도 (External Coupling)
- 공통 결합도 (Common Coupling)
- 내용 결합도 (Content Coupling - Cực xấu)
- 암기 공식 (자스제 외공내)

## 선행·연결 개념 (Kiến thức liên kết)
- [54-bai-hoc.md](54-bai-hoc.md): Đặc điểm của thiết kế phần mềm tốt (Low Coupling, High Cohesion).
- [56-bai-hoc.md](56-bai-hoc.md): Độ gắn kết nội tại (Cohesion) từ xấu đến tốt.
- [57-bai-hoc.md](57-bai-hoc.md): Phương pháp thiết kế module hóa hiệu quả và biểu đồ N-S.

## 읽는 방법 (Cách đọc)
- Khẩu quyết bất hủ bắt buộc phải thuộc làu khi đi thi:
  $$\mathbf{자 \rightarrow 스 \rightarrow 제 \rightarrow 외 \rightarrow 공 \rightarrow 내}$$
  - **자**료 (Data) $\rightarrow$ **스**탬프 (Stamp) $\rightarrow$ **제**어 (Control) $\rightarrow$ **외**부 (External) $\rightarrow$ **공**통 (Common) $\rightarrow$ **내**용 (Content).
  - Chiều mũi tên: **Từ Tốt (Độc lập cao nhất, Coupling yếu nhất) đến Xấu (Phụ thuộc chặt nhất, Coupling mạnh nhất)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng phân loại chi tiết 6 cấp độ kết hợp (Coupling):**

| Thứ tự | Loại 결합도 (Coupling) | Cơ chế giao tiếp & Đặc điểm nhận diện | Đánh giá chất lượng |
| :---: | :--- | :--- | :---: |
| 1 | **자료 (Data Coupling)** | Hai module chỉ truyền nhận **dữ liệu đơn thuần (Scalar values)** qua tham số gọi hàm (ví dụ: `int a, double b`). Không can thiệp bất kỳ cấu trúc hay logic nào của nhau. | **Tốt nhất (Yếu nhất)** |
| 2 | **스탬프 (Stamp Coupling)** | Hai module truyền nhận **cấu trúc dữ liệu phức hợp (Array, Struct, Object)**. Module nhận chỉ dùng một vài trường nhưng buộc phải nhận toàn bộ cấu trúc. | **Khá tốt** |
| 3 | **제어 (Control Coupling)** | Module gọi truyền **cờ điều khiển (Control Flag, Function Code)** để chỉ định module được gọi phải rẽ nhánh hoặc chạy hàm con nào. | **Kém (Cần tránh)** |
| 4 | **외부 (External Coupling)** | Hai module cùng tham chiếu hoặc định dạng dữ liệu theo một **tiêu chuẩn ngoại vi/môi trường bên ngoài** (giao thức mạng, cấu trúc tệp tin, API hệ điều hành). | **Kém** |
| 5 | **공통 (Common Coupling)** | Nhiều module cùng đọc và ghi trực tiếp vào **vùng nhớ toàn cục chia sẻ chung (Global Variables / Shared Memory)**. Một module sửa biến có thể làm sập các module khác. | **Rất xấu** |
| 6 | **내용 (Content Coupling)** | Module này **nhảy thẳng vào giữa thân mã nguồn** của module kia hoặc trực tiếp sửa đổi dữ liệu cục bộ nội bộ của module khác. | **Xấu nhất (Mạnh nhất)** |

- **Minh họa bằng mã nguồn thực tế:**
  - *Data Coupling (Tốt):*
    ```c
    int sum(int a, int b) { return a + b; } // Chỉ truyền 2 số nguyên đơn lẻ
    ```
  - *Stamp Coupling:*
    ```c
    struct Student { int id; char name[20]; float gpa; };
    void printId(struct Student s) { printf("%d", s.id); } // Chỉ cần id nhưng truyền cả struct
    ```
  - *Control Coupling (Xấu):*
    ```c
    void process(int mode) { if (mode == 1) doA(); else doB(); } // Truyền flag để điều khiển nhánh
    ```
  - *Common Coupling (Rất xấu):*
    ```c
    int g_counter = 0; // Biến toàn cục bị 10 module cùng đọc ghi không kiểm soát
    ```

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tại sao Stamp Coupling lại kém tối ưu hơn Data Coupling?**
  - Trong Stamp Coupling, nếu định nghĩa cấu trúc dữ liệu (`struct Student`) bị thay đổi (thêm, xóa hoặc đổi kiểu dữ liệu một trường), tất cả các module có nhận tham số struct này đều buộc phải biên dịch lại (Recompile) và kiểm thử lại, ngay cả khi chức năng của module đó hoàn toàn không sử dụng trường vừa thay đổi.

### 복습 체크리스트
- [ ] Đọc vanh vách khẩu quyết thứ tự: **자스제 외공내** (Data $\rightarrow$ Stamp $\rightarrow$ Control $\rightarrow$ External $\rightarrow$ Common $\rightarrow$ Content).
- [ ] Nhớ Data Coupling là yếu nhất (tốt nhất), Content Coupling là mạnh nhất (xấu nhất).
- [ ] Phân biệt được Stamp Coupling (truyền struct) khác Data Coupling (chỉ truyền tham số đơn).
- [ ] Nhận diện được Control Coupling khi thấy xuất hiện từ khóa "Flag", "Control signal", "chỉ định nhánh".
