# 소프트웨어 테스트 기법 및 결함 생명주기 (Kiểm thử phần mềm & Vòng đời lỗi)

## 학습 목표 (Mục tiêu)
- Nắm vững sự khác nhau giữa Kiểm thử Hộp trắng (화이트박스 테스트 - nhìn thấy code: Statement, Branch, Condition Coverage) và Kiểm thử Hộp đen (블랙박스 테스트 - theo đặc tả chức năng: Equivalence Partitioning, Boundary Value Analysis).
- Phân biệt chính xác hai chiến lược tích hợp module kinh điển trong đề thi: Tích hợp từ trên xuống (하향식 - dùng Stub) và Tích hợp từ dưới lên (상향식 - dùng Driver).
- Thuộc lòng chu trình chuyển trạng thái của Vòng đời lỗi phần mềm (결함 생명주기 - Defect Lifecycle: Open $\rightarrow$ Assigned $\rightarrow$ Fixed $\rightarrow$ Closed) và ý nghĩa của các trạng thái đặc thù: Reopened, Deferred, Clarified/Rejected.

## 핵심 키워드 (Từ khóa)
- 화이트박스 테스트 (White-Box Testing) — Nhìn thấy mã nguồn; kiểm thử cấu trúc logic, đường cơ sở và độ phủ.
- 블랙박스 테스트 (Black-Box Testing) — Không nhìn thấy mã nguồn; kiểm thử chức năng theo đặc tả yêu cầu.
- 경계값 분석 (Boundary Value Analysis) — Phân tích giá trị biên tại ngưỡng chuyển tiếp dữ liệu.
- 하향식 vs 상향식 통합 (Top-Down vs Bottom-Up) — Tầng trên xuống dùng **Stub** vs Tầng dưới lên dùng **Driver**.
- 결함 생명주기 (Defect Lifecycle) — Open, Assigned, Fixed, Closed, Reopened, Deferred.
- 알파 테스트 vs 베타 테스트 (Alpha vs Beta Testing) — Kiểm thử nội bộ tại môi trường nhà phát triển vs Kiểm thử người dùng thực tế.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa từ Biểu đồ luồng điều khiển và Độ phức tạp chu trình McCabe $V(G)$ đã học ở bài `19-thiet-ke-mo-dun-coupling-va-cohesion.md`.
- **Đang giải quyết gì (Current Problem):** Giải quyết câu hỏi: Sau khi hoàn thành việc viết mã nguồn, làm sao kiểm tra được phần mềm không có lỗi tiềm ẩn, các module tích hợp với nhau như thế nào và quy trình phối hợp giữa Tester và Developer diễn ra ra sao khi phát hiện lỗi.
- **Dùng đi đâu (Forward Handoff):** Các lỗi phát sinh sau khi phần mềm đã bàn giao cho khách hàng đưa vào vận hành sẽ chuyển sang giai đoạn Bảo trì và Tái cấu trúc mã nguồn trong bài `21-bao-tri-phan-mem-tai-ky-nghe-va-cong-cu-case.md`.

## 읽는 방법 (Cách đọc)
- **Stub vs Driver:**
  - **Tích hợp từ Trên xuống (하향식 - Top-Down):** Cấp trên có rồi, thiếu cấp dưới $\rightarrow$ Dùng **Stub (mô-đun con bù đắp phía dưới)**.
  - **Tích hợp từ Dưới lên (상향식 - Bottom-Up):** Cấp dưới có rồi, thiếu bộ điều khiển cấp trên $\rightarrow$ Dùng **Driver (mô-đun cha điều khiển phía trên)**.
- **Phân loại kiểm thử:**
  - Cứ có chữ "Đường dẫn (Path)", "Nhánh (Branch)", "Điều kiện (Condition)", "Câu lệnh (Statement)" $\rightarrow$ **Hộp trắng (White-Box)**.
  - Cứ có chữ "Biên (Boundary)", "Phân vùng tương đương (Equivalence)", "Bảng quyết định (Cause-Effect)" $\rightarrow$ **Hộp đen (Black-Box)**.
- **Trạng thái lỗi:** Deferred là "hoãn sửa sang sprint sau"; Reopened là "sửa xong nhưng test lại vẫn thấy lỗi".

---

## 소프트웨어 테스트 기법 및 결함 생명주기

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `화이트박스 테스트는 원시 코드의 제어 구조를 검사(기초 경로, 문장/분기/조건 커버리지)하고, 블랙박스 테스트는 요구사항 명세서 기반으로 기능 검사(동치 분할, 경계값 분석)를 수행한다. 통합 검사에서 하향식은 스텁(Stub), 상향식은 드라이버(Driver)를 사용한다. 결함 생명주기는 Open -> Assigned -> Fixed -> Closed 순서로 전이된다.`
  - [Tiếng Việt]: Kiểm thử hộp trắng kiểm tra cấu trúc điều khiển của mã nguồn (đường cơ sở, độ phủ câu lệnh/nhánh/điều kiện), còn kiểm thử hộp đen kiểm tra chức năng dựa trên đặc tả yêu cầu (phân vùng tương đương, giá trị biên). Tích hợp từ trên xuống dùng Stub, từ dưới lên dùng Driver. Vòng đời lỗi chuyển trạng thái: Open -> Assigned -> Fixed -> Closed.

- **1. Bảng đối chiếu toàn diện: Kiểm thử Hộp trắng vs Kiểm thử Hộp đen:**

| Tiêu chuẩn so sánh | Kiểm thử Hộp trắng (화이트박스 - White-Box) | Kiểm thử Hộp đen (블랙박스 - Black-Box) |
| :--- | :--- | :--- |
| **Góc nhìn mã nguồn** | **Mở mã nguồn:** Nhìn thấy toàn bộ cấu trúc logic, giải thuật và các biến bên trong. | **Đóng mã nguồn:** Hoàn toàn không nhìn vào code; chỉ đối chiếu Đầu vào $\rightarrow$ Đầu ra. |
| **Căn cứ thiết kế test** | Dựa trên **Biểu đồ luồng điều khiển (Control Flow Graph)** và logic rẽ nhánh. | Dựa trên **Tài liệu đặc tả yêu cầu chức năng (Software Requirements Specification)**. |
| **Các kỹ thuật then chốt**| • **기초 경로 검사 (Basis Path Testing):** Dựa trên $V(G)$.<br>• **문장 검증 (Statement Coverage):** Phủ mọi dòng lệnh.<br>• **분기 검증 (Branch Coverage):** Phủ mọi nhánh True/False.<br>• **조건 검증 (Condition Coverage):** Phủ điều kiện đơn lẻ. | • **동치 분할 검사 (Equivalence Partitioning):** Chia nhóm hợp lệ và không hợp lệ.<br>• **경계값 분석 (Boundary Value Analysis):** Test tại các điểm biên.<br>• **원인-효과 그래프 (Cause-Effect):** Lập bảng quyết định.<br>• **오류 예측 (Error Guessing):** Dựa trên kinh nghiệm. |

- **2. Bảng đối chiếu chiến lược tích hợp: Top-Down vs Bottom-Up:**

| Chiến lược tích hợp | Hướng di chuyển module | Mô-đun giả lập hỗ trợ | Đặc điểm và ưu thế chuẩn thi |
| :--- | :---: | :---: | :--- |
| **하향식 통합 (Top-Down)** | **Từ trên xuống:** Từ module điều khiển chính xuống module con. | **스텁 (Stub)** | **Stub đóng vai trò là module cấp dưới tạm thời**; sớm có sản phẩm khung để trình diễn cho khách hàng. |
| **상향식 통합 (Bottom-Up)** | **Từ dưới lên:** Từ các module chức năng cơ sở lên module cha. | **드라이버 (Driver)** | **Driver đóng vai trò là module cấp trên điều phối**; kiểm thử kỹ lưỡng các module xử lý dữ liệu cấp thấp trước. |

- **3. Bảng trạng thái Vòng đời quản lý lỗi phần mềm (결함 생명주기):**

| Trạng thái lỗi | Thuật ngữ Anh / Hàn | Hành động và người chịu trách nhiệm tương ứng |
| :--- | :--- | :--- |
| **Mở lỗi** | **Open** (결함 등록) | Tester phát hiện lỗi mới và ghi nhận chi tiết bước tái hiện vào hệ thống. |
| **Giao việc** | **Assigned** (담당자 할당) | Quản lý dự án phân bổ lỗi cho lập trình viên (Developer) phụ trách sửa. |
| **Đã sửa** | **Fixed** (수정 완료) | Developer đã sửa xong mã nguồn và bàn giao phiên bản mới cho đội kiểm thử. |
| **Đóng lỗi** | **Closed** (종결) | Tester kiểm thử lại (Re-test) và **xác nhận lỗi không còn tái diễn**, đóng vé. |
| **Mở lại** | **Reopened** (재오픈) | Lỗi sau khi sửa **vẫn còn tái phát** khi kiểm thử lại; trả lại cho Dev sửa tiếp. |
| **Hoãn lại** | **Deferred** (연기) | Lỗi được xác nhận nhưng độ ưu tiên thấp; **dời việc sửa chữa sang phiên bản sau**. |
| **Từ chối** | **Clarified / Rejected** | Xác nhận báo cáo không phải lỗi (hệ thống hoạt động đúng theo tài liệu đặc tả). |

- **주의/함정 (Bẫy đề thi):**
  - **Nhầm lẫn Stub và Driver:** Đề thi hỏi *"Trong kiểm thử tích hợp 상향식 (Bottom-Up), thành phần nào được sử dụng?"* $\rightarrow$ Đáp án đúng bắt buộc là **드라이버 (Driver)**, chọn Stub là sai bẫy.
  - **Alpha vs Beta Testing:**
    - Alpha Test: Khách hàng kiểm thử tại **văn phòng của nhà phát triển** (Developer có mặt giám sát).
    - Beta Test: Khách hàng kiểm thử trực tiếp tại **môi trường thực tế của người dùng** (không có Developer can thiệp).

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"Hộp trắng soi dòng soi nhánh, Hộp đen chia vùng quét biên; Top-Down cắm Stub ở dưới, Bottom-Up dựng Driver ở trên; Lỗi Open rồi Fix xong mới Close."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bài toán thiết kế Test Case phân tích giá trị biên (Boundary Value Analysis):
- **Đề bài:** Hệ thống chấm điểm quy định: Một sinh viên đỗ môn học nếu điểm số $X$ là số nguyên thỏa mãn điều kiện: $60 \le X \le 100$.
- **Phân tích thiết kế ca kiểm thử:**
  - Vùng giá trị hợp lệ: $60 \le X \le 100$.
  - Vùng không hợp lệ 1: $X < 60$.
  - Vùng không hợp lệ 2: $X > 100$.
  - **Các giá trị biên bắt buộc phải kiểm tra:**
    - Tại biên dưới ($60$): $59$ (lân cận ngoài - Trượt), **$60$** (ngay biên - Đỗ), $61$ (lân cận trong - Đỗ).
    - Tại biên trên ($100$): $99$ (lân cận trong - Đỗ), **$100$** (ngay biên - Đỗ), $101$ (lân cận ngoài - Lỗi dữ liệu/Trượt).
  - Tập giá trị test tối ưu: $\{59, 60, 61, 99, 100, 101\}$.

#### 2. Minh họa mã nguồn Stub và Driver trong thực tế:
```c
// Ví dụ kiểm thử hàm tính thuế: double calculateTax(double salary)

// TRƯỜNG HỢP 1: TOP-DOWN (Module chính cần gọi hàm con chưa viết xong)
// Ta tạo một STUB giả lập hàm con trả về giá trị cố định:
double calculateTax_Stub(double salary) {
    return 100.0; // Giả lập luôn trả về thuế 100.0 để module chính tiếp tục chạy
}

// TRƯỜNG HỢP 2: BOTTOM-UP (Module con calculateTax đã xong, thiếu giao diện cấp trên)
// Ta tạo một DRIVER để cấp dữ liệu và kích hoạt module con:
int main() {
    // Driver đóng vai trò gọi và in kết quả
    double testSalary = 5000.0;
    double tax = calculateTax(testSalary);
    printf("Driver Test: Luong %.1f -> Thue tinh duoc: %.1f\n", testSalary, tax);
    return 0;
}
```

---

### 복습 체크리스트
- [ ] Phân biệt được: Hộp trắng nhìn thấy mã nguồn, Hộp đen kiểm thử chức năng không nhìn mã nguồn.
- [ ] Thuộc tên các kỹ thuật Hộp trắng: Đường cơ sở, Độ phủ câu lệnh, Độ phủ nhánh, Độ phủ điều kiện.
- [ ] Thuộc tên các kỹ thuật Hộp đen: Phân vùng tương đương, Phân tích giá trị biên, Đồ thị nguyên nhân-kết quả.
- [ ] Nhớ kỹ cặp bài trùng: Tích hợp Top-Down dùng Stub, Tích hợp Bottom-Up dùng Driver.
- [ ] Ghi nhớ chuỗi vòng đời lỗi: Open $\rightarrow$ Assigned $\rightarrow$ Fixed $\rightarrow$ Closed (hoặc Reopened / Deferred).
- [ ] Phân biệt được: Alpha test tại chỗ nhà phát triển, Beta test tại môi trường người dùng thực tế.
