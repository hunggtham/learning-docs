# 20. 하향식 통합 테스트와 테스트 스텁 (Top-down Integration Test & Test Stub)

## 학습 목표 (Mục tiêu)
- Nắm vững quy trình và chiến lược của phương pháp Kiểm thử tích hợp từ trên xuống (하향식 통합 테스트 - Top-down Integration Testing).
- Hiểu rõ bản chất và vai trò của Mô-đun giả lập cấp dưới (테스트 스텁 - Test Stub) trong việc loại bỏ phụ thuộc và cho phép kiểm thử sớm luồng điều khiển chính.
- So sánh toàn diện ưu nhược điểm giữa phương pháp Kiểm thử tích hợp từ trên xuống (Top-down) và Kiểm thử tích hợp từ dưới lên (상향식 - Bottom-up).

## 핵심 키워드 (Từ khóa)
- 하향식 통합 테스트 (Top-down Integration Testing)
- 상향식 통합 테스트 (Bottom-up Integration Testing)
- 테스트 스텁 (Test Stub / 하위 더미 모듈)
- 테스트 드라이버 (Test Driver / 상위 호출 프로그램)
- 깊이 우선 (Depth-First) & 너비 우선 (Breadth-First)
- 샌드위치 테스트 (Sandwich Testing / 혼합식)

## 선행·연결 개념 (Kiến thức liên kết)
- [53-bai-hoc.md](53-bai-hoc.md): 4 cấp độ kiểm thử phần mềm (Tích hợp là cấp độ 2).
- [54-bai-hoc.md](54-bai-hoc.md): Test Oracle và các công cụ trong Test Harness.
- [66-bai-hoc.md](66-bai-hoc.md): Phân tầng kiểm thử tích hợp theo mô hình V-Model.

## 읽는 방법 (Cách đọc)
- Nhớ cặp đôi thần chú bất hủ trong đề thi Kỹ sư xử lý thông tin:
  - **하향식 (Top-down) $\rightarrow$ 테스트 스텁 (Test Stub)**.
  - **상향식 (Bottom-up) $\rightarrow$ 테스트 드라이버 (Test Driver)**.
- Mẹo ghi nhớ: T-S (Top-Stub) và B-D (Bottom-Driver).
- Thấy câu hỏi: "Mô-đun giả lập cấp dưới trả về kết quả giả định để mô-đun cấp trên chạy thử là gì?" $\rightarrow$ Chọn ngay **테스트 스텁 (Test Stub)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Cơ chế Kiểm thử tích hợp từ trên xuống (하향식 통합 테스트):**
  - **Trình tự tích hợp:** Bắt đầu từ **Mô-đun điều khiển chính ở đỉnh cao nhất (Main Control Module)**, sau đó tích hợp dần dần các mô-đun cấp dưới theo cấu trúc phân cấp điều khiển của hệ thống.
  - **Hai chiến lược duyệt cây tích hợp:**
    - **깊이 우선 통합 (Depth-First Integration):** Tích hợp sâu dọc theo một nhánh điều khiển chính cho đến tận đáy trước khi chuyển sang nhánh khác.
    - **너비 우선 통합 (Breadth-First Integration):** Tích hợp tất cả các mô-đun nằm trên cùng một tầng cấp bậc trước khi đi xuống tầng sâu hơn.
  - **Công cụ bổ trợ bắt buộc:** **테스트 스텁 (Test Stub)**:
    - Khi mô-đun cấp trên đã sẵn sàng nhưng các mô-đun con cấp dưới chưa được lập trình xong, ta phải tạo ra các **Test Stub** (mô-đun giả lập cấp dưới tạm thời) để nhận tham số và trả về dữ liệu mẫu giả định (Dummy Data) nhằm giúp mô-đun cấp trên có thể chạy thử nghiệm được.
- **Bảng so sánh chi tiết Top-down vs Bottom-up Integration Testing:**

| Tiêu chí so sánh | 하향식 통합 테스트 (Top-down) | 상향식 통합 테스트 (Bottom-up) |
| :--- | :--- | :--- |
| **Hướng tích hợp** | Từ mô-đun gốc cấp trên đi dần xuống các mô-đun lá cấp dưới | Từ các mô-đun lá cấp dưới cùng đi dần lên mô-đun chính cấp trên |
| **Công cụ hỗ trợ** | **테스트 스텁 (Test Stub)** - Giả lập mô-đun con bị gọi | **테스트 드라이버 (Test Driver)** - Giả lập chương trình chính gọi xuống |
| **Ưu điểm lớn nhất** | Luồng điều khiển kiến trúc chính được kiểm tra rất sớm; **sớm có bản mẫu demo (Prototype)** cho khách hàng xem | Kiểm tra kỹ lưỡng các thuật toán xử lý dữ liệu nặng ở tầng đáy; **dễ viết Test Case** do mô-đun con đã hoàn thiện |
| **Nhược điểm lớn nhất** | Các mô-đun xử lý dữ liệu chi tiết ở tầng dưới bị kiểm tra muộn; tốn công viết nhiều Stub | Mô-đun điều khiển toàn cục ở đỉnh bị kiểm tra muộn nhất; không sớm có bản demo tổng thể |

- **Phương pháp kiểm thử hỗn hợp (샌드위치 테스트 - Sandwich Testing):**
  - Kết hợp đồng thời cả hai hướng: Tầng trên cùng tích hợp Top-down (dùng Stub) và tầng dưới cùng tích hợp Bottom-up (dùng Driver), gặp nhau ở tầng giữa (Middle Layer).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa mã nguồn Test Stub trong thực tế:**
  - Giả sử hàm `OrderService.checkout()` cần gọi `PaymentGateway.chargeCreditCard()`.
  - Nhưng hệ thống thanh toán thẻ tín dụng của ngân hàng chưa kết nối được:
    - Lập trình viên tạo một `PaymentGatewayStub`:
      ```java
      public class PaymentGatewayStub implements PaymentGateway {
          public boolean chargeCreditCard(String cardNo, double amount) {
              return true; // Luôn trả về thành công giả định để kiểm tra OrderService
          }
      }
      ```
    - Nhờ vậy, hàm `OrderService` có thể chạy kiểm thử bình thường mà không bị đình trệ.

### 복습 체크리스트
- [ ] Ghi nhớ: 하향식 (Top-down) bắt buộc sử dụng 테스트 스텁 (Test Stub).
- [ ] Ghi nhớ: 상향식 (Bottom-up) bắt buộc sử dụng 테스트 드라이버 (Test Driver).
- [ ] Phân biệt hai chiến lược duyệt tích hợp: 깊이 우선 (DFS) và 너비 우선 (BFS).
- [ ] Nêu được ưu điểm của Top-down: Sớm có bản mẫu Prototype cho khách hàng xem.
