# 3. 결합도 (Coupling - Độ phụ thuộc)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và ý nghĩa sống còn của Độ kết hợp (`결합도 - Coupling`) trong việc đo lường mức độ phụ thuộc giữa các mô-đun phần mềm.
- Thuộc nằm lòng thứ tự 6 cấp độ kết hợp từ tốt nhất (yếu nhất) đến xấu nhất (mạnh nhất): **자료 $\rightarrow$ 스탬프 $\rightarrow$ 제어 $\rightarrow$ 외부 $\rightarrow$ 공통 $\rightarrow$ 내용**.
- Nhận diện chính xác từng loại kết hợp qua các đoạn mã nguồn và kịch bản truyền dữ liệu trong đề thi trắc nghiệm.

## 핵심 키워드 (Từ khóa)
- 결합도 (Độ kết hợp / Coupling / 모듈 간 상호 의존성)
- 자료 결합도 (Data Coupling / 단순 값 전달 / Tốt nhất)
- 스탬프 결합도 (Stamp Coupling / 배열·객체 구조체 전달)
- 제어 결합도 (Control Coupling / 제어 플래그 전달)
- 외부 결합도 (External Coupling / 외부 선언 변수 공유)
- 공통 결합도 (Common Coupling / 전역 변수 공유)
- 내용 결합도 (Content Coupling / 내부 직접 참조 / Tồi tệ nhất)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([10. 소프트웨어 설계 원리](63-bai-hoc.md)):** Sau khi nắm nguyên lý mô-đun hóa, bài này cung cấp bảng phân tích định lượng chi tiết về mức độ phụ thuộc giữa các mô-đun.
- **Tiếp nối sang bài sau ([4. 응집도 (Cohesion - Độ gắn kết)](65-bai-hoc.md)):** Khảo sát thước đo đối trọng bổ trợ bên trong nội bộ mô-đun: Độ gắn kết (Cohesion).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc làu câu thần chú: **자 - 스 - 제 - 외 - 공 - 내** (Dữ liệu < Stamp < Điều khiển < Ngoài < Chung < Nội dung) - quy tắc vàng: 결합도 càng thấp càng tốt.
- Đọc TẦNG B để phân tích ví dụ mã nguồn minh họa sự khác biệt giữa Common Coupling (dùng biến toàn cục) và Content Coupling (thò tay vào ruột mô-đun khác).

---

## 3. 결합도 (Coupling - Độ phụ thuộc)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Định nghĩa Độ kết hợp):**
  - Là chỉ số đo lường mức độ phụ thuộc lẫn nhau (`상호 의존 정도`) hoặc mức độ liên kết giữa hai hay nhiều mô-đun phần mềm.
  - **Nguyên tắc thiết kế tối thượng:** **결합도는 낮을수록 좋다 (Độ kết hợp CÀNG THẤP CÀNG TỐT)**. 결합도 càng yếu thì mô-đun càng độc lập, hệ thống càng dễ bảo trì và mở rộng.
- **Thứ tự 6 cấp độ 결합도 chuẩn (Từ Yếu nhất/Tốt nhất $\rightarrow$ Mạnh nhất/Tồi tệ nhất):**
  $$\mathbf{자료 (Data) < 스탬프 (Stamp) < 제어 (Control) < 외부 (External) < 공통 (Common) < 내용 (Content)}$$
  - 💡 **Thần chú ghi nhớ:** **자 - 스 - 제 - 외 - 공 - 내** (Dữ liệu -> Stamp -> Điều khiển -> Ngoài -> Chung -> Nội dung).
- **Phân tích đặc trưng chi tiết 6 cấp độ:**
  1. **자료 결합도 (Data Coupling - TỐT NHẤT):**
     - Mô-đun A gọi mô-đun B và chỉ truyền các **giá trị dữ liệu thô đơn thuần (`단순한 데이터 값`)** qua danh sách tham số (ví dụ: `int a, double b`). Mô-đun B nhận và xử lý mà không cần quan tâm đến cấu trúc bên ngoài.
  2. **스탬프 결합도 (Stamp Coupling):**
     - Mô-đun A truyền **toàn bộ một cấu trúc dữ liệu phức tạp (`배열, 레코드, 구조체, 객체`)** cho mô-đun B, dù mô-đun B thực tế chỉ sử dụng một vài trường dữ liệu nhỏ bên trong cấu trúc đó.
  3. **제어 결합도 (Control Coupling):**
     - Mô-đun A truyền một **tín hiệu cờ điều khiển (`제어 플래그 - Flag, Switch, Function Code`)** sang mô-đun B nhằm can thiệp và chỉ đạo trực tiếp luồng logic bên trong của mô-đun B (phá vỡ tính độc lập).
  4. **외부 결합도 (External Coupling):**
     - Hai hay nhiều mô-đun cùng tham chiếu hoặc chia sẻ các biến dữ liệu, giao thức hoặc định dạng được định nghĩa ở bên ngoài hệ sinh thái phần mềm (ví dụ: chia sẻ cấu trúc file I/O ngoại vi).
  5. **공통 결합도 (Common Coupling):**
     - Các mô-đun cùng truy cập và chia sẻ chung một **vùng dữ liệu toàn cục (`전역 변수 - Global Variable / Shared Memory`)**. Khi một mô-đun sửa đổi biến toàn cục, tất cả các mô-đun khác đều bị ảnh hưởng.
  6. **내용 결합도 (Content Coupling - TỒI TỆ NHẤT):**
     - Một mô-đun **trực tiếp tham chiếu hoặc can thiệp sửa đổi dữ liệu nội bộ hay mã lệnh bên trong của một mô-đun khác** mà không thông qua bất kỳ hàm hay giao diện công khai nào.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Mô-đun nào sau đây có chất lượng thiết kế độc lập cao nhất?"* -> Mô-đun có **자료 결합도 (Data Coupling)**.
  - **Bẫy 2:** *"Một mô-đun truyền cờ Function Code để quyết định hành vi mô-đun khác là kết hợp gì?"* -> **제어 결합도 (Control Coupling)**.
  - **Bẫy 3:** *"Các mô-đun chia sẻ biến toàn cục (Global Variable) là kết hợp gì?"* -> **공통 결합도 (Common Coupling)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Độ kết hợp càng thấp càng tốt: Data truyền giá trị thô tốt nhất; Stamp truyền cả struct; Control truyền Flag; Common dùng biến chung; Content can thiệp ruột tồi tệ nhất".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tình huống so sánh mã nguồn:**
  - **Data Coupling:** `double calculateVat(double price) { return price * 0.1; }` $\rightarrow$ Độc lập tuyệt đối.
  - **Control Coupling:** `void printReport(ReportData data, int printMode)` $\rightarrow$ Bên trong hàm có lệnh `if (printMode == 1) printPDF(); else printExcel();` $\rightarrow$ Bị ràng buộc điều khiển từ bên ngoài.
  - **Content Coupling:** Trong ngôn ngữ Assembly hoặc C khi dùng con trỏ nhảy trực tiếp vào giữa một hàm của mô-đun khác để thay đổi giá trị thanh ghi mà không qua lời gọi hàm chính thống $\rightarrow$ Cực kỳ nguy hiểm, dễ gây sập bộ nhớ.

### 복습 체크리스트
- [ ] Khẳng định được quy tắc vàng: 결합도는 낮을수록 좋다.
- [ ] Đọc đúng thứ tự 6 cấp độ từ thấp đến cao: 자료 < 스탬프 < 제어 < 외부 < 공통 < 내용.
- [ ] Nhận diện được ví dụ của Data Coupling (truyền tham số giá trị đơn thuần).
- [ ] Nhận diện được ví dụ của Control Coupling (truyền cờ Flag).
- [ ] Nhận diện được ví dụ của Common Coupling (biến toàn cục 전역 변수).
- [ ] Nhớ 내용 결합도 (Content Coupling) là tồi tệ nhất.
