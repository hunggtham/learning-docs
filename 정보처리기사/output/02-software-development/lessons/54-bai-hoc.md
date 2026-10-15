# 17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)

## 학습 목표 (Mục tiêu)
- Định nghĩa Bản mẫu chân lý kiểm thử (테스트 오라클 - Test Oracle) với tư cách là cơ chế hoặc nguồn thông tin độc lập xác thực kết quả thực thi của phần mềm là Đúng hay Sai.
- Nằm lòng 4 loại Test Oracle kinh điển: 참 오라클 (True Oracle), 샘플링 오라클 (Sampling Oracle), 휴리스틱 / 추정 오라클 (Heuristic Oracle) và 일관성 검사 오라클 (Consistent Oracle).
- Phân biệt các thành phần trong bộ khung giàn giáo kiểm thử (Test Harness): Test Driver, Test Stub, Test Suite, Test Script và Mock Object.

## 핵심 키워드 (Từ khóa)
- 테스트 오라클 (Test Oracle)
- 참 오라클 (True Oracle / 전수 검사)
- 샘플링 오라클 (Sampling Oracle / 대표값)
- 추정 / 휴리스틱 오라클 (Heuristic Oracle)
- 일관성 검사 오라클 (Consistent Oracle / 회귀 테스트)
- 테스트 하네스 (Test Harness)
- 테스트 드라이버 (Test Driver) & 테스트 스텁 (Test Stub)

## 선행·연결 개념 (Kiến thức liên kết)
- [53-bai-hoc.md](53-bai-hoc.md): Các cấp độ kiểm thử phần mềm (Unit, Integration, System, Acceptance).
- [55-bai-hoc.md](55-bai-hoc.md): Chi tiết kiểm thử tích hợp và Test Stub.
- [56-bai-hoc.md](56-bai-hoc.md): Cấu trúc bộ ca kiểm thử (Test Case).

## 읽는 방법 (Cách đọc)
- Cứ thấy đề thi nhắc đến: **"테스트의 결과가 참인지 거짓인지를 판단하기 위해 사전에 정의된 참값을 대입하여 비교하는 활동"** (So sánh kết quả thực thi với giá trị chân lý định trước) $\rightarrow$ Khẳng định ngay **테스트 오라클 (Test Oracle)**.
- Phân biệt 4 loại Oracle:
  - Kiểm tra toàn bộ 100% bằng kết quả chính xác tuyệt đối $\rightarrow$ **참 오라클 (True)**.
  - Chỉ kiểm tra một vài ca mẫu đặc thù $\rightarrow$ **샘플링 오라클 (Sampling)**.
  - Dựa trên kinh nghiệm và ước lượng khi không có kết quả chính xác $\rightarrow$ **휴리스틱 오라클 (Heuristic)**.
  - So sánh tính nhất quán trước và sau khi thay đổi mã $\rightarrow$ **일관성 검사 오라클 (Consistent)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bản chất của Test Oracle (테스트 오라클):**
  - Trong kiểm thử phần mềm, một ca kiểm thử chạy xong sẽ trả về một kết quả đầu ra thực tế (Actual Result). Nhưng làm sao ta biết kết quả đó là Đúng hay Sai? Ta phải có một "nguồn chân lý" để đối chiếu $\rightarrow$ Nguồn đó gọi là **Test Oracle**.
- **Bảng phân loại 4 dạng Test Oracle chuẩn đề thi:**

| Loại Test Oracle | Tên tiếng Hàn & Anh | Cơ chế hoạt động chi tiết | Trường hợp áp dụng |
| :--- | :--- | :--- | :--- |
| **Oracle Chân lý** | **참 오라클 (True Oracle)** | Kiểm tra **tất cả mọi ca kiểm thử (전수 검사)** bằng cách so sánh với kết quả kỳ vọng đúng tuyệt đối | Dành cho các hệ thống an toàn tính mạng, hàng không, y tế, ngân hàng cốt lõi |
| **Oracle Lấy mẫu** | **샘플링 오라클 (Sampling Oracle)** | **Chỉ chọn ra một số ca kiểm thử mẫu đại diện** để đối chiếu kết quả chính xác, các ca còn lại kiểm tra sơ bộ | Dành cho các hệ thống có không gian đầu vào quá lớn không thể kiểm tra hết |
| **Oracle Ước lượng** | **추정 / 휴리스틱 오라클 (Heuristic Oracle)** | Khi không thể tính toán kết quả chính xác, áp dụng **kinh nghiệm, phán đoán của chuyên gia và giải thuật xác suất** để ước lượng tính hợp lý | Hệ thống trí tuệ nhân tạo, đồ họa phức tạp, mô phỏng thời tiết |
| **Oracle Tính nhất quán** | **일관성 검사 오라클 (Consistent Oracle)** | **So sánh kết quả thực thi trước và sau khi sửa đổi mã nguồn** để xem hành vi có bị biến đổi ngoài ý muốn không | Áp dụng chủ yếu trong **Kiểm thử hồi quy (Regression Testing)** |

- **Các thành phần trong Giàn giáo kiểm thử (Test Harness):**
  - **테스트 드라이버 (Test Driver):** Chương trình cấp trên giả lập gọi xuống mô-đun cần test (dùng trong Bottom-up Integration Test).
  - **테스트 스텁 (Test Stub):** Mô-đun cấp dưới giả lập nhận lệnh và trả về kết quả giả định (dùng trong Top-down Integration Test).
  - **테스트 슈트 (Test Suite):** Tập hợp của nhiều Test Case được gom lại để chạy cùng một lúc.
  - **테스트 스크립트 (Test Script):** Tệp lệnh tự động hóa thực thi các Test Case bằng công cụ kiểm thử.
  - **목 오브젝트 (Mock Object):** Đối tượng giả lập hành vi của các thành phần bên ngoài (như DB ảo, Web Service ảo).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Vấn đề bài toán Oracle (The Oracle Problem):**
  - Trong thực tế kiểm thử phần mềm, việc tạo ra một True Oracle hoàn hảo là vô cùng tốn kém chi phí và đôi khi bất khả thi. Vì vậy, các công ty thường kết hợp linh hoạt giữa Sampling Oracle cho các luồng nghiệp vụ chính và Heuristic/Consistent Oracle cho các bài toán hồi quy quy mô lớn.

### 복습 체크리스트
- [ ] Định nghĩa Test Oracle là cơ chế xác định kết quả kiểm thử đúng hay sai.
- [ ] Phân biệt được 4 loại Oracle: 참 (True), 샘플링 (Sampling), 추정/휴리스틱 (Heuristic), 일관성 (Consistent).
- [ ] Nhớ 참 오라클 áp dụng cho các hệ thống y tế/hàng không an toàn cao.
- [ ] Nhớ 일관성 검사 오라클 chuyên dùng cho kiểm thử hồi quy Regression Test.
