# 3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)

## 3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)
Phần “3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 입력 길이·권한·오류 조건을 충분히 검증하지 않는 API를 사용하여 취약점을 만드는 것 (예: C언어의 `strcpy`, `strcat`).
- **Tiếng Việt**: Sử dụng các hàm không an toàn, dễ gây lỗi tràn bộ đệm (như `strcpy`).
- **예시 (Example)**:
  - (KR) 길이 제한이 없는 `strcpy()` 대신 입력 길이와 널 종료를 명시적으로 검증한다. `strncpy()`도 널 종료가 보장되지 않을 수 있으므로 무조건 안전한 대체재로 보지 않는다.
  - (VN) Dùng `strncpy()` (có giới hạn độ dài) thay cho `strcpy()` (copy không giới hạn).

---
