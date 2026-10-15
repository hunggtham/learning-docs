# 45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계

## 학습 목표 (Mục tiêu)
- Định nghĩa Mô hình chữ V (V-모델 - V-Model) và hiểu rõ nguyên lý ánh xạ đối xứng 1-1 giữa các giai đoạn phát triển phần mềm (nhánh trái đi xuống) và các cấp độ kiểm thử tương ứng (nhánh phải đi lên).
- Thuộc nằm lòng 4 cặp tương ứng phát triển - kiểm thử kinh điển: Yêu cầu $\leftrightarrow$ 인수 테스트, Thiết kế hệ thống $\leftrightarrow$ 시스템 테스트, Thiết kế chi tiết $\leftrightarrow$ 통합 테스트, Triển khai mã $\leftrightarrow$ 단위 테스트.
- Phân biệt vai trò của pha Kiểm tra xác minh (Verification / nhánh trái) và pha Kiểm tra xác nhận (Validation / nhánh phải) trong vòng đời phần mềm.

## 핵심 키워드 (Từ khóa)
- V-모델 (V-Model)
- 개발 단계와 테스트 단계 매핑 (Development-Test Phase Mapping)
- 요구사항 분석 ↔ 인수 테스트 (Acceptance Test)
- 시스템 설계 ↔ 시스템 테스트 (System Test)
- 상세 설계 ↔ 통합 테스트 (Integration Test)
- 구현 / 코딩 ↔ 단위 테스트 (Unit Test)
- 검증 (Verification) vs 확인 (Validation)

## 선행·연결 개념 (Kiến thức liên kết)
- [53-bai-hoc.md](53-bai-hoc.md): 4 cấp độ kiểm thử phần mềm (Đơn vị, Tích hợp, Hệ thống, Chấp nhận).
- [57-bai-hoc.md](57-bai-hoc.md): Nguyên lý kiểm thử và cặp khái niệm Verification vs Validation.
- [61-bai-hoc.md](61-bai-hoc.md): Quy trình kiểm thử chuẩn (Test Process 5 bước).
- [66-bai-hoc.md](66-bai-hoc.md): Chi tiết từng tầng kiểm thử theo mô hình V-Model.

## 읽는 방법 (Cách đọc)
- Học thuộc bảng ánh xạ đối xứng 4 tầng của mô hình V-Model. Đi thi trắc nghiệm cứ hỏi:
  - "Kiểm thử đơn vị (Unit Test) được thiết kế đối chiếu với giai đoạn nào?" $\rightarrow$ **구현 / 코딩 (Implementation / Coding)**.
  - "Kiểm thử tích hợp (Integration Test) đối chiếu với giai đoạn nào?" $\rightarrow$ **상세 설계 (Detailed Design)**.
  - "Kiểm thử hệ thống (System Test) đối chiếu với giai đoạn nào?" $\rightarrow$ **시스템 설계 / 기본 설계 (System Design)**.
  - "Kiểm thử chấp nhận (Acceptance Test) đối chiếu với giai đoạn nào?" $\rightarrow$ **요구사항 분석 (Requirements Analysis)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Kiến trúc đối xứng của Mô hình V-Model:**

```
[ 요구사항 분석 ]  <====== (Nghiệm thu thực tế) ======>  [ 인수 테스트 ]
       \                                                      /
   [ 시스템 설계 ]  <==== (Kiểm tra phi chức năng) ====>  [ 시스템 테스트 ]
          \                                                /
      [ 상세 설계 ]  <=== (Kiểm tra Interface) ===>  [ 통합 테스트 ]
             \                                          /
         [ 구현/코딩 ]  <-- (Kiểm tra logic/code) --> [ 단위 테스트 ]
```

- **Bảng ánh xạ chi tiết 4 cặp giai đoạn trong V-Model:**

| Giai đoạn phát triển (Nhánh trái - Verification) | Cấp độ kiểm thử tương ứng (Nhánh phải - Validation) | Mục tiêu kiểm tra trọng tâm |
| :--- | :--- | :--- |
| **요구사항 분석 (Requirements Analysis)** | **인수 테스트 (Acceptance Test)** | Kiểm tra xem sản phẩm hoàn thiện có thỏa mãn đúng các yêu cầu nghiệp vụ ban đầu mà khách hàng ký kết trong hợp đồng hay không (Alpha/Beta Test) |
| **시스템 설계 / 기본 설계 (System Design)** | **시스템 테스트 (System Test)** | Kiểm tra toàn bộ hệ thống trên môi trường thực tế, tập trung vào các yêu cầu phi chức năng: Hiệu năng, Bảo mật, Chịu tải, Phục hồi thảm họa |
| **상세 설계 / 모듈 설계 (Detailed Design)** | **통합 테스트 (Integration Test)** | Kiểm tra sự tương tác, truyền nhận tham số và tính tương thích giao diện (Interface) giữa các mô-đun phần mềm (Top-down / Bottom-up) |
| **구현 / 코딩 (Implementation / Coding)** | **단위 테스트 (Unit Test)** | Kiểm tra từng mô-đun, hàm, lớp riêng lẻ xem mã nguồn có thuật toán đúng, không lỗi lặp, không lỗi cú pháp hay không |

- **Bẫy đề thi trắc nghiệm:**
  - **Bẫy 1:** *"Trong mô hình V-Model, giai đoạn nào là cơ sở trực tiếp để thiết kế Integration Test (통합 테스트)?"* $\rightarrow$ Đáp án chắc chắn là **상세 설계 (Detailed Design)**.
  - **Bẫy 2:** *"Pha nào đối ứng với Acceptance Test?"* $\rightarrow$ Đáp án: **요구사항 분석 (Requirements Analysis)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ý nghĩa sống còn của V-Model trong quản lý chất lượng:**
  - Mô hình V-Model chứng minh rằng: **Kế hoạch kiểm thử không phải đợi đến khi code xong mới viết**.
  - Ngay từ khi Lập tài liệu Yêu cầu (Requirements), kiểm thử viên đã có thể bắt tay vào thiết kế bộ ca kiểm thử cho Acceptance Test.
  - Khi hoàn thành Thiết kế hệ thống, kiểm thử viên lập tức thiết kế Test Plan cho System Test.
  - Cách làm song song này giúp rút ngắn đáng kể thời gian đưa sản phẩm ra thị trường và phát hiện lỗi thiết kế ngay từ trong trứng nước.

### 복습 체크리스트
- [ ] Vẽ lại chuẩn xác mô hình chữ V và 4 cặp giai đoạn tương ứng.
- [ ] Nhớ cặp: Yêu cầu $\leftrightarrow$ 인수 테스트; Thiết kế hệ thống $\leftrightarrow$ 시스템 테스트.
- [ ] Nhớ cặp: Thiết kế chi tiết $\leftrightarrow$ 통합 테스트; Lập trình $\leftrightarrow$ 단위 테스트.
- [ ] Giải thích được tại sao V-Model hỗ trợ lập kế hoạch kiểm thử song song sớm.
