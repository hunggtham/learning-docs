# 097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)

## 학습 목표 (Mục tiêu)
- Nắm vững quy trình 5 bước chuẩn tắc của tiến trình kiểm thử phần mềm (테스트 프로세스 5단계): 계획 및 제어 (Lập kế hoạch & Kiểm soát) $\rightarrow$ 분석 및 설계 (Phân tích & Thiết kế) $\rightarrow$ 구현 및 실현 (Triển khai & Thực thi) $\rightarrow$ 평가 (Đánh giá) $\rightarrow$ 완료 (Hoàn tất).
- Hiểu rõ sản phẩm đầu ra của từng giai đoạn: Test Case được sinh ra ở bước Phân tích & Thiết kế; Test Procedure và Test Log được sinh ra ở bước Triển khai & Thực thi.
- Phân biệt rõ sự khác nhau giữa Ca kiểm thử (테스트 케이스 - Test Case) và Thủ tục kiểm thử (테스트 프로시저 - Test Procedure).

## 핵심 키워드 (Từ khóa)
- 테스트 프로세스 5단계 (Test Process 5 Steps)
- 계획 및 제어 (Test Planning & Control)
- 분석 및 설계 (Test Analysis & Design / Test Case 도출)
- 구현 및 실현 (Implementation & Execution / Test Procedure)
- 평가 (Evaluation / 완료 기준 평가)
- 완료 (Test Completion / 산출물 정리)
- 테스트 프로시저 (Test Procedure / 실행 절차)

## 선행·연결 개념 (Kiến thức liên kết)
- [56-bai-hoc.md](56-bai-hoc.md): Định nghĩa cấu trúc của Bản mô tả ca kiểm thử (Test Case).
- [60-bai-hoc.md](60-bai-hoc.md): Mô hình V-Model phân bổ kiểm thử theo vòng đời phát triển.
- [63-bai-hoc.md](63-bai-hoc.md): Tổng hợp lý thuyết kiểm thử ứng dụng.

## 읽는 방법 (Cách đọc)
- Học thuộc thần chú 5 bước kiểm thử: **"Kế - Phân - Thực - Đánh - Hoàn"** (계획 $\rightarrow$ 분석/설계 $\rightarrow$ 구현/실행 $\rightarrow$ 평가 $\rightarrow$ 완료).
- Nhớ câu hỏi trắc nghiệm hay gài bẫy:
  - "Test Case được tạo ra ở bước nào?" $\rightarrow$ **분석 및 설계 (Phân tích & Thiết kế)**.
  - "Test Procedure (Thủ tục thực hiện kiểm thử) được tạo ra ở bước nào?" $\rightarrow$ **구현 및 실현 (Triển khai & Thực thi)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Quy trình 5 giai đoạn kiểm thử phần mềm chuẩn quốc tế (ISTQB):**
  $$\mathbf{계획\ 및\ 제어} \longrightarrow \mathbf{분석\ 및\ 설계} \longrightarrow \mathbf{구현\ 및\ 실현} \longrightarrow \mathbf{평가} \longrightarrow \mathbf{완료}$$

| Thứ tự bước | Tên tiếng Hàn & Anh | Công việc và Sản phẩm đầu ra cốt lõi |
| :---: | :--- | :--- |
| **Bước 1** | **계획 및 제어 (Planning & Control)** | Xác định mục tiêu, phạm vi, phân tích rủi ro, dự trù ngân sách, phân bổ nhân sự, lập lịch trình và định nghĩa tiêu chí kết thúc kiểm thử (**종료 조건 / Exit Criteria**) |
| **Bước 2** | **분석 및 설계 (Analysis & Design)** | Rà soát tài liệu đặc tả, xác định các điều kiện kiểm thử (Test Conditions), thiết kế Kịch bản kiểm thử (Test Scenario) và chi tiết hóa thành các **Ca kiểm thử (테스트 케이스 - Test Case)** |
| **Bước 3** | **구현 및 실현 (Implementation & Execution)** | Chuẩn bị dữ liệu và môi trường test; soạn thảo **Thủ tục kiểm thử (테스트 프로시저 - Test Procedure)** quy định thứ tự chạy các ca test; trực tiếp bấm chạy test và ghi nhận nhật ký (Test Log), lập báo cáo lỗi (Defect Report) |
| **Bước 4** | **평가 (Evaluation)** | So sánh kết quả thực tế với mục tiêu ban đầu; đánh giá xem đã đạt tiêu chí kết thúc kiểm thử (Exit Criteria) hay chưa để quyết định dừng test hay test tiếp |
| **Bước 5** | **완료 (Completion)** | Đóng gói và lưu trữ toàn bộ hồ sơ kiểm thử; ghi nhận các bài học kinh nghiệm (Lessons Learned); bàn giao phần mềm cho bộ phận vận hành |

- **Phân biệt Test Case vs Test Procedure:**
  - **테스트 케이스 (Test Case):** Là bản mô tả *CẦN PHẢI TEST CÁI GÌ* (Gồm Input và Expected Output). Giống như danh sách các món ăn trên thực đơn.
  - **테스트 프로시저 (Test Procedure):** Là hướng dẫn thao tác *CHẠY CÁC CASE ĐÓ THEO THỨ TỰ NÀO VÀ BẤM NÚT NÀO TRÊN MÀN HÌNH* (Quy trình các bước tuần tự). Giống như công thức nấu nướng từng bước một.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tiêu chí kết thúc kiểm thử (Exit Criteria / 종료 조건):**
  - Không thể kiểm thử vô hạn. Kế hoạch kiểm thử phải định nghĩa trước rõ ràng khi nào thì được phép dừng kiểm thử:
    - Đạt tỷ lệ bao phủ mã nguồn theo yêu cầu (ví dụ: Statement Coverage $\ge 90\%$).
    - 100% các Test Case mức độ nghiêm trọng cao (Critical / High) đều PASS.
    - Tỷ lệ lỗi mở (Open Defect) còn lại dưới mức ngưỡng chấp nhận cho phép.
    - Hết thời gian hoặc hết ngân sách dự án đã được phê duyệt.

### 복습 체크리스트
- [ ] Thuộc lòng 5 bước của quy trình kiểm thử: 계획/제어 $\rightarrow$ 분석/설계 $\rightarrow$ 구현/실행 $\rightarrow$ 평가 $\rightarrow$ 완료.
- [ ] Xác định đúng: Test Case ra đời ở bước 2 (분석 및 설계).
- [ ] Xác định đúng: Test Procedure ra đời ở bước 3 (구현 및 실현).
- [ ] Nêu được vai trò của Tiêu chí kết thúc (종료 조건 / Exit Criteria).
