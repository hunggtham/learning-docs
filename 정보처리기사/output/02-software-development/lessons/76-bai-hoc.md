# 22. 정적 분석 도구 (Static Analysis Tools)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm và nguyên lý hoạt động của các công cụ phân tích tĩnh (정적 분석 도구 - Static Analysis Tools): kiểm tra và đánh giá chất lượng mã nguồn mà không cần thực thi chương trình.
- Phân biệt rõ sự khác nhau giữa công cụ phân tích tĩnh (Static Analysis) và công cụ phân tích động (Dynamic Analysis).
- Nhớ tên và ngôn ngữ hỗ trợ của các công cụ phân tích tĩnh tiêu biểu trong đề thi: PMD, Checkstyle, Cppcheck, và SonarQube.

## 핵심 키워드 (Từ khóa)
- 정적 분석 도구 (Static Analysis Tools / 실행 없이 분석)
- 동적 분석 도구 (Dynamic Analysis Tools / 실행 중 분석)
- pmd (미사용 변수, 미구현 메서드 검출)
- Checkstyle (자바 코딩 표준 준수 여부 검사)
- Cppcheck (C/C++ 메모리 누수 및 버그 분석)
- SonarQube (통합 코드 품질 및 정적 분석 플랫폼)
- 코딩 표준 (Coding Standard)

## 선행·연결 개념 (Kiến thức liên kết)
- [75-bai-hoc.md](75-bai-hoc.md): Mã nguồn người ngoài hành tinh (Alien Code).
- [77-bai-hoc.md](77-bai-hoc.md): Các kiểu kiến trúc tích hợp ứng dụng doanh nghiệp (EAI).
- [52-bai-hoc.md](52-bai-hoc.md): Phương pháp kiểm thử tĩnh và kiểm thử động.

## 읽는 방법 (Cách đọc)
- Phân biệt Static vs Dynamic Analysis:
  - **정적 분석 (Static):** Kiểm tra file code gốc (source code) khi chương trình **chưa chạy** $\rightarrow$ Tìm vi phạm chuẩn code, biến khai báo thừa không dùng, logic chết (Dead Code), nguy cơ tràn bộ đệm.
  - **동적 분석 (Dynamic):** Kiểm tra khi chương trình **đang chạy trên bộ nhớ** $\rightarrow$ Đo rò rỉ bộ nhớ (Memory Leak), đo độ bao phủ kiểm thử (Coverage), đo thời gian thực thi của CPU.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh Phân tích tĩnh vs Phân tích động:**

| Tiêu chí | 정적 분석 도구 (Static Analysis) | 동적 분석 도구 (Dynamic Analysis) |
| :--- | :--- | :--- |
| **Trạng thái thực thi** | **Không chạy chương trình (코드를 실행하지 않음)** | **Bắt buộc phải chạy chương trình (프로그램 실행 중)** |
| **Đối tượng phân tích** | Mã nguồn (Source Code), cấu trúc cú pháp AST | Tiến trình (Process), bộ nhớ RAM, hành vi luồng I/O |
| **Thời điểm áp dụng** | Giai đoạn Coding (trước khi biên dịch và chạy test) | Giai đoạn Test & Vận hành (khi đã build thành file thực thi) |
| **Lỗi tiêu biểu phát hiện** | Biến khai báo mà không dùng, vi phạm quy tắc đặt tên, method rỗng, lỗ hổng bảo mật tĩnh (SQL Injection nguy cơ) | Rò rỉ bộ nhớ (Memory Leak), xung đột khóa chết (Deadlock), tràn bộ đệm khi chạy |

- **Bảng các công cụ phân tích tĩnh xuất hiện trong đề thi:**

| Tên công cụ | Ngôn ngữ hỗ trợ trọng tâm | Chức năng kiểm tra cốt lõi |
| :--- | :--- | :--- |
| **PMD** | Java, JavaScript, XML | Phát hiện các biến không sử dụng (Unused variables), khối `catch` rỗng, code trùng lặp, logic phức tạp không cần thiết |
| **Checkstyle** | Java | Kiểm tra xem mã nguồn có tuân thủ chặt chẽ **quy tắc chuẩn viết mã (Coding Standard/Convention)** hay không (thụt lề, đặt tên biến, comment) |
| **Cppcheck** | C / C++ | Phân tích sâu mã nguồn C/C++, phát hiện lỗi quản lý con trỏ, rò rỉ tài nguyên, truy cập bộ nhớ ngoài phạm vi mảng |
| **SonarQube** | Đa ngôn ngữ (hơn 25 ngôn ngữ) | Nền tảng quản lý chất lượng mã tập trung, tính toán nợ kỹ thuật, quét lỗ hổng bảo mật và tích hợp vào Jenkins CI/CD |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cơ chế phân tích AST (Abstract Syntax Tree):**
  - Các công cụ phân tích tĩnh không đọc code như văn bản đơn thuần mà sử dụng bộ phân tích cú pháp (Parser) để biến mã nguồn thành một Cây Cú pháp Trừu tượng (AST).
  - Từ cây AST, công cụ áp dụng các luật (Ruleset) như XPath hoặc Visitor pattern để kiểm tra các mẫu code vi phạm mà không làm tốn chi phí khởi tạo môi trường chạy.

### 복습 체크리스트
- [ ] Nhớ từ khóa cốt lõi của 정적 분석: "Không thực thi chương trình" (코드를 실행하지 않고 분석).
- [ ] Nhớ PMD (tìm biến thừa, method rỗng) và Checkstyle (kiểm tra chuẩn coding standard) cho Java.
- [ ] Nhớ Cppcheck dành riêng cho C/C++.
- [ ] Phân biệt được sự khác nhau giữa Static Analysis và Dynamic Analysis.
