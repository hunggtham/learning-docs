# 192. 응집도 (Cohesion / Mức độ gắn kết)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa của độ gắn kết nội tại (응집도 - Cohesion) – thước đo mức độ tập trung và liên quan chặt chẽ giữa các thành phần bên trong cùng một module.
- Thuộc lòng thứ tự 7 cấp độ gắn kết từ **Yếu nhất (Xấu nhất - Tản mạn, kém chất lượng)** đến **Mạnh nhất (Tốt nhất - Tập trung cao, thiết kế chuẩn mực)**.
- Nhận diện chính xác từng loại Cohesion thông qua kịch bản nghiệp vụ và ví dụ mã nguồn thực tế.

## 핵심 키워드 (Từ khóa)
- 응집도 (Cohesion)
- 모듈 내부 요소 간 관련성 (Intra-module Element Relatedness)
- 우연적 응집도 (Coincidental Cohesion - Cực xấu)
- 논리적 응집도 (Logical Cohesion)
- 시간적 응집도 (Temporal Cohesion)
- 절차적 응집도 (Procedural Cohesion)
- 통신적/교환적 응집도 (Communication Cohesion)
- 순차적 응집도 (Sequential Cohesion)
- 기능적 응집도 (Functional Cohesion - Cực tốt)
- 암기 공식 (우논시절 교순기)

## 선행·연결 개념 (Kiến thức liên kết)
- [55-bai-hoc.md](55-bai-hoc.md): Chi tiết 6 cấp độ kết hợp ngoài (Coupling) từ tốt đến xấu.
- [54-bai-hoc.md](54-bai-hoc.md): Nguyên tắc thiết kế phần mềm tốt (Low Coupling, High Cohesion).
- [57-bai-hoc.md](57-bai-hoc.md): Thiết kế module hóa hiệu quả và sơ đồ khối N-S Chart.

## 읽는 방법 (Cách đọc)
- Khẩu quyết bất hủ về thứ tự Cohesion từ **Xấu nhất đến Tốt nhất**:
  $$\mathbf{우 \rightarrow 논 \rightarrow 시 \rightarrow 절 \rightarrow 교(통) \rightarrow 순 \rightarrow 기}$$
  - **우**연적 (Coincidental) $\rightarrow$ **논**리적 (Logical) $\rightarrow$ **시**간적 (Temporal) $\rightarrow$ **절**차적 (Procedural) $\rightarrow$ **교**환/통신적 (Communication) $\rightarrow$ **순**차적 (Sequential) $\rightarrow$ **기**능적 (Functional).
  - Chiều tăng dần: **Từ Yếu nhất (Tệ nhất) đến Mạnh nhất (Đạt chuẩn cao nhất)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng đối chiếu toàn diện 7 cấp độ gắn kết (Cohesion):**

| Thứ tự | Loại 응집도 (Cohesion) | Bản chất thiết kế & Ví dụ điển hình | Đánh giá |
| :---: | :--- | :--- | :---: |
| 1 | **우연적 (Coincidental)** | Các lệnh trong module hoàn toàn không có mối liên hệ logic hay dữ liệu nào, chỉ ngẫu nhiên bị ném chung vào một chỗ. | **Tệ nhất (Yếu nhất)** |
| 2 | **논리적 (Logical)** | Gom các thao tác có tính chất tương tự nhau theo góc nhìn logic nhưng chức năng khác nhau (ví dụ: gom tất cả các thao tác I/O hoặc in ấn vào chung một hàm và dùng mã lệnh để chọn). | **Rất yếu** |
| 3 | **시간적 (Temporal)** | Các thao tác được gom chung vì chúng **cùng diễn ra tại một thời điểm** nhất định trong chu kỳ chương trình (ví dụ: hàm `init()` khởi tạo biến hệ thống, mở tệp, kết nối DB; hoặc hàm `cleanup()` đóng tệp). | **Yếu** |
| 4 | **절차적 (Procedural)** | Các lệnh được thực thi theo một **trình tự các bước (Sequence of Steps)** định trước để hoàn thành một nhiệm vụ lớn, nhưng không truyền dữ liệu trực tiếp cho nhau. | **Trung bình** |
| 5 | **교환적 / 통신적 (Communication)** | Các lệnh cùng thao tác hoặc **sử dụng chung cấu trúc dữ liệu đầu vào hoặc đầu ra**, dù các bước xử lý có thể độc lập. | **Khá** |
| 6 | **순차적 (Sequential)** | **Dữ liệu đầu ra (Output) của lệnh phía trước trở thành dữ liệu đầu vào (Input) của lệnh phía sau** theo dạng đường ống (Pipe-and-Filter). | **Mạnh** |
| 7 | **기능적 (Functional)** | Tất cả các phần tử bên trong module cùng hiệp lực tập trung giải quyết **đúng một chức năng nghiệp vụ duy nhất** (ví dụ: hàm `calculateSquareRoot()`, `sin()`). | **Tốt nhất (Mạnh nhất)** |

- **Phân biệt hai loại dễ nhầm lẫn nhất trong đề thi:**
  - *Procedural (절차적):* Nhấn mạnh vào **trình tự thời gian thực hiện** các bước $A \rightarrow B \rightarrow C$.
  - *Sequential (순차적):* Nhấn mạnh vào **dòng chảy dữ liệu**: Kết quả bước $A \rightarrow$ truyền vào làm nguyên liệu cho bước $B \rightarrow$ kết quả bước $B \rightarrow$ truyền vào bước $C$.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Mối tương quan giữa Cohesion và Coupling:**
  - Module có **Functional Cohesion** thường tự nhiên đạt được **Data Coupling** với các module khác, bởi vì khi một module chỉ làm đúng một việc duy nhất, nó chỉ cần nhận các tham số đầu vào tối thiểu và trả về đúng một kết quả đầu ra, không tạo ra các trạng thái phụ (Side Effects) phức tạp.

### 복습 체크리스트
- [ ] Đọc vanh vách khẩu quyết Cohesion từ xấu đến tốt: **우논시절 교순기**.
- [ ] Nhớ Coincidental Cohesion là yếu nhất, Functional Cohesion là mạnh nhất.
- [ ] Phân biệt được Temporal (gom việc chạy cùng thời điểm như `init`) với Logical (gom việc cùng nhóm logic).
- [ ] Nhận diện Sequential Cohesion qua dấu hiệu "Output của bước này là Input của bước sau".
