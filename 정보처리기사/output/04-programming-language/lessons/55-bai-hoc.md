# 191. 결합도 (Coupling / Mức độ phụ thuộc)

## 191. 결합도 (Coupling / Mức độ phụ thuộc)
Phần “191. 결합도 (Coupling / Mức độ phụ thuộc)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 모듈 간에 상호 의존하는 정도. 약할수록 독립성이 높고 품질이 좋음.
- **결합도가 약한 것부터 강한 순서 (Tốt -> Xấu)**:
  1. **자료 (Data)**: 파라미터로 단순 데이터(값)만 전달 (가장 좋음).
  2. **스탬프 (Stamp)**: 배열이나 레코드 등 자료 구조를 전달.
  3. **제어 (Control)**: 제어 신호(Flag)를 전달하여 상대 모듈의 흐름을 제어.
  4. **외부 (External)**: 외부에서 선언된 데이터를 참조.
  5. **공통 (Common)**: 전역 변수(공통 데이터 영역)를 여러 모듈이 사용.
  6. **내용 (Content)**: 다른 모듈의 내부 기능이나 변수를 직접 참조/수정 (가장 나쁨).

**Giải thích (Vietnamese):**
Coupling đánh giá mức độ "dính líu" giữa 2 module. Càng dính líu nhiều, khi sửa module này sẽ làm hỏng module kia.
Tốt nhất là Data (chỉ truyền tham trị như `int a`). Tệ nhất là Content (module A nhảy thẳng vào code của module B để sửa biến).

**💡 Mẹo ghi nhớ (Mnemonics):**
**자스제 외공내** (Tự - Tem - Chế - Ngoại - Công - Nội): 자료 (Data) -> 스탬프 (Stamp) -> 제어 (Control) -> 외부 (External) -> 공통 (Common) -> 내용 (Content). Từ Tốt đến Xấu.

---
