# 3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

취약한, API, 사용

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)** và nối nó với **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)
- **개념**: 입력 길이·권한·오류 조건을 충분히 검증하지 않는 API를 사용하여 취약점을 만드는 것 (예: C언어의 `strcpy`, `strcat`).
- **Tiếng Việt**: Sử dụng các hàm không an toàn, dễ gây lỗi tràn bộ đệm (như `strcpy`).
- **예시 (Example)**:
  - (KR) 길이 제한이 없는 `strcpy()` 대신 입력 길이와 널 종료를 명시적으로 검증한다. `strncpy()`도 널 종료가 보장되지 않을 수 있으므로 무조건 안전한 대체재로 보지 않는다.
  - (VN) Dùng `strncpy()` (có giới hạn độ dài) thay cho `strcpy()` (copy không giới hạn).

---
