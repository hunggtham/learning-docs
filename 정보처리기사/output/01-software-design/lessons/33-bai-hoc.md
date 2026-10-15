# 9. 효과적인 모듈 설계 방안 (Effective Module Design)

## 학습 목표 (Mục tiêu)
- Nắm vững 6 nguyên tắc chỉ đạo trong việc thiết kế mô-đun phần mềm đạt hiệu quả kỹ thuật cao nhất.
- Khắc sâu mối quan hệ giữa Phạm vi kiểm soát (`제어 영역 - Scope of Control`) và Phạm vi ảnh hưởng (`영향 영역 - Scope of Effect`): Phạm vi ảnh hưởng phải nằm trọn trong phạm vi kiểm soát.
- Phân biệt bản chất của `Fan-in` (số mô-đun gọi vào) và `Fan-out` (số mô-đun được gọi ra), cùng tiêu chí tối ưu hóa Fan-in cao và Fan-out thấp.

## 핵심 키워드 (Từ khóa)
- 효과적인 모듈 설계 (Thiết kế mô-đun hiệu quả / Effective Module Design)
- 결합도 낮춤 / 응집도 높임 (Low Coupling / High Cohesion)
- 팬인 / 팬아웃 (Fan-in / Fan-out)
- 제어 영역 (Phạm vi kiểm soát / Scope of Control)
- 영향 영역 (Phạm vi ảnh hưởng / Scope of Effect)
- 단일 입구·단일 출구 (Single Entry / Single Exit)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([7. 공통 모듈](32-bai-hoc.md)):** Sau khi xem xét 5 nguyên tắc đặc tả mô-đun dùng chung (정명완일추), bài này đúc kết toàn diện chiến lược thiết kế mô-đun tối ưu cấu trúc.
- **Tiếp nối sang cụm sau ([9. 소프트웨어 품질 특성 (ISO/IEC 9126)](34-bai-hoc.md) và [8. 디자인 패턴](35-bai-hoc.md)):** Khảo sát sâu các mẫu thiết kế hướng đối tượng kinh điển (GoF Design Patterns: Creational, Structural, Behavioral).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để ghi nhớ chắc chắn: Fan-in cao là tốt (được tái sử dụng nhiều); Fan-out thấp là tốt (ít phụ thuộc bên dưới); và nguyên tắc sống còn "Ảnh hưởng nằm trong Kiểm soát".
- Đọc TẦNG B để theo dõi sơ đồ cây phân cấp mô-đun và cách tính toán chỉ số Fan-in / Fan-out trong câu hỏi đề thi.

---

## 9. 효과적인 모듈 설계 방안 (Effective Module Design)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **6 nguyên tắc vàng thiết kế mô-đun hiệu quả (효과적인 모듈 설계 원칙):**
  1. **결합도와 응집도 (Độ kết hợp và gắn kết):**
     - **결합도는 낮추고 (Coupling $\downarrow$)**, **응집도는 높인다 (Cohesion $\uparrow$)**. Đây là nguyên tắc nền tảng tối thượng.
  2. **모듈의 크기 (Kích thước mô-đun):**
     - Kích thước mô-đun không được quá lớn (gây phức tạp, khó hiểu) và cũng không được quá nhỏ (làm tăng chi phí tích hợp và giao tiếp mạng); duy trì ở mức kích thước vừa phải và tối ưu.
  3. **제어 영역과 영향 영역 (Phạm vi kiểm soát và ảnh hưởng):**
     - **Nguyên tắc sống còn:** **모듈의 영향 영역은 그 모듈의 제어 영역 내에 있어야 한다 (Phạm vi ảnh hưởng của mô-đun PHẢI NẰM HOÀN TOÀN TRONG phạm vi kiểm soát của chính nó)**. Nếu một mô-đun gây ảnh hưởng đến một mô-đun nằm ngoài tầm kiểm soát của nó, cấu trúc hệ thống sẽ bị hỗn loạn khi có lỗi phát sinh.
  4. **팬인(Fan-in)과 팬아웃(Fan-out):**
     - `팬인 (Fan-in)`: Số lượng các mô-đun cấp trên gọi đến mô-đun hiện tại (Mũi tên đi vào). **Fan-in cao là tốt (`높은 팬인 권장`)** vì chứng tỏ mô-đun có tính tái sử dụng cao.
     - `팬아웃 (Fan-out)`: Số lượng các mô-đun cấp dưới mà mô-đun hiện tại trực tiếp gọi đến (Mũi tên đi ra). **Fan-out nên duy trì ở mức thấp hoặc vừa phải (`낮은 팬아웃 권장`)** để tránh việc mô-đun bị phụ thuộc quá nhiều vào các mô-đun con.
  5. **단일 입구와 단일 출구 (Single Entry, Single Exit):**
     - Mỗi mô-đun chỉ nên có **MỘT cổng vào duy nhất và MỘT cổng ra duy nhất**, tránh việc nhảy vào hoặc thoát ra tùy tiện giữa chừng làm khó kiểm soát bộ nhớ.
  6. **인터페이스의 단순성 (Giao diện đơn giản):**
     - Giao diện kết nối và số lượng tham số truyền giữa các mô-đun phải tối giản, dễ hiểu, tránh các tham số điều khiển phức tạp.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Phạm vi kiểm soát (제어 영역) phải nằm trong phạm vi ảnh hưởng (영향 영역)?"* -> **Sai hoàn toàn, ngược lại mới đúng**. **Phạm vi ảnh hưởng phải nằm trong phạm vi kiểm soát (영향 영역 $\subseteq$ 제어 영역)**.
  - **Bẫy 2:** *"Một thiết kế tốt là thiết kế có Fan-out càng cao càng tốt?"* -> **Sai**. Fan-out cao nghĩa là mô-đun đó kiểm soát quá nhiều mô-đun con, làm tăng độ phức tạp. Thiết kế tốt là **Fan-in cao (tái sử dụng nhiều) và Fan-out vừa phải/thấp**.
  - **Bẫy 3:** *"Mô-đun có thể có nhiều điểm vào (Entry Point) tùy tiện để lập trình viên nhảy vào gọi trực tiếp?"* -> **Sai**. Phải tuân thủ nguyên tắc **단일 입구, 단일 출구**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Thiết kế mô-đun chuẩn: Kết hợp thấp Gắn kết cao, Ảnh hưởng nằm trong Kiểm soát, Fan-in cao Fan-out thấp, Một vào Một ra".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa trực quan về Scope of Control vs Scope of Effect:**
  - `Phạm vi kiểm soát (Scope of Control)` của mô-đun A: Là chính mô-đun A và tất cả các mô-đun con cấp dưới chịu sự điều khiển trực tiếp hoặc gián tiếp của A.
  - `Phạm vi ảnh hưởng (Scope of Effect)` của mô-đun A: Là tất cả các mô-đun bị tác động bởi một quyết định rẽ nhánh logic hoặc cờ điều khiển phát sinh từ bên trong mô-đun A.
  - *Quy tắc:* Nếu mô-đun A đưa ra quyết định mà lại làm thay đổi hành vi của mô-đun B (nằm ngoài nhánh cây con của A), thì khi bảo trì, lập trình viên sửa A sẽ không bao giờ ngờ tới B bị lỗi. Vì vậy, B bắt buộc phải là con cháu nằm trong cây điều khiển của A.

### 복습 체크리스트
- [ ] Khẳng định được nguyên tắc: 결합도는 낮추고 응집도는 높인다.
- [ ] Nhớ mệnh đề chuẩn: 모듈의 영향 영역은 제어 영역 내에 있어야 한다.
- [ ] Phân biệt được Fan-in (số module gọi nó - nên cao) và Fan-out (số module nó gọi - nên thấp).
- [ ] Nêu được ý nghĩa của nguyên tắc 단일 입구와 단일 출구 (Single Entry, Single Exit).
