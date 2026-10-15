# 9. 소프트웨어 품질 특성 (ISO/IEC 9126)

## 학습 목표 (Mục tiêu)
- Nắm vững 6 đặc tính chất lượng phần mềm quốc tế theo tiêu chuẩn `ISO/IEC 9126` và thuộc lòng các đặc tính con (Sub-characteristics) tương ứng.
- Phân biệt rõ sự chuyển giao từ tiêu chuẩn ISO/IEC 9126 sang bộ tiêu chuẩn chất lượng hiện đại `ISO/IEC 25010 (SQuaRE)`.
- Nhận diện chính xác các câu hỏi bẫy trong đề thi về phân loại thuộc tính chất lượng (ví dụ: Bảo mật thuộc Tính chức năng, Khả năng chịu lỗi thuộc Độ tin cậy).

## 핵심 키워드 (Từ khóa)
- ISO/IEC 9126 (Tiêu chuẩn chất lượng phần mềm)
- ISO/IEC 25010 (SQuaRE - Software Product Quality)
- 기능성 (Tính chức năng / Functionality: 적절성, 정밀성, 상호운용성, 보안성, 준수성)
- 신뢰성 (Độ tin cậy / Reliability: 성숙성, 결함 허용성, 회복성)
- 사용성 (Tính khả dụng / Usability: 이해성, 학습성, 운용성, 친근성)
- 효율성 (Tính hiệu quả / Efficiency: 시간 반응성, 자원 활용성)
- 유지보수성 (Khả năng bảo trì / Maintainability: 분석성, 변경성, 안정성, 시험성)
- 이식성 (Khả năng khả chuyển / Portability: 적응성, 설치성, 공존성, 대체성)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([9. 효과적인 모듈 설계 방안](33-bai-hoc.md)):** Sau khi xem xét các nguyên tắc thiết kế mô-đun tối ưu (Fan-in/Fan-out, Coupling/Cohesion), bài này đo lường chất lượng tổng thể của hệ thống qua khung tiêu chuẩn quốc tế ISO.
- **Tiếp nối sang bài sau ([8. 디자인 패턴](35-bai-hoc.md)):** Khảo sát 23 mẫu thiết kế GoF Design Patterns nhằm nâng cao trực tiếp tính bảo trì (Maintainability) và tính tái sử dụng của phần mềm.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc 6 đặc tính bằng thần chú **기 - 신 - 사 - 효 - 유 - 이** và nhớ 3 thuộc tính con hay bị bẫy nhất: Bảo mật (기능성), Chịu lỗi (신뢰성), Thích ứng (이식성).
- Đọc TẦNG B để hiểu tại sao trong ISO 25010 mới, Bảo mật (Security) đã được tách thành một đặc tính độc lập ngang hàng với Chức năng.

---

## 9. 소프트웨어 품질 특성 (ISO/IEC 9126)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng 6 đặc tính chất lượng phần mềm chuẩn ISO/IEC 9126:**
  1. **기능성 (Functionality - Tính chức năng):**
     - Phần mềm đáp ứng đúng và đủ các chức năng đã quy định khi vận hành trong điều kiện xác định.
     - *Đặc tính con:* `적절성 (Suitability - Phù hợp)`, `정밀성 (Accuracy - Độ chính xác)`, `상호운용성 (Interoperability - Tương tác)`, `보안성 (Security - Bảo mật)`, `준수성 (Compliance - Tuân thủ)`.
  2. **신뢰성 (Reliability - Độ tin cậy):**
     - Khả năng hệ thống duy trì mức hiệu năng quy định và không bị sập trong khoảng thời gian xác định.
     - *Đặc tính con:* `성숙성 (Maturity - Chín muồi)`, `결함 허용성 (Fault Tolerance - Chịu lỗi)`, `회복성 (Recoverability - Phục hồi)`.
  3. **사용성 (Usability - Tính khả dụng):**
     - Mức độ dễ hiểu, dễ học và thao tác thoải mái đối với người dùng.
     - *Đặc tính con:* `이해성 (Understandability - Dễ hiểu)`, `학습성 (Learnability - Dễ học)`, `운용성 (Operability - Dễ vận hành)`, `친근성 (Attractiveness - Thân thiện)`.
  4. **효율성 (Efficiency - Tính hiệu quả):**
     - Hiệu năng xử lý tối ưu tương ứng với lượng tài nguyên phần cứng tiêu tốn.
     - *Đặc tính con:* `시간 반응성 (Time Behaviour - Thời gian đáp ứng)`, `자원 활용성 (Resource Utilisation - Tận dụng tài nguyên)`.
  5. **유지보수성 (Maintainability - Khả năng bảo trì):**
     - Mức độ dễ dàng sửa đổi phần mềm khi phát sinh lỗi hoặc cần nâng cấp tính năng mới.
     - *Đặc tính con:* `분석성 (Analysability - Dễ phân tích lỗi)`, `변경성 (Changeability - Dễ sửa đổi)`, `안정성 (Stability - Độ ổn định)`, `시험성 (Testability - Dễ kiểm thử)`.
  6. **이식성 (Portability - Khả năng khả chuyển / Di động):**
     - Khả năng chuyển đổi và cài đặt phần mềm sang một môi trường phần cứng hoặc hệ điều hành khác.
     - *Đặc tính con:* `적응성 (Adaptability - Dễ thích ứng)`, `설치성 (Installability - Dễ cài đặt)`, `공존성 (Co-existence - Khả năng cùng tồn tại)`, `대체성 (Replaceability - Dễ thay thế)`.
  - 💡 **Thần chú ghi nhớ 6 đặc tính:** **기 - 신 - 사 - 효 - 유 - 이** (Kỹ Năng Sống Tối Ưu, Hữu Ích).
- **Chuyển giao sang ISO/IEC 25010 (SQuaRE):**
  - ISO 25010 mở rộng từ 6 đặc tính lên **8 đặc tính chất lượng**:
    - Tách `보안성 (Security)` từ Tính chức năng ra làm đặc tính độc lập thứ 7.
    - Bổ sung thêm đặc tính thứ 8: `호환성 (Compatibility - Tính tương thích)`.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Trong tiêu chuẩn ISO/IEC 9126, Tính bảo mật (보안성) nằm trong đặc tính nào?"* -> **기능성 (Functionality - Tính chức năng)**, KHÔNG PHẢI 신뢰성 (Độ tin cậy).
  - **Bẫy 2:** *"Khả năng phục hồi dữ liệu sau khi hệ thống gặp sự cố (회복성) thuộc đặc tính nào?"* -> **신뢰성 (Reliability - Độ tin cậy)**.
  - **Bẫy 3:** *"Khả năng dễ kiểm thử (시험성 - Testability) thuộc đặc tính nào?"* -> **유지보수성 (Maintainability - Khả năng bảo trì)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "ISO 9126 gồm 6 trụ cột 기신사효유이; Bảo mật thuộc Chức năng, Chịu lỗi thuộc Tin cậy, Dễ test thuộc Bảo trì".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tình huống trắc nghiệm nhận diện đặc tính con:**
  - *"Hệ thống ATM khi mất điện đột ngột có thể tự động khôi phục lại dữ liệu giao dịch dở dang ngay khi có điện trở lại"* -> Đây là chỉ tiêu **회복성 (Recoverability)** thuộc nhóm **신뢰성 (Reliability)**.
  - *"Phần mềm kế toán cho phép người dùng tự do xuất dữ liệu sang định dạng Excel của Microsoft và Google Sheets một cách trơn tru"* -> Đây là chỉ tiêu **상호운용성 (Interoperability)** thuộc nhóm **기능성 (Functionality)**.

### 복습 체크리스트
- [ ] Đọc thuộc 6 đặc tính lớn của ISO/IEC 9126: 기능성, 신뢰성, 사용성, 효율성, 유지보수성, 이식성.
- [ ] Nhớ chính xác 보안성 thuộc nhóm 기능성 trong ISO 9126.
- [ ] Nhớ 결함 허용성 và 회복성 thuộc nhóm 신뢰성.
- [ ] Nhớ 시험성 (Testability) thuộc nhóm 유지보수성.
- [ ] Nêu được điểm mới của ISO 25010 (tách riêng Security và bổ sung Compatibility).
