# 120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)

## 학습 목표 (Mục tiêu)
- Tổng hợp toàn diện hệ thống lý thuyết kiểm thử ứng dụng phần mềm gồm các nguyên lý cơ bản và bản đồ phân loại đa chiều.
- Nằm lòng các nguyên lý cốt lõi: Quy luật Pareto 80:20 (결함 집중), Nghịch lý thuốc trừ sâu (살충제 패러독스) và Tính bất khả thi của kiểm thử tuyệt đối.
- Thuần thục việc phân nhóm các phương pháp kiểm thử theo 3 trục tiêu chí: Trạng thái thực thi mã nguồn (Tĩnh vs Động), Căn cứ thiết kế (Đặc tả vs Cấu trúc vs Kinh nghiệm) và Mục tiêu kiểm tra chuyên biệt.

## 핵심 키워드 (Từ khóa)
- 애플리케이션 테스트 이론 (Application Testing Theory)
- 파레토 법칙 (Pareto Principle 80:20)
- 살충제 패러독스 (Pesticide Paradox)
- 정적 테스트 (Static: 워크스루, 인스펙션)
- 동적 테스트 (Dynamic: 화이트박스, 블랙박스)
- 명세 기반 & 구조 기반 & 경험 기반
- 목적별 테스트 (스트레스, 회귀, 회복, 병행)

## 선행·연결 개념 (Kiến thức liên kết)
- [57-bai-hoc.md](57-bai-hoc.md): Chi tiết 7 nguyên lý kiểm thử phần mềm ISTQB.
- [58-bai-hoc.md](58-bai-hoc.md): Phân loại kiểm thử theo trạng thái, căn cứ và mục đích.
- [64-bai-hoc.md](64-bai-hoc.md): Đi sâu vào kiểm thử hộp trắng (White-box Testing).
- [65-bai-hoc.md](65-bai-hoc.md): Đi sâu vào kiểm thử hộp đen (Black-box Testing).

## 읽는 방법 (Cách đọc)
- Ôn tập theo sơ đồ mạng nhện:
  - Nhánh 1: Nguyên lý kiểm thử (Pareto $\rightarrow$ 80% lỗi ở 20% code; Pesticide $\rightarrow$ Test hoài 1 bài sẽ nhờn lỗi).
  - Nhánh 2: Không chạy code $\rightarrow$ **Tĩnh (Static: Inspection)**; Chạy code $\rightarrow$ **Động (Dynamic: White/Black box)**.
  - Nhánh 3: Mục đích kiểm thử (Quá tải $\rightarrow$ Stress; Sửa xong test lại $\rightarrow$ Regression).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Các nguyên lý kiểm thử ứng dụng sống còn:**
  - **파레토 법칙 (Pareto 80/20 Rule - 결함 집중):** Khoảng 80% số lỗi nghiêm trọng của toàn bộ phần mềm tập trung trong 20% số mô-đun phức tạp nhất. Do đó cần tập trung nguồn lực kiểm thử sâu vào nhóm mô-đun rủi ro cao này.
  - **살충제 패러독스 (Pesticide Paradox):** Việc dùng mãi một bộ Test Case lặp lại nhiều lần sẽ làm mất khả năng phát hiện lỗi mới. Bắt buộc phải định kỳ viết thêm các Test Case mới với các góc nhìn dị thường.
  - **완벽한 테스트 불가능 (Exhaustive Testing is impossible):** Không bao giờ có thể kiểm thử toàn bộ 100% mọi khả năng kết hợp.
- **2. Bản đồ phân loại kiểm thử ứng dụng toàn diện:**

```
+---------------------------------------------------------------------------------+
| PHÂN LOẠI KIỂM THỬ ỨNG DỤNG                                                     |
|                                                                                 |
| 1. THEO THỰC THI (실행 여부):                                                    |
|    - 정적 (Static - Không chạy code): 워크스루 (Walkthrough), 인스펙션 (Inspection) |
|    - 동적 (Dynamic - Chạy code): 화이트박스 (White-box), 블랙박스 (Black-box)       |
|                                                                                 |
| 2. THEO CĂN CỨ (기반):                                                           |
|    - 명세 기반 (Specification): 동치 분할, 경계값 분석 (Black-box)               |
|    - 구조 기반 (Structure): 구문 커버리지, 결정 커버리지 (White-box)             |
|    - 경험 기반 (Experience): 오류 예측 (Error Guessing), 탐색적 테스팅           |
|                                                                                 |
| 3. THEO MỤC ĐÍCH (목적):                                                         |
|    - 강도 (Stress): Ép tải cực đoan vượt giới hạn để xem hệ thống sập thế nào   |
|    - 회귀 (Regression): Sửa code xong kiểm tra xem có phát sinh lỗi mới không   |
|    - 회복 (Recovery): Cố tình tạo sự cố để đo khả năng tự phục hồi dữ liệu      |
|    - 병행 (Parallel): Chạy đồng thời hệ thống mới và cũ để so sánh kết quả      |
+---------------------------------------------------------------------------------+
```

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Sự khác biệt giữa Walkthrough và Inspection trong Kiểm thử tĩnh:**
  - **워크스루 (Walkthrough):** Buổi trao đổi bán chính thức, do chính tác giả của đoạn code chủ trì để giới thiệu giải thuật cho đồng nghiệp xem và góp ý.
  - **인스펙션 (Inspection):** Buổi thẩm định chính thức cực kỳ nghiêm ngặt do một chuyên gia kiểm duyệt độc lập (Moderator) chủ trì. Các thành viên phải dùng danh mục tiêu chí kiểm tra (Checklist) chuẩn hóa để soi từng dòng code và lập biên bản ghi nhận lỗi chính thức.

### 복습 체크리스트
- [ ] Nhớ quy luật Pareto 80:20 trong kiểm thử phần mềm.
- [ ] Giải thích nguyên lý 살충제 패러독스 (Pesticide Paradox).
- [ ] Phân loại đúng: Walkthrough và Inspection thuộc Kiểm thử tĩnh (Static).
- [ ] Nhớ định nghĩa Regression Test: Kiểm tra lại sau khi sửa mã để tránh lỗi mới.
